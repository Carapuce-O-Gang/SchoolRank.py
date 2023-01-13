FROM python:latest

WORKDIR /usr/src

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080