![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)


# 0x10. Python - Network #0

This diretory contains solutions and implementation for the 0x10. Python - Network #0 project. The project is part of the alx_Africa Software Engineering School curriculum and focuses on learning and implementing networking concepts using Python.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction

The **0x10. Python - Network #0** project covers various networking concepts, including making HTTP requests, working with sockets, handling APIs, and parsing responses. The project aims to build a solid understanding of network-related operations using Python programming language.

## Requirements

- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Usage

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/azukauteh/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```
   cd 0x10-python-network_0
   ```

3. Run the desired Python scripts:
   ```
   python3 script_name.py

## Project Structure

The project is organized into different Python scripts, each addressing a specific networking concept. The files are named accordingly to represent the topic or concept being covered.

- `0-body_size.sh`:  Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
- `1-body.sh`:  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
- `2-delete.sh`:Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
- ` 3-methods.sh`: Bash script that takes in a URL and displays all HTTP methods the server will accept.
- `4-header.sh`: Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
- `5-post_params.sh`:  Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
- `6-peak.py, 6-peak.txt`: a function that finds a peak in a list of unsorted integers..
