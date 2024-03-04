# Alura Space Project

## Description

This is a project developed during the Alura course. It's a space-themed website that showcases the latest news, images, and information about space exploration. The website utilizes the APOD (Astronomy Picture of the Day) API from NASA.

 
## Downloading the Project

Firstly, we need to have the project on our machine. This can be done in two ways: 

- Executing the command `git clone https://github.com/ana-rabelo/space-django` in the terminal, in the directory where you want to save the project. This will create a folder called `space-django` with the project files.
- Downloading the project as a zip file through the link [https://github.com/ana-rabelo/space-django/archive/refs/heads/main.zip](https://github.com/ana-rabelo/space-django/archive/refs/heads/main.zip) and extracting it.

## Running the Project

To run the project, we need to have Python installed on our machine. If you don't have it, you can download it from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/).

We also need to have pip installed. Execute the command `python get-pip.py` in the terminal to install it.

After installing Python and pip, open the terminal and navigate to the project folder. Then, execute the following commands:

- `pip install virtualenv` to install the virtual environment package.
- `python -m virtualenv .venv` to create a virtual environment.
- `source .venv/bin/activate` to activate the virtual environment.
- `pip install -r requirements.txt` to install the project dependencies.
- `python manage.py runserver` to start the server.

After running the last command, the terminal will display a message with the address where the project is running. Press `Ctrl + Click` on the link to open the website in your browser.

``` 
Homepage interface: The background is dark blue. At the top left, there is the Alura Space logo — a planet with a diagonal ring and a small star, followed by the words "Alura Space" in rounded letters. At the top right, there is a search field. On the left side of the page, we have the navigation menu with the options "Home", "Mais vistas", "Novas" and "Supreenda-me". In the body of the page, at the top, there is a banner with an image of space and the text "The most complete gallery of space photos!". Below it, it is written "Search by tags", followed by the tags "Nebulosa", "Estrela", "Galáxia" and "Planeta" in separate rectangles. Below, we have the section "Navegue pela galeria", followed by cards arranged in two columns with space-themed images. Each image has a tag in the upper right corner and information written at the bottom. (Translated from the Alura course project description) 
```
    