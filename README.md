# Web Scraping using Beautiful Soup

This project is a Python script that demonstrates web scraping using the Beautiful Soup library. It allows you to scrape job postings from a specific website and filter them based on a skill that you are unfamiliar with.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed on your system
- Required Python packages:
  - beautifulsoup4
  - requests

You can install these packages by running the following command:

```python 
pip install beautifulsoup4 requests 
```

## Getting Started

To use this script, follow these steps:

1. Clone or download the project to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

## Usage
1. Open the script file scraping.py.
2. Scroll to the section where it prompts you to enter an unfamiliar skill:
```python
print('Put some skill that you are not familiar with:')
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill}')
```
3. Enter a skill you want to filter out from the job postings and press Enter.
4. The script will start scraping the job postings from the TimesJobs website and save the filtered results in individual text files.
5. The script will run continuously, scraping the website at regular intervals (default: 30 seconds) and updating the filtered results.

## Customization
You can customize the script according to your needs. Here are a few things you can modify:

- Website URL: If you want to scrape job postings from a different website, you can change the URL in the following line:

```python
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
```

- Time Interval: By default, the script waits for 30 seconds between each scrape. You can adjust the time interval by modifying the following line:


```python
time_wait = 0.5
```
- Output Directory: The script saves the filtered results in the Posts directory. If you want to change the output directory, you can modify the following line:

```python
with open(f'Posts/{index}.txt','w') as f:
