# Python-Best-Buy-Web-Scraper

This project is a Python-based web scraper that uses Selenium to extract product review data from BestBuy.com.
It collects reviewers' names and the number of reviews they've written, saving the results into a JSON file.
It also identifies "credible" reviewers (those who have written more than one review).

# Overview

The script automates browsing through Best Buy product review pages, scraping:

* Reviewer names
* Total reviews written by each reviewer
* Marks reviewers with more than one review as "credible"

At the end, it saves all collected data into a bestbuy_reviews.json file.

# Necessary Installations

Ensure the following is installed:

* Python 3.7+
* Firefox browser
* Geckodriver for Selenium
* Selenium package

Selenium can be installed by pasting this command into a terminal: 
pip install selenium

# How to Run

Enter this command into a terminal to run:
python bestbuy_scraper.py

This will: 
* Open Firefox
* Navigate to the specified Best Buy product review page
* Scrape review data across all pages
* Save the results to bestbuy_reviews.json

# Features

* Automated Pagination: Scrapes through all available review pages
* Credibility Check: Flags reviewers with more than one review
* JSON Output: Saves all collected data in a clean JSON format
* Robust Error Handling: Skips incomplete reviews without crashing

# Notes

* This scraper is targeted to a specific product page on Best Buy.
* You can modify the URL inside driver.get() to scrape different products.
* Always respect Best Buy’s Terms of Service when scraping.

# License

This project is open source and available under the MIT License.





