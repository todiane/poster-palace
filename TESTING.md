# Poster Palace Testing Information

to be added...

I started by running python -m flake 8 in the CLI to get a list of any code issues (add image flake-8 list in screenshots folder)

BUGS

When saving a product to the wishlist you can not select a size. If you select XL size an error occurs. Doesn’t always happen on heroku but size isn't an option for the wishlist, just the product.


Installed Black app

https://learndjango.com/tutorials/django-testing-tutorial 

In testing talk about the importance of testing out changes to model.py before committing them in case of errors. This avoids database failures/crashes

Temporary emails used when testing

Use temp mail

https://temp-mail.org/en/view/6585f978a31e9e00ee8c2619

# Making migrations
To avoid destablising the database I performed a dry run test on the makemigration and migrate process. This was something I learnt from the Django 4 By Example book I own

```python manage.py makemigrations --dry-run```

this will list out what actions are about to happen, if there are any errors they will be highlighted so they can be fixed and not introduced to the actual database.

Once I am happy with the migrations about to take place I simply remove the "--dry-run" code and run makemigrations

```python manage.py migrate --plan```

Using --plan will highlight the final migration before the database is changed/added to and is another opportunity to check for/catch any errors that may be present.



# ENV.PY SETUP

Create env.py setup process

using django to create secret key

You can use django to generate a secret key

python manage.py shell

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

and that generates a key for you

09qa!+09qa*95355w*64mi-fr534td-402xlemskq

#1. **Product Listing**: Test if digital art products are listed correctly.
#2. **Product Detail**: Test if individual product details are correct when selected.
#3. **Add to Cart**: Test if items can be added to the shopping cart.
#4. **Cart Operations**: Test operations like updating quantity, removing items, etc.
#5. **Checkout Process**: Test the checkout process including customer information collection, payment processing, and order confirmation.
#6. **Order Posting**: Test if the order details are correctly posted to the database and if the order processing (e.g., preparing for delivery) starts as expected.
