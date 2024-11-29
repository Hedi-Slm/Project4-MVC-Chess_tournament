# **Chess Tournament MVC**

This is a fully written in Python project. This application uses a Model-View-Controller (MVC) architecture to separate his different components.
It is an offline chess tournament manager that allows the user to create and manage tournaments. The user can use different menus to navigate through all the features of the application.
All the data is saved in JSON files and loaded on startup.


## **Features**

-  **Manage players:**
    - Add a player to the player database


-  **Manage tournaments:** 

    - Create a tournament
    - Modify a tournament parameters
    - Add players to a tournament
    - Start a round
    - End a round


- **Generate reports:**
    - List of all players in alphabetical order
    - List of all tournaments
    - Choose a specific tournament based on its information
    - List of all players in a tournament
    - List of all tournament rounds and all round matches


- **Save and Load system:**
    - Save all data to a JSON files after each action, separated between players, tournaments and rounds
    - Load all data on startup


- **Compliant with PEP8:**
    - Code formated with Flake8 and allow to generate HTML report with flake8-html


## Installation:
Clone the repository:
```
git clone https://github.com/Hedi-Slm/Project4-MVC-Chess_tournament.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage:
Run the application from the command line:
```
python main.py
```
Use the menu to navigate through the different features of the application.

## Code compliance:
To check PEP8 compliance, run the following command:
```
flake8
```
To generate an HTML report, run the following command:
```
flake8 --format=html --htmldir=reports
```
The report will be generated in the "reports" directory.

## Requirements:
Python 3.10 or higher

Command line tools (Windows, Linux, macOS)

The project requires the following Python tools:
- flake8
- flake8-html
