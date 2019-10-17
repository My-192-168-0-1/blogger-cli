import os
import shutil
from pathlib import Path

HOME = os.path.expanduser("~")


def get_docs():
    tmp = os.path.join(HOME, "tmp1234")
    os.mkdir(tmp)
    docs_path = os.path.join(tmp, "docs")
    readme = os.path.join(tmp, "README.md")
    licence = os.path.join(tmp, "LICENSE")
    get_blogger = os.path.join(tmp, "get_blogger.py")
    os.system("git clone https://github.com/hemanta212/blogger-cli " + tmp)
    shutil.copytree(docs_path, "tmp_docs")
    os.system("cp " + readme + " " + get_blogger + " " + licence + " tmp_docs/")
    shutil.rmtree(tmp)


def configure_and_convert():
    os.system("blogger rmblog blogger_cli")
    os.system("blogger addblog blogger_cli -s")
    os.system("blogger setdefault blogger_cli")
    os.system("blogger config -re blogger_cli.json")
    os.system("blogger convert tmp_docs/* --topic docs -no-ex")
    os.system("blogger convert tmp_docs/README.md -no-ex")
    os.system("cp tmp_docs/*.py tmp_docs/LICENSE .")
    os.system("mv README.html index.html")


def do_post_processing():
    os.system("rm -rf tmp_docs/")
    os.system("rm docs/*.md")
    os.system("rm docs/README.html")
    readme = Path("index.html")
    readme_text = readme.read_text(encoding="utf-8")
    modified_text = readme_text.replace(".md", ".html")
    readme.write_text(modified_text, encoding="utf-8")
    print("DONE")


if __name__ == "__main__":
    get_docs()
    configure_and_convert()
    do_post_processing()