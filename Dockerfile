FROM python:3.10

RUN mkdir /spring
WORKDIR /spring

COPY spring ./spring
COPY run_spring.py /spring/
COPY requirements.txt /spring/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "run_spring.py"]