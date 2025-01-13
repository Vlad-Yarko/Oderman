FROM python:3.12

WORKDIR /app

#ENV PYTHONPATH="${PYTHONPATH}:/app/src"

COPY . .

RUN pip install -r requirements.txt

CMD [ "hypercorn", "-b", "0.0.0.0:8000", "app.main:a"]