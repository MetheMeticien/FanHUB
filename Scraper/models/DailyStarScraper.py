from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from .Scraper import WebScraper, Story

class DailyStarScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.thedailystar.net/entertainment")

    def fetch_with_playwright(self, urls):
        stories_content = {}
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            
            context.route(
                "**/*", lambda route, request: route.abort()
                if request.resource_type in ["stylesheet", "font", "other"]
                else route.continue_()
            )

            page = context.new_page()

            for url in urls:
                try:
                    print(f"Fetching {url}")
                    page.goto(url, timeout=120000, wait_until="domcontentloaded")  
                    stories_content[url] = page.content()
                except Exception as e:
                    print(f"Failed to fetch {url}: {e}")
                    stories_content[url] = None

            browser.close()
        return stories_content

    def extract_all_stories(self):
        print("Trying to make connection")
        urls = [
            self.url,
            f"https://www.thedailystar.net/sports"
        ]
        all_story_links = set()
        print(f"Fetching {len(urls)} pages...")
        pages_content = self.fetch_with_playwright(urls)

        for url, content in pages_content.items():
            if content:
                soup = BeautifulSoup(content, 'html.parser')
                headlines = soup.find_all(['h3', 'h4'], class_=['title', 'fs-18', 'fs-26'])
                for headline in headlines:
                    link = headline.find('a')
                    if link:
                        href = link.get('href')
                        if href and not href.startswith("http"):
                            href = f"https://www.thedailystar.net{href}"                          
                        if href:
                                all_story_links.add(href)
            
        print(f"Fetching {len(all_story_links)} stories...")
        story_contents = self.fetch_with_playwright(all_story_links)

        for link, content in story_contents.items():
            if content:
                story = self.extract_story(content,link)
                if story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories:
                    self.stories.append(story)
                    self.celebrity_find(story)

    def extract_story(self, page_content,link):
        try:
            article_soup = BeautifulSoup(page_content, 'html.parser')
            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            paragraphs = article_soup.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else "No article body found"

            img_url = "No image found"
            og_image_tag = article_soup.find('meta', property='og:image')

            if og_image_tag and 'content' in og_image_tag.attrs:
                img_url = og_image_tag['content']  

            return Story(headline_text, body_text,"The Daily Star",link, img_url)

        except Exception as e:
            print(f"Error parsing story: {e}")
            return Story("No headline found", "No article body found", "No image found")

# dstar = DailyStarScraper()
# dstar.extract_all_stories()
# dstar.printAll()
