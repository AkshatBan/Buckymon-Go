FROM python:3.9-slim
ENV MYSQL_ROOT_PASSWORD=databasemysql
WORKDIR /app
COPY Backend ./
RUN pip install -u Flask
EXPOSE 5000
