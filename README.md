<p align="center" style="height: 70%;">
   <img alt="scrape.py" src="./assets/logo.svg" /><br/>
scrape.py is a product scraper for https://www.dentalinstall.com/shop using Python FastAPI
</p>

# Capabilities

- Scrapes the product name, price, and image from each page of the catalogue (it’s not necessary to open each product
  card).
- Different settings can be provided as input, but implements only two optional settings:
    - The first one will limit the number of pages from which we need to scrape the information (for example, 5 means
      that we want to scrape only products from the first 5 pages).
    - The second one will provide a proxy string that tool can use for scraping
- Stores the scraped information in a database. For simplicity, stores it on local storage as a JSON file in the
  following format:

```jsx
[
{
"product_title":"",
"product_price":0,
"path_to_image":"", # path to image at your PC
}
]
```

- At the end of the scraping cycle, notifies designated recipients about the scraping status - simple message that
  states how many products were scraped and updated in DB during the current session. For simplicity, this information
  is printed in the console. However, there are other easy ways to use another notification strategy. If the scraped
  product price has not changed, doesn't update the data of such a product in the DB.
- Provides a simple retry mechanism for scraping, e.g. if a page cannot be reached because of a destination site server
  error, retries it in N seconds.
- Provides endpoint authentication using a static token.
