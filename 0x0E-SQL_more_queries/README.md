![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)

---

# 0x0E. SQL - More queries

Welcome to the "0x0E. SQL - More queries" project! In this module, we'll dive deeper into SQL and explore more advanced querying techniques and database manipulation.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Advanced Querying](#advanced-querying)
- [Subqueries and Joins](#subqueries-and-joins)
- [Aggregation and Analysis](#aggregation-and-analysis)
- [Project Files](#project-files)
- [Resources](#resources)
- [More Info](#More Info)

## Introduction

"0x0E. SQL - More queries" is designed to build upon your existing SQL knowledge and introduce you to more complex queries and data manipulation tasks. You'll learn how to use subqueries, joins, aggregation functions, and other advanced SQL concepts to retrieve and manipulate data more effectively.

## Getting Started

To get started with this project, you'll need:

1. A database management system (DBMS) installed. Popular options include MySQL, PostgreSQL, SQLite, and Microsoft SQL Server.
2. A code editor or SQL client to write and execute SQL queries.

## Advanced Querying

In this module, you'll explore advanced querying techniques such as:

- **Subqueries:** Using subqueries to retrieve data within another query and perform calculations.
- **Joins:** Combining data from multiple tables using INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.
- **Advanced Filtering:** Applying complex WHERE conditions and logical operators.
- **Sorting and Grouping:** Ordering results using ORDER BY and grouping data using GROUP BY.

## Subqueries and Joins

Learn how to use subqueries to:

- Retrieve data based on conditions from another query.
- Perform calculations and comparisons within subqueries.
- Use EXISTS and NOT EXISTS to check for the existence of related data.

Explore joins to:

- Combine data from multiple tables based on related columns.
- Understand different join types: INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

## Aggregation and Analysis

Discover the power of aggregation functions to:

- Summarize data using functions like COUNT, SUM, AVG, MIN, and MAX.
- Analyze data distribution and perform calculations on grouped data.
- Understand HAVING clause for filtering aggregated results.

## Project Files

The project files for "0x0E. SQL - More queries" will include:

- SQL query files for various exercises and tasks.
- Sample databases or data sets to practice querying.
- Test files for verifying your queries against expected results.

## Resources

Here are some helpful resources to enhance your understanding of advanced SQL concepts:

- [W3Schools SQL Advanced Tutorial](https://www.w3schools.com/sql/sql_advanced.asp)
- [SQLZoo Advanced SQL Tutorial](https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial)

## More Info

* Comments for your SQL file:

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

* Install MySQL 8.0 on Ubuntu 20.04 LTS

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
* Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

* Ask for container Ubuntu 20.04

Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   

* Starting MySQL database server mysqld 

$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
- In the container, credentials are root/root

* How to import a SQL dump

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
