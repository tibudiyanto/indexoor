FROM python:3.9.9-slim-buster

RUN apt-get update && apt-get install build-essential -y

RUN adduser --disabled-password --gecos "" worker
USER worker
WORKDIR /home/worker

COPY --chown=worker:worker requirements.txt requirements.txt

# add user namespace pip install location to PATH
ENV PATH="$PATH:/home/worker/.local/bin"

# install in user namespace
RUN pip install \
    --no-cache-dir \
    --requirement requirements.txt \
    --user

COPY --chown=worker:worker ./indexoor indexoor

WORKDIR /home/worker/indexoor

CMD ["gunicorn", "--config", "gunicorn.conf.py", "web:app"]
 