# Install Django2

1. From the root of the repo install Django2
```
pipenv install django==2.2.*
```

2. Verify the Django version:
```
pipenv run python -c "import django;print(django.__version__)"
```
Should get: `2.2.3`
