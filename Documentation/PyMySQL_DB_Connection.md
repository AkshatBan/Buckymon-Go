# PyMySQL Database Connection
Below is the code and parameters necessary for connecting the backend to the database docker container

```
connection = pymysql.connect(host='172.17.0.2', 
                             user='root', 
                             password='databasemysql', 
                             database='Buckymon_Go_DB', 
                             cursorclass=pymysql.cursors.DictCursor)
```

The host refers to the container's ip address. This can be found by running `docker inspect <container_id_or_name> | grep IPAddress`.

By default, the docker container creates a root user for itself and assigns this root user whatever password was specified in the Dockerfile.

The database name can be found in db_setup.sql