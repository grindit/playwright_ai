# playwright_ai
This is a sample projest to demonstrate how to use Azure OpenAI to generate automated tests with Playwright.

## Prerequisites
Create environmental variable 'AZURE_OPENAI_KEY' with a token to you model.
Update model value in the config.py file.
Update azure_endpoint value in the config.py file.

## Prepare environment
```
npm i -D @playwright/test
npx playwright install   
```

```
pip install pipenv
pipenv shell   
pip install openai
pip install pyyaml
```

## Generate tests
```
python generate.py
```


## Execute tests
```
python execute_tests.py
```

## Sample test definition (yaml)
```yaml
Test:
  Name: "Search test no 1"
  Description: "Tests that check search functionality"
  Steps:
    - "Open google.com page."
    - "Confirm cookie policy."
    - "Click on a <textarea> and that search for Playwright text."
```

Run a test manually
```
npx playwright test sampletest1.spec.js
```
