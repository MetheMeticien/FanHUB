import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class IGNScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.ign.com/pc?filter=articles")
    
    def extract_all_stories(self):
        urls = [
            self.url,
            "https://www.ign.com/tv?filter=articles",
            "https://www.ign.com/movies?filter=articles"
        ]

        processed_links = set()

        for url in urls:
            self.url = url
            self.fetch_homepage()
            soup = BeautifulSoup(self.homepage_content, 'html.parser')
            headlines = soup.find_all('a', class_=["item-body"])
            for headline in headlines:
                link = headline.get('href')
                if link in processed_links:
                    continue
                
                img_tag = headline.find('img')
                if img_tag:
                    thumbnail_link = img_tag['src']
                    high_res_link = thumbnail_link.split('?')[0]
                else:
                    high_res_link = "No image found"
                story = self.extract_story(link, high_res_link)
                
                if (story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories):
                    self.stories.append(story)
                    processed_links.add(link) 
                    self.celebrity_find(story)

        
    
    def extract_story(self, link,thumbnail_link=None):
        try:
            print("Connecting to webpage...")
            article_url = f"https://www.ign.com{link}"
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            article_body = article_soup.find('div', class_='jsx-3517015813 article-content page-0')
            if article_body:
                paragraphs = article_body.find_all('p')
                body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
                img_wrap = article_soup.find('div', class_='jsx-2813394464 article-header-image')
                if img_wrap:
                    source_tag = img_wrap.find('img') 
                    img_url = source_tag['srcset'].split(',')[0].strip() if source_tag and 'srcset' in source_tag.attrs else "No image found"
                else:
                    img_url = thumbnail_link
            else:
                body_text = "No article body found"
                img_url = "No image found by default"

        except requests.exceptions.Timeout:
            print("Connection timed out")
            headline_text = "No headline found"
            body_text = "Connection timed out"

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            headline_text = "No headline found"
            body_text = str(e)

        return Story(headline_text, body_text,img_url)
        

# ign_game = IGNScraper()
# ign_game.extract_all_stories()
# ign_game.printAll()
