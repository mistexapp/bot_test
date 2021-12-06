FROM python:3.8

MAINTANER Lexusobm "dev@mistexapp.com"

COPY .* .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app.py"]
