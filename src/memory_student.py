from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        from .utils import cap_query, join_nonempty
        
        prime_eval_thread(self.client, user_id, thread_id, query)
        
        context_res = ""
        context = self.client.thread.get_user_context(thread_id=thread_id)
        if context and context.context:
            context_res = str(context.context)
            
        try:
            results = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20
            )
            edges_res = render_graph_search(results)
        except Exception:
            edges_res = ""
            
        return join_nonempty([context_res, edges_res])

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        from .utils import cap_query
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=5
        )
        return render_graph_search(results, episode_char_cap=200)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        from .utils import cap_query, join_nonempty
        capped_query = cap_query(query)
        chunks = []
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_query,
                scope="episodes",
                limit=8
            )
            import json
            seen = set()
            for ep in getattr(results, "episodes", []) or []:
                content = getattr(ep, "content", "")
                if not content:
                    continue
                if content.strip().startswith('{"id":'):
                    try:
                        obj = json.loads(content)
                        content = obj.get("summary", content)
                    except Exception:
                        pass
                if content not in seen:
                    seen.add(content)
                    chunks.append(f"EPISODE: {content}")
        except Exception:
            pass
            
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=capped_query,
                scope="nodes",
                limit=3
            )
            chunks.append(render_graph_search(results))
        except Exception:
            pass
            
        return join_nonempty(chunks)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
