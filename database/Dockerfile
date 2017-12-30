#docker run -d \
#       --name postgres dechiada/sampleblogdb

FROM postgres:latest

ENV POSTGRES_USER john
ENV POSTGRES_PASSWORD potato12
ENV POSTGRES_DB microblog

VOLUME /docker-entrypoint-initdb.d
COPY microblog_creates.sql /docker-entrypoint-initdb.d/microblog_creates.sql
COPY microblog_inserts.sql /docker-entrypoint-initdb.d/microblog_inserts.sql
