# RMICS

## Description
Welcome to the RMICS (Reliability Maintenance Information and Collaboration System) project, a Django-based web application that revolutionizes maintenance operations by centralizing data storage and promoting efficient collaboration among multiple maintenance groups nationwide. The project addresses the current challenge of decentralized data storage by providing a unified platform for managing maintenance records, replacing individual Excel templates used across different plant locations. The system not only centralizes data but also offers robust data analysis capabilities, allowing users to consolidate maintenance records for specific equipment models.

RMICS comprises several integrated systems:
AMS (Asset Management System): Manages equipment registration to prevent duplications and associates records from DRMS (Daily Report Management System) with specific equipment across operations.
DRMS (Daily Report Management System): Records daily maintenance activities for the entire operations team.
CFMS (Critical Findings Management System): Enforces a strong Condition-based maintenance management system by alerting field personnel to unusual equipment findings and planning subsequent actions.
DROM (Daily Report to Operations Manager): Handles the consolidation and reporting of daily operations to the operations manager.
DVMS (Deliverable Management System): A task management system to enhance productivity and monitor the progress of deliverables.
The project leverages the "gentelella Alela!" pre-built Bootstrap theme to ensure a sleek and user-friendly interface. With RMICS, we aim to not only centralize and analyze maintenance data but also foster collaboration, streamline reporting, and improve overall productivity. Join us on GitHub (https://github.com/fctadena/rmics.git) to contribute and be a part of transforming maintenance operations nationwide.

## Getting started
### Activate virtual environment
```bash
python3 -m venv venv
```

### Activate virtual environment
```bash
source venv/bin/activate
```

### Set .env configuration
```bash
# For linux
cd rmics/
cp .env-example .env
```

```bash
# For windows
# if you are using a Windows command prompt (CMD)
cd rmics/
copy .env-example .env

# or
# if you are using PowerShell, you can use the Copy-Item cmdlet
Copy-Item .env-example .env
```
Note: you need to populate the values inside example;
```
# App config
APP_NAME=rmics
SECRET_KEY="django-insecure-p!3m&cr@)34&e##10v+#$-*txnf+-!)&&@1dtr*$w^v@bm-n2)"
DEBUG=True

# Database config
DATABASE_HOST=127.0.0.1
DATABASE_NAME=rmics_db_v2
DATABASE_USER=user
DATABASE_PASS=password
DATABASE_PORT=3306
```

### Install dependencies
```bash
cd rmics/
pip install -r requirements.txt
```

### Run migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Seed the database (adjust the command accordingly)
```bash
python3 manage.py createdefaultusers
```

### Collect static files
```bash
python3 manage.py collectstatic --noinput
```

### Run the development server
```bash
python3 manage.py runserver
```
