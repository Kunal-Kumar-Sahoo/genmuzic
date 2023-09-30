FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y git

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8051

CMD ["streamlit", "run", "app.py"]