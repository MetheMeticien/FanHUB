import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class PeopleScraper(WebScraper):
    def __init__(self):
        super().__init__("https://people.com/celebrity/")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', class_=["comp mntl-card-list-items mntl-universal-card mntl-document-card mntl-card card card--no-image"])
        for headline in headlines:
            link = headline.get('href')
            story = self.extract_story(link)
            if(story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories):
                self.stories.append(story)
                self.celebrity_find(story)
        
    
    def extract_story(self, link):
        img_url = "No image found"
        try:
            print("Connecting to webpage...")
            article_url = f"{link}"
            # Set a timeout of 10 seconds (adjustable as needed)
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the headline
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"
            # Extract the body content
            article_body = article_soup.find('main', class_='loc main')
            
            if article_body:
                paragraphs = article_body.find_all('p')
                body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
                # Check for an image within an <img> tag
                figure_tags = article_body.find_all('figure', class_='comp figure-article')
                for figure in figure_tags:
                    img_tag = figure.find('img')
                    if img_tag and img_tag.get('src'):
                        img_url = img_tag['src']
                        break  # Stop at the first valid image

                # 2. If not found, check for any <img> tag inside <figure> tags
                if img_url == "No image found":
                    figure_tags = article_body.find_all('figure')
                    for figure in figure_tags:
                        img_tag = figure.find('img')
                        if img_tag and img_tag.get('src'):
                            img_url = img_tag['src']
                            break

                # 3. If still not found, check for standalone <img> tags in the article body
                if img_url == "No image found":
                    img_tags = article_body.find_all('img')
                    for img_tag in img_tags:
                        if img_tag.get('src'):
                            img_url = img_tag['src']
                            break

                # 4. Handle srcset for higher-quality images if available
                if img_url == "No image found":
                    for img_tag in img_tags:
                        if img_tag.get('srcset'):
                            srcset_urls = [entry.split(' ')[0] for entry in img_tag['srcset'].split(',')]
                            img_url = srcset_urls[0]  # Take the first image from srcset
                            break
            else:
                body_text = "No article body found"

        except requests.exceptions.Timeout:
            print("Connection timed out")
            # Return a story with a placeholder headline and body text
            headline_text = "No headline found"
            body_text = "Connection timed out"

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            headline_text = "No headline found"
            body_text = str(e)

        return Story(headline_text, body_text,"People", link, img_url)

        
# ppl = PeopleScraper()
# ppl.extract_all_stories()
# ppl.printAll()
