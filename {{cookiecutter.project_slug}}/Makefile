.PHONY: create-env activate-env freeze-env pip-install

create-env:
	conda create --name {{ cookiecutter.project_slug }} python

activate-env:
	conda init
	conda activate {{ cookiecutter.project_slug }}

freeze-env: activate-env
	conda env export > environment.yml

pip-install: activate-env
	pip install -e .

