from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cliifs",
    version="0.61",
    packages=find_packages(),
    entry_points={'console_scripts': ['cliifs=cliifs.cliifs:main']},

    author="Raphael Reyna",
    author_email="raphaelreyna@protonmail.com",
    description="Render and view fractals from iterated functions systems right on your terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-3.0",
    keywords="fractals chaos ifs",
    url="https://github.com/raphaelreyna/cliifs",
    project_urls={
        "Bug Tracker": "https://github.com/raphaelreyna/cliifs/issues",
        "Documentation": "https://github.com/raphaelreyna/cliifs",
        "Source Code": "https://github.com/raphaelreyna/cliifs/issues",
    }
)
