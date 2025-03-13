import requests
from bs4 import BeautifulSoup
import json
import os
import datetime


class Story:
    def __init__(self, headline, story, source_name, source_url, medialink=None):
        self.headline = headline
        self.body = story
        self.celeb_tags = []
        self.date_time = datetime.datetime.now()
        self.medialink = medialink
        self.source_name = source_name
        self.source_url = source_url
        
    def printStory(self):
        print(self.headline)


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.hompage_content = None
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",  
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
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
            "Vinicius Jr",
            "Kylian Mbappe",
            "Neymar",
            "Mohamed Salah",
            "Virgil van Dijk",
            "Lamine Yamal",
            "Erling Haaland",
            "Dua Lipa",
            "Elizabeth Olsen",
            "Hugh Jackman",
            "Tom Holland",
            "Scarlett Johansson",
            "Chris Hemsworth",
            "Chris Evans",
            "Robert Downey Jr",
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
            "Mustafijur Rahman",
            "Taskin Ahmed",
            "Shakib Al Hasan",
            "Tamim Iqbal",
            "Nazmul Hossain Shanto",
            "Mehazabien Chowdhury",
            "Nusrat Faria",
            "Mahiya Mahi",
            "Siam Ahmed",
            "Tahsan Rahman Khan",
            "Mithila",
            "Salman Muqtadir",
            "Alaeddine",
            "Sonic",
            "Tom Cruise",
            "Zoe Saldana",
            "Selena Gomez",
            "Denzel Washington",
            "Colin Farrell",
            "Megan Fox",
            "Jenna Ortega",
            "Jennifer Lopez",
            "Tom Hanks",
            "Keanu Reeves",
            "Eva Longoria",
            "Billie Eilish",
            "Donald Trump",
            "Kamala Harris",
            "Elon Musk",
            "Barack Obama",
            "Bill Gates",
            "Muhammad Yunus",
            "NASA",
            "JD Vance",
            "Jake Paul",
            "Logan Paul",
            "Linkin Park",
            "Shawn Mendes",
            "Timothée Chalamet",
            "Zendaya",
            "Coldplay",
            "Taylor Swift",
            "Ryan Reynolds",
            "Sydney Sweeney",
            "Tate McRae",
            "Sabrina Carpenter",
            "Lady Gaga",
            "Calvin Harris",
            "Dwayne Johnson",
            "Camila Cabello",
            "Ubisoft",
            "Rockstar Games",
            "Electronic Arts",
            "Activision",
            "Guerrilla Games",
            "Kojima Productions",
            "Insomniac Games",
            "Bethesda",
            "Witcher",
            "From Software",
            "Fifa",
            "CD Projekt Red",
            "Naughty Dog",
            "Square Enix",
            "Nintendo",
            "Sony",
            "Real Madrid",
            "Barcelona",
            "Atletico Madrid",
            "Manchester United",
            "Manchester City",
            "Liverpool",
            "Arsenal",
            "Chelsea",
            "Tottenham Hotspur",
            "La Liga",
            "Premier League",
            "Champions League",
            "Al Nassr",
            
        ]
    
    def fetch_homepage(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.homepage_content = soup.prettify()
            else:
                print(f"Failed to retrieve webpage, status code: {response.status_code}")
        except Exception as e:
            print(f"An error has occurred: {e}")
    
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
        
    def write_to_json(self):
        print("Writing stories to JSON file...")
        filename = "stories.json"
        
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        for story in self.stories:
            if story is None:
                print("Story is None")
                continue
            data.append({
                "headline": story.headline,
                "body": story.body,
                "celeb_tags": story.celeb_tags,
                "date_time": str(story.date_time),
                "medialink": story.medialink,
                "source_name": story.source_name,
                "source_url": story.source_url
            })

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Stories successfully written to {filename}")
                


# url = "https://www.espn.in"
# web = WebScraper(url)
# web.fetch_homepage()
# web.print_html()

