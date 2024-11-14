import requests
from bs4 import BeautifulSoup
import datetime


class Story:
    def __init__(self, headline, story, medialink=None):
        self.headline = headline
        self.body = story
        self.celeb_tags = []
        self.date_time = datetime.date.today()
        self.medialink = medialink
        
    def printStory(self):
        print(self.headline)


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
            "Tulisa",
            "Coleen Rooney",
            "Ant McPartlin",
            "Wilder McPartlin",
            "David Beckham",
            "Connie Nielsen",
            "Andrew Scott",
            "Paul Mescal",
            "Maura Higgins",
            "Pete Wicks",
            "Gigi Hadid",
            "A$AP Rocky",
            "Rihanna",
            "Eamonn Holmes",
            "Lottie Moss",
            "Olivia Rodrigo",
            "Gemma Collins",
            "Meghan Markle",
            "Victoria Beckham",
            "Cruz Beckham",
            "David Coote",
            "Harry Kane",
            "Rory McIlroy",
            "Katie Taylor",
            "Mike Tyson",
            "Diego Forlan",
            "Charles Leclerc",
            "Carlos Sainz",
            "Sonia Bompastor",
            "Danny Cipriani",
            "Rob Cross",
            "Nelly Korda",
            "Rúben Amorim",
            "LeBron James",
            "Tilak",
            "Arshdeep",
            "Alaeddine",
            "Sonic"
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

    def extract_story(self, link,thumbnail_link=None):
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
            print(story.medialink)
            print(story.celeb_tags)


# url = "https://www.espn.in"
# web = WebScraper(url)
# web.fetch_homepage()
# web.print_html()

