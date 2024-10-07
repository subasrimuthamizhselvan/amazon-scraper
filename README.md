Amazon Product Scraper
This project is an Amazon web scraper built using Python, Selenium, and BeautifulSoup. The scraper extracts information about products based on a given search query and saves the data in CSV and JSON formats.

Features
Extracts product names, prices, ratings, reviews, availability, and image URLs.
Saves the data in CSV and JSON formats.
User-friendly for beginners with clear step-by-step implementation.
Prerequisites
Python 3.x
Google Chrome
ChromeDriver
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-username/amazon-scraper.git
cd amazon-scraper
Install the required Python packages:

sh
Copy code
pip install -r requirements.txt
Usage
Edit the Search Query: Update the search_query variable in the script with your desired search term.

Run the Script:

sh
Copy code
python amazon_scraper.py
Output: The scraped data will be saved to:

amazon_products.csv
amazon_products.json
