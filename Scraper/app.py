from flask import Flask, jsonify, request, abort
import csv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read_news_csv(file_name='news_headlines.csv'):
    news_data = []
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                news_title, news_content = row
                news_data.append({
                    'title': news_title,
                    'content': news_content
                })
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return news_data

@app.route('/api/news', methods=['GET'])
def get_news():
    news_data = read_news_csv()
    if not news_data:
        return jsonify({"error": "No news found"}), 404
    return jsonify(news_data)


@app.route('/api/news/<string:title>', methods=['GET'])
def get_news_by_title(title):
    news_data = read_news_csv()
    for article in news_data:
        if article['title'].lower() == title.lower():
            return jsonify(article)
    abort(404, description="News article not found")


@app.route('/')
def index():
    return """
    <h1>Welcome to the News API</h1>
    <p>Use <code>/api/news</code> to get all articles or <code>/api/news/&lt;title&gt;</code> to get a specific article by its title.</p>
    """

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
