from config import  client, messages, template_content


# Function to add a new message and get a response
def send_message(new_message):
    messages.append({"role": "user", "content": new_message})
    completion = client.chat.completions.create(
        model="playwright_ai",
        messages=messages,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    response = completion.choices[0].message.content
    messages.append({"role": "system", "content": response})
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

    message_text = "Insert" + generated_code_as_string + "into the test template ... " + template_content


    return send_message(message_text)