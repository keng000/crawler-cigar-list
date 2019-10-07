FROM python:3.7-slim

WORKDIR /home
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install pipenv && \
    pipenv install 

COPY cuban cuban
WORKDIR /home/cuban
CMD ["pipenv", "run", "scrapy", "crawl", "products", "-o all.json"]