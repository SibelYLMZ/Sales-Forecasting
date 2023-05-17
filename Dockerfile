FROM python:3.9
WORKDIR /service
COPY requirements.txt .
RUN pip install --upgrade pip setuptools
COPY . /service
CMD ["python", "./app.py"]