# APIs
## Objectives
In this module, you will learn:

 - What an API is and why it is useful
 - The basics of HTTP

## What is an API?

An *Application Programming Interface* (API) is a way for two pieces of software to talk to each other. There is no need for human interaction (e.g. clicking, typing). 

/// define
API

- a defined interface that allows one program to request data or actions from another, without needing to know how the other program works internally.
///

Many APIs exist, in all kind of forms. Modern software heavily relies on a piece of software (e.g. the weather app on your phone) to "ask for" data over an internet connection (e.g. the weather data of a meteorological institute). There might be a lot of data processing going on at the server, but the client is not interested in that. It asks for the weather information for a particular area and time, and receives it from the interface.
For the purpose of this course, we will be exploring accessing APIs for the purpose of obtaining data for your coding practise.

## HTTP

*HyperText Transfer Protocol* (HTTP) is the foundation of data exchange on the web. When your code talks to an API, it does so by sending an **HTTP request** and receiving an **HTTP response**.
In human terms: one persons (the client) asks a question. The other person (the server) answers.

/// define
HTTP

- a request–response protocol: a client sends a request to a server, and the server sends back a response containing a status code and, usually, some data.

Here, a **client** is the entity making the request. In our case: our Python software. The **server** is whatever is hosting the API. 
///

We will not go too deep into the intricacies of HTTP, but some concepts are important for effectively using an API.

Each request uses a **method** that describes the intended action:

| Method | Meaning |
|--------|---------|
| `GET` | Retrieve data|
| `POST` | Send data / create a resource |
| `PUT` / `PATCH` | Update a resource |
| `DELETE` | Remove a resource |

For most data-fetching use cases you will only need `GET`. Occasionally, `POST` is used, for example when you need to supply some data to succesfully retrieve another piece of data.

The response always includes a **status code** that tells you whether the request succeeded:

 - `2xx` — success (e.g. `200 OK`). Happy times.
 - `4xx` — client error (e.g. `404 Not Found`, `401 Unauthorized`). These are the clients "fault".
 - `5xx` — server error (e.g. `500 Internal Server Error`). This is the servers "fault", something went wrong beyond your control.

 /// details | HTTP status codes
    type: tip
- [Wikipedia article on HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [Silly one: "HTTP 418: I'm a teapot"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/418)
///    

## API accessibility

Not all APIs are freely available. Some are open and require no authentication, but many are paid services or restrict access to registered users. In those cases, you will need an **API key**: a secret token you include with each request to prove your identity. These are often provided when making an account with an organisation that provides the API. The key may have limitations associated to it, e.g. only allowing you to make 5 requests per day. When the 6th request using the same key is made, the server will respond with an error.

/// details | Keep your API keys secret
    type: warning

Treat API keys like a password. Never hardcode it directly in your script or commit it to a public repository. Use environment variables or a secrets file that is listed in `.gitignore`.
///

A *good* API will include documentation that outlines the exact requests a client can make, and what responses it can expect. As with all things programming, in reality things are not always that neat. Some APIs take some experimentation to figure out.
