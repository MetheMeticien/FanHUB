import requests
from bs4 import BeautifulSoup
from .Scraper import WebScraper
from .Scraper import Story

class GamespotScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.gamespot.com/games/")
    
    def extract_all_stories(self):
        self.fetch_homepage()  
        
        soup = BeautifulSoup(self.homepage_content, 'html.parser')
        headlines = soup.find_all('a', class_=["promo--object promo--offset-wide promo-type--overlay  js-click-tag","js-click-tag","card-item__link text-decoration--none"])

        for headline in headlines:
            link = headline.get('href')
            story = self.extract_story(link)
            if(story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories):
                self.stories.append(story)
                self.celebrity_find(story)
        
    
    def extract_story(self, link):
        media_url = "No image found by default"
        try:
            print("Connecting to webpage...")
            if link.startswith("http"):
                article_url = link
            elif link.startswith("/articles"):
                article_url = f"https://www.gamespot.com{link}"
            else:
                return Story("No headline found", "No article body found")
            response = requests.get(article_url, headers=self.headers, timeout=10)
            print("Connection established")

            article_soup = BeautifulSoup(response.content, 'html.parser')

            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"
            print(article_url)
            print(headline_text)
            article_body = article_soup.find('div', class_=["image-gallery__list-item-content typography-format flexbox-flex-even","js-image-gallery__list-wrapper image-gallery__list-wrapper","js-content-entity-body content-entity-body"])
            if article_body:
                print("Article body found")
                paragraphs = article_body.find_all('p')
                body_text = "\n".join([p.get_text(strip=True) for p in paragraphs])

                video_wrap = article_soup.find('div', class_='js-video-player-new')
                img_wrap = article_soup.find('div', class_='jsx-2813394464 article-header-image')

                if video_wrap:
                    video_data = video_wrap.get('data-video')
                    import json
                    video_json = json.loads(video_data.replace('&quot;', '"'))
                    media_url = video_json.get('share', {}).get('linkUrl', "No video URL found")
                elif img_wrap:
                    source_tag = img_wrap.find('img') 
                    media_url = source_tag['srcset'].split(',')[0].strip() if source_tag and 'srcset' in source_tag.attrs else "No image found"
                else:
                    img_wrap = article_soup.find('div', class_='image-gallery__image-wrapper')
                    if img_wrap:
                        source_tag = img_wrap.find('img')
                        media_url = source_tag['src'] if source_tag and 'src' in source_tag.attrs else "No image found"
                    else:
                        media_url = "No image/video found within article"
               
            else:
                print("No article body found")
                body_text = "No article body found"
            print(media_url)
            
        except requests.exceptions.Timeout:
            print("Connection timed out")
            # Return a story with a placeholder headline and body text
            headline_text = "No headline found"
            body_text = "Connection timed out"

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            # Return a story with a placeholder headline and body text for any other request errors
            headline_text = "No headline found"
            body_text = str(e)

        return Story(headline_text, body_text,media_url)

        
        

# gamespot = GamespotScraper()
# gamespot.extract_all_stories()
#gamespot.printAll()
