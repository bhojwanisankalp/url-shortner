# url-shortner

This project is a python/Django based web application to create short urls and redirect to original url when key in the shorten urls.

# prerequisite 
1. Python version 3.6 version or greater and pip package [Link to install](https://realpython.com/installing-python/).
2. virtualenv for python [Link to install](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

# setup
1. Create and activate a virtual environment using virtualenv [Link to virtualenv](https://docs.python.org/3/library/venv.html).
2. Install all dependencies using "pip install -r requirements.txt".
3. In terminal  go to project_root_dir where manage.py is kept and run make migrations using "python manage.py makemigrations ".
4. Apply migrations using "python manage.py migrate" using same terminal.
5. Runserver using "python manage.py runserver" using same terminal.
6. Goto to the url provided in terminal after successfully running server.
7. This project uses SQLite as a default. This can be change from settings.py [Click here to know more](https://docs.djangoproject.com/en/3.2/ref/databases/)