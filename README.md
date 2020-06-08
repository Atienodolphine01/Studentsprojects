## Studentsprojects
This app allows one to post his/her project and get reviews from other users.

## Requirements
Clone the the repository by running

```
git clone https://github.com/Atienodolphine01/Studentsprojects.git
or download a zip file of the project from github then unzip.
```

Navigate to your project directory

## Create a virtual environment
Install Virtualenv

```
pip install virtual venv
```

To create a virtual environment named virtual, run

```
virtualenv virtual
```
To activate the virtual environment we just created,
run

```
source virtual/bin/activate
```

## Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql

 Then run the following query to create a new database named  instagram

```
create database instagram
```


## Install dependencies
To install the requirements from requirements.txt file,

```
pip install -r requirements.txt
```

## Create Database migrations
Making migrations on postgres using django
run

```
python3 manage.py makemigrations  gram
```
then run the command below;

```
python3 manage.py migrate
```
## Run the app
To run the application on your development machine,

```
python3 manage.py runserver
```
## Running Tests
To run tests

```
python3 manage.py test
```

## Technologies Used
- Django
- Python
- Html
- Css
- Javascript
- Bootstrap

## User stories

As a user of the application I should be able to:

- View posted projects and their details.
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects
- View projects overall score
- View my profile page

## Codebeat




## LICENSE
[LICENSE](license)

__Copyright (c) {2020} AtyenohD.__
