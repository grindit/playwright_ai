import requests
from bs4 import BeautifulSoup
import json
from config import page_url

def fetch_page(url):
    """Fetch the content of the web page with custom headers."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None

def extract_elements(html_content, url):
    """Extract and return link, form information, standalone input details, standalone button details, and other page details."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the title of the page
    title = soup.title.string if soup.title else 'No title found'

    # Extracting all links
    links = []
    for link in soup.find_all('a', href=True):
        links.append({
            'href': link['href'],
            'text': link.get_text(strip=True),
            'id': link.get('id', ''),
            'title': link.get('title', '') 
        })

    # Extracting forms and their input fields, buttons, and textareas
    forms = []
    for form in soup.find_all('form'):
        form_data = {
            'action': form.get('action', ''),
            'method': form.get('method', 'get').upper(),  # Default method is GET if not specified
            'inputs': [],
            'buttons': [],
            'textareas': []
        }
        # Extract inputs and buttons within the form
        for input_tag in form.find_all('input'):
            input_info = {
                'type': input_tag.get('type', 'text'),  # Default type is text if not specified
                'name': input_tag.get('name', ''),
                'value': input_tag.get('value', ''),
                'id': input_tag.get('id', ''),
                'placeholder': input_tag.get('placeholder', '')
            }
            form_data['inputs'].append(input_info)
        for button in form.find_all('button'):
            button_info = {
                'type': button.get('type', 'button'),
                'text': button.text.strip(),
                'id': button.get('id', ''),
                'title': button.get('title', '') 
            }
            form_data['buttons'].append(button_info)
        for textarea in form.find_all('textarea'):
            textarea_info = {
                'name': textarea.get('name', ''),
                'text': textarea.text.strip(),
                'id': textarea.get('id', ''),
                'placeholder': textarea.get('placeholder', '')
            }
            form_data['textareas'].append(textarea_info)
        forms.append(form_data)
    
    # Extract standalone input fields and buttons not within forms
    standalone_inputs = []
    standalone_buttons = []
    standalone_textareas = []
    for input_tag in soup.find_all('input'):
        if not input_tag.find_parents('form'):
            standalone_input_info = {
                'type': input_tag.get('type', 'text'),
                'name': input_tag.get('name', ''),
                'value': input_tag.get('value', ''),
                'id': input_tag.get('id', ''),
                'placeholder': input_tag.get('placeholder', '')
            }
            standalone_inputs.append(standalone_input_info)
    for button in soup.find_all('button'):
        if not button.find_parents('form'):
            standalone_button_info = {
                'type': button.get('type', 'button'),
                'text': button.text.strip(),
                'id': button.get('id', ''),
                'title': button.get('title', '') 
            }
            standalone_buttons.append(standalone_button_info)

    for textarea in soup.find_all('textarea'):
        if not textarea.find_parents('form'):
            standalone_textarea_info = {
                'type': textarea.get('type', 'button'),
                'text': textarea.text.strip(),
                'id': textarea.get('id', ''),
                'placeholder': textarea.get('placeholder', '')
            }
            standalone_textareas.append(standalone_textarea_info)

    return {
        'url': url,
        'title': title,
        'links': links,
        'forms': forms,
        'standalone_inputs': standalone_inputs,
        'standalone_buttons': standalone_buttons,
        'standalone_textareas': standalone_textareas
    }

def save_to_json(data, filename):
    """Save the data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    url = page_url  # Replace with your target URL
    html_content = fetch_page(url)
    if html_content:
        page_data = extract_elements(html_content, url)
        print(page_data['title'])
        save_to_json(page_data, 'crawler_results/page_data.json')
        print("Data has been written to crawler_results/page_data.json")
    else:
        print("Failed to retrieve the page")

if __name__ == "__main__":
    main()
