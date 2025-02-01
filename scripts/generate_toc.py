import os
from pathlib import Path

def generate_toc():
    # Get the project root directory
    root_dir = Path(__file__).parent.parent
    prompts_dir = root_dir / "prompts"
    readme_path = root_dir / "README.md"
    template_path = root_dir / "scripts" / "readme_template.md"

    # Generate the table of contents
    toc_lines = []

    # Walk through the prompts directory
    for root, dirs, files in os.walk(prompts_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # Get relative path from prompts directory
        rel_path = Path(root).relative_to(prompts_dir)
        
        # Skip root directory in output
        if rel_path != Path('.'):
            # Calculate indent level based on directory depth
            indent = "  " * (len(rel_path.parts) - 1)
            # Add directory as a section
            toc_lines.append(f"{indent}- {rel_path.parts[-1]}\n")
        
        # Add all markdown files in current directory
        for file in sorted(files):
            if file.endswith('.md'):
                # Calculate indent for files
                indent = "  " * len(rel_path.parts)
                # Create relative link to file
                file_path = Path(root) / file
                rel_link = os.path.relpath(file_path, root_dir)
                # Remove .md extension from display name
                display_name = file[:-3]
                toc_lines.append(f"{indent}- [{display_name}]({rel_link})\n")

    # Read the template
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Replace the placeholder with the generated TOC
    final_content = template_content.replace('{TOC_PLACEHOLDER}', ''.join(toc_lines))

    # Write to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    generate_toc() 