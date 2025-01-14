FROM --platform=linux/arm64 python:3.13-slim

RUN python3.13 -m pip install -U pip
RUN python3.13 -m pip install pipenv

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pipenv install --system --deploy

EXPOSE 5000

ENV FLASK_APP=application.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["gunicorn", "-b", "0.0.0.0:5001", "application:home"]
# CMD [ "flask", "run" ]
