import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def scrape_amazon(search_query, max_pages=3):
    # Setup Selenium
    options = webdriver.ChromeOptions()
    # Remove headless mode to see the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    products = []
    page = 1

    while page <= max_pages:
        # Perform search
        url = f'https://www.amazon.com/s?k={search_query}&page={page}'
        driver.get(url)

        # Let the page load
        time.sleep(100)

        # Parse HTML
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract product details
        for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
            name = item.h2.text.strip() if item.h2 else 'N/A'
            price = item.find('span', 'a-price-whole').text.strip() if item.find('span', 'a-price-whole') else 'N/A'
            rating = item.find('span', 'a-icon-alt').text.strip() if item.find('span', 'a-icon-alt') else 'N/A'
            reviews = item.find('span', {'class': 'a-size-base'}).text.strip() if item.find('span', {'class': 'a-size-base'}) else 'N/A'
            availability = item.find('span', 'a-declarative').text.strip() if item.find('span', 'a-declarative') else 'In Stock'
            img_url = item.find('img', {'class': 's-image'})['src'] if item.find('img', {'class': 's-image'}) else 'N/A'

            products.append({
                'name': name,
                'price': price,
                'rating': rating,
                'reviews': reviews,
                'availability': availability,
                'image_url': img_url
            })

        page += 1

    driver.quit()
    return products

if __name__ == "__main__":
    search_query = 'phone'  # You can change this to any search term
    products = scrape_amazon(search_query)

    # Save to CSV and JSON
    df = pd.DataFrame(products)
    df.to_csv('amazon_products.csv', index=False)
    df.to_json('amazon_products.json', orient='records', indent=4)

    print('Data saved to amazon_products.csv and amazon_products.json')
