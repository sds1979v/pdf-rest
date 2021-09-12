FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV TIMEOUT="500"

RUN apt update && apt install -y \
tesseract-ocr tesseract-ocr-ces ocrmypdf

COPY ./src /app
RUN pip install -r /app/requirements.txt
