FROM python:3.4-alpine
ADD . /code
WORKDIR /code
CMD ["python", "adder.py"]

