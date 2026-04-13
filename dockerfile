FROM python:3.13

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

CMD ["bash", "start.sh"]