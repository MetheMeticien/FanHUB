# Import the necessary functions from the ScrapeUniversally module
from ScrapeUniversally import ScrapeESPN, ScrapeSkysports

def main(n):
    # Call the scraping functions
    espn_articles = ScrapeESPN()
    skysports_articles = ScrapeSkysports()

    # Merge the dictionaries
    merged_articles = {**espn_articles, **skysports_articles}

    # Store only the first n articles
    limited_articles = dict(list(merged_articles.items())[:n])

    # Print the limited articles
    for title, story in limited_articles.items():
        print(f"Title: {title}\nStory: {story}\n{'-'*40}")

if __name__ == "__main__":
    # Specify how many articles to store
    n = 5  # Change this to the desired number of articles
    main(n)
