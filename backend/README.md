# Govtech 2021 TAP Assignment - URL Shortener Backend

Backend of URL Shorterner service. 

View [live demo](https://govtech-url-shorterner.herokuapp.com/docs)



## Requirements

Python 3.6+

PIP



## Installation

1. Create virtual environment

   ```
   $ virtualenv venv
   ```

2. Install required packages

   Mac OS / Linux:

   ```
   $ source venv/bin/activate
   ```

   Windows:

   ```
   $ source venv\Scripts\activate
   ```

3. Install required packages

   ```
   $ pip install -r requirements.txt
   ```



## Connect Database

1. Setup a mysql database

2. Add database credentials at the end of `venv/bin/activate`

   ```
   # Set server variables
   export DB_USER="admin"
   export DB_PASSWORD="password"
   export DB_PORT=3306
   export DB_URL=database.xxxx.us-east-1.rds.amazonaws.com
   export DB_NAME=db
   ```

   

## Run the app

Change directory to `src` and run the app. 

```
$ cd src
$ uvicorn index:app --reload
```



## Run test

Unit testcases are written in `src/test`. To run all the testcases, change directory to `src` and run pytest. 

```
$ cd src
$ PYTHONPATH=. pytest
```

