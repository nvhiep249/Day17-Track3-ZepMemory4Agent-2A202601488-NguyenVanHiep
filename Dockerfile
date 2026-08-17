FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/workspace

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /tmp/requirements.txt

COPY . /workspace

CMD ["sleep", "infinity"]
