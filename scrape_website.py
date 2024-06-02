import requests
from bs4 import BeautifulSoup


def scrape_website_tool(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    try:
        # Send a GET request to the URL
        response = requests.get(url, 
                                headers=headers, 
                                )
        # Check if the request was successful (status code 200)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the page title
    title = soup.title.string if soup.title else 'No title found'

    text = soup.get_text()
    text = '\n'.join([i for i in text.split('\n') if i.strip() != ''])
    text = ' '.join([i for i in text.split(' ') if i.strip() != ''])
    return title, text