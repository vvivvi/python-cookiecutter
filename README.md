# Cookiecutter Python template and style guide

Starter template for Python projects made with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/).

## Usage

Install [`cookiecutter`](https://pypi.org/project/cookiecutter/):

```bash
pip install cookiecutter
```

Create project from template with

```bash
# SSH
$ cookiecutter git@bitbucket.org:siloai/cookiecutter-python-project.git
# HTTPS
$ cookiecutter https://<BITBUCKET_USERNAME>@bitbucket.org/siloai/cookiecutter-python-project.git
```

Answer the questions and you have a new folder setup:

- `project_name`: README title
- `project_slug`: Name of the created folder and the name of the installable Python library
- `package_name`: Name of the Python package created under `src/` folder. For example, if you set `package_name` to `silo`, you can import your package with `import silo`.
- `contact_name`: Name used for author and maintainer metadata
- `contact_email`: E-mail used for author and maintainer metadata
- `project_short_description`: Description of the project included in package description and README
- `use_bitbucket_pipelines`: Create `bitbucket-pipelines.yml`
- 'use_precommit_hook': Create `.pre-commit-config.yaml` with defaults for black and pytest.

After creating the template:

- Navigate to the created folder, for example: `cd <PROJECT_SLUG>`
- Initialize Git: `git init`
- Add files to index: `git add .`
- Commit: `git commit -m "First commit."`

To enable pre-commit hooks:

- Run `pre-commit install` or to only run pre-push `pre-commit install --hook-type pre-push`


To create a remote repository in Bitbucket:

- Navigate to your Bitbucket workspace in [bitbucket.org/](https://bitbucket.org/)
- Click "Create" -> "Repository"
- Select the correct workspace, project and repository name (project slug). Choose `Private` access level. Select default branch name `main` (or any other name). **Do not include README or .gitignore.** In advanced settings, you may add description and select Python as language. Click "Create repository".
- In your local folder, set the remote to point to your remote repository: `git remote set-url origin git@bitbucket.org:siloai/<PROJECT_SLUG>.git`
- Update branch name if needed: `git checkout -b main`
- Push to remote: `git push -u origin main`

To understand how `cookiecutter` templates work, see [this tutorial](https://cookiecutter.readthedocs.io/en/1.7.2/tutorial1.html).

## Contributing

Install dependencies:

```bash
$ pip install -e .[dev]
# With zsh:
$ pip install -e '.[dev]'
```

Enable pre-commit hooks:

- Run `pre-commit install` or to only run pre-push `pre-commit install --hook-type pre-push`
- To check if pre-commits are working correctly: `pre-commit run --all-files`
# python-cookiecutter
