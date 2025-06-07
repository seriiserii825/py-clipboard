#!/usr/bin/env python3
import os
import pyperclip
import time
import subprocess

print("1) strong")
print("2) h2")
print("3) h3")
print("4) span")
print("5) li")
print("6) sup")
print("7) each word capitalize")

choose = input("Choose: ")


def wrap_in_list(clipboard_content):
    """Wrap each line of clipboard content in <li> tags and return wrapped content."""
    lines = clipboard_content.splitlines()  # Split clipboard content into lines
    # Wrap each line
    wrapped_lines = [f"<li>{line}</li>" for line in lines if line.strip()]
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
            elif choose == '5':
                temp_file = os.path.join(projects_dir, 'temp.txt')
                with open(temp_file, 'w') as file:
                    file.write(current_clipboard_content)
                wrapped_content = wrap_in_list(current_clipboard_content)
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '4':
                wrapped_content = f"<span>{current_clipboard_content}</span>"
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '2':
                tag = 'h2'
                wrapped_content = f"<{tag}>{current_clipboard_content}</{tag}>"
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '3':
                tag = 'h3'
                wrapped_content = f"<{tag}>{current_clipboard_content}</{tag}>"
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '6':
                wrapped_content = f"<sup>{current_clipboard_content}</sup>"
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
            elif choose == '7':
                wrapped_content = current_clipboard_content.title()
                pyperclip.copy(wrapped_content)
                last_clipboard_content = wrapped_content
                subprocess.Popen(['notify-send', last_clipboard_content])
        time.sleep(0.5)


if __name__ == "__main__":
    main()
