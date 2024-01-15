#before using please make sure to install the required moduls
#pip install requests
#pip install time
#pip install beautifulsoup4 

import requests
from bs4 import BeautifulSoup
import time

def check_website(url, not_found_text):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        if not_found_text not in soup.get_text():
            return True
        else:
            return False
    except (requests.RequestException, Exception) as e:
        print(f"Error: {e}")
        return False

def main():
    website_url = "https://www.haag-networx.at" #page to check
    not_found_text = "Hier siehst du aktuelle Neuigkeiten." #text that should be checked

    while True:
        if not check_website(website_url, not_found_text):
            print(f"Website {website_url} shows '{not_found_text}'. Retrying in 1 minutes...")
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
            print("Current System Time:", formatted_time)
            time.sleep(60)  # seconds, break
        else:
            print(f"Website {website_url} is accessible now. Exiting.")
            break

if __name__ == "__main__":
    main()
