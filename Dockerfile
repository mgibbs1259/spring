FROM python:3.10

RUN mkdir /code
WORKDIR /code

COPY spring /code/
COPY run_spring.py /code/

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install paho-mqtt rachiopy python-dotenv

CMD ["python", "run_spring.py"]