from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from .Scraper import WebScraper, Story


class BillboardScraper(WebScraper):
    def __init__(self):
        super().__init__("https://www.billboard.com/c/music/music-news/")

    def fetch_with_playwright(self, urls):
        stories_content = {}
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            
            context.route(
                "**/*", lambda route, request: route.abort()
                if request.resource_type in ["stylesheet", "font","other"]
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
            f"{self.url}page/2/",
            f"{self.url}page/3/"
        ]

        all_story_links = set()
        print(f"Fetching {len(urls)} pages...")
        pages_content = self.fetch_with_playwright(urls)

        for url, content in pages_content.items():
            if content:
                soup = BeautifulSoup(content, 'html.parser')
                sub_headlines = soup.find_all('a', class_="c-title__link lrv-a-unstyle-link lrv-u-color-brand-primary:hover")
                processed_links = set() 
                
                for headline_tag in sub_headlines:
                    link = headline_tag.get('href')
                    if link and not link.startswith("http"):
                        link = f"https://www.billboard.com{link}"
                    if link:
                        all_story_links.add(link)

        print(f"Fetching {len(all_story_links)} stories...")
        story_contents = self.fetch_with_playwright(all_story_links)

        for link, content in story_contents.items():
            if content:
                story = self.extract_story(content)
                if story.headline != "No headline found" and story.body != "No article body found" and story not in self.stories:
                    self.stories.append(story)
                    self.celebrity_find(story)

    def extract_story(self, page_content):
        try:
            article_soup = BeautifulSoup(page_content, 'html.parser')

            headline = article_soup.find('h1')
            headline_text = headline.get_text(strip=True) if headline else "No headline found"

            paragraphs = article_soup.find_all('p')
            body_text = "\n".join([p.get_text(strip=True) for p in paragraphs]) if paragraphs else "No article body found"

            img_wrap = article_soup.find(['img', 'video'], class_=['c-lazy-image__img', 'cnx-video-tag'])

            if img_wrap:
                if img_wrap.name == 'img':
                    img_url = img_wrap['src'] if 'src' in img_wrap.attrs else "No image found"
                elif img_wrap.name == 'video':
                    img_url = img_wrap['poster'] if 'poster' in img_wrap.attrs else "No video thumbnail found"
            else:
                img_url = "No image or video found"


            return Story(headline_text, body_text, img_url)
        
        except Exception as e:
            print(f"Error parsing story: {e}")
            return Story("No headline found", "No article body found", "No image found")

# billboard = BillboardScraper()
# billboard.extract_all_stories()
# billboard.printAll()
