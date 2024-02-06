FROM python:latest

RUN apt update && apt install nginx -y

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY . .

RUN pip install --upgrade pip
RUN pip install --upgrade django
# RUN cat requirements.txt | xargs -n 1 pip install --root-user-action=ignore --no-cache-dir --ignore-installed
RUN pip install --root-user-action=ignore --no-cache-dir --ignore-installed -r requirements.txt

WORKDIR /
COPY run.sh .

RUN chmod +x run.sh

CMD ["./run.sh"]