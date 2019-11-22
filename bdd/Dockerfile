FROM postgres:10

ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD user
ENV POSTGRES_DB hashtagbdd

ADD createdb.sql /docker-entrypoint-initdb.d/

