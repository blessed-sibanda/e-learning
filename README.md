# E-Learning

A django e-learning platform

## Features

- Content Management System for instructors to create courses, modules and their contents

- Course catalog where students can browse and enroll in different courses. 

- Students can access contents for their enrolled courses

- JSON RESTful API with endpoints to retrieve subjects, retrieve available courses and their contents, and enroll in a course

## SetUp Instructions

### Install [Git](https://git-scm.com/downloads)

Clone this repo and `cd` into it

```bash
$ git clone https://github.com/blessed-sibanda/e-learning
$ cd e-learning
```

### Install [Python](https://python.org/downloads) (version 3.8 or later)

Install pipenv using pip

```bash
$ pip install --user pipenv
```

Create a pipenv virtual environment

```bash
$ pipenv shell --python 3.8
```

Install pip dependencies

```bash
(e-learning) $ pipenv install
```

### Install [PostgreSQL](https://www.postgresql.org/download/)

After installing postgresql (using the above link), open `psql` shell

```bash
$ sudo su - postgres
$ psql
```

Create database

```psql
postgres=# CREATE DATABASE e_learning;
postgres=# CREATE USER e_learning;
postgres=# GRANT ALL ON DATABASE e_learning to "e_learning";
postgres=# ALTER USER e_learning PASSWORD '1234pass';
postgres=# ALTER USER e_learning CREATEDB;
postgres=# \q;
```

Exit postgresql shell

```bash
$ exit
```

Run database migrations (in project root folder)

```bash
(e-learning) $ python manage.py migrate
```

Create a superuser account

```bash
(e-learning) $ python manage.py createsuperuser
```

Load sample data to database using fixtures

```bash
(e-learning) $ python manage.py loaddata subjects groups users
```

### Install Memcached

Download Memcached from [https://memcached.org/downloads](https://memcached.org/downloads). If you are using
Linux, you can download and install Memcached using the following commands:

```bash
$ wget http://memcached.org/latest
$ tar -zxvf latest
$ cd memcached-1.x.x
$ ./configure && make && make test && sudo make install
```

If you are using macOS, you can install Memcached with the Homebrew package manager using the command brew install memcached . You can download Homebrew from https://brew.sh/ .

After installing Memcached, open a shell and start it using the following command:

```bash
$ memcached -l 127.0.0.1:11211
```

Run the development server

```bash
(e-learning) $ python manage.py runserver
```

Open the application in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)
