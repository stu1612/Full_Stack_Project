# Full Stack Project

[![Build Status](https://travis-ci.org/stu1612/Full_Stack_Project.svg?branch=master)](https://travis-ci.org/stu1612/Full_Stack_Project)

Graphic Design is a django based project with the purpose of creating a web application where the owner of the site is able to create bespoke design service which are made available for the user to purchase.  The user, after having registered an account and logged in is able to purchase and add design specification details.  After payment, the design specifications is viewable for the site admin to inspect where they can send back a design type to the user's foreign id.  

This web application's purpose is to present potential graphic design features for the user where they can order and specifiy their design needs.

# UX

  - Introduction

When the user enters the site, all content is available where the graphical design features are cleary presented - type of design, sales marketing about the beneficial features of the design, cost, production qty, size dimension of design, some design notice information to help the user think about what content would be good to include when adding their design specification details.

> "As a user i want to clearly see the graphic design services and the basic details of what the design includes.

  - Design confidence

For the site to maintain a professional standard and instill confidence to the user, the site will have clear navigation to testimonials and previous design jobs created.

> "As a user i want to be able to see past design features and past client testimonials"

  - Registration

So that the user can investigate the site before having to fill out forms, no registration is required to see the design services.  Only when the user wishes to pay for a service, is the user directed to register.  The reason for this is to allow the user the freedom to navigate and learn without making any commitments until needed, thereby allowing increased time for the user to stay on the site and thereby increase the chances of the user making a purchase.

> "As a user i want to be able to navigate through the graphic design content before having to fill out forms - if i want to purchase a product/fill out forms it is because i am ready to make a commitment"

- User authentication

As the user registers, logs in and logs out, performs payment - messages will confirm this action to provide site user security that the action performed was succesful or not.

> "As a user I would like feedback if my desired action worked or not - especially when making a payment"

- User navigation

To support the user in knowing how to navigate throught the process of finding their design services and then processing a payment - a step by step guide notification is available which helps familiarise the user in knowing what to do

> "As a user it would be nice to have some visual and informational guide as to how i go about finding the services i am interested in, how i can process my payments, and know what happens next"

# Features
The features of this site will be specificied by the generated apps and the purpose of these functions

- accounts / services

Contains the logic that performs the registration, log in/out, testimonial reviews and index/profile html redirect functionality as well as the logic to display the services available for the user to choose from.  Orginally a task app was developed in this feature to show past jobs done.  However, for now, it was changed to just add reviews to the site rather than from the admin panel.  Reason is because of long term considerations.  As the site would grow it is expected that similiar services, such as LOGO DESIGN, would require more detailed content and become more specific.  Thereby, for one particular service, there would be a variety of choices for the user to search and select from.  Therefore, the long term plan would be to showcase previous jobs done when the user selects a specific service type.
> "My client needs a logo design for a startup vegan restaurant which wants to advertise itself as a high street restaurant which appeals for all food eater"

The example above shows the need for the user to want to see previous jobs done related to :FOOD, HIGH STREET BRANDING, VEGAN.

This too would also mean that the service app would develop along these lines - whereby rather than having a general list of services - they would be categorised, and within these categories the user would find specific services.

- cart / checkout

These features allows the user to save items they wish to buy (service) and then proceed to the checkout for payment.  The payment functionality is a Stripe API.  Currently, the user adds their design specifications before confirming their payment details.  

For future features, the site would be built to not handle payments depending on the job requirement.  If costs of the job were over x amount, then a online payment invoice would be sent asking that the user pay a percentage of the toal costs prior to project start date.  Upon completion and the user having signed off the job, then a final invoice would be sent.  The online invoice payment would be sent to the users profile ID.

- search

Allows the user to add generic search parameters to filter the service items

- notifications

Allows the user to add a testimonial to the site

# Technologies Used

* [HTML 5](https://html.spec.whatwg.org/) - basic templating language
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) - site styling
* [Bootstrap](https://getbootstrap.com/) - HTML structure for mobile first navigation
* [JQuery](https://code.jquery.com/) - front end site functionality
* [JavaScript](https://www.keycdn.com/support/javascript-cdn-resources) - required code to action Stripe API
* [Django](https://www.djangoproject.com/) - python platform for project
* [Python](https://www.python.org/) - backend functionality
* [Stripe API](https://stripe.com/en-se) - API to process online payments
* [AWS](https://aws.amazon.com/) - devlopment platform 
* [Travis](https://travis-ci.org/) - test integration for site
* [Heroku](https://dashboard.heroku.com/) - site hosisting platform

# Testing

Testing of the site was done ad-hoc or when de-bugging.  After each app was created the functionality and styling was applied.  Key problem areas were implementing the notifications app and stripe app.  When building the notification functionality - the returned data from the admin appeared on all user "My_Project" pages.  Also, the stripe payments did not process because the admin.py did not have the required models.

- User login/logout - can the user login and logout and see confirmation that this has worked?
- User Registration - can the user register an account and see confirmation that this has worked?
- User Service selection - can thr user easily see the graphic design services, select a design and see that their order has been recorded?
- User Cart - can the user see their listed ordered items and alter this selection and confirm to payment plan?
- User Checkout - can the user see a confirmation and cost breakdown of their order, add graphic design information to help with the design they need, add personal information and process their payment ?
- Can the the admin see this order and communicate back to the user the finished artwork?
- Can the user add a testimonial review ?

The site was tested to be mobile first repsonsive and navigate easily for the user. 

- Deployment - when connecting with travis errors were encountered as I had pycurl added to the requirements.txt which didnt need to be there.  Once removed and other dependencies updated, the build succesfully passed.  
- when swithcing from Github version, the "SECRET_KEY" needs to be added in settings.py before being linked to the env.py file when hoisting to Heroku.  Local version wont load otherwise.



# Deployment

This is the third version of the planned project which is why various git commits are not available.  Upon deployment of the orginal version a manage.py file was created within my project folders which caused the site to not deploy to Heroku correctly.

 - this project was created on AWS and connected to my GitHub account during the production stage.  When completed, the project build was tested with Travis and when succesful, connected with Heroku.
 - Github - to run on local version - the command line is - python3 manage.py runserver $IP:$PORT
 - Local version wont run unless SECRET_KEY is installed in settings.py
 - Developed version - https://github.com/stu1612/Full_Stack_Project / https://97813ff8ec87479597c709b9583fa00a.vfs.cloud9.us-east-2.amazonaws.com/
 - Deployed site version - https://stu-fullstackproject.herokuapp.com/


# Credits

This project contains code from Code Institute django project learnings - Eccommerce.  In particular, code extracted was the accounts functionality, stripe installation and JS code, cart and checkout functionality, settings.py.  Some minor changes were made but the overall code was taken used from the learning content.  

# Media

Images were obtained from Unsplash.com