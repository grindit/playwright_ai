import config as cfg

# Function to add a new message and get a response
def send_message(new_message):
    cfg.messages.append({"role": "user", "content": new_message})
    completion = cfg.client.chat.completions.create(
        model=cfg.model,
        messages=cfg.messages,
        temperature=cfg.temperature,
        max_tokens=cfg.max_tokens,
        top_p=cfg.top_p,
        frequency_penalty=cfg.frequency_penalty,
        presence_penalty=cfg.presence_penalty,
        stop=cfg.stop
    )
    response = completion.choices[0].message.content
    cfg.messages.append({"role": "system", "content": response})
    print(response)
    return response

def generate_playwright_code(prompts):   
    results = []
    preText = ""
    postText = ""
    
    for prompt in prompts:
        try:
            results.append(send_message(preText + prompt + postText))    
        except Exception as e:
            print(f"Error while generating code for prompt: {prompt}\n{str(e)}")  
    return results

def generate_playwrite_test(prompts):

    generated_code = generate_playwright_code(prompts)
    generated_code_as_string = "\n".join(generated_code)

    for code in generated_code:
        print(code)

    message_text = "Insert" + generated_code_as_string + "into the test template ... " + cfg.template_content

    return send_message(message_text)