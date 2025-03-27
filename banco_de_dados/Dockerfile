FROM postgres:15-alpine

ENV POSTGRES_DB=ans_db
ENV POSTGRES_INITDB_ARGS="--encoding=UTF8" 

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=test_password

WORKDIR /docker-entrypoint-initdb.d/

COPY schema.sql /docker-entrypoint-initdb.d/
COPY data/ /docker-entrypoint-initdb.d/data/

RUN chown -R postgres:postgres /docker-entrypoint-initdb.d && \
    chmod -R 750 /docker-entrypoint-initdb.d 

EXPOSE 5432

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s \
            CMD pg_isready -U $POSTGRES_USER -d $POSTGRES_DB || exit 1
