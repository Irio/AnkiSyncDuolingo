# Contributing

Before building the project locally, we recommend creating a virtual environment. Do so using pyenv with the following commands:

```sh
pyenv install 3.8.3
pyenv virtualenv 3.8.3 duolingosync
pyenv activate duolingosync
```

Now, install the Python package and its dependencies, and run the tests:

```sh
pip install -e ".[dev]"
pytest
```
