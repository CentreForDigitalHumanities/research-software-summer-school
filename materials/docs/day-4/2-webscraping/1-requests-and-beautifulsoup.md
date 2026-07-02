# Scraping part 1: requests and BeautifulSoup

*By [Erik Hekman](https://www.linkedin.com/in/erikhekman/)*

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

/// details | Forgetting something?
    type: warning

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

Always glance at `res.status_code` (200 = OK) before parsing — a `403`, a `202`,
or a suspiciously tiny response usually means you did not get the real page.

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

/// details | Scraping is maintenance work
    type: warning

Your code depends on the site's structure. If PBS renames a class, your
scraper breaks. That is normal — a scraper is software you maintain, not a
one-time script. Prefer stable anchors (like `<meta>` tags, see part 2) when
you can.
///

## Exercise: scrape a list of recipes from BBC Good Food

The demo pulled a **list** of results from one PBS search page. Do the same on a
recipe site. Open a BBC Good Food search and look at the results in your browser:
[bbcgoodfood.com/search/recipes?q=chilli](https://www.bbcgoodfood.com/search/recipes?q=chilli).

Build a **list** where each recipe is a dictionary with a **title** and a
**url** — exactly the `find` / `find_all` / `select` skills from the demo.

Useful selectors (confirm them with Inspect element first!):

- each recipe card: `article.card`
- the title inside a card: `h2.heading-4`
- the link inside a card: the card's `<a>` — its `href` is the recipe URL

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.bbcgoodfood.com/search/recipes?q=chilli'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(res.content, 'html.parser')

recipes = []
for card in soup.select('article.card'):
    title = card.find(class_='heading-4')
    link = card.find('a', href=True)
    if title and link:                       # skip cards that aren't recipes
        recipes.append({
            'title': title.get_text(strip=True),
            'url': link['href'],
        })

for recipe in recipes:
    print(recipe)
```

**Stretch goals (if you finish early):** add one more field you can see on each
card (for example the star rating). You will also notice some cards are
*premium* — how would you keep only the free `/recipes/` links? Collecting
*every* recipe across all the result pages is the job of
[part 2](2-pagination-and-data.md).