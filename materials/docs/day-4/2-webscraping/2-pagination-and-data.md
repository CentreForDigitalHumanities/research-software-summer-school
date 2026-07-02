# Scraping part 2: pagination and building a dataset

*By [Erik Hekman](https://www.linkedin.com/in/erikhekman/)*

## Objectives

In this module, you will learn:

- How to move from a single page to **many** pages (pagination)
- Why you should **download once and parse locally**, saving each page to its
  own file
- How to turn a folder of HTML into a clean dataset with a reusable function
- How to save your dataset as **JSON** and **CSV**
- How to scrape **politely**

## From one page to many

In part 1 we scraped a single search page. Real datasets span dozens or
hundreds of pages. The PBS NewsHour search puts the page number in the URL:

```
https://www.pbs.org/newshour/search-results?q=%22artificial+intelligence%22&pnb=2
```

First we find out how many pages there are. The pagination widget lists the page
numbers, and the **last** one is the total:

```python
total_pages = int(soup.find_all(class_='pagination__number')[-1].get_text())
```

Then we walk every page and collect the article links:

```python
import time

url_list = []
for page in range(1, total_pages + 1):
    time.sleep(2)                                  # be polite
    page_url = f'https://www.pbs.org/newshour/search-results?q=%22artificial+intelligence%22&pnb={page}'
    res  = requests.get(page_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.content, 'html.parser')
    for item in soup.find_all(class_='search-result'):
        url_list.append(item.find('a')['href'])
```

/// details | Be polite — `time.sleep()` is not optional
    type: warning

A room full of laptops requesting a site as fast as possible looks like an
attack. Pause between requests, identify yourself with a `User-Agent`, and
check the site's `robots.txt` and terms of service. Politeness keeps
scraping sustainable for everyone.
///

## Download once, save each page to its own file

Once you have the article URLs, download each page **once** and save it as its
own file. Then all your later experiments run on local files: fast,
reproducible, and kind to the server.

```python
import os

os.makedirs('data/PBS', exist_ok=True)
for url in url_list:
    filename = url.replace('https://www.pbs.org/newshour/', '').replace('/', '-').strip('-') + '.html'
    path = os.path.join('data/PBS', filename)
    if os.path.isfile(path):        # already downloaded? skip it
        continue
    time.sleep(2)
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(path, 'w', encoding='utf-8') as f:
        f.write(res.text)
```

You now have a folder of `.html` files — one article each. That folder *is* your
raw dataset.

## A reusable extraction function

This is the heart of the "Beyond Notebooks" idea: once you wrap your logic in a
**function**, it works on one file or on ten thousand. That is the difference
between a throwaway snippet and reusable research software.

News sites helpfully embed machine-readable metadata in `<meta>` tags in the
page `<head>`. These are far more stable than visible layout classes:

```html
<meta property="og:title" content="…">
<meta property="article:published_time" content="…">
```

```python
from bs4 import BeautifulSoup

def extract(path):
    """Read one saved HTML file and return a dict of its fields."""
    with open(path, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    def meta(prop, default=None):
        tag = soup.find('meta', property=prop)
        return tag['content'] if tag else default

    body = []
    content = soup.find(class_='body-text')
    if content:
        for p in content.find_all('p'):
            text = p.get_text().strip()
            if text and 'WATCH:' not in text:
                body.append(text)

    return {
        'title': meta('og:title'),
        'description': meta('og:description', 'No description found'),
        'published_time': meta('article:published_time'),
        'section': meta('article:section'),
        'content': ' '.join(body),
    }
```

/// details | Handle missing elements gracefully
    type: tip

Some pages simply lack a field. The little `meta()` helper returns a default
instead of crashing. A single broken page should never kill your whole run —
wrap `extract()` in a `try/except` and log the failures.
///

## Build and save the dataset

```python
import glob, json, csv

files = glob.glob('data/PBS/*.html')
dataset = []
for path in files:
    try:
        dataset.append(extract(path))
    except Exception as exc:
        print('could not parse', path, '->', exc)

# JSON keeps nested structure (e.g. lists of tags)
with open('data/pbs_articles.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

# CSV is flat and opens in any spreadsheet
with open('data/pbs_articles.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset)
```

/// define
JSON vs CSV

- Use **JSON** when your records are nested (lists, dictionaries within a record). Use **CSV** when the data is flat and you want to open it in Excel or load it into pandas. It is common to save both.
///

## Exercise: build a recipe dataset from BBC Good Food

Apply the same pipeline to the recipe site from part 1. BBC Good Food's search
paginates through the URL, too:

```
https://www.bbcgoodfood.com/search/recipes?q=chilli
```

Your steps:

1. **Paginate.** Pick a dish you like (`curry`, `pasta`, `cake`, `soup`…) and
   walk the search pages. Take a look at how pagination is handled.
   There is no page-count widget here, so **stop when a page adds nothing new**:

2. **Download once, one file each.** Save every recipe into `data/recipes/`,
   named after its slug (`.../butternut-chilli` → `butternut-chilli.html`).

3. **Extract with a function.** Reuse your part 1 recipe selectors
   (`h1`, `ul.ingredients-list li.ingredients-list__item`,
   `li.method-steps__list-item`, the nutrition and serves/cook items) inside an
   `extract(path)` function, and run it over the folder.

4. **Save + analyse.** Write the dataset to JSON, then answer: **which recipe
   has the most ingredients? The fewest calories?**

You are practising the whole pipeline: **paginate → download many files →
extract with a function → collect into a list → save**
