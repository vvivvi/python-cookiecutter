# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## What's included

- [`pyproject.toml`](./pyproject.toml): Project metadata containing build information and package metadata. For more information, see [here](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/).
- [`requirements.txt`](./requirements.txt): Package dependencies
- [`dev-requirements.txt`](./dev-requirements.txt): Optional dependencies for development
- [`src`](./src): Package source code stored in [`src-layout`](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout)
- [`notebooks`](./notebooks): Jupyter notebooks and other interactive documents

## Development

1. Create new virtual environment
1. Upgrade pip: `pip install --upgrade pip`
1. Install the package in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html): `pip install -e '.[dev]'`
{% if cookiecutter.use_precommit_hook == 'y' -%}
1. Install pre-commit hook: `pre-commit install` or to only run pre-push: `pre-commit install --hook-type pre-push`
{%- endif %}

### Tests

Project is tested with [`pytest`](https://docs.pytest.org/en/latest/). Run tests with:

```bash
$ pytest
```

{% if cookiecutter.use_bitbucket_pipelines == 'y' -%}
### Automated testing

Bitbucket pipeline configuration can be found in [bitbucket-pipelines.yml](./bitbucket-pipelines.yml).
{%- endif %}
