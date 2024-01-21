# FizzBuzz API Documentation

## **FizzBuzz Endpoint**

* Endpoint: '/fizzbuzz'
* Method: 'GET'
* Parameters:
    * 'int1' (integer, required): First divisor.
    * 'int2' (integer, required): Second divisor.
    * 'limit' (integer, required): Upper limit for FizzBuzz.
    * 'str1' (string, required): String to be displayed for numbers divisible by int1.
    * 'str2' (string, required): String to be displayed for numbers divisible by int2.

Example

    ```bash
    curl -X GET "http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz"

Response

       ```json
       ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]

**Error response**

* 400 Bad Request: Invalid input parameters
* 429 Too Many Requests: Rate limit exceeded


## **Statistics Endpoints**

**URL**: '/statistics'
**Method**: 'GET'

Example

       ```bash
       curl -X GET "http://localhost:5000/statistics"

Response

       ```json
       {
       "most_used_request": {
           "int1": 3,
           "int2": 5,
           "limit": 15,
           "str1": "fizz",
           "str2": "buzz"
       },
       "hits": 1
       }

## Rate Limiting

The FizzBuzz endpoint is subject to rate limiting to prevent abuse. The current rate limits are as follows:

* 5 requests per minute.
* 200 requests per day.
* 50 requests per hour.

## Input validation
Input parameters for the FizzBuzz endpoint are validated using Marshmallow. If the input is invalid, the API will return an error message specifying the validation failure.

       ```json
       {
           "error": "Input validation failed",
           "details": {
               "int1": ["Must be greater than or equal to 1."],
               "int2": ["Must be greater than or equal to 1."],"limit": ["Must be greater than or equal to 1."]
               }
       }
