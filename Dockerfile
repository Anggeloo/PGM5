FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir flask waitress werkzeug
COPY PGM5.py .
EXPOSE 8080
CMD ["python", "PGM5.py"]
