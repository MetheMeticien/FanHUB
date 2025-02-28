import json
from hdfs import InsecureClient
from datetime import datetime

from google import genai

def summarize_text(text):
    client = genai.Client(api_key="AIzaSyDps8o4RTRq4uNZAFFt8e4VlX8niaOxo6A")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[f"Provide a concise summary of the following article. Only return the summary without any introductory phrases:\n\n{text}"]
    )
    return response.text.strip()  



class HDFSJsonReader:
    def __init__(self, hdfs_url, hdfs_user):
        self.hdfs_url = hdfs_url
        self.hdfs_user = hdfs_user
        self.client = InsecureClient(self.hdfs_url, user=self.hdfs_user)

    def read_json_from_hdfs(self, hdfs_path):
        try:
            with self.client.read(hdfs_path, encoding="utf-8") as reader:
                return json.load(reader)  
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def read_first_article(self, hdfs_path):
        articles = self.read_json_from_hdfs(hdfs_path)

        if articles:
            print(json.dumps(articles[0], indent=4))  
        else:
            print("No articles found in the JSON file.")

    def get_latest_stories(self, hdfs_path, celeb_name, n):
        articles = self.read_json_from_hdfs(hdfs_path)

        celeb_articles = [
            article for article in articles 
            if any(celeb_name.lower().strip() == tag.lower().strip() for tag in article.get("celeb_tags", []))
        ]


        celeb_articles.sort(key=lambda x: x.get("date_time", ""), reverse=True)

        for article in celeb_articles[:n]:
            print(json.dumps(article, indent=4))

        if not celeb_articles:
            print(f"No articles found for {celeb_name}.")
    
    def get_summarized_articles(self, hdfs_path, celeb_name, n):
        articles = self.read_json_from_hdfs(hdfs_path)

        # Filter articles matching the celeb name
        celeb_articles = [
            article for article in articles
            if any(celeb_name.lower().strip() == tag.lower().strip() for tag in article.get("celeb_tags", []))
        ]

        # Sort articles by date_time (latest first)
        celeb_articles.sort(key=lambda x: x.get("date_time", ""), reverse=True)

        # Summarize the articles and add extra fields
        for article in celeb_articles[:n]:
            article["summarized_body"] = summarize_text(article["body"])
            article["likes"] = 0  # Initialize likes to 0
            article["comments"] = []  # Initialize comments as an empty list

        if celeb_articles:
            # Create a JSON filename based on the celebrity name
            safe_celeb_name = celeb_name.lower().replace(" ", "_")  # Replace spaces with underscores
            file_name = f"{safe_celeb_name}_summarized_articles.json"

            # Save the articles to a local JSON file
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(celeb_articles[:n], f, indent=4, ensure_ascii=False)

            print(f"Summarized articles saved to: {file_name}")
        else:
            print(f"No articles found for {celeb_name}.")

    
    def get_total_articles(self, hdfs_path, celeb_name):
        articles = self.read_json_from_hdfs(hdfs_path)

        count = sum(1 for article in articles if celeb_name in article.get("celeb_tags", []))

        print(f"Total articles for {celeb_name}: {count}")

if __name__ == "__main__":
    hdfs_url = "http://localhost:9870"  # Replace with your NameNode's URL
    hdfs_user = "user"  # Replace with your HDFS username

    reader = HDFSJsonReader(hdfs_url, hdfs_user)

    hdfs_path = "/user/user/stories/celebrity_articles2.json"  

    # Read and print the first article
    # reader.read_first_article(hdfs_path)

    # Get the latest 3 stories of a celebrity
    reader.get_summarized_articles(hdfs_path, "Billie Eilish", 2)


    # Get the total number of articles for a celebrity
    # reader.get_total_articles(hdfs_path, "Cristiano Ronaldo")
