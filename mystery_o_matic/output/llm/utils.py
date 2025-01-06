from contextlib import suppress
from os import makedirs
from string import Template
from emoji import replace_emoji

def create_txt_template(str):
    return Template(str)

def read_txt_template(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            template = create_txt_template(f.read())
            return template
    except FileNotFoundError:
        raise ValueError(f"Template file not found: {filename}")
    except UnicodeDecodeError:
        raise ValueError(f"Template file has invalid encoding: {filename}")

def get_bullet_list(elements, level):
    r = ""
    for element in elements:
        if level == 0:
            r += "* " + element + "\n"
        else:
            r += "    - " + element + "\n"
    return r

def remove_emojis(text):
    return replace_emoji(text, "")

def save_txt(outdir, txt, filename):
    output_dir = f"{outdir}"
    with suppress(OSError):
        makedirs(output_dir)

    filename = f"{output_dir}/{filename}"
    try:
        with open(filename, "w", encoding='utf-8') as f:
            f.write(txt)
    except OSError as e:
        raise RuntimeError(f"Failed to save LLM txt file: {e}")

    return filename
