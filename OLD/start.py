
import os
import subprocess
from openai import AzureOpenAI


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
  model="playwright_ai",
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
message_text = [{"role":"system","content":"Generate Playwright code which will open google.com confirm cookie policy (text='Zaakceptuj wszystko') than click on a <textarea> and search for Playwright text (in the text area). Make sure to update Test name and test case description accorting to this prompt. Use this code as a test template" + templateContent +  ".Generate only JS code without additional description. Check if search any search result contains 'playwright' string."}]

completion = client.chat.completions.create(
  model="playwright_ai",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)


code = completion.choices[0].message.content

with open(testDirectory + '/test1.spec.js', 'w') as file:
    file.write(code)

for filename in os.listdir(testDirectory):
    if filename.endswith(".spec.js"):
        print("Running test: " + filename)
        subprocess.run(["npx", "playwright", "test", testDirectory + "/" + filename])
    else:
        continue