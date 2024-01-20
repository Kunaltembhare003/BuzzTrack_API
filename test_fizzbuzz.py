import unittest
import requests

class TestFizzBuzzServer(unittest.TestCase):
    base_url = "http://127.0.0.1:5000"

    def test_fizzbuzz_endpoint(self):
        url = f"{self.base_url}/fizzbuzz"
        params = {"int1": 3, "int2": 5, "limit": 15, "str1": "fizz", "str2": "buzz"}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_output = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
        self.assertEqual(data, expected_output)

    def test_statistics_endpoint(self):
        url = f"{self.base_url}/statistics"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("most_used_request", data)

    def test_fizzbuzz_custom_params(self):
        url = f"{self.base_url}/fizzbuzz"
        params = {"int1": 2, "int2": 7, "limit": 14, "str1": "even", "str2": "odd"}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        expected_output = ["1", "even", "3", "even", "5", "even", "odd", "even", "9", "even", "11", "even", "13", "evenodd"]
        self.assertEqual(data, expected_output)

if __name__ == "__main__":
    unittest.main()
