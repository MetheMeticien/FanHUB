   filename = "stories.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)