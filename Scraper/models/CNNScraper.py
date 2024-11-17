import requests
from bs4 import BeautifulSoup
from Scraper import WebScraper
from Scraper import Story

class CNNScraper(WebScraper):
    def __init__(self):
        super().__init__("https://edition.cnn.com/entertainment")
    
    def extract_all_stories(self):
        print("Trying to make connection")
        self.fetch_homepage()  
        print("Connection Established")
        
        # List of URLs to scrape
        urls = [
            self.url,
            f"https://edition.cnn.com/sport/football"
        ] 
        
        processed_links = set()  # To avoid duplicate stories

        # Iterate over all URLs in the list
        for page_url in urls:
            print(f"Fetching stories from: {page_url}")
            self.homepage_content = requests.get(page_url, headers=self.headers, timeout=10).content
            soup = BeautifulSoup(self.homepage_content, 'html.parser')
            headlines = soup.find_all('a', attrs={'data-link-type': 'article'})

            for headline in headlines:
                link = headline.get('href')
                full_link = f"https://edition.cnn.com{link}"

                if full_link not in processed_links:
                    story = self.extract_story(full_link)
                    processed_links.add(full_link)  # Mark this link as processed
                    if story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories:
                        self.stories.append(story)
                        self.celebrity_find(story)

    def extract_story(self, link):
        try:
            print("Connecting to article page...")
            response = requests.get(link, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')

            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"
            # Extract the body content
            paragraphs = article_soup.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else "No article body found"

            img_wrap = article_soup.find('div', class_='image__container')
            img_url = "No image found"

            if img_wrap:
                picture_tag = img_wrap.find('picture')
                if picture_tag:
                    source_tag = picture_tag.find('source', media="(min-width: 1280px)") 
                    if source_tag:
                        img_url = source_tag['srcset'] 
                    else:
                        img_tag = picture_tag.find('img')
                        if img_tag and 'src' in img_tag.attrs:
                            img_url = img_tag['src']

                else:
                    img_tag = img_wrap.find('img')
                    if img_tag and 'src' in img_tag.attrs:
                        img_url = img_tag['src']

            img_url = f"{img_url}" if img_url != "No image found" else img_url

        except requests.exceptions.Timeout:
            print("Connection timed out")
            headline_text = "No headline found"
            body_text = "Connection timed out"
            img_url = "No image found"

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            headline_text = "No headline found"
            body_text = str(e)
            img_url = "No image found"
        
        return Story(headline_text, body_text, img_url)


cnn = CNNScraper()
cnn.extract_all_stories()
cnn.printAll()
