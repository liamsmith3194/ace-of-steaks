# Ace Of Steaks

![Booking Page](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/booking-page.PNG)


## Agile Methodology - Planning & Requirements

-   GitHub Issues - [View](https://github.com/liamsmith3194/ace-of-steaks/issues)
![GitHub Issues](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/github-issues.PNG)
-   Project Planning Board - [View](https://github.com/liamsmith3194/ace-of-steaks/projects/1)
![GitHub Project Planning Board](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/github-project-planning-board.PNG)

### Site Visitor Goals

1.  As a site visitor, I want the theme of the restaurant to be immediately clear, for example: Fast food, Thai, Sushi, Steakhouse etc.
2.  As a site visitor, I want some sort of confirmation of my booking.
3.  As a site visitor, I want access to my booking should I need to cancel my table.
4.  As a site visitor, I want to be able to amend my booking, whether that is by changing the date and/or time or number of guests.
5.  As a site visitor, I want the menu or sample menu to be easily available.

### Admin User/Owner Goals

1.  As the site owner/admin user, I want the ability to amend and delete reservations, updating the site to allow the table to be replaced by a new booking.
2.  As the site owner/admin user, I want to ensure a table can not be booked for the same date and time (double booked).

### Django Admin Site
-   fjdsfgjd 


### Wireframes

-   Figma Desktop Wireframe - [View](https://www.figma.com/file/JePmpqBjAyO6VrkuiHi4Fp/Ace-Of-Steaks---Desktop?node-id=0%3A1)

![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/desktop-wireframes-1.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/desktop-wireframes-2.PNG)
![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/desktop-wireframes-3.PNG)

-   Figma Mobile Wireframe - [View](https://www.figma.com/file/tF92jalVcQwe1qMrQD85GQ/Ace-Of-Steaks---Mobile?node-id=0%3A1)

![Figma Mobile Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/mobile-wireframe.PNG)

### Flowchart

-   Lucidchart - [View](https://lucid.app/lucidchart/05f9c042-a9a0-4282-a11f-2fcfde94bfee/edit?invitationId=inv_335d6257-282e-4923-848d-2f21a828f50e)

![Lucid Snake Flowchart](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/lucid-flowchart.PNG)


## Agile Methodology - Design

### Colour Scheme
-   #CCA232 - Gold
-   #C0C0C0 - Silver
-   #000000 - Black
-   #FFFFFF - White
-   #343A40 - Grey
-   #DC3545 - Red

-   The site colour scheme is all about contrast.
-   The full length white navigation bar against the sharp image, but also black text and eye catching pseudo-classes.

-   The gold is used throughout the site, for the logo, all headings, subheadings and buttons.
-   All main buttons in their native form are gold and black text.
-   When hovered over the buttons, they reverse in style, black background and gold text.

-   The navigation menu items are black, when hovered over the links change colour to gold and the font weight is raised to the thickest possible to ensure the user is certain where the cursor is positioned.
-   The active class is styled using the hover classes attributes but underlined with a silver bar similar to the logo design. This make it even more clear for the user to know which page they are on.

-   The only other colours to mention are taken from the Bootstrap button classes (dark & danger).
-   The grey is used for the 'Update' button.
-   The red is used for the 'Delete' button.

### Typography
-   All titles use the bold striking typeface of Bebas Neue all with various letter spacing differences between headings and subheadings to make them more legible.
-   The body typeface of Montserrat produces a sharp contrast from the titles. This is a very popular font for web design because of its readability.

### Imagery
-   One image used throughout the site, which sits behind the transparent body content window.
-   It is quite a dark image to ensure the content is at the forefront of the user's attention and help the readability of the headings.

## Features
Below is a brief overview showing the main features of the site.

### Layout
-   Using the grid set up from Bootstrap, 12 columns split into 3 for the navigation and 9 for the content.
-   The hero image covers the "content" side of the screen and lays behind the transparent window.
-   All the page titles use a consistent theme.
-   All page content including forms, buttons and text is presented inside the window.

### Navigation Bar
-   Located on the left side of screen, which includes the logo, menu items, opening times information and social media links.

![Navigation Bar - Standard](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/nav-bar-new-user.PNG)

-   The navigation bar automatically collapses at a screen width of 767px. This produces the "Hamburger button" to open and close the nav bar on a click.

![Navigation Bar - Hamburger button](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/nav-bar-hamburger-button.PNG)

-   More menu items are available and shown after a user has signed in or registers for the first time. For example, 'Book A Table' and 'Manage Booking'.

![Navigation Bar - User logged in](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/nav-bar-existing-user.PNG)

### Allauth
-   Allauth has been installed to enable users to create, login and sign out of their accounts.
-   The register form has been amended to include first and last name.
-   All the user details are submitted and saved to the database.

![Allauth - Register Form](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/allauth-register-page.PNG)

### Boostrap Alerts
-   When the user logs in, an alert appears in the navigation bar to show the user they have successfully signed in.
-   The alert is also triggered when the user logs outs.

![Boostrap - Alert](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/bootstrap-alert.PNG)

### Boostrap Nav Pills
-   The menu page uses the bootstrap component nav pills.
-   By default it shows the starters but choices span across the window showing the mains, sides and desserts. Clicking on any of these options changes the data correspondingly.

![Menu Page - Nav pills](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/menu-page.PNG)

### Book A Table
-   The booking form self populates with the user's first name, last name and email address, taken from the registration form.

![Booking Page - Form](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/booking-page.PNG)

-   Bookings must be submitted one day in advance and maximum 30 days prior.?????
-   On a successful submission, the user will receive an automated email confirmation, showing the location, date and time and the number of guests.
-   Also on a successful submission, the user will be redirected to the 'Manage Booking' page.
-   If the date and time isn't available on submit, the user is greeted with a validation error "Date and/or time not available, please try again."
-   If the user already has a booking that hasn't expired, they will be forced to either amend or delete their reservation by clicking on the 'Manage Booking' button.

![Existing Booking Page](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/existing-booking-page.PNG)

### Manage Booking
-   The booking data is presented in showing only the critical details such as location, date and time and number of guests.
-   The user has two clear buttons to amend or delete the booking.
-   Clicking the amend button produces the booking form again with the previously entered booking data.
-   When the user amends the booking and saves, the database is updated and when redirected, the manage booking page is updated to show the change(s).
-   If the user clicks the delete button, they are asked to confirm this, "Are you sure you want to delete your booking?". This is displayed alongside two options "No, Cancel" and "Yes, Delete"
-   Clicking on either of the buttons redirects the user back to the 'Manage Booking' Page, whether the booking is still seen is determined by which button the user clicked.
-   If the user doesn't have a booking in the database, they are notified by a simple paragraph "There is no booking currently in the database" and shown a button linking them to the 'Book A Table'.

![Manage Booking](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/manage-booking-page.PNG)


## Agile Methodology - Implementation

### Created by using:

-   HTML5
-   CSS3
-   JavaScript
-   Python
-   Django

### Programs including:

-   [Heroku](https://www.Heroku.com/) was used to share the app online.
-   [Bootstrap](https://getbootstrap.com/) was used to create the framework for the site, including the grid set up and other components such as buttons and alerts.
-   [Font Awesome](https://fontawesome.com/) was used for the social media icons within the collapsable navigation bar.
-   [Google Fonts](https://fonts.google.com/) was used to import the 'Bebas Neue' and 'Montserrat' into the style.css file.
-   [GitPod](https://gitpod.io/) was used to create and update the website throughout via the terminal to push changes to GitHub.
-   [GitHub](https://github.com/) was used to commit changes during development and ensure no work was lost.
-   [EmailJS](https://www.emailjs.com/) was used to send email booking confirmations to the user.
-   [Figma](https://figma.com/) was used to create the wireframes during the design process.
-   [Lucidchart](https://lucidchart.com/) was used to create the step by step workflow to visualise how the user can book and manage their reservation.

## Agile Methodology - Testing

### Validation Testing

The W3C Markup Validator and W3C CSS Validator Services were used to ensure there were no syntax errors in the project.

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fliamsmith3194.github.io%2Face-of-steaks%2F)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fliamsmith3194.github.io%2Face-of-steaks)
- [Jshint JavaScript linter](https://jshint.com/) - 26 warnings, the mast majority:
    -   'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    -   'template literal syntax' is only available in ES6 (use 'esversion: 6'.
- [PEP8](http://pep8online.com/) Python linter was used to ensure there were no syntax errors in the project.
On the first use my code produced over 45 warnings and/or errors including:
- "blank line contains whitespace"
- "indentation is not a multiple of four"
- "line too long (93 > 79 characters)"

These have now all be rectified and the link to the results text document is below.
- [Final results](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/pep8-results.txt)

### Manual Testing

- Responsive Testing
    -   d

- Index Page
    -   Ace of Steaks logo link
    -   Individual page links
    -   Social media links open in new tab.
    -   Window link to menu page
    
- Register Page
    -   Username taken
    -   All fields required
    -   Not a recognised email address
    -   Passwords don't match
    -   Sign in link

- Login Page
    -   Invalid credientials
    -   Remember me
    -   Register link

- Logout Page
    -   Logout link

- Booking Page
    -   All fields required
    -   Date unavailable before or on the day of booking
    -   No bookings will be taken after 30 days in advance.
    -   Double booking
    -   All account details coming through

- Manage Booking Page (Overview)
    -   All data matches user input

- Manage Booking Page (Update)
    -   Form loads user entry
    -   Date unavailable before or on the day of booking
    -   No bookings will be taken after 30 days in advance.
    -   Double booking
    -   Booking change saved and updated in overview and database.

- Manage Booking Page (Delete)
    -   Cancel button keeps booking and returns user the manage page.
    -   Delete button removes booking from users view and from the database.

- Menu Page
    -   All links show correct data
        
### Lighthouse Testing

- text

- Desktop Results

![Lighthouse Desktop Results](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/lighthouse-desktop.PNG)

98
Performance
92
Accessibility
92
Best Practices
89
SEO

- Mobile Results

![Lighthouse Mobile Results](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/lighthouse-mobile.PNG)

85
Performance
97
Accessibility
92
Best Practices
91
SEO


### Continued Testing

- The Website was tested on Google Chrome, Internet Explorer (see glitches), Microsoft Edge and Safari browsers.
- The website has been displayed on various devices such as Desktop PC, iMac, Laptop, iPhone X & iPad Pro
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Glitches
#### Computers
-   Whitenoise - CSS styles not showing in Heroku [Heroku Dev Center](https://devcenter.heroku.com/articles/django-assets)

-   Django - [Errno 111] Connection refused [Stackoverflow](https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused)

-   Internet Explorer - The website doesn't display any images or button labels. This leads to no functionality.

#### Mobile (iPhone X)
-   The hover pseudo has been removed on smaller devices (tablet-phone) to ensure the user the game has been reset, as the button were not returning to original style after selection.
-   The button images appear stretched. However, there were no issues via inspect mode in a browser.
-   The button labels don't line up centrally beneath the buttons. Again, there were no issues via inspect mode in a browser.

## Deployment

### Heroku & GitPod

Heroku & GitPod were the program used to share and deploy the app, it was accomplished by using the following steps:

1. Log in to Heroku. On your dashboard, click "New" and then click "Create new app".

2. Fill in the field for App name - It must be a unique name to Heroku. 
    -   Then select the region of Europe and click "Create app"

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/heroku-create-app.PNG)

3. In the "Resources" tab, scroll down to "Add-ons" and search for "Heroku Postgres".
    -   Once selected and saved in the "Settings" tab click "Reveal Config Vars", this produces a database url

![Heroku - Add Heroku Postgres](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/heroku-resources.PNG)

4. In GitPod set up a env.py file in the repository.
    -   Create an environment variable for "DATABASE_URL" and paste the value from Heroku.
    -   Create an environment variable for "SECRET_KEY" and create your key using any characters available.

5.  Copy the secret key to Heroku by adding the variable in the "Config Vars" section.

6.  In the settings.py file import:
    -   os
    -   dj_database_url
-   Add the if statement:
    -   if os.path.isfile('env.py'): import env

7.  Amend the secret key variable to the secure key created earlier:
    -   "SECRET_KEY = os.environ.get('SECRET_KEY')

8.  Add our Heroku host name into the allowed hosts, this is your Heroku app name followed by herokuapp.com.
    -   Add "localhost" too, so the app can be ran locally.

9.  Scroll down the "DATABASES" section
    -   Comment out the default code and add the "DATABASE_URL" variable created earlier:
    -   DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

10. Create a procfile
    -   It must be named like so; "Procfile" and sit in the root directory.
    -   Inside the file add "web: gunicorn" followed by the app name .wsgi
    -   For example: "web: gunicorn aceofsteaks.wsgi"

11. Scroll back and click the tab "Deploy"
    -   Choose "GitHub" as the Deployment method
    -   Enter the GitHub repository name and click "Search"
    -   The repository should appear below, then click "Connect"

![Heroku - Deployment method](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/heroku-deploy-section.PNG)

12.  Then click the "Deploy Branch" button in the "Manual deploy" section. This way you can see the code being written.

![Heroku - Manual deployment](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/heroku-manual-deploy.PNG)

13. Once that is complete, a message will appear with "Your app was successfully deployed" and a "View" button. This will take you to the app directly.

![Heroku - Successfully Deployed](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/static/images/readme-images/heroku-deployed-successfully.PNG)

## Agile Methodology - Evaluation

### Site Visitor Goals

1.  As a site visitor, I want the theme of the restaurant to be immediately clear, for example: Fast food, Thai, Sushi, Steakhouse etc.
2.  As a site visitor, I want some sort of confirmation of my booking.
3.  As a site visitor, I want access to my booking should I need to cancel my table.
4.  As a site visitor, I want to be able to amend my booking, whether that is by changing the date and/or time or number of guests.
5.  As a site visitor, I want the menu or sample menu to be easily available.

### Admin User/Owner Goals

1.  As the site owner/admin user, I want the ability to amend and delete reservations, updating the site to allow the table to be replaced by a new booking.
2.  As the site owner/admin user, I want to ensure a table can not be booked for the same date and time (double booked).

### Future Features

-   Social media sign in and register

## References

### Code

-   Extending and customizing django-allauth [GeeksforGeeks](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)

-   How To Add Database Forms To A Web Page [Youtube - Codemy.com](https://www.youtube.com/watch?v=CVEKe39VFu8&t=357s)

-   Create a datepicker [stackoverflow](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django/35968816#35968816)

-   Display data based on logged in user [stackoverflow](https://stackoverflow.com/questions/53453746/django-displaying-appointment-linked-to-a-particular-user-on-their-profile-only)

-   Bring through user id automatically [Youtube - Codemy.com](https://www.youtube.com/watch?v=TAH01Iy5AuE)

-   Count post by user [stackoverflow](https://stackoverflow.com/questions/50393455/count-the-number-of-posts-by-a-user-django)

-   Avoid duplicate records [poopcode.com](https://poopcode.com/python-code-snippet-how-to-avoid-inserting-duplicate-records-in-orm-django/)

-   Filter on date and time today [stackoverflow](https://stackoverflow.com/questions/11245483/django-filter-events-occurring-today)

-   Remove username from allauth [stackoverflow](https://stackoverflow.com/questions/19683179/remove-username-field-from-django-allauth)

## Conclusion

### Content

-   All content was written by the developer.

#### Import
    ???

### Mentions

-   My Mentor for answering my questions throughout.

-   Slack users for constructive feedback, suggestions for improvements and video calls.
