FROM python:3.7 AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN python -m venv /venv
RUN /venv/bin/pip install -r requirements.txt --no-cache-dir
# RUN /venv/bin/pip install -r requirements.txt


FROM python:3.7-slim AS app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONPATH=/app

WORKDIR /app
COPY --from=builder /venv /venv
COPY cuban cuban

CMD ["/venv/bin/python", "cuban/tasks/workflow.py", "Diff", "--local-scheduler"]
# ENTRYPOINT ["/venv/bin/python", "cuban/tasks/workflow.py", "Diff", "--local-scheduler"]
