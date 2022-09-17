Create a project dir and cd into the dir

(Optional) create a virtual environment: python3 -m venv "virtual environment name"

if virtual environment created, activate the virtual environment with this command: source "virtual environment name"/bin/activate

Clone the file within the directory

cd into the project file

Run command: pip3 install -r requirements.txt

Run command: python manage.py shell
# Enter the following commands sequentially
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()

# Copy the secret key and replace secret_key in your settings.py file inside ACM_website folder
# Replace SECRET_KEY = env('secret_key') with the random secret key you just copied.

# to create super user
Run Command : python manage.py createsuperuser

Run command: python3 manage.py runserver

# path to access admin page(localhost:8000/admin/)
