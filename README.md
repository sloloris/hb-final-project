# Welcome to FriendKeeper
### The email-automating web application for those of us who struggle to keep in touch with the people who matter!

![alt text](https://github.com/sloloris/hb-final-project/blob/scheduleview/static/img/landing_page_readme.png "FriendKeeper landing page.")

## Table of Contents

## Introduction
FriendKeeper was my final project for the Software Engineering Fellowship at Hackbright Academy and the first full web application I built. 

## Stack
__Backend:__ Python, Flask, SQLAlchemy, PosgreSQL
__Frontend:__ React/Redux, JavaScript, jQuery, HTML5, CSS3
__APIs:__ Google Contacts, Gmail

## About The App
FriendKeeper both motivates and helps you to keep in touch by allowing you to schedule when it will reach out to your friends for you - so you don't have to think about it until they respond! With FriendKeeper, you can set a start date and a period (measured in days) on any given contact according to which FriendKeeper will send them one of your self-created email templates. Then you just have to wait for them to follow up.

![alt text](https://github.com/sloloris/hb-final-project/blob/scheduleview/static/img/scheduleview.png "ScheduleView. This portion of the app is a single-page app built complete using React/Redux.")

## Tech Specs

### Google OAuth 2.0
Login is implemented using Google OAuth 2.0. Upon login, the server pulls the user's profile and contact information using the Google Contacts API and saves it to the database (for new users) or updates it (for existing users). (Most of the relevant functions can be found in [server_functions.py](./blob/scheduleview/server_functions.py)). If later calls to the API are needed, the app can request a refresh token (code in [quickstart.py](./blob/scheduleview/quickstart.py)).

### Webpack 
Webpack is a module bundler that makes it easier to organize your JavaScript into bite-sized pieces upon which Webpack can build a dependency graph, or model your DOM, in order to condense all of the code into a single file. This allows your frontend to load all components using a single HTTP request.

### React/Redux

### Python & Flask 

### SQLAlchemy

## TODO
* fix autocomplete case sensitivity
* appearing 'schedule' button on selected contacts
* add user's google photo to leftnav
* contact sort by field on click
* pageview for scheduled messages
* pageview for sent messages
* pageview for preferences


## About the Developer
Isabelle is a recent graduate of Hackbright Academy, a San Francisco-based accelerated full-stack software development program for women. Prior to that, she completed a Master of Public Policy with a concentration in statistical analysis at the Hertie School of Governance in Berlin, [where she was first exposed to coding in R in the context of quantitative social science research.](https://github.com/sloloris/IsabelleandDiegosFinalResearchProject/tree/master/FinalPaper) Her main passion lies in the use of data-driven technologies to improve governance and policymaking, with a focus on improving integration of immigrants and equity of opportunity for women and minority groups through digital democracy technologies and better access to government services.

Isabelle's other interests include linguistics, ceramics, cookies, and amateur acrobatics. She holds a B.A. in Linguistics and International Relations from Tulane University.

Visit her LinkedIn profile [here](https://www.linkedin.com/in/isabelle-miller/).

