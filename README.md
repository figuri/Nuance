# Nuance
Upload download from browser with Python, Django, node, and AWSec2


Welcome one and all to Nuance, a web application that allows users to upload and download files from their browser. This project was created by a team of two developers, [Cal], and [Sam] as a Scaffolding for a larger idea.

## Table of Contents
1. [Technologies](#technologies)
2. [Setup](#setup)
3. [Features](#features)
4. [Status](#status)

## Technologies
- Python 3.8.5
- Django 3.1.2
- Node.js 12.19.0
- AWS EC2
- AWS S3

## Setup
To run this project, you will need to install the previously mentioned technologies. Once you have done that, you can clone this repository and run the following commands in your terminal:

```python3.8 -m venv env
source env/bin/activate
pip install django
django-admin startproject myproject
cd myproject
django-admin startapp filehandler

source venv/Scripts/activate

and then run the server with the following command:
python manage.py runserver

```

## Features
- Upload files from your browser
- Download files from your browser
- Delete files from your browser
- View files you have uploaded
- Update those files

## Status
This project is currently in development. We are working on adding more features and improving the user interface.