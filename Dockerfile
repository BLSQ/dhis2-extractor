FROM python:3

RUN apt-get update
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python", "-m", "dhis2_extractor.cli"]
