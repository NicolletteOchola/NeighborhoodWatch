# Project Name
Neighbourhood watch

## Author
Nicollette Ochola

## Description
- A private network for your neighbourhood, that allows members of the same community to post businesses and anything that concerns the members of the community. 

## User Stories
- Users create an account.
- Users can log in to application and view available Neighborhoods once they have an account.
- Users can navigate to, and view a neighborhood as well as its details, including business posts and an option to join.
- Users can create business posts.
- Users can view their profile page.
- Users can use the side navigation bar to navigate to the home page, profile page as well, login and logout.

## BDD
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Users can sign up for an account | Input credentials in the registration form then click Sign Up | Users are prompted to login into their account |
| Users can log into their account | Input the correct credentials of an existing account in the login form | Once verified, users are navigated to the home page where they can view available neighborhoods |
| Users can view the details of a specific neighborhood | Click on a given neighborhood | Users are directed to the neighborhood's page where its details, business posts as well as an option to Join, are displayed |
| Users can view their profiles | Click on Profile in the side navigation | Users are directed to their profile page with their profile information displayed |
| Users can create business posts | Click on the Post Business option in the side navigation bar | User will be navigated to a new page with a form to create a new post |\

## Technologies Used
- Django 1.11 (Python3.6)
- HTML/CSS
- Bootstrap (MDB bootstrap)
- Javascript

## Setup Requirements
Here is a run through of how to set up the application:

- Step 1 : Clone this repository using the git clone link:
git clone https://github.com/Isaacg94/Neighbourhood-Watch.git
- Step 2 : Navigate to the directory:
cd Neighbourhood-Watch-master
- Step 3 : Open the directory created with your favorite IDE. If Atom type atom . if VSCode type code . . This will lauch the editor with the project setup,
- Now feel free to hack around the project.

## Testing
- To run the tests on the application run `python3.6 manage.py test app`

## Known Bugs
Posts are added from the admin side, user can not directly add posts and businesses.


## Contacts
nicoeochola@gmail.com

## Live Link
https://nicolewatch.herokuapp.com/


## License
MIT Licence (c) Nicollette Ochola 2020


