import json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


review_counter = 0  # Total number of reviews encountered
credible_review_counter = 0  # Number of credible reviews


def fetch_bestbuy_product_reviews():
    # Initialize WebDriver (Using Firefox here)
    driver = webdriver.Firefox()
    driver.get('https://www.bestbuy.com/site/reviews/apple-iphone-15-pro-256gb-apple-intelligence-black-titanium-verizon/6525476?variant=A')

    global credible_review_counter, review_counter  # Access the global counters

    all_reviews = []  # List to store all review information
    while True:
        # Wait for the reviews section to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "review-item"))
            )
        except TimeoutException:
            print("Failed to load reviews in time.")
            break

        # Collect the reviews on the current page
        current_reviews = driver.find_elements(By.CLASS_NAME, "review-item")
        review_counter += len(current_reviews)
        print(f"Reviews on this page: {len(current_reviews)}\n")  # Display review count on this page

        for review in current_reviews:
            try:
                # Fetch the reviewer's name
                reviewer_name = review.find_element(By.CLASS_NAME, "ugc-author").text
                print(f"Reviewer: {reviewer_name}")

                # Click on the reviewer button to see additional review information
                review_button = review.find_element(By.CLASS_NAME, "c-button-link.author-button")
                review_button.click()

                # Wait for the review count to appear in the dropdown
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "number-display"))
                )

                # Retrieve the reviewer's total number of reviews
                reviewer_total_reviews = review.find_element(By.CLASS_NAME, "number-display").text

                # Increment the counter if the reviewer has more than one review
                if int(reviewer_total_reviews) > 1:
                    credible_review_counter += 1  # Mark as a credible review
                    print(f"Total Reviews: {reviewer_total_reviews} (Credible)")
                else:
                    print(f"Total Reviews: {reviewer_total_reviews}")

                # Store review data
                all_reviews.append({
                    "reviewer_name": reviewer_name,
                    "reviewer_total_reviews": reviewer_total_reviews
                })

                # Close the dropdown menu by clicking the button again
                review_button.click()
            except NoSuchElementException:
                print("Reviewer info not found, skipping this review.")
                continue  # Skip to the next review if some data is missing
            except Exception:
                # Handle other exceptions and move on
                continue

        # Check for the "Next" button to load more pages
        try:
            next_page_button = driver.find_element(By.XPATH, "//span[@class='sr-only' and text()='next Page']/parent::*")
            next_page_button.click()  # Navigate to the next page
            WebDriverWait(driver, 5).until(EC.staleness_of(current_reviews[0]))  # Wait for old page to refresh
        except (NoSuchElementException, TimeoutException):
            print("No more pages available.")
            break  # Exit loop when no more pages are available

    # Close the browser once the data is gathered
    driver.quit()

    #display the count of credible reviews
    print(f"Credible Reviews: {credible_review_counter}/{review_counter}")

    #save the gathered reviews to a JSON file
    with open("bestbuy_reviews.json", "w") as json_file:
        json.dump(all_reviews, json_file, indent=4)

    print("---PROCESS COMPLETE---")


#start the review scraping process
fetch_bestbuy_product_reviews()
