![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)

---
# 0x0F. Python - Object-relational Mapping



## Overview

This project focuses on understanding and implementing Object-Relational Mapping (ORM) using Python. Object-Relational Mapping is a programming technique used to interact with databases using an object-oriented paradigm, allowing developers to work with databases using Python classes and objects.

In this project, we explore how to use an ORM library (like SQLAlchemy) to interact with a database, define models, perform CRUD (Create, Read, Update, Delete) operations, and establish relationships between objects.

## Project Structure

The project is organized into the following directories:

- ** 0-select_states.py **: Script that lists all states from the database hbtn_0e_0_usa.
- ** 1-filter_states.py **: Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:.
- ** 2-my_filter_states.py **: Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa .
- ** 3-my_safe_filter_states.py**:  SQL Injection...
- ** 4-cities_by_state.py **: script that lists all cities from the database hbtn_0e_4_usa
- ** 5-filter_cities.p **: script that takes in the name of a state as an argument and lists all cities( All cities by state)
- ** model_state.py **: python file that contains the class definition of a State and an instance Base = declarative_base():
- ** 7-model_state_fetch_all.py **: Script that lists all State objects from the database hbtn_0e_6_usa
- ** 8-model_state_fetch_first.py **: Script that prints the first State object from the database hbtn_0e_6_usa
- ** 9-model_state_filter_a.py **: Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
- ** 10-model_state_my_get.py **: Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
- ** 11-model_state_insert.py **:  script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.
- ** 12-model_state_update_id_2.py **: script that changes the name of a State object from the database hbtn_0e_6_usa
- ** 13-model_state_delete_a.py **: script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa


## Requirements

 # General

- Allowed editors: vi, vim, emacs

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

- Your files will be executed with MySQLdb version 2.0.x

- Your files will be executed with SQLAlchemy version 1.4.x

- All your files should end with a new line

- The first line of all your files should be exactly #!/usr/bin/python3

- Your code should use the pycodestyle (version 2.8.*)

- All your files must be executable

- The length of your files will be tested using wc

- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')

- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')

- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

- You are not allowed to use execute with sqlalchemy


## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/azukauteh/alx-higher_level_programming.git
   ```

```bash
   cd 0x0F-python-object-relational-mapping
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x0F-python-object-relational-mapping
   ```

3. Run the main script to demonstrate ORM functionality:

   ```bash
   python main.py
   ```

   Modify the `main.py` script as needed to interact with the ORM models and perform various database operations.

## Testing

To run the test cases, navigate to the `tests/` directory and execute the test script:

```bash
cd tests
python test_models.py
```

The test cases ensure the correct implementation of the ORM models and operations.

## More Info

- Install and activate venv

To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

```bash
 sudo apt-get install python3.8-venv
```
```bash
 python3 -m venv venv

```bash
 source venv/bin/activate
```
- Install MySQLdb module version 2.0.x
   For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

```bash
 sudo apt-get install python3-dev
```
```bash
 sudo apt-get install libmysqlclient-dev
```
```bash
 sudo apt-get install zlib1g-dev
```
```bash
 sudo pip3 install mysqlclient
```

 python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x

```bash
 sudo pip3 install SQLAlchemy
```

 python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
- Also, you can have this warning message:

```
 /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```
You can ignore it.
