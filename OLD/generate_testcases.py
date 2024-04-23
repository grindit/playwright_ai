

def generate_playwright_code(prompts, client):   
    results = []
    preText = "Generate only a step for Playwright to: "
    postText = "Show only code as a string."
    
    for prompt in prompts:
        message_text = [{"role": "system", "content": preText + prompt + postText}]
        try:
            completion = client.chat.completions.create(
                model="playwright_ai",  # Update this to your actual deployment name
                messages=message_text,
                temperature=0.7,
                max_tokens=500,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            results.append(completion.choices[0].message.content)
        except Exception as e:
            print(f"Error while generating code for prompt: {prompt}\n{str(e)}")  
    return results

def generate_playwrite_test(prompts, client):

    generated_code = generate_playwright_code(prompts, client)
    generated_code_as_string = "\n".join(generated_code)

    for code in generated_code:
        print(code)

    message_text = [{"role":"system","content":"Insert" + generated_code_as_string + "into the test template ... " + templateContent + " ... At the end update Test name and test case description according to the actions"}]

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
    return completion.choices[0].message.content 