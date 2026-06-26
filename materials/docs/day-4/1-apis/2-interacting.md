# Interacting with an API
## Objectives
In this module, you will learn:

 - How to send a HTTP GET request and receive a response
 - How to build a request URL and use query parameters

## Example API: Fruityvice
- [Fruityvice](https://www.fruityvice.com) is a small open API that returns nutritional information about fruit. It requires no API key.
- There is documentation on the website to help you construct the requests you will need in the exercises.
- The website also contains a playground where you can type in URLs and receive the response in a text box.

## Making a GET request

An HTTP request is essentially a URL with some extra information attached. At its simplest, a `GET` request is just a URL you point your code at. The server processes it and returns a response — usually in **JSON** format.

You can execute a `GET` request in many ways. For example, in the command line execute:

```bash
curl https://www.fruityvice.com/api/fruit/banana
```

Alternatively, paste the URL in your browser. Your browser will then show the response of the request.

## JSON
As mentioned, many APIs will respond with **JSON** data.
/// define
JSON

- *JavaScript Object Notation*: a lightweight text format for structured data. It uses key–value pairs and is the most common format for API responses, though other return formats exist.
///


/// details | HTML responses
One very common response format is HTML. Note that rendering a website is actually nothing more then making a `GET` request to a server, and getting a HTML file in response. Your browser then renders this HTML as a website.
We will leverage this fact later on when we scrape the web.
///

JSON maps very well to Python dictionaries. A single JSON entry looks a lot like a nested Python dictionary:

```json
{
  "name": "Banana",
  "id": 1,
  "family": "Musaceae",
  "order": "Zingiberales",
  "genus": "Musa",
  "nutritions": {
    "calories": 96,
    "fat": 0.2,
    "sugar": 17.2,
    "carbohydrates": 22,
    "protein": 1
  }
}
```

Multiple entries look a lot like a Python list:
```json
[
  {
    "name": "Persimmon",
    "id": 52,
    "family": "Ebenaceae",
    "order": "Rosales",
    "genus": "Diospyros",
    "nutritions": {
      "calories": 81,
      "fat": 0,
      "sugar": 18,
      "carbohydrates": 18,
      "protein": 0
    }
  },
  {
    "name": "Strawberry",
    "id": 3,
    "family": "Rosaceae",
    "order": "Rosales",
    "genus": "Fragaria",
    "nutritions": {
      "calories": 29,
      "fat": 0.4,
      "sugar": 5.4,
      "carbohydrates": 5.5,
      "protein": 0.8
    }
  }
]
```
Conversion of JSON objects to and from Python objects is very easy, and mostly occurs automatically when using Python HTTP packages.


## Building the URL
Most APIs let you refine your request by making the url more specific. Let's take a look at two examples:

Request data on all the fruit in the API:
```
https://www.fruityvice.com/api/fruit/all/
```

Request data on a specific fruit:
```
https://www.fruityvice.com/api/fruit/banana/
```

How URLs are to be constructed is often found in the API documentation. 

## Query parameters

Sometimes, APIs allow the client to supply extra information in a `GET` request. This is done through **query parameters**: key–value pairs appended to the URL after a `?`.

Parameters are separated by `&`. The API documentation will tell you which parameters are available and what values they accept.


## Exercise: Explore the Fruityvice API
 - Open the [Fruityvice website](https://www.fruityvice.com) and explore its documentation.
 - Try constructing a few URLs directly in your browser:
    - Look up your favourite fruit by name
    - See what happens when you request a fruit that doesn't exist
 - Note the structure of the JSON response — what fields does it contain?
 - Build some more complex requests:
    - List all the fruits of a specific genus (use the genus of the previous request)
    - List all fruits that are low in calories (under 100kcal)

/// details | How to make the requests
    type: hint
You can use one of three methods to make `GET` requests:

- Paste the URL in your browser
- Use `curl <url>` in the command line
- Use the playground on the Fruityvice website
///
