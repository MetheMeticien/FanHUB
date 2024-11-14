        headline_link = item.find('a', class_="sdc-site-tile__headline-link")
            if headline_link:
                link = headline_link.get('href')
            else:
                link = "No headline link found"
            
            # Find the thumbnail image within the same item
            img_tag = item.find('img', class_="sdc-site-tile__image")
            if img_tag:
                thumbnail_link = img_tag['src']
            else:
                thumbnail_link = "No image found"
            
            # Extract the story with link and thumbnail
            story = self.extract_story(link, thumbnail_link)