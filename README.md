# Wellth Water

## Log drink money and donate to well constructions (back-end)

* * *

### Log, track and donate to help provide clean water worldwide.

![Screenshot](https://imgur.com/oWTyRPh.jpg)

### Base Endpoint

```
http://wellth-water.herokuapp.com/
```

### Features

*   Drink logs saved to production back-end
*   User login/logout functionality

### Tech Stack

*   Python ~ Psycopg2 & Django
*   PostgreSQL
*   TravisCI & Heroku

### Installation

* Front-end:
```
https://github.com/shannonmoranetz/Wellth_Water_FE
```
* Dependencies:
```
pip install -r requirements.txt
```
* Start:
```
python manage.py runserver
```
* Test:
```
python manage.py test
```

### Documentation

##### Users ~ GET

All Users:
```
/api/v1/users
```

##### Entries ~ GET

All Entries:
```
/api/v1/entries
```

##### Entries ~ POST

Query by entry:
```
/api/v1/entries/4/tea/240/
```

##### Users ~ GET:

Query by ID:
```
/api/v1/users/1/entries
```

### Contributors

* [Shannon Moranetz](https://github.com/shannonmoranetz)
* [Justin Mauldin](https://github.com/shannonmoranetz)
* [Ben Lee](https://github.com/bendelonlee)