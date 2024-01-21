# FizzBuzz API

This is a simple Flask API that implements the FizzBuzz algorithm with customizable parameters. It also includes basic input validation using Marshmallow.

## Getting Started

To run the FizzBuzz API locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fizzbuzz-api.git
   cd fizzbuzz-api

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

1. Run the Flask application:
    ```bash
    python app.py

The API will be accessible at 'http://localhost:5000'.

## Endpoints

### FizzBuzz

* Endpoint: '/fizzbuzz'
* Method: 'GET'
* Parameters:
    * 'int1' (integer, required): First divisor.
    * 'int2' (integer, required): Second divisor.
    * 'limit' (integer, required): Upper limit for FizzBuzz.
    * 'str1' (string, required): String to be displayed for numbers divisible by int1.
    * 'str2' (string, required): String to be displayed for numbers divisible by int2.

### Exaple Request
    ```bash
    curl -X GET "http://localhost:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz"

### Example Response
    ```json
    ["1","2","fizz","4","buzz","fizz","7","8","fizz","buzz","11","fizz","13","14","fizzbuzz"]

## Statistic

* Endpoint: '/statistics'
* Method: 'GET'

### Example Request
    ```bash
    curl -X GET "http://localhost:5000/statistics"

### Example Response
    ```json
    {"most_used_request": {
    "int1": 3,
    "int2": 5,
    "limit": 15,
    "str1": "fizz",
    "str2": "buzz"},
    "hits": 1}

## Input validation
Input parameters for the FizzBuzz endpoint are validated using Marshmallow. If the input is invalid, the API will return an error message specifying the validation failure.







