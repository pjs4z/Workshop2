import re
import os

def split_ufo_notes(filename, output_path):
    # Ensure the directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Improved Regex to capture the content between the markers
    # It looks for the start of YAML and captures until the next YAML block or end of file
    pattern = r"(---.*?# (.*?)\n.*?)(?=---|$)"
    matches = re.findall(pattern, content, re.DOTALL)

    if not matches:
        print("No matches found. Check if the source file contains the expected format.")
        return

    for body, title in matches:
        # Sanitize filename (remove characters that OS doesn't like)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title.strip())
        file_name = f"{safe_title}.md"
        full_path = os.path.join(output_path, file_name)
        
        # Clean the body
        # 1. Strip whitespace
        # 2. Remove the opening and closing markdown code block backticks
        clean_body = body.strip()
        clean_body = re.sub(r'^```markdown\n', '', clean_body)
        clean_body = re.sub(r'\n```$', '', clean_body)
        clean_body = clean_body.strip()
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(clean_body)
        print(f"Created: {full_path}")

# Configuration
SOURCE_FILE = 'wip/source.txt'
DESTINATION = '/Users/pablo/Dopamine'

split_ufo_notes(SOURCE_FILE, DESTINATION)