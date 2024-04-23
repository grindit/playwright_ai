# playwrite_ai

## Prepare environment
npm i -D @playwright/test
npx playwright install   
npx playwright test sampletest1.spec.js

pip install pipenv
pipenv shell   
pip install openai


## Generate tests
python generate.py


## Execute tests
python execute_tests.py

## Sample test definition

Test:
  Name: "Search test no 1"
  Description: "Tests that check search functionality"
  Steps:
    - "Open google.com page."
    - "Confirm cookie policy."
    - "Click on a <textarea> and that search for Playwright text."