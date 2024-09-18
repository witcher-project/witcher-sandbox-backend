server:
	python manage.py migrate && python manage.py runserver

lint:
	flake8 witcher_sandbox
	mypy witcher_sandbox

black:
	python -m black witcher_sandbox

cleanimports:
	isort .
	autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports witcher_sandbox

clean-lint: cleanimports black lint

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

superuser:
	python manage.py createsuperuser

install-hooks:
	pre-commit install

populate-interests:
	python manage.py populate_interests