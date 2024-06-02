from autogen import AssistantAgent

def llm_summary(text):

    llm_config_llama3 = {
        "config_list": [
            {
                "model": "llama3",
                "base_url": "http://127.0.0.1:4000",
                "api_type": "openai",
            },
        ],
        "temperature": 0.2,
    }

    writer = AssistantAgent(
        name="Writer", 
        llm_config=llm_config_llama3,
        system_message="""You are an experienced writer. You write detailed and engaging summaries about the given content.
                        """
    )

    task = f"""Your task is to analyze and summarize the following text given in backticks.
            Summarize this report in a concise and clear manner, and identify key takeaways. Make sure to include all relevant details in your summary.
            Output the content as text. Only return your final work without additional comments.
            text: ```{text}```
            """
    
    reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])

    return reply