import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.espn.in/football/story/_/id/41847318/premier-league-speeds-revealed-erling-haaland-fastest'  # ESPN India website

# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a GET request to fetch the raw HTML content with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the raw HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the header/title
    header = soup.find('h1').get_text(strip=True)  # Assuming the header is inside an <h1> tag

    # Extract the story content
    story_content = soup.find_all('p')  # Assuming paragraphs are used for the story content
    story = '\n'.join([paragraph.get_text(strip=True) for paragraph in story_content])  # Join all paragraphs into a single string

    # Print the header and story
    print("Header:", header)
    print("\nStory:\n", story)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
