FROM python:3.11.1-bullseye
WORKDIR /code
COPY ./src/requirements.txt /code/requirements.txt
RUN apt-get update && apt-get install -y gcc curl wget
RUN pip install uvicorn
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt-get update && apt-get install -y supervisor
COPY ./src/app /code/app

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]