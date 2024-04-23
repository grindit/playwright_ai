#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
import subprocess
from openai import AzureOpenAI
from generate_testcases import generate_playwrite_test


client = AzureOpenAI(
  azure_endpoint = "https://testservicepoc.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


testDirectory = "generated_tests"
codeTempplateFile = "templates/template1.js"

with open(codeTempplateFile, 'r') as file:
    templateContent = file.read()

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

print('### Generate Tests ###')


# Example usage
prompts = [
    "Open google.com page",
    "Confirm cookie policy.(google.com)",
    "Click on a <textarea> and that search for Playwright text(google.com)"
]

generated_test = generate_playwrite_test(prompts, client)


with open(testDirectory + '/test1.spec.js', 'w') as file:
    file.write(generated_test)

for filename in os.listdir(testDirectory):
    if filename.endswith(".spec.js"):
        print("Running test: " + filename)
        subprocess.run(["npx", "playwright", "test", testDirectory + "/" + filename])
    else:
        continue