# Website Summarizer
This project aims to use the power of open source LLMS to summarize the content of a website and paste them as a page in the Notion app.

## Overview
This project allows users to input a URL, scrape the content from the specified website, summarize the content using a Large Language Model (LLM), and automatically add the summary as a new page in the Notion app.
I've used Autogen here and created an agent to summarise the content. Please feel free to change this part and summarize the content directly without the agent.

## Features
- **Content Scraping**: The application scrapes the content from the provided URL. Note: Please check if the website allows scraping of their content.
- **Content Summarization**: The scraped content is summarized using an LLM.
- **Notion Integration**: The summary is added as a new page in the user's Notion workspace (inside another page as I think that would be useful to identify all the AI created summaries).

## Technologies Used
- **Python**: Core programming language.
- **BeautifulSoup**: For web scraping.
- **Requests**: For handling HTTP requests.
- **Ollama**: For running the LLM locally.
- **Llama3**: LLM used
- **Autogen**: An agent to summarize content.
- **Notion API**: For creating new pages in Notion.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Notion API token
- OpenAI API key
- Ollama

## Usage

1. Run your desired LLM using Ollama in the background. 
2. Install required dependencies.
3. Run main.py
4. Enter a valid URL in the input field.
5. The application will process the content and generate a summary.
6. The summary will be added as a new page in your Notion workspace.

## Acknowledgements

- [OpenAI](https://openai.com/)
- [Notion](https://www.notion.so/)
- [Ollama](https://ollama.com/)
- [Llama3](https://llama.meta.com/llama3/)

## References
- Using [Autogen with Ollama](https://microsoft.github.io/autogen/docs/topics/non-openai-models/local-litellm-ollama/)

