# Python Command Injection Demo

A simple vulnerable web application built with Python Flask to demonstrate command injection for security learning and VAPT training.

## Description

This project simulates a network diagnostic tool that allows users to ping a host from a web interface. The application intentionally executes user input inside a system command without sanitization, which allows command injection.

This project is meant for educational purposes only.

## Features

- Simple Flask web application
- Basic frontend interface
- Vulnerable command execution
- Demonstrates command injection attacks

## Project Structure

```
command-injection-demo/
│
├── app.py
├── requirements.txt
│
├── templates/
│ index.html
│
└── static/
style.css
```

## Install Dependancies 

```
pip install -r requirements.txt
```
