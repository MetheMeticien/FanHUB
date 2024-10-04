import csv

def read_news_csv(file_name):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Skip the header row
            next(reader)
            
            for row in reader:
                title, content = row
                print(f"News Title: {title}\n")
                print(f"Content:\n{content}\n")
                print("-" * 80)  # Divider between news items
                
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the CSV file to read from
csv_file = 'news_headlines.csv'

# Call the function to read and print the data
read_news_csv(csv_file)
