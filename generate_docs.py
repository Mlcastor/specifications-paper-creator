# generate_docs.py

import os
import shutil
import subprocess


def generate_docs():
    docs_dir = "docs"
    build_dir = os.path.join(docs_dir, "build")
    source_dir = os.path.join(docs_dir, "source")

    # Remove the existing build directory
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    # Run the Sphinx build command
    subprocess.run(["sphinx-build", "-b", "html", source_dir, build_dir])


if __name__ == "__main__":
    generate_docs()
