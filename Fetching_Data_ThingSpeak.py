import requests
from datetime import datetime
import os

# ====== CONFIG ======
CHANNEL_ID = "3244898"                 # Replace with your ThingSpeak Channel ID
READ_API_KEY = "P3NOJ7KKOURVD8ZE"      # Replace with your ThingSpeak Read API Key
RESULTS = 100                          # Number of latest entries to fetch
DATA_FOLDER = "data"                   # Folder to store CSV files
# ===================

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Build ThingSpeak CSV URL
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.csv?api_key={READ_API_KEY}&results={RESULTS}"

# Fetch data
response = requests.get(url)
if response.status_code == 200:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{DATA_FOLDER}/thingspeak_data_{timestamp}.csv"
    with open(filename, "w") as f:
        f.write(response.text)
    print(f"[✔] Data saved to {filename}")
else:
    print(f"[✖] Failed to fetch data. Status code: {response.status_code}")
