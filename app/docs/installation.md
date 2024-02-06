# Installation

The project relies on various dependencies that must be installed.

## Quick start

1. `poetry shell` - Activate an environment.
2. `poetry install` - Install the dependencies.
3. `docker compose build` - Build the project.
4. `docker compose up` - Start the services.
5. `docker compose run --rm app sh -c "python manage.py test"` - Run tests.

## Project layout

    ├── Dockerfile
    ├── app/
    │   ├── app     # Django Settings
    │   ├── core    # Core package; contains shared code and commands
    │   ├── docs    # The documentation
    │   ├── items/  # App represents items from the game
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   ├── admins
    │   │   ├── apps.py
    │   │   ├── filters
    │   │   ├── interfaces
    │   │   ├── migrations
    │   │   ├── models
    │   │   ├── serializers
    │   │   ├── tests
    │   │   ├── urls.py
    │   │   └── views
    │   ├── manage.py
    │   ├── media       # Directory contains assets & user's uploads
    │   ├── mkdocs.yml  # Docs settings
    │   ├── templates   # Rewritten templates for django admin
    │   └── users       # App handles API's users
    ├── docker-compose.yml
    ├── poetry.lock
    └── pyproject.toml  # Dependencies
