# Poster Palace Testing Information

This is the testing information for my project 5 eCommerce store Poster Palace

The main README information is [HERE](https://github.com/todiane/poster-palace)

The site is [DEPLOYED HERE](https://posterpalace-a7414f135cf3.herokuapp.com/)

Admin Panel is [DEPLOYED HERE](https://posterpalace-a7414f135cf3.herokuapp.com/admin)

Developer: [Diane Corriette](https://todiane.dev) - [LinkedIn](https://linkedin.com/in/todianedev)

[Features Testing](#features-testing)

[Browser Compatibility](#browser-compatibility)

[Responsiveness](#responsiveness)

[Code Validation](#code-validation)

[Bugs](#bugs)

[Lighthouse](#lighthouse)

[Accessibility](#accessibility)

## Features Testing

#1. **Product Listing**: Test if products are listed correctly.
#2. **Product Detail**: Test if individual product details are correct when selected.
#3. **Add to Cart**: Test if items can be added to the shopping cart.
#4. **Cart Operations**: Test operations like updating quantity, removing items, etc.
#5. **Checkout Process**: Test the checkout process including customer information collection, payment processing, and order confirmation.
#6. **Order Posting**: Test if the order details are correctly posted to the database and if the order processing (e.g., preparing for delivery) starts as expected.

## Browser Compatibility

## Responsiveness

## Code Validation

I have been using linter and flake8 to test for code errors. Using the command python -m flake8 I was given a list of changes that needed to be made. I changed most of what was suggested however there are a new lines that remain over 79 characters because it broke the code when I added it to another line. I will continue working on removing as many of them as I can but a few may remain after project submission.

<img src="readme/testing/rm-flake8-messages.png" width="90%"><br><br>

Once I had completed the store I used the [Black code formatter](https://pypi.org/project/black/) to ensure the code is formatted correctly.




## Bugs

- When saving a product to the wishlist you can not select a size. If you select XL size an error occurs. Doesn’t always happen on heroku, but size isn't an option for the wishlist, just the product. The ability to add size and an add to cart button have been included in future implementation.

- Phone number area on checkout form let me put in letters. It should be numbers only and an attempt was made to change that but this broke the checkout process. Further investigation into making it work is needed.

# name and email didnt appear on the profile after an order was placed - detail how you sorted that one out

## Lighthouse

## Accessibility





<p align="right">(<a href="#table-of-content">back to top</a>)</p>




Automated Testing

However, you can also separate your database for testing and production benefits and update the settings.py file depending on whether you are testing or the project is complete and deployed so should be in production.

````
DEVELOPMENT_DB = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

PRODUCTION_DB = {"default": dj_database_url.parse(os.getenv("DATABASE_URL"))}

DATABASES = PRODUCTION_DB
``````




