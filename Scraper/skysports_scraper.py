import requests
from bs4 import BeautifulSoup
import csv

def scrape_news_paragraphs(url):
    try:
        page = requests.get(url)
        page.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
    
    soup = BeautifulSoup(page.text, 'lxml')
    
    try:
        title = soup.title.string.strip()
    except AttributeError:
        title = "No title found"
    
    paragraphs = soup.find_all('p')
    article_body = "\n\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
    
    if not article_body:
        article_body = "No content found in <p> tags."
    
    return article_body


url = 'https://www.skysports.com/'


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


news_headlines = soup.find_all('h3')


news_data = []

for headline in news_headlines:
    a_tag = headline.find('a')  
    if a_tag:
        news_title = a_tag.get_text().strip()
        news_link = a_tag['href']

        if not news_link.startswith('http'):
            news_link = f'https://www.skysports.com{news_link}'

        print(f"Scraping news: {news_title}")
        
        article_content = scrape_news_paragraphs(news_link)
        
        if article_content:
            news_data.append((news_title, article_content))

csv_file = 'news_headlines.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['News Title', 'Paragraphs'])
    
    # Write the news data
    for title, content in news_data:
        writer.writerow([title, content])

print(f"Data has been written to {csv_file}")
