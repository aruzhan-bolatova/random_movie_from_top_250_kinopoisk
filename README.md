# Movie Scraper and Randomizer

## Project Overview

This project is a web scraper that collects a list of the top 250 movies from **Kinopoisk**, a popular movie rating platform across post-Soviet countries. The purpose of this scraper is to provide users with a curated list of top-rated movies, which can be filtered by genre and used for random movie selection. This project is designed for educational purposes to demonstrate the use of web scraping and randomization techniques.

## Features

- **Top 250 Movies Scraper**: Scrapes a list of the 250 highest-rated movies from Kinopoisk.
- **Genre Filtering**: Users can scrape all genres or specify a single genre for targeted scraping.
- **Random Movie Selection**: Once the scraping is completed, the tool can randomly select a movie from the scraped data.
- **Web Scraping Tools**: Utilizes **Selenium** to navigate web pages and **BeautifulSoup** to extract relevant movie data.

## Data Description and Purpose

The data uncovered by the scraper includes:
- Movie title
- Link to the movie description page
- Genre

The purpose of collecting this data is to provide users with a list of highly rated movies from Kinopoisk and allow them to receive a random movie suggestion from the list. This project serves as an educational tool for demonstrating web scraping and data manipulation techniques.

## Website Used and Why

The scraper collects data from [Kinopoisk](https://www.kinopoisk.ru), a widely used movie rating and review platform in post-Soviet countries. Kinopoisk was chosen because of its extensive and credible database of top-rated movies, making it a valuable resource for building a movie recommendation tool. The data is publicly accessible, and the scraper adheres to ethical practices outlined in our ETHICS.md file such as respecting the site’s `robots.txt` and terms of service.

### Technologies Used

- **Python**: For data processing and automation.
- **Selenium**: For scraping top250 data from the web.

### How to Run the Project

1. **Clone this repository.**

2. **Install the Required Libraries**: `pip install -r requirements.txt`

3. **Download ChromeDriver**:
    - Visit [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) to download the correct version for your browser.
  
5. **Set Path to ChromeDriver**:
    - Ensure that the path to the ChromeDriver is correctly specified in the script:
      ```python
      from selenium import webdriver
      
      # Set the path to the ChromeDriver
      driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
      ```

5. **Running the Code**:
    - Execute the script to begin scraping TOP 250 movies and getting randomized suggestion from the website.

