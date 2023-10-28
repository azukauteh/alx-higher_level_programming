# 0x14. JavaScript - Web scraping


## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Why JavaScript Programming is Amazing](#why-javascript-programming-is-amazing)
- [Manipulating JSON Data](#manipulating-json-data)
- [Using Request and Fetch API](#using-request-and-fetch-api)
- [Reading and Writing Files with the fs Module](#reading-and-writing-files-with-the-fs-module)
- [Example: JSON Manipulation](#example-json-manipulation)
- [Example: Making an API Request](#example-making-an-api-request)
- [Example: Reading and Writing Files](#example-reading-and-writing-files)
- [More info](#more info)

## Introduction

Welcome to  0x14-javascript-web_scraping directory.! This README outlines the key learning objectives you'll achieve by the end of this project. JavaScript is a versatile and powerful programming language used for web development, server-side scripting, and more. It's essential to grasp its fundamentals to become a proficient developer.

## Learning Objectives

By the end of this project, you will have the knowledge and skills to:

### Why JavaScript Programming is Amazing

- Understand the significance of JavaScript in modern web development.
- Explore the various applications of JavaScript, from frontend web development to server-side scripting.
- Recognize the role of JavaScript in creating dynamic and interactive web applications.

### Manipulating JSON Data

- Comprehend the structure and purpose of JSON (JavaScript Object Notation) data.
- Learn how to create and manipulate JSON objects in JavaScript.
- Understand how to serialize JavaScript objects into JSON and vice versa.

### Using Request and Fetch API

- Discover the importance of making HTTP requests in web development.
- Master the use of the `request` module for server-side HTTP requests.
- Explore the modern approach to making asynchronous HTTP requests using the Fetch API in browsers.

### Reading and Writing Files with the fs Module

- Learn about the `fs` module in Node.js for file system operations.
- Understand how to read and write files synchronously and asynchronously in JavaScript.
- Gain insights into handling errors and exceptions when working with the file system.

## Why JavaScript Programming is Amazing

JavaScript is amazing for several reasons:

- Versatility : It's a multi-paradigm language suitable for both frontend and backend development.

- Widespread Usage : JavaScript is the de facto language of the web, ensuring a vast job market and community support.

- Dynamic and Interactive : It allows you to create dynamic and interactive web applications, enhancing user experiences.

## Manipulating JSON Data

JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write and easy for machines to parse and generate. It's essential for web applications, APIs, and data storage. By mastering JSON manipulation, you can effectively work with data in your applications.

### Example: JSON Manipulation

Here's an example of creating and manipulating JSON data in JavaScript:

```javascript
// Creating a JSON object
const person = {
  name: "John Doe",
  age: 30,
  hobbies: ["Reading", "Hiking", "Gaming"],
};

// Converting JSON object to a JSON string
const jsonStr = JSON.stringify(person);

// Parsing a JSON string back to an object
const parsedPerson = JSON.parse(jsonStr);

console.log(parsedPerson.name); // Outputs: John Doe
```

## Using Request and Fetch API

HTTP requests are fundamental in web development. You'll learn how to make HTTP requests in JavaScript using the traditional `request` module and the more modern Fetch API. This knowledge is crucial for fetching data from remote servers, APIs, and databases.

### Example: Making an API Request

Here's an example of making an HTTP request to fetch data from an API using the Fetch API:

```javascript
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

## Reading and Writing Files with the fs Module

The file system (fs) module in Node.js is essential for handling files in server-side applications. You'll learn how to read and write files, manage directories, and handle common file-related tasks. This knowledge is vital for server-side scripting, data processing, and building file-based applications.

### Example: Reading and Writing Files

Here's an example of reading a file and writing to a file using the `fs` module in Node.js:

```javascript
const fs = require("fs");

// Reading a file
fs.readFile("example.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

// Writing to a file
fs.writeFile("output.txt", "Hello, world!", (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log("Data written to output.txt");
});
```
## More Info

# Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- Your code should be semistandard compliant. Rules of Standard + semicolons on top.
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

# Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
## Install semi-standard

- Documentation
```bash
$ sudo npm install semistandard --global
```
## Install request module and use it

- Documentation
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

