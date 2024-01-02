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

The development of an ecommerce store specialising in large and extra-large posters has been driven by several clear rationales:

<details>

**Market Demand**
While there are a number of sites offering wall art in a large range of sizes, there are very few offering larger sizes in wall art making it an underserved market. The platform also embraces a niche focus catering to customers searching for larger sized posters, providing an opportunity to differentiate from competitors and attract customers looking for a specialised product.

**Target Audience:**
Niche products attract a niche target audience. High quality attracts people willing to pay for luxury products. The large and extra-large sizes of these posters along with the printing quality means our product will attract a specific demographic including interior designers, business owners looking for wall art for their office or individuals with large homes looking for statement pieces to enhance their living space and aesthetics and of any room. 

Potential buyers include:

- Interior designers, landlords or homeowners who want posters to decorate their property.

- Office business owners looking for statement wall pieces or large pieces of art for their office and/or boardroom

- Retail business owners looking for large pieces of wall art to display in their shop or cafe.

- Travel enthusiasts, music lovers, sports enthusiasts, art admirers, etc. who might be interested in purchasing niche poster designs.

- Parents looking to decorate their child’s room with a statement piece.

<br>

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

The objective of this project is to build a Full-Stack eCommerce site with payment system and product structure based on business logic used to control a centrally-owned dataset.

As well as employing advanced User Experience Design to build this Full-Stack web application, search engine optimisation (SEO) and social media marketing techniques have been used in the delivery of content and images to improve audience and brand reach. Objectives include:

<details>

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

The above objectives outline what I wanted to complete when creating this project, which led to the creation of the following outcomes (achieved results):

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

# Model View Template

I used MVT to help define the project's requirements, features, and structure by considering the following questions:

<details>

## Model (Database Design)

**Authentication and role-based Authorisation:** How will we include authentication and role-based authorisation in our data model? What information will we request and store?

**Admin Area:** How will we ensure only authorised users have access to this information and what will be included?

**Product Information:** What attributes will each product have? (e.g., name, price, description, category, delivery, quantity etc.)

**Buyer Accounts:** What information will we store about our customers? (e.g., name, email, password, address, telephone number, purchase history etc)

**Order Management:** How will we track orders? What information is needed for each order? (e.g., customer details, order status, payment information etc)

**Inventory Management:** Will we need to manage an inventory for physical products or rely on print-on-demand?

**Security Management:** How will we store and manage customer information in our database? What security measures will be in place to prevent unauthorised access or distribution?

**Wish List, Reviews and Ratings:** What will we include in our system for customer feedback on products? How will authorised users be able to save products while browsing?

## Views (User Interface)

**Product Browsing:** How will products be displayed and organised for easy browsing? (e.g., categories, filters, search functionality)

**Wish List, Reviews and Ratings:** What information will customers be able to save and review? What will they see and how will it be managed.

**Product Pages:** What information will be displayed on individual product pages? (e.g., images, descriptions, price, reviews)

**Shopping Cart:** How will the shopping cart function? What information will be displayed in the cart?

**Checkout Process:** What steps will the user go through during checkout? (e.g., address input, payment method selection). Will anonymous checkout be included?

**User Account Management:** How will registered users view and manage their accounts? (e.g., view purchase history, update personal information)

**Responsive Design:** Will the design be responsive to different devices (mobile, tablet, desktop)?

## Templates (Front-End Design)

**Branding:** How will the store's branding be incorporated into the design?

**Navigation:** How will users navigate through the site? (e.g., menu layout, footer links etc)

**Consistency:** How will we ensure a consistent look and feel across different pages?

**Customisation:** How easily can templates be customised for special promotions or changes in/additions to product?

## Authorisation and Security

**User Authentication:** How will users log in and manage their accounts? What security measures will be in place for password protection?

**Payment Processing:** How will we handle payment authorisation securely? Will we use a third-party payment gateway?

**Access Control:** How will we control access to different parts of the site (e.g., admin panel)?

**Data Protection:** How will we protect user data, especially sensitive information like addresses and payment details?

**Compliance:** How will we handle consent management?  Are there any legal compliance issues to consider, such as GDPR for European customers?

## Additional Considerations

**SEO Optimisation and Marketing:** How will we optimise product pages and web content for search engines?

**Analytics and Reporting:** How will we track and analyse user behaviour, sales trends, etc.?

**Customer Support:** How will customer inquiries and issues be handled?

**Marketing and Promotions:** How will we market our products and manage promotions?

</details>
<br>

# Using Agile Terminologies

My aim throughout this project was to focus my working time using agile terminologies:

•	Create backlog

•	Divide work into sprints

•	Create subset sprints

•	Review work - completed yesterday, to do today, any challenges

•	Testing - developer tool, (print) command, keep an eye on terminal/console area.

•	Obtain feedback.

•	Maintain product backlog and prioritise items/adapt to change.

