"""
Test creating a Cookiecutter project.
Uses pytest-cookies: https://github.com/hackebrot/pytest-cookies.
"""
from contextlib import contextmanager
import shutil


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        if result.project_path is not None:
            shutil.rmtree(result.project_path)


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.is_dir()

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "bitbucket-pipelines.yml" in found_toplevel_files


def test_bake_without_pipelines(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"use_bitbucket_pipelines": "n"}
    ) as result:
        assert result.exit_code == 0
        assert result.exception is None
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert not "bitbucket-pipelines.yml" in found_toplevel_files
