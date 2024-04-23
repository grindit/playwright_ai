import os
from openai import AzureOpenAI

# Setup the Azure OpenAI client as a global variable
azure_endpoint = "https://testservicepoc.openai.azure.com/"
api_key = os.getenv("AZURE_OPENAI_KEY")
api_version = "2024-02-15-preview"
test_directory = "generated_tests"
code_template_file = "templates/main_template.js"
test_cases_definitions_dir = "test_cases_definitions"
# Initialize the list to keep track of all messages
messages = []

with open(code_template_file, 'r') as file:
    template_content = file.read()

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version
)

#remember to add the model name of your deployed model
model = "playwright2_ai"
temperature=0.7
max_tokens=800
top_p=0.95
frequency_penalty=0
presence_penalty=0
stop=None