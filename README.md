# Ace Of Steaks

IMAGE OF INDEX PAGE

## User Experience (UX)

### Site Visitor Goals

1. As a site visitor, I want the theme of the restaurant to be immediately clear, for example: Fast food, Thai, Sushi, Steakhouse etc.
2. As a site visitor, I want booking a table to be a painless experience with as little input as possible to make my reservation.
3. As a site visitor, I want some sort of confirmation of my booking.
4. As a site visitor, I want access to my booking should I need to cancel my table.
5. As a site visitor, I want to be able to contact the restaurant either via an email form or a telephone number.
6. As a site visitor, I want to be able to use my location to find the restaurant closest to me, especially if it is part of a chain with hundreds of sites.
7. As a site visitor, I want the menu or sample menu to be easily available.

### Admin User/Owner Goals

1. As the site owner/admin user, I want the ability to amend and delete reservations, updating the site to allow the table to be replaced by a new booking.
2. Ensure a table can not be booked for the same time (double booked).

### Design

- #### Colour Scheme
    - #CCA232 - Gold
    - #C0C0C0 - Silver
    - #000000 - Black


- #### Typography
    Bebas Neue 
    Montserrat

- #### Imagery
    dark, detailed images

### Wireframes

- Figma Desktop Wireframe - [View](https://www.figma.com/file/JePmpqBjAyO6VrkuiHi4Fp/Ace-Of-Steaks---Desktop?node-id=0%3A1)

![Figma Desktop Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/desktop-wireframe.PNG)

- Figma Mobile Wireframe - [View](https://www.figma.com/file/tF92jalVcQwe1qMrQD85GQ/Ace-Of-Steaks---Mobile?node-id=0%3A1)

![Figma Mobile Wireframe](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/mobile-wireframe.PNG)

### Flowchart

- Lucidchart - [View](https://lucid.app/lucidchart/05f9c042-a9a0-4282-a11f-2fcfde94bfee/edit?invitationId=inv_335d6257-282e-4923-848d-2f21a828f50e)

![Lucid Snake Flowchart](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/lucid-flowchart.PNG)

# TO COMPLETE WHEN/AFTER BUILD

## Features
Below is a brief overview showing the main features of the site.

### Feature1
- Sign in model
- manage booking - Cancel table.
- book table - form (self populating when signed in)
- menu sample
- contact form
- google map with pin markers for restuarant locations
- show/hide menu button


## Future Features

- text
## Technologies

### Created by using:

- HTML5
- CSS3
- JavaScript
- Python
- Django

### Programs including:

- [Heroku:](https://www.Heroku.com/)
- Heroku was used to share the app online.
- [Cloudinary](https://www.cloudinary.com/)
- Cloudinary was used to store all imagery for the site.
- [Google Fonts:](https://fonts.google.com/)
- Google fonts were used to import the 'Bebas Neue' into the style.css file.
- [GitPod:](https://gitpod.io/)
- GitPod was used to create and update the website throughout via the terminal to push changes to GitHub.
- [GitHub:](https://github.com/)
- GitHub was used to commit changes during development and ensure no work was lost.
- [Figma:](https://figma.com/)
- Figma was used to create the wireframes during the design process.

## Testing

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

### Lighthouse Testing

- text

- Desktop Results

![Lighthouse Desktop Results](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/lighthouse-desktop.PNG)

- Mobile Results

![Lighthouse Mobile Results](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/lighthouse-mobile.PNG)

### Testing User Stories from User Experience (UX) Section

- #### site Visitor Goals

Q1. As a site visitor, I want a clear understanding of the interactive game on show.

- A large majority of the world's population have played or understand how Rock, Paper Scissors is played. As soon as users enter the site, it is abundantly clear what the game is and how to play it. The default icons on show increase the clarity.

Q2. As a site visitor, I want a brief description of the rules in order to win the game.

- The rules are very clear to see, labelled up beneath the interactive buttons. "ROCK BEATS SCISSORS" etc.

Q3. As a site visitor, I want to have live scoring round by round.

- Round by round after the alert message of the outcome, the round number is updated along with the tally of rounds won, rounds drawn or rounds lost, all looking from the user's perspective.

Q4. As a site visitor, I want to enjoy the game and come back again and again.

- The way the game is run is so easy to play and understand. I have found myself saying "one more round" constantly, just to finish with a win and beat the computer.

### Continued Testing

- The Website was tested on Google Chrome, Internet Explorer (see glitches), Microsoft Edge and Safari browsers.
- The website has been displayed on various devices such as Desktop PC, iMac, Laptop, iPhone X & iPad Pro
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Glitches
#### Computers

- Internet Explorer - The website doesn't display any images or button labels. This leads to no functionality.

#### Mobile (iPhone X)
- The hover pseudo has been removed on smaller devices (tablet-phone) to ensure the user the game has been reset, as the button were not returning to original style after selection.
- The button images appear stretched. However, there were no issues via inspect mode in a browser.
- The button labels don't line up centrally beneath the buttons. Again, there were no issues via inspect mode in a browser.

## Deployment
Whitenoise
https://devcenter.heroku.com/articles/django-assets

### Heroku

Heroku was the program used to share the game, it was accomplished by using the following steps:

1. Log in to Heroku. On your dashboard, click "New" and then click "Create new app".

2. Fill in the field for App name - It must be a unique name to Heroku. 
    -   Then select the region of Europe and click "Create app"

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/heroku-new-app.PNG)

3. In the "Settings" tab, scroll down to "Buildpacks" and click "Add buildpack".
    -   Select "python" and click "Save changes"
    -   Select "node.js" and click "Save changes"

![Heroku - Add buildpack](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/heroku-add-buildpack.PNG)

4. Scroll back and click the tab "Deploy"
    - Choose "GitHub" as the Deployment method
    - Enter the GitHub repository name and click "Search"
    - The repository should appear below, then click "Connect"

![Heroku - Deployment method](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/heroku-deployment-method.PNG)

5. Then click the "Deploy Branch" button in the "Manual deploy" section. This way you can see the code being written.

![Heroku - Manual deployment](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/heroku-manual-deploy.PNG)

6. Once that is complete, a message will appear with "Your app was successfully deployed" and a "View" button. This will take you to the app directly.

![Heroku - New app](https://raw.githubusercontent.com/liamsmith3194/ace-of-steaks/main/assets/readme-images/heroku-deployed-successfully.PNG)

## References

### Code

- Extending and customizing django-allauth [GeeksforGeeks](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)

- How To Add Database Forms To A Web Page [Youtube - Codemy.com](https://www.youtube.com/watch?v=CVEKe39VFu8&t=357s)

- Create a datepicker [stackoverflow](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django/35968816#35968816)

- Display data based on logged in user [stackoverflow](https://stackoverflow.com/questions/53453746/django-displaying-appointment-linked-to-a-particular-user-on-their-profile-only)

- Bring through user id automatically [Youtube - Codemy.com](https://www.youtube.com/watch?v=TAH01Iy5AuE)

- Count post by user [stackoverflow](https://stackoverflow.com/questions/50393455/count-the-number-of-posts-by-a-user-django)

- Avoid duplicate records [poopcode.com](https://poopcode.com/python-code-snippet-how-to-avoid-inserting-duplicate-records-in-orm-django/)


- Filter on date and time today [stackoverflow](https://stackoverflow.com/questions/11245483/django-filter-events-occurring-today)

### Content

- All content was written by the developer.

#### Import
- Pygame Module - "a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language." [pygame.org](https://www.pygame.org/wiki/about)

- Random Module - "The random module is a built-in module to generate the pseudo-random variables. It can be used to perform some action randomly such as to get a random number, selecting a random element from a list, shuffle elements randomly, etc." [Tutorials Teacher](https://www.tutorialsteacher.com/python/random-module)

### Mentions

- My Mentor for answering my questions throughout.

- Slack users for constructive feedback, suggestions for improvements and video calls.





























![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome liamsmith3194,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
