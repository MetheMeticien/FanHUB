import json
from hdfs import InsecureClient

class HDFSJsonUploader:
    def __init__(self, hdfs_url, hdfs_user):
        """
        Initialize the HDFSJsonUploader with HDFS connection details.

        :param hdfs_url: URL of the HDFS NameNode (e.g., "http://localhost:9870").
        :param hdfs_user: HDFS username (e.g., "user").
        """
        self.hdfs_url = hdfs_url
        self.hdfs_user = hdfs_user
        self.client = InsecureClient(self.hdfs_url, user=self.hdfs_user)

    def upload_json_to_hdfs(self, local_path, hdfs_path):
        """
        Upload a JSON file from the local file system to HDFS.

        :param local_path: Path to the local JSON file (e.g., "/home/user/stories.json").
        :param hdfs_path: Path in HDFS where the file will be stored (e.g., "/user/user/stories/celebrity_articles.json").
        """
        try:
            # Read the JSON file
            with open(local_path, "r") as file:
                json_data = json.load(file)  # Load JSON data

            # Upload the JSON data to HDFS
            with self.client.write(hdfs_path, encoding="utf-8") as writer:
                json.dump(json_data, writer, indent=4)  # Write JSON data to HDFS

            print(f"JSON file uploaded to HDFS at: {hdfs_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # HDFS connection details
    hdfs_url = "http://localhost:9870"  # Replace with your NameNode's URL
    hdfs_user = "user"  # Replace with your HDFS username

    # Initialize the HDFSJsonUploader
    uploader = HDFSJsonUploader(hdfs_url, hdfs_user)

    # Local path to the JSON file
    local_path = "/home/user/Documents/Software/Hadoop/stories.json"  # Replace with your local file path

    # HDFS path where the file will be uploaded
    hdfs_path = "/user/user/stories/celebrity_articles2.json"  # Replace with your desired HDFS path

    # Upload the JSON file to HDFS
    uploader.upload_json_to_hdfs(local_path, hdfs_path)