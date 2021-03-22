FROM python:3.9
RUN pip install pipenv
COPY . /simpleflask
WORKDIR /simpleflask
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "app"]
