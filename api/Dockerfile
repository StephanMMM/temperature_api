FROM python:3.10
WORKDIR /temperature_api
COPY requirements.txt ./app/
RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt
COPY . .
EXPOSE 80