import os
from openai import AzureOpenAI


def initialize():
    client = AzureOpenAI(
    azure_endpoint = "https://testservicepoc.openai.azure.com/", 
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version="2024-02-15-preview"
    )
    message_text = [{"role":"system","content":"You are automation expert in Playwright. Don't give the full response, just confirm that you are ready"}]
    print('### Initiate context ###')

    completion = client.chat.completions.create(
        model="playwright_ai", # model = "deployment_name"
        messages = message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    print(completion.choices[0].message.content)
    return client
    
