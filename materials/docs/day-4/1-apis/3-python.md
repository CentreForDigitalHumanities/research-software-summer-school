# Using Python to interact with an API

## Objectives
In this module, you will learn:

 - How to use the `requests` library to make HTTP requests
 - How to pass query parameters
 - How to read the response status and parse JSON


## The `requests` library
Python's standard library can make HTTP requests, but it is a bit sluggish. The [`requests`](https://docs.python-requests.org) library is very user-friendly (and powerful!) and is widely used.

### Installing
Install `requests` into your virtual environment:
```bash
pip install requests
```

/// details | Forgetting something?
    type: warning

Update your requirements file with the new library!
///


## Making a GET request

```python
import requests

response = requests.get("https://www.fruityvice.com/api/fruit/banana")
```

There are two ways to construct a query with parameters:


- Query parameters can be appended to the URL manually:
```
url = "https://www.fruityvice.com/api/fruit/fat?min=5"
```


- Let requests build the URL for you by supplying a `params` parameter to the request. This is much cleaner.
```python
response = requests.get(
    "https://www.fruityvice.com/api/fruit/fat",
    params={"min": 5},
)

print(response.url)     # confirm that requests built the right URL
```

`requests` will encode and append the parameters to the URL for you.


## Working with the response

The `response` object contains everything the server sent back. See [this w3schools article](https://www.w3schools.com/Python/ref_requests_response.asp) for documentation on the response object.

```python
print(response.status_code)     # hopefully, 200

data = response.json()          # parses the JSON response into a Python object
print(data)                     # inspect the output
print(data["name"])
```

/// details | Always check the status code
    type: tip

It is a good idea to always check if a response was succesful. Below are some ways to do so:

```python
assert 200 <= response.status_code < 300
```

```python
response.raise_for_status()  # built-in method of requests.response, raises an exception if unsuccesful
```

If a request failed, the response body can still have valuable information on what went wrong.
///


## Exercise

Repeat the Fruityvice exploration from the previous section, but this time entirely in Python.
You can copy the code examples above to a new Python file, and modify it.

 - Look up your least favourite fruit by name and print its protein content.
 - Request all fruits and find the one with the highest sugar content.
 - Try requesting a fruit that does not exist. What status code do you get? Does the response contain any information?

/// details | Bonus points
    type: tip

 - Be neat and reproducible! Use functions for repeated code, naming conventions, documentation, etc.
 - Check in the Python file under version control.
///