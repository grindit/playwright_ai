from helpers import generate_playwrite_test, send_message, update_test_case, remove_markdowns
from config import test_directory, test_cases_definitions_dir
import yaml
import os, subprocess

send_message("Act as a code generator for Playwright automation tests. I will ask you to generate specific code parts which will be later combined with a template file. Generate only code in plain text without descriptions or explanations and without ```.")


for filename in os.listdir(test_cases_definitions_dir):
    if filename.endswith(".test_case.yaml"):
        with open(test_cases_definitions_dir + '/' + filename, 'r') as file:
            test_case = yaml.safe_load(file)
            # Accessing data from the YAML file
            test_name = test_case['Test']['Name']
            description = test_case['Test']['Description']
            steps = test_case['Test']['Steps']
            generated_test = generate_playwrite_test(steps)
            base_filename = filename.replace('.test_case.yaml', '')
            generated_test = update_test_case(generated_test, test_name, description)
            generated_test = remove_markdowns(generated_test)

            with open(test_directory + '/' + base_filename + '.spec.js', 'w') as file:
                file.write(generated_test)
    else:
        continue



