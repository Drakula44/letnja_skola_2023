import os
import shutil


def create_markdown_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def process_python_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    file_name = os.path.basename(file_path)
    title = f"## {file_name}\n\n"
    markdown_content = f"{title}```python\n{content}\n```"

    md_file_name = os.path.splitext(file_path)[0] + ".md"
    create_markdown_file(md_file_name, markdown_content)
    return md_file_name


def find_python_scripts(folder):
    python_scripts = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                python_scripts.append(os.path.join(root, file))
    return python_scripts


def create_summary_file(file_list):
    summary_content = "\n".join(
        [f"* [{os.path.basename(file)}]({file})" for file in file_list])
    create_markdown_file("Summary.md", summary_content)


def main():
    folder_to_process = "./python_files"  # Current working directory
    python_scripts = find_python_scripts(folder_to_process)
    generated_files = []

    for script in python_scripts:
        md_file = process_python_file(script)
        generated_files.append(md_file)

    create_summary_file(generated_files)


if __name__ == "__main__":
    main()
