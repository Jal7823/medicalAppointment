# :thumbsup: Medical Appointment
---
This is a medical appointment web service, this shows all branch office and the work specialties in this branch, also have a system to reserve an appointment, besides having a custom admin panel for use by doctors where they can manage all patients, their diseases, and pathologies.

## Technologies used

* Server
    * Django
* Data Base
    * MySQL
* Styles 
    * Boostrap

## Installation and configuration

### Environment

:warning: Is very important before install any package create a environment, you can use **virtualenv** or **anaconda**


## Activate environments:

##### Anaconda
```
conda activate nameofyourenvironent
```

##### virtualenv (Linux) 
```
source nameofyourenvironment/bin/activate
```

##### virtualenv (Windows) 
```
.\nameofyourenvironment\Script|activate
```
### :gear: Installed packages

All packages will be installed running the next command line

```
pip3 install -r requirements.txt
```

### :gear: Configure Data Base


 In the folder *settings.py* you can find a *DATABASES* variable you can switch the value for *db.DB_LOCAL* for working with sqlite3 or *db.DB_WEB* for production

### Run project

### Make Migrations

The first step is flow this command for do migrations

```
python3 manage.py makemigrations
```
the next step is do migrate:
```
python3 manage.py migrate
```
## Start Project

Now, open this [link]('http://localhost:8000').


## Quick start

this will be enabled soon through Docker
