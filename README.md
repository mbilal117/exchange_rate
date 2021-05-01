# exchange_rate
An API to get exchange rate from one currency - digital or Physical - to another.

## Clone repository

* create .env file and change the required database and api key values
* pip install -r requirement.txt
* Run python manage.py migrate
* Run python manage.py collectstatic

## Get
 http://localhost:8000/api/v1/quotes
## Response
[{
    "id": 4,
    "from_currency": "BTC",
    "from_currency_name": "Bitcoin",
    "to_currency": "USD",
    "to_currency_name": "United States Dollar",
    "exchange_rate": "57544.88000000",
    "last_refreshed": "2021-05-01T14:25:01Z"
},
{
    "id": 5,
    "from_currency": "BTC",
    "from_currency_name": "Bitcoin",
    "to_currency": "USD",
    "to_currency_name": "United States Dollar",
    "exchange_rate": "57544.88000000",
    "last_refreshed": "2021-05-01T14:25:01Z"
}]


## POST
* Params = {
    "from_currency":"BTC",
    "to_currency":"USD"
}

## Reponse
{
    "id": 4,
    "from_currency": "BTC",
    "from_currency_name": "Bitcoin",
    "to_currency": "USD",
    "to_currency_name": "United States Dollar",
    "exchange_rate": "57544.88000000",
    "last_refreshed": "2021-05-01T14:25:01Z"
}
