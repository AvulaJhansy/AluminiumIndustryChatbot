# AluminumIndustryChatbot

## Overview

This project scrapes news articles related to the aluminum industry, preprocesses the text data, generates embeddings using OpenAI's API, and saves the results in a structured format. The goal is to gather relevant industry news and convert it into a machine-readable format for further analysis or AI model development.

## Project Structure

- **Web Scraping**: Uses Selenium to scrape articles from the [Metal Industry News](https://news.metal.com/list/industry/aluminium) website.
- **Data Preprocessing**: Formattign data and time in teh dataset.
- **Embedding Generation**: Generates text embeddings using OpenAI's `text-embedding-ada-002` model.
- **Saving Results**: Stores the processed data and embeddings in a JSON file.

## Requirements

- Python 3.x
- Selenium
- Pandas
- NLTK
- OpenAI API
- FAISS (for vector search)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. **Install Python dependencies**:
    ```bash
    pip install selenium pandas nltk openai faiss-cpu
    ```

3. **Download ChromeDriver**:
    - Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your desired location.
    - Update the `Service` path in the script with your ChromeDriver path.


