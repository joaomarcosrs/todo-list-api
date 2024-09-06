### Project Page URL: [Project Page](https://roadmap.sh/projects/todo-list-api)

### Initial Requirements
  - [python 3.12+](https://www.python.org/downloads/)
  - [pip](https://pip.pypa.io/en/stable/installation/)

### Intructions:

#### Clone the repository
```bash
git clone https://github.com/joaomarcosrs/todo-list-api.git
```

#### After creating your virtual environment and activate it
```bash
pip install -r requirements.txt
```

#### Create a .env file with the Django SECRET_KEY, you can use the command above to generate the SECRET KEY
```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Run the project
```
python manage.py runserver
```
