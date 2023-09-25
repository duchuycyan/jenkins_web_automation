FROM hub.paas.vn/public/python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ALLOWED_HOSTS pricelist-test-self.apps.lab.okd.fis.vn

EXPOSE 80