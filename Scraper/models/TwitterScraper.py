from playwright.sync_api import sync_playwright
from Scraper import WebScraper, Story

class TwitterScraper(WebScraper):
    def __init__(self):
        super().__init__(None)
        
    def extract_story(self, link):
        _xhr_calls = []

        def intercept_response(response):
            if response.request.resource_type == "xhr":
                _xhr_calls.append(response)
            return response

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            page.on("response", intercept_response)

            try:
                page.goto(link, timeout=10000, wait_until="domcontentloaded")  # Added timeout for page loading
                page.wait_for_selector("[data-testid='tweet']", timeout=10000)
            except Exception as e:
                print(f"Error loading page {link}: {e}")
                browser.close()  # Close browser on error
                return Story("Error", f"Unable to load the page {link}.", "No image found")

            # Collect all relevant XHR calls
            tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
            if not tweet_calls:
                print(f"No tweet data found for {link}")
                browser.close()  # Close browser after extraction
                return Story("No Tweet Found", "Unable to retrieve tweet content.", "No image found")

            for xhr in tweet_calls:
                try:
                    # Ensure that the data is valid before parsing
                    data = xhr.json()
                    if not data:
                        raise ValueError(f"Empty data received from {link}")

                    tweet_result = data['data']['tweetResult']['result']
                    text = tweet_result.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {}).get("text", None)
                    
                    if not text:
                        import re
                        text = tweet_result.get("legacy", {}).get("full_text", "No text found")
                        text = re.sub(r'https?://\S+', '', text).strip()
                    img_url = None

                    # Check extended_entities for video media
                    if 'extended_entities' in data['data']['tweetResult']['result']['legacy']:
                        for media in data['data']['tweetResult']['result']['legacy']['extended_entities']['media']:
                            if media['type'] == 'video':
                                # Extract the video URL from the variants
                                for variant in media['video_info']['variants']:
                                    img_url = variant['url']
                                    
                            else:
                                # If it's not a video, fallback to image URL from legacy entities
                                media = data['data']['tweetResult']['result']['legacy'].get('entities', {}).get('media', [])
                                img_url = media[0]['media_url_https'] if media else "No image found"
                                break  # Stop once the image URL is found

                    # If no media is found in extended_entities, check legacy entities for image
                    if not img_url:
                        media = data['data']['tweetResult']['result']['legacy'].get("entities", {}).get("media", [])
                        img_url = media[0]['media_url_https'] if media else "No image found"
                            
                    print(f"Extracted tweet: {text}")
                    print(f"Extracted image: {img_url}")
                    return Story("Twitter Post", text, img_url)

                except Exception as e:
                    print(f"Error extracting tweet data from {link}: {e}")
                    continue
            browser.close()

    def extract_all_stories(self):
        _xhr_calls = []
        tweet_links = []

        urls = [
            "https://x.com/realDonaldTrump",
            "https://x.com/KamalaHarris",
            "https://x.com/elonmusk",
            # Add more URLs as needed
        ]

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
                    page.goto(url, timeout=10000, wait_until="domcontentloaded")  # Set timeout for page loading
                    page.wait_for_selector("[data-testid='primaryColumn']", timeout=10000)
                except Exception as e:
                    print(f"Error loading {url}: {e}")
                    continue

                # Simulate scrolling to load more tweets
                for _ in range(10):  # Adjust range for more/less scrolling
                    page.mouse.wheel(0, 5000)  # Scroll down
                    page.wait_for_timeout(2000)  # Wait for new tweets to load

                # Find all XHR calls that fetch tweets
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
                                tweet_id = entry.get("content", {}).get("itemContent", {}).get("tweet_results", {}).get("result", {}).get("rest_id")
                                if tweet_id:
                                    tweet_links.append(f"{url}/status/{tweet_id}")
                    except Exception as e:
                        print(f"Error parsing tweets from {url}: {e}")
                page.close()

            browser.close()

        # Process all collected tweet links by calling `self.extract_story` on each one
        for link in tweet_links:
            print(f"Extracting tweet from: {link}")
            self.extract_story(link)


# Instantiate and run the scraper
twitter = TwitterScraper()
twitter.extract_all_stories()
#twitter.extract_story("https://x.com/elonmusk/status/1854026234339938528")  
