from helpers import generate_playwrite_test, send_message
from config import test_directory


send_message("Act as a code generator for Playwright automation tests. I will ask you to generate specific code parts which will be later combined with a template file. Generate only code without descriptions or explanations.")

prompts = [
    "Open google.com page",
    "Confirm cookie policy.",
    "Click on a <textarea> and that search for Playwright text"
]

generated_test = generate_playwrite_test(prompts)


with open(test_directory + '/test1.spec.js', 'w') as file:
    file.write(generated_test)


