# docker run -it -d \
#        -p 5000:5000 \
#        -v <location of app config.py>:/config
#        --name app dechiada/sampleblogapp

FROM alpine:latest

EXPOSE 5000

COPY blog /blog
COPY requirements.txt /blog/requirements.txt
RUN apk --update add --no-cache python
RUN apk add --no-cache py2-psycopg2
RUN apk add --no-cache py-pip
RUN pip install --no-cache-dir -r /blog/requirements.txt

RUN ln -s /config/config.py /blog/config.py

CMD ["python","/blog/run.py"]
