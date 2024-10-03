from bs4 import BeautifulSoup
import requests

url = 'https://www.skysports.com/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# Find all headline elements (usually inside <h3> tags or similar)
news_headlines = soup.find_all('h3')

# Loop through each headline and find the link inside
for headline in news_headlines:
    a_tag = headline.find('a')  # Find the <a> tag inside the headline
    if a_tag:
        news_title = a_tag.get_text().strip()  # Extract the text of the link
        news_link = a_tag['href']  # Extract the href attribute (the URL)
        print(f'Headline: {news_title}')
        print(f'Link: {news_link}\n')
