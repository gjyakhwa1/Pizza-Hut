# Project 3

Web Programming with Python and JavaScript

### account app

It handles all the account related activities like register, login, logout.

##### templates folder in account app

It contains three templates
1. accountlayout.html--->provides a base layout for register and login form
2. loginpage.html---->page from which user can login
3. registerpage.html---->page from which new user can be registered

##### forms.py
It is created to handle the register forms

#### Other python files are as per the Django documentation

### orders app

It is created show as to display the menu list and order different stuff from the menu list

##### templates folder in orders app

It contains eight templates
1. baselayout.html---->provides the base layout for our website, created with help of bootstrap and custom CSS
2. cart.html----->provides a virtual cart for registered user, each cart is associated with only one user ,cart is unique for every user
3. confirm.html----->file which displays the confirm order, can only be view by person whose account is superuser
4. dinnerplatters.html---->displays the list of dinner platters from Pinocchio's pizza and subs
5. pasta.html--->displays the list of pasta from Pinocchio's pizza and subs
6. pizza.html--->displays the list of pizza from Pinocchio's pizza and subs
7. salad.html---->displays the list of salad from Pinocchio's pizza and subs
8. subs.html----->displays the list of subs from Pinocchio's pizza and subs

### static folder
It handles all the CSS as well as images of website


