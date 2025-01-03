# Scrapy Spider for TCDB Data Extraction

This project is a Scrapy-based web scraper that extracts data from the Trading Card Database (TCDB) website. The spider collects details such as player names, team names, card images, total cards, and release dates for baseball card sets.

## Table of Contents
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Scrapes data from [TCDB](https://www.tcdb.com).
- Supports pagination and multiple detail pages.
- Extracts:
  - Player names
  - Team names
  - Card images
  - Total cards in a set
  - Release dates
- Saves data in CSV format.

## Setup and Installation

### Prerequisites
1. Python 3.8+
2. Scrapy library

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tcdb-scrapy-spider.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tcdb-scrapy-spider
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Spider
1. Open a terminal in the project directory.
2. Run the spider using the following command:
   ```bash
   scrapy crawl spidername
   ```
3. The output will be saved in `TCDb_output2.csv` in the project directory.

### Customizing the Spider
- Modify the `start_urls` variable to target different years or categories on TCDB.
- Update the `allowed_domains` list as needed.

## Output Format
The scraped data is saved in a CSV file (`TCDb_output2.csv`) with the following columns:
- **Image 1**: URL of the first card image.
- **Image 2**: URL of the second card image (if available).
- **Player Name**: Name of the player on the card.
- **Team Name**: Team associated with the card.
- **First Set**: Name of the card set.
- **Total Cards**: Total number of cards in the set.
- **Released Date**: Release date(s) of the set.

## Project Structure
```
TCDb/
|
|-- spider.py                # Scrapy spider script
|-- requirements.txt         # Python dependencies
|-- TCDb_output2.csv         # Output file (generated after running the spider) 
```

## Contributing
Contributions are welcome! If you have suggestions for improvement, please fork the repository, create a feature branch, and submit a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---


