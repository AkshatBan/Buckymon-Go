FROM python:3.9-slim
ENV MYSQL_ROOT_PASSWORD=databasemysql
WORKDIR /app
COPY requirements.txt ./
RUN pip install Flask Flask-Cors PyMySQL -r requirements.txt
COPY Backend ./
EXPOSE 5000