•	Future implementations/scalability and performance optimisation.

User stories were created and the GitHub project area was used to manage this process.
You can see the [Poster Palace Project Process here.](https://github.com/users/todiane/projects/10)

The sprint was divided into three sections:

<details>

| First Sprint | Second Sprint | Final Sprint |
| ------------ | ------------- | ------------ |
| Balsamiq wireframes created | Products designed and added| Add additional pages e.g. 404, 500, sitemap, cookie banner etc |
|Project Structure considered | Views and templates working – checks and tested | Fix any bugs and further testing using Dev tools|
| Database model ideas created and tested. | Payment system setup with emails | Creation of README |
| Django apps created – models and views added | UX and UI design decided and implemented | Submit for Peer to Peer review |
| Templates set up to accommodate models and views | Code refactoring takes place if needed | Final overview before submission |
| Initial Deployment to Heroku | Users added as fake customers to test site | Ensure DEBUG set to False |
| SEO & Marketing created | Full site is manually tested. Email set up tested. | Project Submission. Drink wine! |

</details>

<br>

# UX AND UI Design

As always with my projects, the design was developed with minimalism in mind. Colours were kept to a minimum. The main structure/look of the store was taken from the Code Institute Boutique Ado project.

The font used is a Google Font called Mulish and the main colour of the store is #45526e which is a very dark desaturated blue.

Having worked in online marketing, digital marketing and search engine optimisation for several years I am familiar with the concepts needed to promote a website, however UX and UI design are still fairly new to me. Further research was undertaken on UX AND UI principles, not only what was taught on the course but also via my own reading. 

<details>

This led to some key considerations being considered when designing the store including:

## User Experience (UX) Design:

**User Research:** Understand the target audience, their needs, and behaviours. Conduct usability testing.

**Information Architecture:** Content organised in a logical and intuitive manner with clear navigation paths for users and instant notification of changes using toast messages.

**Wireframing:** Wireframes created to outline the layout and structure before building.

**Usability Testing:** Store was tested by users to identify potential issues. Any feedback given was used to improve user experience. e.g. Being told the font in some areas was too small.

**Accessibility:** Ensure the store is accessible to all users and follow [web content accessibility guidelines (WCAG)](https://www.w3.org/WAI/fundamentals/components/).

**Consistency:** A unified experience across different pages was implemented along with maintaining consistency in design elements so all pages look and feel the same.

**Feedback and Error Handling:** Clear feedback provided once a user takes action e.g. adds or deletes a review. Error messages provided that guide users to a solution, e.g. 404.html error page takes users back to products or homepage.

**User Journey Mapping:** A clear pathway was created from the moment a user lands on the homepage until they checkout. That includes email messages sent for authorisation and any sent once products have been purchased or if a user requests a password change.


## User Interface (UI) Design:

**Visual Hierarchy:** A clear visual hierarchy is in place that guides users through the content. Important elements of the store are highlighted using images, size, colour and placement. Above-the-fold marketing was implemented on the home page.

**Typography:** A readable and accessible font has been used, consistency maintained, and attention has been paid to font size and line spacing.

**Colour Scheme:** One main colour has been used throughout to align with the brand. Colour accessibility was considered when adding colour to templates.

**Imagery, Icons and Whitespace:** High quality designs were used for images of posters and font awesome icons were added to break up content. Whitespace was used to enhance readability and avoid visual clutter.

**Responsive Design:** The site is fully responsive and works well on different screen sizes.

**Consistent Branding:** Brand identity has been maintained throughout the site and included in all information, e.g. the PDF created to highlight the [winners of a competition](https://www.canva.com/design/DAF3uqhD65Y/iSDvZb0f6r-yHmMw7Z8hBg/view) included the same colour as the website. 

**Scalability:** I considered how UI will adapt to changes in content or functionality and designed with scalability in mind.

</details>

<br>

## Testing

Please see my separate [Testing MD page HERE](/TESTING.md) that includes information on testing, viability and bugs.

## Deployment



Deployment took place soon after installing Django, ElephantSQL and Cloudinary.
<br>
<details>

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

- Code Institute [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) example and training

- About Us App - Used this to help me create about us app

- [Contact Us App](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid) - I used this to create my contact form app 

[Add Reviews](https://www.youtube.com/watch?v=3KCBN7WJXMY&list=PLFNQLcwO1GaY3dy2i6F5vQ60YGDRUD-bX&index=2) - video used to help add reviews


- [Collapse faq on contact page](https://bootsnipp.com/snippets/Elqk5)

- [Photo gallery on homepage](https://www.freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c/)


- [XML-Sitemap](https://www.xml-sitemaps.com/) - Used to create sitemap

- [Cookie Banner](https://pypi.org/project/django-cookiebanner/) - used to handle consent management

- [Perplexity AI](https://perplexity.ai) - To help with product descriptions, which were adapted into my own words and to fit SEO.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


