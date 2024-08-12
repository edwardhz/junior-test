FROM mysql:latest

COPY db_greetings_schema.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=admin123

# ENV MYSQL_DATABASE=prueba

USER mysql
