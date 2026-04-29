# Blog-app-with-Django
DofE skill

!! - settings.py has been hidden to keep my device safe as it contains passwords

1 - Created a virtual environment for Django and mysqlclient, connected Django to MySql, created and migrated an inital model (posts and comments), some templates created and linked to a url / view but remain empty for now


2 - Started to make some of the HTML pages' content (mainly only index.html which can then be copied as needed to others), made the basic functionality for posts to be added to the database automatically. Next week(s), to add functionality that allows users to control and view posts in the browser and to allow for authentication.


3 - made the sign-up logic in the backend using a Django form to gather the data from the user and then creating the new user in the User model.Created the sign-up page to the URL: /accounts/signup/    Also, created some CSS for the login and signup pages.

4 - Creating the authentication and login features (including login sessions). Beginning to make an alert feature so that I can display errors to the user in a clean, simple way (to be finished next week)

5 - Made the alert box and some JS that will make the alert box appear ONLY whent there is an error. I found a few bugs when I was testing the app and have fixed them (such as templateSyntaxErrors that went unoticed before). I made a dummy model inside the accounts app that will allow me to set up some permissions and groups when the time comes. 

6 - The creator field has been added to the posts model. It allows me to access it later on and find all their details. I have made the UI on the create page better (although some bugs stils)

7 - I have made the myposts.html page with the logic that will show only the posts that the logged in user has posted. I have started to work on the edit page but couldn't work out how to make the form prefilled.

8 - I have created all the logic for the prefilled edit form and a delete function by using variable passed in through the URL

9 - I have started with the search feature. I want to make it so that there will a split between the users' own created posts and the others in the whole site. This should be done in the views and I have already made the .exclude() that should allow this to happen (in the users' own ones I should make another content in the dictionary)

10 - Tried to change the search feature because it wasn't working. Still not working so I will need to keep looking into it. Should have it completed by next week

11 - Found the issue with the search. Spent a long time looking at the view function but it turns out that the template would always show the error message even when there is posts. Made a simple view post page for the specific posts by using the post_id (need to work on this next week though to make it more advanced). It will check for the post to see if it exists and then it will show the pafe is it does. Otherwise it will show the home page again. Next week I need to tidy up the whole site to make it more usable. 

12 - Cleaned the website up. Completely changed the UI to make it more modern and clean. All the buttons should now work and lead to the correct page. Created some back buttons for certain pages and now all the pages should link together. Fixed a small search issue again. All should now be working as it is meant to. 