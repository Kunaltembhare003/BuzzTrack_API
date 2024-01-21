# FizzBuzz API

This is a simple Flask-based REST API that provides a FizzBuzz endpoint and a statistics endpoint. The FizzBuzz API generates FizzBuzz sequences based on user-defined parameters and keeps track of usage statistics.

## Tabel of Contents
- [Getting Started](#Getting-Started)
- [Third-party Libraries](#Third-Party-Libraries)
- [Endpoints](#Endpoints)
- [Running the Server](#Running-the-Server)
- [Testing](#Testing)

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

## Third-party Libraries
This project utilizes the following third-party libraries:

* Flask: Web framework for building the REST API.

* Marshmallow: Used for object serialization and validation of input data.

* Flask-Limiter: Implements rate limiting to prevent abuse and control the number of requests.

* Requests: Simplifies making HTTP requests in the unit tests.



## Endpoints

### FizzBuzz

* Endpoint: '/fizzbuzz'
* Method: 'GET'

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

## Running the server
    ```bash
    python app.py

By default, the server runs in the debug mode.

## Testing Server
To run the unit test, excute the following command:
    ```bash
    python testunit.py


# API documentation
For detailed API documentation, refer to the API Documentation.





