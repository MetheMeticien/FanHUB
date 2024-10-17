import requests
from bs4 import BeautifulSoup

def ScrapeESPN():
    url = "https://www.espn.in"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    }
    articles = {}

    # Send the request to the ESPN website
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        article_links = soup.find_all('a', href=True)

        for link in article_links:
            href = link['href']
            if href.startswith('/'):
                href = url + href  # Convert relative path to full URL
            
            if 'article' in href or 'story' in href:
                header, story = extract_story(href)
                if header and story:
                    articles[header] = story
    else:
        print(f"Failed to retrieve ESPN page. Status code: {response.status_code}")

    return articles

def ScrapeSkysports():
    url = 'https://www.skysports.com/'
    news_data = {}

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_headlines = soup.find_all('h3')

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
                news_data[news_title] = article_content

    return news_data

def extract_story(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        header = soup.find('h1')
        if header:
            header = header.get_text(strip=True)
        else:
            header = "No Header Found"

        story_content = soup.find_all('p')
        story = '\n'.join([paragraph.get_text(strip=True) for paragraph in story_content if paragraph.get_text(strip=True)])

        if not story:
            story = "No Story Content Found"
        
        return header, story
    else:
        print(f"Failed to retrieve the story. Status code: {response.status_code}")
        return None, None

def scrape_news_paragraphs(url):
    try:
        page = requests.get(url)
        page.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
    soup = BeautifulSoup(page.text, 'lxml')
    
    title = soup.title.string.strip() if soup.title else "No title found"
    paragraphs = soup.find_all('p')
    article_body = "\n\n".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

    if not article_body:
        article_body = "No content found in <p> tags."
    
    return article_body
