import requests
from scrape_website import scrape_website_tool
from autogen_summary import llm_summary
import re

NOTION_API_KEY = "NOTION API KEY"
PAGE_ID = "NOTION PAGE ID"
NOTION_API_URL = 'https://api.notion.com/v1'
NOTION_VERSION = '2022-06-28'

HEADERS = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': NOTION_VERSION
}

def notion_request(method, endpoint, data=None):
    """Helper function to send requests to the Notion API."""
    url = f'{NOTION_API_URL}/{endpoint}'
    response = requests.request(method, url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def update_page(page_id, data):
    """Update a Notion page with the given data."""
    return notion_request('patch', f'blocks/{page_id}/children', data)

def create_page(data):
    """Create a new Notion page with the given data."""
    return notion_request('post', 'pages', data)

def split_text(text, max_length=2000):
    """Split text into chunks of a specified maximum length."""
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def split_text_by_heading(text, heading_level=1):
    """
    Split text into chunks based on the specified heading level.
    
    Args:
    - text (str): The Markdown text to split.
    - heading_level (int): The level of heading to split by (default is 1 for '#').

    Returns:
    - List[str]: A list of text chunks split by the specified heading level.
    """
    import re

    # Define the regex pattern for the specified heading level
    heading_pattern = re.compile(rf'(^|\n){"#"*heading_level} .*')

    # Find all matches for the heading
    headings = list(heading_pattern.finditer(text))

    # If no headings found, return the whole text as one chunk
    if not headings:
        return split_text(text, max_length=2000)
        # return [text]

    # Split text at each heading
    chunks = []
    for i in range(len(headings)):
        start_idx = headings[i].start()
        end_idx = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        chunks.append(text[start_idx:end_idx].strip())

    return chunks

def build_notion_block(text):
    """Create a Notion block for a given text."""
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {"content": text}}]
        }
    }

def main():
    url = input("Enter URL: ")
    title, text = scrape_website_tool(url)

    if title:
        sum_content = llm_summary(text=text)
        base_data = {
            "parent": {"page_id": PAGE_ID},
            "properties": {
                "title": {
                    "title": [{"type": "text", "text": {"content": title}}]
                }
            },
            "children": []
        }

        base_data["children"].append(build_notion_block("Source: "+url))
        response = create_page(base_data)
        page_id = response['id']

        if len(sum_content) < 2000: #notion limit of 2000 characters
            base_data["children"].append(build_notion_block(sum_content))
            response = update_page(page_id, {"children": [build_notion_block(sum_content)]})

        else:
            chunks = split_text_by_heading(sum_content)
            for chunk in chunks:
                response = update_page(page_id, {"children": [build_notion_block(chunk)]})

if __name__ == "__main__":
    main()