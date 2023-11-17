# Process Automation:

# Automating File Backups:
# You can create a Python script to automatically backup files from one directory to another at scheduled intervals using the shutil library.


import shutil
import time
import requests
from bs4 import BeautifulSoup

source_dir = "/path/to/source"
backup_dir = "/path/to/backup"

while True:
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    backup_folder = f"{backup_dir}/backup_{current_time}"
    shutil.copytree(source_dir, backup_folder)
    time.sleep(3600)  # Backup every hour

# Automating Data Extraction:
# You can automate the extraction of data from a website using libraries like BeautifulSoup and requests.


url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data from the webpage
data = soup.find("div", {"class": "content"}).text
print(data)