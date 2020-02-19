# DS2020
Distributed Systems 2020 course work

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have following software installed.

```
docker
mysql server
python
```

### Installing

Install docker. Find instructions for your OS from https://docs.docker.com/install/ 

Install mysql server using there instructions: https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/general-installation-issues.html 

Log in to the mysql.

```
mysql -u root -p
```

Create database and use it.

```
CREATE DATABASE sensorDB;
USE sensorDB;
```

Create table.

```
CREATE TABLE sensorTable(id INT NOT NULL AUTO_INCREMENT, sensor INT, data INT, submission_date TIMESTAMP, PRIMARY KEY ( id ));
```


## Deployment

To deploy the system, run the following commands.

```
./setup-vms.sh

python cloud/app.py 
```

## Built With

* [Docker](https://www.docker.com/) - Deployment and virtualization.
* [Python](https://www.python.org/) 
* [Flask](https://palletsprojects.com/p/flask/) - Web service deployment
* [MySQL](https://www.mysql.com/) - Database





