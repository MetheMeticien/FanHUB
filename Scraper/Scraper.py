import requests
from bs4 import BeautifulSoup



class Story:
    def __init__(self, headline, story):
        self.headline = headline
        self.body = story
        self.celeb_tags = []


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.hompage_content = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com",
        }
        self.stories = []
        self.celebrity_names = [
            "Mikel Arteta",
            "Martin Odegaard",
            "Ruud van Nistelrooy",
            "Bruno Fernandes",
            "Matheus Cunha",
            "Antonee Robinson",
            "Luke Littler",
            "Luke Humphries",
            "Alejandro Garnacho",
            "Jos Buttler",
            "Jake Bates",
            "Jobe Bellingham",
            "Lewis Hamilton",
            "Wayne Mardle",
            "Alexander Isak",
            "Joelinton",
            "Harvey Barnes",
            "Jannik Sinner",
            "Daniil Medvedev",
            "James Wade",
            "Pep Guardiola",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Erling Haaland",
            "Ødegaard (Martin Ødegaard)",
            "Salima Tete",
            "Varun",
            "Christopher Nkunku",
            "Salima Tete"
        ]
    
    def fetch_homepage(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.homepage_content = soup.prettify()
            else:
                print(f"Failed to retrieve webpage")
        except Exception as e:
            print(f"An error has occured: {e}")
    
    def extract_all_stories(self):
        pass

    def extract_story(self, link):
        pass

    def print_html(self):
        print(self.homepage_content)
    
    def celebrity_find(self, story):
        for celeb in self.celebrity_names:
            if celeb.lower() in story.headline.lower() or celeb.lower() in story.body.lower():
                story.celeb_tags.append(celeb)

        
    def printAll(self):
        for story in self.stories:
            print(story.headline)
            print(story.celeb_tags)


# url = "https://www.espn.in"
# web = WebScraper(url)
# web.fetch_homepage()
# web.print_html()

