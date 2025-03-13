from playwright.sync_api import sync_playwright
from Scraper import WebScraper, Story
import re
from datetime import datetime, timedelta

class TwitterScraper(WebScraper):
    def __init__(self):
        super().__init__("https://x.com/")
        self.one_day_ago = datetime.now() - timedelta(days=7)  

    def extract_story(self, link):
        _xhr_calls = []

        def intercept_response(response):
            if response.request.resource_type == "xhr":
                _xhr_calls.append(response)

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.on("response", intercept_response)

            try:
                page.goto(link, timeout=10000, wait_until="domcontentloaded")
                page.wait_for_selector("[data-testid='tweet']", timeout=10000)
            except Exception as e:
                print(f"Error loading page {link}: {e}")
                browser.close()
                return None

            tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
            if not tweet_calls:
                browser.close()
                return None

            for xhr in tweet_calls:
                try:
                    data = xhr.json()
                    tweet_result = data['data']['tweetResult']['result']
                    text = tweet_result.get("legacy", {}).get("full_text", "No text found")
                    text = re.sub(r'https?://\S+', '', text).strip()
                    
                    created_at = tweet_result.get("legacy", {}).get("created_at")
                    tweet_time = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
                    
                    if tweet_time < self.one_day_ago:
                        print(f"Skipping old tweet: {link}")
                        continue

                    media = tweet_result.get("legacy", {}).get("entities", {}).get("media", [])
                    img_url = media[0]['media_url_https'] if media else "No image found"
                    
                    print(f"Extracted tweet: {text}")
                    print(f"Extracted image: {img_url}")
                    return Story("Twitter Post", text, "Twitter", link, img_url)

                except Exception as e:
                    print(f"Error extracting tweet data from {link}: {e}")
                    continue
            
            browser.close()

    def extract_all_stories(self):
        _xhr_calls = []
        tweet_links = []
        urls = ["https://x.com/realDonaldTrump", "https://x.com/KamalaHarris", "https://x.com/elonmusk"]

        def intercept_response(response):
            if response.request.resource_type == "xhr":
                _xhr_calls.append(response)

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})

            for url in urls:
                page = context.new_page()
                page.on("response", intercept_response)

                try:
                    page.goto(url, timeout=10000, wait_until="domcontentloaded")
                    page.wait_for_selector("[data-testid='primaryColumn']", timeout=10000)
                except Exception as e:
                    print(f"Error loading {url}: {e}")
                    continue

                for _ in range(5):  # Reduce scrolling depth to limit to recent tweets
                    page.mouse.wheel(0, 5000)
                    page.wait_for_timeout(2000)

                tweet_calls = [f for f in _xhr_calls if "UserTweets" in f.url or "Timeline" in f.url]
                for xhr in tweet_calls:
                    try:
                        data = xhr.json()
                        instructions = data.get("data", {}).get("user", {}).get("result", {}).get("timeline_v2", {}).get("timeline", {}).get("instructions", [])
                        for instruction in instructions:
                            for entry in instruction.get("entries", []):
                                tweet = entry.get("content", {}).get("itemContent", {}).get("tweet_results", {}).get("result", {})
                                tweet_id = tweet.get("rest_id")
                                created_at = tweet.get("legacy", {}).get("created_at")
                                
                                if tweet_id and created_at:
                                    tweet_time = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
                                    if tweet_time >= self.one_day_ago:
                                        tweet_links.append(f"{url}/status/{tweet_id}")
                    except Exception as e:
                        print(f"Error parsing tweets from {url}: {e}")
                page.close()
            
            browser.close()

        for link in tweet_links:
            print(f"Extracting tweet from: {link}")
            self.extract_story(link)

twitter = TwitterScraper()
twitter.extract_all_stories()