# FizzBuzz API

This is a simple Flask-based REST API that provides a FizzBuzz endpoint and a statistics endpoint. The FizzBuzz API generates FizzBuzz sequences based on user-defined parameters and keeps track of usage statistics.

## Tabel of Contents
- [Getting Started](#Getting-Started)
- [Third-party Libraries](#Third-Party-Libraries)
- [Endpoints](#Endpoints)
- [Testing](#Testing)

## Getting Started

To run the FizzBuzz API locally, follow these steps:

1. Clone the repository:

   ```bash
   https://github.com/Kunaltembhare003/BuzzTrack_API.git
   cd BuzzTrack_API

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

1. Run the Flask application:
    ```bash
    python app.py

The API will be accessible at 'http://localhost:5000'.
By default, the server runs in the debug mode.

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

Let's break down the components of the cURL command:
* -X GET: Specifies the HTTP method to be used, in this case, it's a GET request. 
* "http://localhost:5000/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz": The URL to which the GET request is being made. This URL includes query parameters that will be used as inputs for the FizzBuzz program.
* int1=3: The first integer for the FizzBuzz program.
* int2=5: The second integer for the FizzBuzz program.
* limit=15: The limit or length of the FizzBuzz sequence.
* str1=fizz: The string to be used when a multiple of int1 is encountered in the FizzBuzz sequence.
* str2=buzz: The string to be used when a multiple of int2 is encountered in the FizzBuzz sequence.

So, when you run this cURL command, it sends a GET request to the specified URL with the provided query parameters, and the server at "http://localhost:5000/fizzbuzz" is expected to respond with the corresponding FizzBuzz sequence based on the given parameters.

### Example Response
    ```json
    ["1","2","fizz","4","buzz","fizz","7","8","fizz","buzz","11","fizz","13","14","fizzbuzz"]

### Statistic

* Endpoint: '/statistics'
* Method: 'GET'

### Example Request
    ```bash
    curl -X GET "http://localhost:5000/statistics"


## Testing Server
To run the unit test, excute the following command:
    ```bash
    python test_fizzbuzz.py


# API documentation
For detailed API documentation, refer to the [API Documentation](https://github.com/Kunaltembhare003/BuzzTrack_API/blob/main/API_Documentation.md).





