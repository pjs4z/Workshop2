import os
import re
import argparse
import sys

def sanitize_filename(name):
    """
    Cleans up a string to make it a valid, safe filename.
    Removes special characters and replaces spaces with underscores.
    """
    # Remove any characters that aren't alphanumeric, spaces, dashes, or underscores
    clean_name = re.sub(r'[^\w\s-]', '', name)
    # Strip leading/trailing whitespace and replace inner spaces with underscores
    return clean_name.strip().replace(' ', '_') + '.md'

def extract_title(markdown_content, default_index):
    """
    Searches the markdown content for a level-1 heading (# Title) to use as the filename.
    Falls back to a default name if no heading is found.
    """
    # Regex to find a line starting with '# ' followed by the title text
    match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
    
    if match:
        return sanitize_filename(match.group(1))
    else:
        # Fallback if no # heading exists
        return f"Untitled_Note_{default_index}.md"

def process_file(input_filepath, output_dir):
    """
    Reads the input file, extracts markdown blocks, and saves them as separate files.
    """
    # Ensure the output directory exists; create it if it doesn't
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
        sys.exit(1)

    # Regex to find content between ```markdown and ```
    # re.DOTALL ensures that '.' matches newlines as well
    pattern = re.compile(r'```markdown\n(.*?)\n```', re.DOTALL)
    matches = pattern.findall(content)
    
    if not matches:
        print("No markdown blocks found in the source file.")
        return

    print(f"Found {len(matches)} notes to extract. Processing...")

    # Loop through each extracted markdown block
    for index, note_content in enumerate(matches, start=1):
        # Determine the filename
        filename = extract_title(note_content, index)
        filepath = os.path.join(output_dir, filename)
        
        # Write the content to the new markdown file
        with open(filepath, 'w', encoding='utf-8') as out_file:
            # We strip leading/trailing whitespace to keep the file clean, 
            # but preserve the internal formatting.
            out_file.write(note_content.strip() + "\n")
            
        print(f"  -> Created: {filename}")
        
    print(f"\nSuccess! Exported {len(matches)} notes to the '{output_dir}' directory.")

def main():
    """
    Sets up the Command Line Interface (CLI) arguments.
    """
    parser = argparse.ArgumentParser(description="Extract markdown blocks into individual Obsidian notes.")
    parser.add_argument("input_file", help="Path to the text file containing the raw data.")
    parser.add_argument(
        "-o", "--output", 
        default="obsidian_export", 
        help="Directory to save the extracted notes. Defaults to 'obsidian_export'."
    )
    
    args = parser.parse_args()
    
    process_file(args.input_file, args.output)

if __name__ == "__main__":
    main()