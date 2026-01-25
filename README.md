# Blog-app-with-Django
DofE skill

!! - settings.py has been hidden to keep my device safe as it contains passwords

1 - Created a virtual environment for Django and mysqlclient, connected Django to MySql, created and migrated an inital model (posts and comments), some templates created and linked to a url / view but remain empty for now


2 - Started to make some of the HTML pages' content (mainly only index.html which can then be copied as needed to others), made the basic functionality for posts to be added to the database automatically. Next week(s), to add functionality that allows users to control and view posts in the browser and to allow for authentication.


3 - made the sign-up logic in the backend using a Django form to gather the data from the user and then creating the new user in the User model.Created the sign-up page to the URL: /accounts/signup/    Also, created some CSS for the login and signup pages.

4 - Creating the authentication and login features (including login sessions). Beginning to make an alert feature so that I can display errors to the user in a clean, simple way (to be finished next week)

5 - Made the alert box and some JS that will make the alert box appear ONLY whent there is an error. I found a few bugs when I was testing the app and have fixed them (such as templateSyntaxErrors that went unoticed before). I made a dummy model inside the accounts app that will allow me to set up some permissions and groups when the time comes. 

6 - (to make this week: the account edit and dashboard for logging out, finish and finalize the button on the index.html that currently says different things for people that are logged in and not logged in but doesn't behave differently, begin on the posting functions) NOT COMPLETED WEEK 6 YET, NEXT WEEK