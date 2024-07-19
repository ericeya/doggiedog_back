# Doggie Dog Backend server
 

## Description

This is the repo for Doggie Dog web app's backend server. It uses Python framework `Django` to run the endpoints to save the data to `Sqlite3` database. Models are based on ORM structure with images being stored through `AWS S3 bucket`. 

Checkout our frontend repo [👉here](https://github.com/ericeya/doggiedog)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Resources](#resources)
- [Contributing](#contributing)
- [Contact-Me](#contact-me)

## Installation

In order to run this repo, run this command in your root folder: 
```
git clone https://github.com/ericeya/doggiedog_back.git
```

Python must be installed in order to run this app. 

Please note that `.env` file with environment variables are required. You must use your own AWS S3 bucket access keys. Environment variables used are:
```
SECRET_KEY='django generic key when installed'
DEBUG=1
ALLOWED_HOST='your_domain'
JWT_SECRET='can be whatever phrase'
AWS_ACCESS_KEY_ID='Your_access_key'
AWS_SECRET_ACCESS_KEY='your_secret_access_key'
AWS_STORAGE_BUCKET_NAME='your_s3_bucket_name'
AWS_S3_SIGNATURE_NAME='s3v4'
AWS_S3_REGION_NAME='your_bucket_region'
DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
```

You also must be in virtual environment in order to start install dependencies and run the server. If you're on windows VSCode, run:
```
python -m venv venv
. venv/scripts/activate
```

- Then install dependencies by running:
    ```
    pip install -r requirements.txt
    ```

- Afterwards, run the following commands to initiate the server (_ensure you're at correct path of your root folder_):

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```


## Technologies

- Python
- Django (for backend)
- Sqlite3
- JWT

## Contributing

Feel free to reach out for any issues, remarks, or feature requests!


## Contact-Me

Contributors contact:

GitHub account: [Eric Lee](https://github.com/ericeya)