FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN apt update
RUN apt install gettext -y

RUN pip install -r requirements.txt

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

#COPY ./montechelo/run-data /run-data
#RUN sed -i 's/\r$//g' /run-data
#RUN chmod +x /run-data

COPY ./compose/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

COPY . /app/

#EXPOSE $PORT
#
#ENTRYPOINT ["/start"]