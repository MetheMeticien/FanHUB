import requests
from bs4 import BeautifulSoup
import csv

def extract_articles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com",
    }

    articles = []

    # Send the request to the website
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 403:
        print("Access forbidden.")
        return articles
    elif response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all article links
        article_links = soup.find_all('a', href=True)

        for link in article_links:
            href = link['href']
            if href.startswith('/'):
                href = url + href  # Convert relative path to full URL
            
            # Filter for relevant article links
            if 'article' in href or 'story' in href:
                articles.append(href)

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    # print(articles)
    return articles

def extract_story(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the header/title
        header = soup.find('h1')
        if header:
            header = header.get_text(strip=True)
        else:
            header = "No Header Found"

        # Extract the story content
        story_content = soup.find_all('p')
        story = '\n'.join([paragraph.get_text(strip=True) for paragraph in story_content if paragraph.get_text(strip=True)])

        if not story:
            story = "No Story Content Found"
        
        return header, story
    else:
        print(f"Failed to retrieve the story. Status code: {response.status_code}")
        return None, None

csv_file = "ESPN.csv"
def save_to_csv(articles):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
    # Write the header row
        writer.writerow(['News Title', 'Paragraphs'])
        
        # Write the news data
        for article in articles:
            header, story = extract_story(article)
            if header and story:
                writer.writerow([header, story])
    # Write each article's header and story to the CSV

# Example usage
url = "https://www.espn.in"
articles = extract_articles(url)

print(extract_story("https://www.espn.in/olympics/story/_/id/40609447/india-olympics-paris-2024-latest-news-schedule-features-videos-analysis"));

if articles:
    # save_to_csv(articles)
    print("Data saved to ESPN.csv.")
else:
    print("No articles found.")
