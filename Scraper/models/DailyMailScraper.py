import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class DailyMailScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.dailymail.co.uk/tvshowbiz/index.html")
    
    def extract_all_stories(self):
        print("Trying to make connection")
        self.fetch_homepage()  
        print("Connection Established")
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', itemprop="url")

        for headline in headlines:
            link = headline.get('href')
            if link:
                link = link.replace("index.html", "")
                full_link = f"https://www.dailymail.co.uk{link}"
                story = self.extract_story(full_link)
                if(story.headline != "No headline found" and story.body != "No article body found"):
                    self.stories.append(story)
                    self.celebrity_find(story)
    
    def extract_story(self, link):
        try:
            print("Connecting to webpage...")
            response = requests.get(link, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the headline
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            # Extract the body content
            paragraphs = article_soup.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else "No article body found"

            # Extract the image URL
            img_wrap = article_soup.find('div', class_='artSplitter mol-img-group')
            if img_wrap:
                img_tag = img_wrap.find('img')
                img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else "No image found"
            else:
                img_url = "No image found"

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

        return Story(headline_text, body_text,"Daily Mail",link, img_url)


# dailymail = DailyMailScraper()
# dailymail.extract_all_stories()
# dailymail.printAll()
