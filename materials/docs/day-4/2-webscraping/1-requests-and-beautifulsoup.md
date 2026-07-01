# Scraping part 1: requests and BeautifulSoup

*By [Erik Hekman](mailto:erik.hekman@hu.nl)*

## Objectives

In this module, you will learn:

- Why a web page is really just an HTTP response containing HTML
- How to download that HTML with the `requests` library
- How to parse and navigate the HTML with **BeautifulSoup**
- How to pull structured fields (title, link, date, …) out of a list of results

## From API to web page

In the previous module you sent a `GET` request to an API and received **JSON**.
Scraping a website is the *same idea* with a different response format: you send
a `GET` request to a normal page URL and the server returns **HTML**.

Rendering a website is nothing more than your browser making a `GET` request and
drawing the HTML it gets back. When we scrape, we make that same request from
Python and read the HTML ourselves — no browser required.

/// define
HTML

- *HyperText Markup Language*: the nested tag structure (`<div>`, `<a>`, `<p>`, …) that describes a web page. BeautifulSoup lets us search this structure.
///

## The BeautifulSoup library

You already have `requests` from the API session. To parse HTML we add
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), a friendly
library for searching and navigating the tag structure.

### Installing

Install BeautifulSoup into your virtual environment:

```
pip install beautifulsoup4
```

Note the package is called `beautifulsoup4`, but you **import** it as `bs4`:

```python
from bs4 import BeautifulSoup
```

/// warning | Forgetting something?
Update your requirements file with the new library!
///
## The example: PBS NewsHour

Throughout parts 1 and 2 we scrape search results from
[PBS NewsHour](https://www.pbs.org/newshour/). It is a large, well-structured
news site, and searching returns a tidy list of articles we can turn into data.

Our starting page is a search for the phrase *"artificial intelligence"*:

```
https://www.pbs.org/newshour/search-results?q=%22artificial%20intelligence%22
```

Open it in your browser. Everything we do in code, you should first be able to
see with your own eyes.

## Step 1 — download the page

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.pbs.org/newshour/search-results?q=%22artificial%20intelligence%22'
res = requests.get(url)

print(res.status_code)      # 200 means OK
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.find('title').get_text())
```

/// tip | Always check what you got back
Look at `res.status_code` (200 = OK) and `len(res.content)` before parsing.
A `403`, a `202`, or a suspiciously tiny response usually means the site
did **not** give you the real page.
///
## Step 2 — find elements

Using the browser's **Inspect element** tool, we can see that every result
title carries the CSS class `search-result__title`.

- `soup.find(...)` returns the **first** match.
- `soup.find_all(...)` returns a **list** of every match.

```python
items = soup.find_all(class_='search-result__title')
for item in items:
    print(item.get_text().strip())
```

## Step 3 — build a full record

A title alone is not very useful. Each result is wrapped in an element with the
class `search-result`. Inside it we can dig for the pieces we want:

```python
items = soup.find_all(class_='search-result')

for item in items:
    title       = item.find(class_='search-result__title').get_text().strip()
    link        = item.find('a')['href']          # read the href attribute
    description = item.find('p').get_text().strip()
    date        = item.find(class_='search-result__date').get_text().strip()
    print(title, '—', date)
    print(link)
```

Two things to notice:

- `.get_text()` reads the **text** inside an element; `item['href']` reads an
  **attribute**.
- We select by class (`class_=`), by tag name (`'a'`, `'p'`), or by both.

/// warning | Scraping is maintenance work
Your code depends on the site's structure. If PBS renames a class, your
scraper breaks. That is normal — a scraper is software you maintain, not a
one-time script. Prefer stable anchors (like `<meta>` tags, see part 2) when
you can.
///
## Exercise: scrape a recipe from BBC Good Food

Now apply the same three steps to a richer, real-world site — a recipe page:
[Next level chilli con carne](https://www.bbcgoodfood.com/recipes/next-level-chilli-con-carne).

Build a dictionary describing the recipe with its **name**, a list of
**ingredients**, the **steps**, how many it **serves**, the **cook time** and
the **calories**. Everything comes straight from the HTML tags — exactly the
`find` / `find_all` / `select` skills from the demo.

Useful selectors (find them yourself with Inspect element first!):

- title: the page `<h1>`
- ingredients: `ul.ingredients-list` → `li.ingredients-list__item`
- method steps: `li.method-steps__list-item` (the step text is inside a
  `.editor-content` element; the "step 1" label is a separate heading you can
  ignore)
- nutrition: `ul.nutrition-list` → `li.nutrition-list__item` (each reads like
  `"kcal 463"`, `"fat 24 g"`, …)
- serves / prep / cook: `.recipe-cook-and-prep-details__item` (these read
  `"Serves 8"`, `"Prep: 25 mins"`, `"Cook: 3 hrs"`)

```python
name = soup.find('h1').get_text().strip()

ingredients = [li.get_text(' ', strip=True)
               for li in soup.select('ul.ingredients-list li.ingredients-list__item')]

steps = []
for li in soup.select('li.method-steps__list-item'):
    steps.append(li.find(class_='editor-content').get_text(strip=True))
```

/// tip | Use `get_text(' ', ...)` for the ingredients
An ingredient's amount and name sit in separate tags. Passing a space to
`get_text(' ', strip=True)` keeps them apart — `"2 dried ancho chillies"`
instead of `"2dried ancho chillies"`.
///
/// tip | Stretch goals if you finish early
- A [collection page](https://www.bbcgoodfood.com/recipes/collection/chilli-recipes)
  lists many recipes. Find every recipe link on it (they look like
  `/recipes/<slug>`), scrape each into your dictionary, and you have a
  **dataset** — exactly the idea of [part 2](2-pagination-and-data.md).
- Which recipe has the fewest ingredients?
///
/// note | A more robust shortcut exists (for later)
Pages like this *also* embed the whole recipe as machine-readable JSON in a
`<script type="application/ld+json">` tag (the
[schema.org/Recipe](https://schema.org/Recipe) standard). That can be more
stable than parsing HTML, and it becomes really useful in
[part 3](3-dynamic-pages.md) — but for this exercise, practise the HTML-tag
approach above.
///