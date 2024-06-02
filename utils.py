import os
from dotenv import load_dotenv, find_dotenv

# Add a .env file in the directory
def load_env():
    _ = load_dotenv(find_dotenv())

def get_notion_api_key():
    load_env()
    notion_api_key = os.getenv("NOTION_API_KEY")
    return notion_api_key

def get_page_id():
    load_env()
    page_id = os.getenv("PAGE_ID")
    return page_id