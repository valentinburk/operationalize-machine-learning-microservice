FROM python:3.7.3-stretch

WORKDIR /app

COPY ./app.py /app/
COPY ./model_data/* /app/model_data/
COPY ./requirements.txt /app/

# hadolint ignore=DL3013
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]