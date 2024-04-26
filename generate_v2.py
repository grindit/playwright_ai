from helpers import initialize_conversation_context, send_message, autogenerate_playwrite_test
from config import test_directory, messages, crawler_results_dir, page_url
import os
import json

pages = []
# Read JSON data
for filename in os.listdir(crawler_results_dir):
    if filename.endswith(".json"):
        with open(crawler_results_dir + '/' + filename, 'r', encoding='utf-8') as f:
            pages.append(json.load(f))
    else:
        continue
#initialize_conversation_context()

for page in pages:
    print(page['links'])

    result = send_message('Generate Playright test for this set of data. Remember that first setp should be - Go to ' + page_url +'.Pull required informations from json I send: ' + str(page['links']))
    generated_test = autogenerate_playwrite_test(result)
    with open(test_directory + '/generated.spec.js', 'w', encoding='utf-8') as file:
        file.write(generated_test)
                