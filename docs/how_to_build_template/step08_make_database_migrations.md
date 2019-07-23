# Make Database Migration(s)

1. Run manage.py to make a migrations file for the Users app:
```bash
pipenv run python src/manage.py makemigrations
```
Should see:
```bash
Migrations for 'users':
  src/users/migrations/0001_initial.py
    - Create model User
```

2. Verify 2 new files:
```bash
git status
```
Should See:
```bash
Untracked files:
	src/db.sqlite3
	src/users/migrations/0001_initial.py
```

3. Update `.gitignore` to ignore the SQLite file:
Add this line to `#Files to ignore` section:
```bash
db.sqlite3
```

4. Check `git status` again to make sure SQLite file will not be checked in:
```bash
git status
```
Should see something like:
```bash
Changes not staged for commit:
	modified:   .gitignore

Untracked files:
	src/users/migrations/0001_initial.py
```
