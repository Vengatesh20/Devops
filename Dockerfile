FROM python:latest

WORKDIR /

COPY . /

CMD ["python", "python.py"]
