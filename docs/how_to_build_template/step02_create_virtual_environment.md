# Create Virtual Environment (Setup Python and Pipenv)

1. Setup to use Python v3.7.3 in the root folder of the repo
```
pyenv local 3.7.3
```

2. Verify that `.python-version` now exists:
```
cat .python-version
```
Should see: `3.7.3`


3. Create virtual environment
```
pipenv install --python 3.7.3
```
4. Verify virtual environment
```
pipenv run python --version
```
Should see: `Python 3.7.3`

