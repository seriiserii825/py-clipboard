#!/usr/bin/env python3
import os
import pyperclip
import time
import subprocess

print("1) strong")
print("2) li")

choose = input("Choose: ")

def wrap_in_list(clipboard_content):
    """Wrap each line of clipboard content in <li> tags and return wrapped content."""
    lines = clipboard_content.splitlines()  # Split clipboard content into lines
    wrapped_lines = [f"<li>{line}</li>" for line in lines if line.strip()]  # Wrap each line
    return f"<ul>\n{'\n'.join(wrapped_lines)}\n</ul>"  # Enclose in <ul> tags

def main():
    # Initialize the last clipboard content to an empty string
    last_clipboard_content = ""
    projects_dir = os.path.expanduser('~/Downloads')

    while True:
        current_clipboard_content = pyperclip.paste()
        if current_clipboard_content != last_clipboard_content:
            subprocess.Popen(['notify-send', current_clipboard_content])
            if choose == '1':
                wrapped_content = f"<strong>{current_clipboard_content}</strong>"
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '2':
                temp_file = os.path.join(projects_dir, 'temp.txt')
                with open(temp_file, 'w') as file:
                    file.write(current_clipboard_content)
                wrapped_content = wrap_in_list(current_clipboard_content)
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
        time.sleep(0.5)

if __name__ == "__main__":
    main()
