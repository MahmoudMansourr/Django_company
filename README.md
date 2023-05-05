# Employee and Department CRUD Django Project

This Django project is a simple web application for managing employee and department records. The project includes basic CRUD functionality for both employees and departments, as well as a relationship between employees and departments.

## Requirements

To run this Django project, you will need the following:

- Python 3.x
- Django 3.x
- MySQL

## Installation

To install and run the project, follow these steps:

1. Clone the project repository to your local machine.
2. Create a virtual environment for the project: `python -m venv env`
3. Activate the virtual environment: `source env/bin/activate` (on Linux/Mac) or `env\Scripts\activate` (on Windows)
4. Install the project dependencies: `pip install -r requirements.txt`
5. Create a MySQL database and update the `DATABASES` settings in the `settings.py` file to point to your database.
6. Run the database migrations: `python manage.py migrate`
7. Start the Django development server: `python manage.py runserver`
8. Access the web application at `http://localhost:8000/`

## Usage

Once the web application is running, you can use it to perform CRUD operations on employees and departments. Here's a brief overview of the functionality provided by the application:

### Employee CRUD

The employee CRUD functionality allows you to create, read, update, and delete employee records. To access the employee CRUD pages, navigate to `http://localhost:8000/employee/`.

#### Create

To create a new employee record, click the "Add New Employee" button on the employees list page. You will be taken to a form where you can enter the employee details and submit the form to create the record.

#### Read

To view the details of an existing employee record, click the "Show" button next to the employee's name on the employees list page. You will be taken to a page displaying the employee details.

#### Update

To update an existing employee record, click the "Edit" button next to the employee's name on the employees list page. You will be taken to a form where you can update the employee details and submit the form to save the changes.

#### Delete

To delete an existing employee record, click the "Delete" button next to the employee's name on the employees list page. You will be asked to confirm the deletion before the record is deleted.

### Department CRUD

The department CRUD functionality allows you to create, read, update, and delete department records. To access the department CRUD pages, navigate to `http://localhost:8000/departments/`.

#### Create

To create a new department record, click the "Add New Department" button on the departments list page. You will be taken to a form where you can enter the department details and submit the form to create the record.

#### Read

To view the details of an existing department record, click the "Show" button next to the department's name on the department list page. You will be taken to a page displaying the department details.

#### Update

To update an existing department record, click the "Edit" button next to the department's name on the departments list page. You will be taken to a form where you can update the department details and submit the form to save the changes.

#### Delete

To delete an existing department record, click the "Delete" button next to the department's name on the departments list page. You will be asked to confirm the deletion before the record is deleted.

### Employee-Department Relationship

In addition to basic employee and department CRUD functionality, the application also supports a relationship between employees and departments. Each employee record is associated with a department record.

