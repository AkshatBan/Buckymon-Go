# Use latest MySQL image from Docker Hub
FROM mysql:latest

# Setting up the environment variables
ENV MYSQL_ROOT_PASSWORD=databasemysql


# Copy the DB setup and test scripts into the container
COPY db_setup.sql /docker-entrypoint-initdb.d/
COPY db_test.sql .
COPY clean_db.sql .

# Expose port
EXPOSE 3306