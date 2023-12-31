![logo](static/images/posterpalace-logo.png)

## Table of Content

[Overview](#overview)

+ [Project Rationale](#project-Rationale)

+ [Project Objectives and Outcomes](#project-objectives-and-outcomes)

+ [Target Audience](#target-audience)

[Model Views Template (mvt)](#model-views-template-mvt)

+ [Agile Terminologies](#agile-terminologies)

[Database Structure](#database-structure)

[Site Structure](#site-structure)

Home App

+ [User features and design](#user-features-and-design)

+ [Epics and user stories](#epics-and-user-stories)
    + [Epics](#epics)
    + [Admin](#admin)
    + [User](#user)

+ [Authentication and Authorisation](#authentication-and-authorisation)

    +[Emails](#emails)

+ [Navigation](#navigation)

+ [Products](#Products)

+ [Product Menu](#Product Menu)

+ Shopping Cart / Bag App

+ [Checkout App](#Checkout App)



+ [Reviews](#reviews)



+ [User Profiles](#user-profile)

+ [Site Colours and Font](#site-colours-and-font)

[CRUD Functionality](#crud-functionality)

ONLINE MARKETING - marketing app

Keywords and Meta

Social Media

Web content

Newsletter

Diverse Design Competition

[Placeholders and future updates](#placeholders-and-future-updates)

[Testing](#testing)

[Deployment](#deployment)

[Technologies Used](#technologies-used)

[Resources Used](#resources-used)

[Acknowledgements](#acknowledgements)

[Retrospective](#retrospective)


# Project Overview

Poster Palace - Beautify your room. Uplift your spirit.

The place to buy large (61 x 91 cm or 24.02 x 35.83 inches) and extra large (80 x 120 cm or 31.50 x 47.24 inches) posters to beautify your room and uplift your spirit. These high quality, designer inspired posters are statement pieces meant for display on a large statement wall. They have been designed for customers looking for unique and impactful wall art.

# Project Rationale

<details>

The development of an ecommerce store specialising in large and extra-large posters has been driven by several clear rationales:


**Market Demand**
While there are a number of sites offering wall art in a large range of sizes, there are very few offering larger sizes in wall art making it an underserved market. The platform also embraces a niche focus catering to customers searching for larger sized posters, providing an opportunity to differentiate from competitors and attract customers looking for a specialised product.

**Target Audience:**
Niche products attract a niche target audience. High quality attracts people willing to pay for luxury products. The large and extra-large sizes of these posters along with the printing quality means our product will attract a specific demographic including interior designers, business owners looking for wall art for their office or individuals with large homes looking for statement pieces to enhance their living space and aesthetics and of any room. 

Potential buyers include:

- Interior designers, landlords or homeowners who want posters to decorate their property.

- Office business owners looking for statement wall pieces or large pieces of art for their office and/or boardroom

- Retail business owners looking for large pieces of wall art to display in their shop or cafe.

- Travel enthusiasts, music lovers, sports enthusiasts, art admirers, etc. who might be interested in purchasing niche poster designs.

Parents looking to decorate their child’s room with a statement piece.

**Print Quality and Materials**
Posters will be produced using high-quality printing techniques and materials making them durable and long-lasting. Our commitment to quality will build brand trust with customers and support with any community engagement plans.

 **Online Shopping Trends:**
With the convenience of e-commerce we are leveraging the growing trend of online shopping. Customers can easily browse and purchase posters from the comfort of their homes, making it important that the website  is user-friendly and optimised for online transactions and engagement.

**Global Reach:**
The posters can be shipped internationally, providing an opportunity for the business to reach a broader audience and tap into markets beyond our immediate location.

**Customisation Options**
Customisation is an extremely popular and growing trend in online shopping. While customisation isn’t currently available on the platform there is the potential to offer this option, providing a more personalised touch and a unique selling point.
We can not only offer the chance for customers to customise using words but also using their own images.

</details>
<br>

# Project Objectives

<details>

The objective of this project is to build a Full-Stack eCommerce site with payment system and product structure based on business logic used to control a centrally-owned dataset.

As well as employing advanced User Experience Design to build this Full-Stack web application, search engine optimisation (SEO) and social media marketing techniques have been used in the delivery of content and images to improve audience and brand reach.

Objectives include:

**Develop a Comprehensive Product Catalog**
Design an appealing selection of posters in a variety of different areas, e.g. nature, zodiac, children etc.

**Implement Robust eCommerce Technology** 
Use Django as a reliable eCommerce platform that supports product listing and apps that support shopping cart management, checkout processes, and customer account management.

**Role-Based Access Control (RBAC)**
Implement RBAC to define and manage the roles of users. Superusers will have elevated privileges, including direct access to the admin area and data store. Non-admin users e.g. buyers will have the ability to use the site, update their profile and leave reviews but will not have direct access to the admin area.

**Ensure Mobile Responsiveness and Accessibility**
A mobile-first approach is taken to ensure the store is accessible and user-friendly on various devices, including smartphones and tablets.

**Integrate Stripe Secure Payment Gateway**: 
Incorporate Stripe as a trusted payment solution to facilitate secure and convenient transactions for buyers and prompt payment of funds to the owner.

**Set Up Customer Support System** 
Implement customer service solutions, including FAQs and email support, to assist customers effectively.

**Compliance and Legal Considerations**
Ensure the store complies with relevant laws and regulations, including data protection, terms and conditions, privacy policy and intellectual property rights.

**Optimize for Search Engines (SEO)**
Ensure the website, images and product pages are optimised for search engines to increase visibility and attract organic traffic. Writing optimised web content is important.

**Establish Effective Digital Marketing Strategies**
Digital marketing techniques such as social media marketing, email campaigns, and content marketing will be implemented to attract and retain customers. Ensuring above the fold content management.

**Create a Community Engagement Plan**
Develop strategies to engage with customers and create a community around the brand, such as through social media, competitions, and newsletters.
</details>
<br>

# Project Outcomes

<details>

**Functional eCommerce Platform**
A fully operational online store with a relational database that allows users to browse, select, and purchase posters to be delivered to their homes. The fully responsive platform will provide a wide range of products for sale and will be managed using role-based access to control the flow of information and ensure data is secure.

**Secure Site Registration**
Authentication mechanism deployed that lets users register and login so that their order details and address can be saved for future reference. All users must go through the confirmation of their email address before being allowed to log-in. The ability for users to buy products anonymously is also available if they prefer to do so.

**User-Friendly Interface**
An intuitive and easy-to-navigate website that provides a seamless shopping experience for customers. Includes the ability to search for products and to add potential products to a wishlist.

**Secure Payment Processing**
Using Stripe payment as a reliable and secure system for handling transactions, protecting customer data, and ensuring privacy.

**Effective Delivery Management**
Efficient delivery of products to customers within the stated delivery times.

**Customer Support Management**
Ability for customers to gain support with their order and/or use of the site, e.g. registration and logging in. Support is also available for non-registered users to get in touch.

**Customer Engagement and Retention**: 
Strong online presence via social media and SEO. A store that attracts customers via its activity and also encourages repeat business and customer loyalty.

</details>
<br>


## Testing

Please see my separate [Testing MD page HERE](/TESTING.md) that includes information on testing, viability and bugs.

## Deployment

<details>

Deployment took place immediately after installing Django.
<br>


#### Installing libraries

The following steps outline all libraries needed for successful deployment on Heroku. All neccessary-requirements and settings updates will not be discussed in this section as they are assumed as logical follow-up steps to installments. For a full explanation of how to install these libraries, refer to the links provided in [Technologies Used](#technologies-used).

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-Cloudinary-storage``


#### Create a PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Datacenter
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but create a more secure password.)


#### Update Settings

- Add the following code at the top of ``settings.py`` to connect the Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove the insecure secret key provided by Django in settings.py and refer to a variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to the new database, replace the provided **DATABASE** variable with 
    ````
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made


#### Connect to Cloudinary

- In the Cloudinary dashboard, copy **API Environment variable**
- In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"`` and remove ``CLOUDINARY_URL=`` from the variable string
- Add same variable value as new Heroku config var named **CLOUDINARY_URL**
- In ``settings.py``, in ``INSTALLED_APPS`` list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
- To define Cloudinary as static file storage add the following to settings.py
    ````
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

#### Allow Heroku as host

- In ``settings.py`` add
    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
    ````


***Deploy To Heroku***

First create A Pipfile in your project terminal.

In the terminal enter the command  pip3 freeze > requirements.txt, and a file with all requirements will be created.


***Setting up Heroku***

- Go to the Heroku website (https://www.heroku.com/)
- Login to Heroku and choose Create App.
- Click New and Create a new app.
- Choose a name and select your location.
- Navigate to the Deploy tab.
- Click on Connect to Github and search for your repository.
- Navigate to the Settings tab.
- Reveal Config Vars and add your Cloudinary, Database URL (from ElephantSQL) Email details, Stripe details and Secret key.

<img src="readme/images/rm-deployment-heroku.png" width="80%"><br><br>


***Deployment on Heroku***

- Go to the Deploy tab.

- For the very first deployment select manual deploy and wait as Heroku builds the logs. Once complete click on the button to view the app.

- After the initial deployment you can then enable automatic deployment.


***DEBUG Status***

- For the final deployment to Heroku once the project is complete and ***before*** submission of the project to Code Institute, ensure DEBUG is changed from True to ***False***.


***Fork the repository***

For creating a copy of the repository on your account and change it without affecting the original project, useFork directly from GitHub:

On [My Repository Page](https://github.com/todiane/poster-palace), press Fork in the top right of the page.
A forked version of my project will appear in your repository.

***Clone the repository***

For creating a clone of the repository on your local machine, useClone:

On [My Repository Page](https://github.com/todiane/poster-palace), click the Code green button, right above the code window
Chose from HTTPS, SSH and GitClub CLI format and copy (preferably HTTPS)
In your IDE open Git Bash
Enter the command git clone followed by the copied URL
Your clone was created

</details>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


# MARKETING

Social Media Pages

https://www.pinterest.co.uk/poster_palace/ 

https://www.facebook.com/profile.php?id=61555270165633  

brand awareness - design competition

SEO - keywords - I Used descriptive metadata for SEO that accurately reflect the site’s purpose.

the primary marketing strategy behind the application

# Technology Used


- [GitHub](https://github.com/) - remote code storage
- [GitHub projects](https://github.com/users/todiane/projects/10/views/1?layout=board) - managing and monitoring progress
- [GitPod](https://gitpod.com) - Main IDE provider
- [Google Developer Tools](https://developer.chrome.com/docs/devtools/)

## Front-End
- Bootstrap4 - frontend framework for styling
- CSS - language used to style webpage
- Google Fonts - project fonts
- HTML - base markup language
- jQuery - for JavaScript functionality


## Back-End
- [Black](https://github.com/psf/black)
- [Cloudinary](https://cloudinary.com) - remote image hosting
- [Django](https://www.djangoproject.com/) - main framework
- [ElephantSQL](https://www.elephantsql.com/) - remote PostgreSQL database
- [Heroku](https://heroku.com) - website hosting platform
- [Python](https://python.org) - backend programming language
- [Stripe](www.stripe.com) - payment processess for secured payments

## Additional Resources

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Canva](https://www.canva.com/en_gb/) = used to make product images and delivery PDF
- [Diffchecker to check code](https://www.diffchecker.com/text-compare/ ) - to check for differences in code
- [Favicon Generator](https://realfavicongenerator.net/)
- [Font Awesome](https://www.fontawesome.com) - for icons used
- [Miro](https://miro.com/index/) - for database schema
- [PNG to WEBP converter](https://www.freeconvert.com/png-to-webp) - Changing images to webp


## Resources Used

This list contains resources I have used to help me start, create and manage this project.
Use Ctrl (or Cmd) + click to open in new window.
<br>

- About Us App - Used this to help me create about us app

- [Contact Us App](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid) - I used this to create my contact form app 

[Add Reviews](https://www.youtube.com/watch?v=3KCBN7WJXMY&list=PLFNQLcwO1GaY3dy2i6F5vQ60YGDRUD-bX&index=2) - video used to help add reviews


- [Collapse faq on contact page](https://bootsnipp.com/snippets/Elqk5)

- [Photo gallery on homepage](https://www.freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c/)


- [XML-Sitemap](https://www.xml-sitemaps.com/) - Used to create sitemap

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

