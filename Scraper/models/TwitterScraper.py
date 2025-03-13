from playwright.sync_api import sync_playwright
from .Scraper import WebScraper, Story
import re
from datetime import datetime, timedelta
import random

class TwitterScraper(WebScraper):
    def __init__(self):
        super().__init__("https://x.com/")

    def extract_story(self, link, celeb_name):
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
                page.goto(link, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_selector("[data-testid='tweet']", timeout=30000)
            except Exception as e:
                print(f"Error loading page {link}: {e}")
                browser.close()
                return None

            tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
            if not tweet_calls:
                print(f"No tweet data found for {link}")
                browser.close()
                return None

            for xhr in tweet_calls:
                try:
                    data = xhr.json()
                    if not data:
                        raise ValueError(f"Empty data received from {link}")

                    tweet_result = data['data']['tweetResult']['result']
                    text = tweet_result.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {}).get("text", None)

                    if not text:
                        text = tweet_result.get("legacy", {}).get("full_text", "No text found")
                        text = re.sub(r'https?://\S+', '', text).strip()

                    img_url = None

                    if 'extended_entities' in tweet_result['legacy']:
                        for media in tweet_result['legacy']['extended_entities']['media']:
                            if media['type'] == 'video':
                                for variant in media['video_info']['variants']:
                                    img_url = variant['url']
                            else:
                                media = tweet_result['legacy'].get('entities', {}).get('media', [])
                                img_url = media[0]['media_url_https'] if media else "No image found"
                                break

                    if not img_url:
                        media = tweet_result['legacy'].get("entities", {}).get("media", [])
                        img_url = media[0]['media_url_https'] if media else "No image found"

                    text = re.sub(r'\s+', ' ', text).strip()

                    print(f"Extracted tweet: {text}")
                    print(f"Extracted image: {img_url}")

                    story = Story("Twitter Post", text, "Twitter", link, img_url)
                    story.celeb_tags.append(celeb_name)  # Use the provided celeb name
                    return story

                except Exception as e:
                    print(f"Error extracting tweet data from {link}: {e}")
                    continue
            browser.close()

    def extract_all_stories(self):
        _xhr_calls = []
        tweet_data = []

        urls = [
            ("https://x.com/realDonaldTrump", "Donald Trump"),
            ("https://x.com/elonmusk", "Elon Musk"),
            ("https://x.com/yunus_centre", "Muhammad Yunus"),
            ("https://x.com/people","Media"),
            ("https://x.com/TMZ","Media"),
            ("https://x.com/FabrizioRomano/","Media"),
            ("https://x.com/brfootball","Media"),
            ("https://x.com/BarackObama", "Barack Obama"),
            ("https://x.com/NASA", "NASA"),
            ("https://x.com/BillGates", "Bill Gates")
        ]

        def intercept_response(response):
            if response.request.resource_type == "xhr":
                _xhr_calls.append(response)

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})

            for url, celeb_name in urls:
                page = context.new_page()
                page.on("response", intercept_response)

                try:
                    page.goto(url, timeout=30000, wait_until="domcontentloaded")
                    page.wait_for_selector("[data-testid='primaryColumn']", timeout=30000)
                except Exception as e:
                    print(f"Error loading {url}: {e}")
                    continue

                for _ in range(10):
                    page.mouse.wheel(0, random.randint(3000, 7000))
                    page.wait_for_timeout(random.randint(3000, 7000))

                tweet_calls = [f for f in _xhr_calls if "UserTweets" in f.url or "Timeline" in f.url]
                for xhr in tweet_calls:
                    try:
                        data = xhr.json()
                        if not data:
                            raise ValueError(f"Empty data received from {url}")

                        instructions = data.get("data", {}).get("user", {}).get("result", {}).get("timeline_v2", {}).get("timeline", {}).get("instructions", [])
                        for instruction in instructions:
                            entries = instruction.get("entries", [])
                            for entry in entries:
                                tweet = entry.get("content", {}).get("itemContent", {}).get("tweet_results", {}).get("result", {})
                                tweet_id = tweet.get("rest_id")
                                created_at = tweet.get("legacy", {}).get("created_at")

                                if tweet_id and created_at:
                                    tweet_time = datetime.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")

                                    if tweet_time >= datetime.now(tweet_time.tzinfo) - timedelta(days=7):
                                        tweet_data.append({
                                            "link": f"{url}/status/{tweet_id}",
                                            "created_at": tweet_time,
                                            "celeb_name": celeb_name
                                        })

                    except Exception as e:
                        print(f"Error parsing tweets from {url}: {e}")
                page.close()

            browser.close()

        sorted_tweets = sorted(tweet_data, key=lambda x: x["created_at"], reverse=True)

        for tweet in sorted_tweets:
            link = tweet["link"]
            celeb_name = tweet["celeb_name"]
            print(f"Extracting tweet from: {link} ({celeb_name})")
            story = self.extract_story(link, celeb_name)
 
            if (story is not None and (story.body or story.medialink != "No image found") and story not in self.stories):
                    if celeb_name == 'Media':
                        self.celebrity_find(story)
                        if len(story.celeb_tags) > 1:
                            self.stories.append(story)
                    else:
                        self.stories.append(story)
            
# sc = TwitterScraper()
# sc.extract_all_stories()
