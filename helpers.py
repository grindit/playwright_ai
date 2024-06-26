import config as cfg
import asyncio

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
    return response

def generate_playwright_code(prompts):   
    results = []
    preText = ""
    postText = ""    
    for prompt in prompts:
        try:
            results.append(send_message(preText + prompt['Action'] + postText + prompt['Selector']))    
        except Exception as e:
            print(f"Error while generating code for prompt: {prompt}\n{str(e)}")  
    return results

def generate_playwrite_test(prompts):

    generated_code = generate_playwright_code(prompts)
    generated_code_as_string = "\n".join(generated_code)

    for code in generated_code:
        print(code)

    output = cfg.template_content.replace("// Insert code here", generated_code_as_string)
    
    return output

def autogenerate_playwrite_test(results):

    output = cfg.template_content.replace("// Insert code here", results)
    return output

def remove_markdowns(text):
    return text.replace("```", "").replace("javascript", "").replace("python", "")

def update_test_case(test_code, test_name, description):
    test_code = test_code.replace('<Test Name>', test_name)
    return test_code

def initialize_conversation_context():
    for prompt in cfg.init_prompts:
        print(send_message(prompt))