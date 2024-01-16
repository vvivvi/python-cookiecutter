#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


BOLD = "\033[1m"
END = "\033[0m"

if __name__ == "__main__":
    if "{{ cookiecutter.use_bitbucket_pipelines }}" != "y":
        remove_file("bitbucket-pipelines.yml")
    if "{{ cookiecutter.use_precommit_hook }}" == "None":
        remove_file(".pre-commit-config.yaml")

    print(f"Created directory: {BOLD}{PROJECT_DIRECTORY}{END}")
