# !/bin/bash
conda init && conda activate {{ cookiecutter.project_slug }} && conda env export > environment.yml
