# README

## Overview

This README provides a step-by-step guide for setting up and running the `resume_processor` project. Follow these instructions to activate the virtual environment, navigate the project directories, edit necessary files, run the development server, and test the API endpoint.

## Prerequisites

Before you start, ensure you have:

- Python installed on your system.
- A virtual environment set up (e.g., `my_env`).
- The `curl` command-line tool installed for testing API endpoints.

## Steps to Follow

### 1. Activate Virtual Environment

Activate your Python virtual environment to ensure you are using the correct dependencies.

```bash
source my_env/bin/activate
```

### 2. Navigate to Project Directory

Change into the project directory:

```bash
cd newproject/
```

### 3. Navigate to `resume_processor` Directory

Change into the `resume_processor` directory:

```bash
cd resume_processor/
```

### 4. Edit `manage.py`

Open `manage.py` using a text editor (e.g., `nano`) for editing:

```bash
nano manage.py
```

### 5. Edit `urls.py` in `resume_processor`

Open `urls.py` for editing:

```bash
nano urls.py
```

### 6. Navigate to `resumeapi` Directory

Change into the `resumeapi` directory:

```bash
cd resumeapi/
```

### 7. Edit `utils.py`

Open `utils.py` for editing:

```bash
nano utils.py
```

### 8. Edit `urls.py` in `resumeapi`

Open `urls.py` for editing:

```bash
nano urls.py
```

### 9. Edit `views.py`

Open `views.py` for editing:

```bash
nano views.py
```

### 10. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 11. Test the API Endpoint

Use `curl` to send a POST request with a file to the API endpoint:

```bash
curl -X POST -F 'file=@/home/rohit/Downloads/resume.pdf' http://127.0.0.1:8000/api/test_upload/
```

This command uploads `resume.pdf` to the specified API endpoint (`http://127.0.0.1:8000/api/test_upload/`).
