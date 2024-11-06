import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    longDesc = f.read()

__version__ = "0.0.0"

repo_name = "E2E_ML_Project_MLflow"
auth_username = "palakprashant01"
src_repo = "ml_proj"
auth_email = "palakprashant01@gmail.com"

setuptools.setup(
    name = src_repo,
    version = __version__,
    author = auth_username,
    author_email=auth_email,
    description = "python package for ml application",
    long_description=longDesc,
    long_description_content = "text/markdown",
    url = f"https://github.com/{auth_username}/{repo_name}",
    project_urls = {
        "bug log": f"https://github.com/{auth_username}/{repo_name}/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where = "src")
)