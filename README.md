# Wellth Water


Wellth Water is an app for logging and tracking drink amounts & types that you choose to give up over a months time in order to instead donate the money you would have spent to fund a clean water well for people around the world who do not access to clean water.  Wellth Water then uses the Stripe API in order to process a payment for your total amount you saved over the month.

**"We as Wellth Water believe in the power of giving up a small amount of your own personal wealth, in order to build a well to give people access to clean water."**

Wellth Water is a Mod4 cross-pollination project at [Turing School of Software & Design](https://turing.io/) where three students *(2 students from the backend program, and 1 student from the frontend program)* with 6 months experience in software development create an Angular/Typescript framework on the frontend, while consuming a Django API on the backend, while using the Stripe API in order to process payments.



#### Wellth Water App Production Link:

http://

#### Wellth Water Backend API Production Link:

http://wellth-water.herokuapp.com/

#### Wellth Water Frontend App - Github Repository:
https://github.com/shannonmoranetz/Wellth_Water_FE

#### Wellth Water Backend API - Github Repository:
https://github.com/justinmauldin7/Wellth_Water_BE

#### Wellth Water Project Board Link:
https://github.com/justinmauldin7/Wellth_Water_BE/projects/1






## Wellth Water API Endpoints:

##### Get All Users:

```
GET /api/v1/users

[
    {
        "id": 17,
        "name": "Justin",
        "email": "Justin@gmail.com"
    },
    {
        "id": 18,
        "name": "Ben",
        "email": "Ben@gmail.com"
    },
    {
        "id": 19,
        "name": "Shannon",
        "email": "Shannon@gmail.com"
    }
]
```


##### Get All Entries:
```
GET /api/v1/entries

[
    {
        "user_id": 1,
        "type": "wine",
        "amount": 299,
        "created_at": "2019-04-04T18:43:17.276189Z"
    },
    {
        "user_id": 1,
        "type": "mixed drinks",
        "amount": 299,
        "created_at": "2019-04-04T18:43:17.277840Z"
    },
    {
        "user_id": 1,
        "type": "tea",
        "amount": 550,
        "created_at": "2019-04-04T18:43:17.279036Z"
    },
    {
        "user_id": 1,
        "type": "coffee",
        "amount": 350,
        "created_at": "2019-04-04T18:43:17.281216Z"
    },
    {
        "user_id": 1,
        "type": "beer",
        "amount": 350,
        "created_at": "2019-04-04T18:43:17.291405Z"
    },
    {
        "user_id": 1,
        "type": "soda",
        "amount": 350,
        "created_at": "2019-04-04T18:43:17.297320Z"
    }    
]
```

##### Get One User And Their Entries:

```
/api/v1/users/4/entries/

{
    "id": 4,
    "name": "Sal",
    "email": "Sal@gmail.com",
    "entries": [
        {
            "user_id": 4,
            "type": "beer",
            "amount": 550,
            "created_at": "2019-04-05T21:43:59.063906Z"
        },
        {
            "user_id": 4,
            "type": "beer",
            "amount": 550,
            "created_at": "2019-04-05T21:43:59.068701Z"
        },
        {
            "user_id": 4,
            "type": "coffee",
            "amount": 250,
            "created_at": "2019-04-05T21:43:59.073146Z"
        }
    ]
}
```

##### Get All Transactions:
```
GET /api/v1/transactions

[]
```


##### Create an Entry:
```
POST /api/v1/entries/4/tea/240/

{
    "user_id": 4,
    "drinktype": "tea",
    "amount": 240,
    "created_at": "2019-04-06T22:43:03.396548Z"
}
```

##### Create a Transaction:
```
POST /api/v1/transactions/1/10000
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

#### Prerequisites:

* Install Python (Version 3.7.3) [Download here](https://www.python.org/downloads/)
* Heroku Account - (Create free account [here](https://signup.heroku.com/) if you don't have on already.)


### Installing:

To run this application locally, clone this [repo](https://github.com/justinmauldin7/Wellth_Water_BE) and follow the steps below:

1) Install dependencies:
```
$ pip install -r requirements.txt
```

2) Create virtual environment:
```
$ virtualenv --python=python3 env
```

3) Active virtual environment:
```
$ python  env/bin/activate
```

4) Create postgreSQL database:
```
$ psql -d postgres
  > CREATE USER wellth_water;
  > CREATE DATABASE wellth_water_db;
```

5) Migrate database:
```
$ python manage.py migrate
```

6) Start your server:
```
$ python manage.py runserver
```

7) Open browser and navigate to:

```
localhost:8000/api/v1/users
localhost:8000/api/v1/entries
localhost:8000/api/v1/transactions
```


## Running the Test Suite

Wellth Water has a suite of tests for every API endpoint in the app.

#### Running the Full Test Suite:

From the root of the directory, type the below command to run the full test suite:

```
$ python manage.py test
```


## Deployment

To deploy this app through Heroku as we have, you can follow these [instructions](https://devcenter.heroku.com/articles/git) on Heroku's website.

## Built With

* [Python - Version 3.7.3](https://docs.python.org/3/) - Base code language for backend
* [Typescript - Version 3.2.2](https://www.typescriptlang.org/docs/home.html) - Base code language for backend
* [Django - Version 2.0.3](https://docs.djangoproject.com/en/2.2/) - Backend Web framework used
* [AngularJS - Version 7.2.0](https://angularjs.org/) - Frontend Web framework used
* [Django REST API framework](https://www.django-rest-framework.org/) - API framework used
* [PostgreSQL](https://www.postgresql.org/docs/) - Database used
* [Psycopg2](https://pypi.org/project/psycopg2/) - Database adapter for the Python
* [Stripe API](https://stripe.com/docs/api) - Used to process payments
* [TravisCI](https://travis-ci.org/) - Used for continuous integration
* [Heroku](https://www.heroku.com/) - Used to deploy to production


## Contributing

If contributing to the backend repository, you can submit a pull request [here](https://github.com/justinmauldin7/Wellth_Water_BE).

If contributing to the frontend repository, you can submit a pull request [here](https://github.com/shannonmoranetz/Wellth_Water_FE).

We will review the request and merge it into master if it looks good.


## Authors

* **Ben Lee** - *Team member* - [Ben's Github](https://github.com/bendelonlee)
* **Justin Mauldin** - *Team member* - [Justin's Github](https://github.com/justinmauldin7)
* **Shannon Moranetz** - *Team member* - [Shannon's Github](https://github.com/shannonmoranetz)


## Acknowledgments

* Thanks to our Mod4 instructors [Corey Westerfield](https://github.com/corywest) & [Dione Wilson](https://github.com/dionew1) for all their help and insight on this project.

* Thanks to all our other fellow [Turing School of Software & Design](https://turing.io/) - Mod4 classmates that helped think through design decisions on this project as well.
