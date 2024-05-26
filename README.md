# Job Scraper using BeautifulSoup for Bing

This project is a web application built with Flask that takes a URL from Microsoft Bing's job search page, scrapes job details using BeautifulSoup, and outputs the results as a JSON file.

## Features

- Input a URL from Microsoft Bing's job search page.
- Scrape job details such as job titles, companies, and locations.
- Download the scraped job details as a JSON file.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- BeautifulSoup4
- Requests

## Installation

__Clone the repository:__

```bash
git clone https://github.com/yourusername/job-scraper-flask.git
cd job-scraper-flask
```

__Create and activate a virtual environment:__
```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate
```
__Install the required packages:__
```bash
pip install -r requirements.txt
```

__Start the Flask application:__
```bash
python app.py
```
__Open your web browser and navigate to http://127.0.0.1:5000/__

__Enter a Bing job search URL (e.g., https://www.bing.com/jobs?q=ml+jobs&scp=0&rb=0&rc=20&L2=true&c=1&form=JOBL2S) and click the submit button.__

__The application will scrape job details and will automatically download a JSON file containing the results.__


## How to Use?

- ### Search for any job role, scroll down and navigate to jobs tab:
![image](https://github.com/iiakshat/google-jobs/assets/92530735/e839280b-9c99-4d5b-9a5a-e21a605b772a)



- ### Click on 'See more listings` and Copy the URL from the header:
![image](https://github.com/iiakshat/google-jobs/assets/92530735/7c8e964d-02d2-480c-8801-bdde53e9ed8f)



- ### Go to `http://127.0.0.1:5000/`, and paste the URL in the input area:
![image](https://github.com/iiakshat/google-jobs/assets/92530735/acf6161f-480c-4cc7-a5fc-0c1d44f705ac)


- ### Hit `Submit` and download will begin automatically:
![image](https://github.com/iiakshat/google-jobs/assets/92530735/5c2ddfc1-b68b-4fbb-9af2-de59b2ddf4dd)


