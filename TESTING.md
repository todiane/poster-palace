# Poster Palace Testing Information

This is the testing information for my project 5 eCommerce store Poster Palace


[DEPLOYED SITE IS HERE](https://posterpalace-a7414f135cf3.herokuapp.com/)  |  [ADMIN PANEL IS HERE](https://posterpalace-a7414f135cf3.herokuapp.com/admin)

[READ ME IS HERE](https://github.com/todiane/poster-palace)  |  [DEVELOPER: Diane Corriette](https://todiane.dev) - [LinkedIn](https://linkedin.com/in/todianedev)

<br>

## CONTENTS

[Features Testing](#features-testing)

[Browser Compatibility](#browser-compatibility)

[Responsiveness](#responsiveness)

[Code Validation](#code-validation)

[Bugs](#bugs)

[Lighthouse](#lighthouse)

[Accessibility](#accessibility)

[Resources](#resources)

## Admin Features Testing

Manual tests were conducted in the admin area to ensure everything is working. There was an error when deleting orders and the necessary refactoring of code took place to remove that error. 

Admin Area - Role based access control successful - users are unable to log into the admin area

<img src="readme/testing/rm-testing-admin.png" width="90%"><br><br>


**Admin Features Testing:**

In the admin area products/categories/reviews can be added, edited and deleted. The following manual tests took place to ensure they all worked.

Reviews area:
<img src="readme/testing/rm-admin-reviews.png" width="90%"><br><br>

Review selected and ready to delete - PASSED
<img src="readme/testing/rm-admin-reviews-delete.png" width="90%"><br><br>

Confirm deletion of review - PASSED
<img src="readme/testing/rm-admin-reviews-delete-confirm.png" width="90%"><br><br>

Success message to show review has been deleted - PASSED
<img src="readme/testing/rm-admin-reviews-delete-success.png" width="90%"><br><br>

Highlight orders to be deleted - PASSED
<img src="readme/testing/rm-admin-delete-orders.png" width="90%"><br><br>

Confirmation of order deletion - PASSED
<img src="readme/testing/rm-admin-delete-orders-confirm.png" width="90%"><br><br>

Adding new categories - PASSED
<img src="readme/testing/rm-admin-category.png" width="90%"><br><br>

Adding new products - PASSED
<img src="readme/testing/rm-admin-add-product.png" width="90%"><br><br>

## On Site Features

Tests have been undertaken to ensure the registration, email confirmation, confirming email, log-in, log out and password request all work.
Also tested has been the shopping journey from adding to wishlist, adding and removing products to shopping cart and checking out as an anonymous buyer as well as a registered buyer.
The process of adding a review has been tested for buyers and also for unregistered users.
This has all been documented on the [READ ME IS HERE](https://github.com/todiane/poster-palace)

Other manual tests have taken place. 

I went through the customer journey procedure myself and three other people tested the site and the checkout process as well as adding a review and using the wishlist. Below are the results



|     |                 TEST                 |                            INSIGHTS                                                                                                                                     |     RESULT        |
| :-: | :----------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------|
| 01  |   test column 1 line 1               |                             HTML5 and CSS3                            Learn the basic underpinnings behind HTML 5 awith new CSS training [README](https://gi            | Passed    |
| 02  |   test column 1 line 2               |                               JavaScript                             Using JavaScript to create a game. For loops, functions, methods, cond                             | Passed    |
| 03  |   test column 1 line 3               |                                Python                              Use Python to create a project. Created a portal for contractors with Google API.                    | Passed    |
| 04  |   test column 1 line 4               |                        Full Stack Toolkit                            Using Django, buo share their favourite spot. [README](https://github.com/todia                    | Passed    |
| 05  |   test column 1 line 5               |                        Specialisation project                         Learn about functions and methods to manage an application's logic flow                           | Passed    |








## UI testing

Bootstrap is a responsive language so the mobile-first design approach has been taken care of for the most part, however, tests were performed to ensure the following:

| Test | Result | 
|:---|:---: |
| Toggle navbar doesn’t convert to navbar until over 990px |  PASS  |
| Search bar placeholder is always fully visible  |  PASS  |
| Size of social button icons respond as space increases |  PASS  |
| Product list scales from two columns to four at medium breakpoint  |  PASS  |
| Footer scales according to screen size |  PASS  |
| Search features remain visible on all screen sizes  |  PASS  |



## Browser Compatibility

Layout: The layout and appearance of the site has been tested for consistency throughout browsers. Browers tested include the main four:

- Chrome
- Firefox
- Safari
- Microsoft Edge

All links were tested and working. All pages load as expected and all features work as expected.

## Responsiveness

The eCommerce store looks and functions as intended on different browsers.

| Test | Screenshot View | 
|:---|:---: |
| 1700 px Desktop |  ![Desktop](readme/testing/rm-screen-1700.png)  |
| Laptop  |  ![Laptop](readme/testing/rm-screen-1280.png)  |
| iPad Air - Tablet |  ![iPad](readme/testing/rm-screen-ipad-air.png)  |
| Mobile - Pixel 7  |  ![Mobile](readme/testing/rm-screen-pixel7.png)  |

## Code Validation

I have been using linter and flake8 to test for code errors. Flake8 is installed and being used to ensure PEP8 python standard

Using the command python -m flake8 I was given a list of changes that needed to be made. I changed most of what was suggested however there are a new lines that remain over 79 characters because it broke the code when I added it to another line. I will continue working on removing as many of them as I can but a few may remain after project submission.

<img src="readme/testing/rm-flake8-messages.png" width="90%"><br><br>

Once I had completed the store I used the [Black code formatter](https://pypi.org/project/black/) to ensure the code is formatted correctly.


## Bugs

- When saving a product to the wishlist you can not select a size. If you select XL size an error occurs. Doesn’t always happen on heroku, but size isn't an option for the wishlist, just the product. The ability to add size and an add to cart button have been included in future implementation.

- Phone number area on checkout form let me put in letters. It should be numbers only and an attempt was made to change that but this broke the checkout process. Further investigation into making it work is needed.

- when you write a review selecting a star rating is required however no error message appears if you do not select stars. I have attempted to add it using the following as shown at [Geeksforgeeks](https://www.geeksforgeeks.org/error_messages-django-form-field-validation/)

```
class Meta:
        model = Reviews
        fields = ['subject', 'rating', 'review']
        error_messages = {
            'rating': {
                'required': "Please select a rating."  # Custom error message for the required field
            }
        }
```
and to override the __init__ method of the form and set the required attribute for the "rating" field to True. Neither worked. The review won't submit without the rating but no indication as to why shows up for the user, which is not UI friendly.

```
class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].required = True
        self.fields['rating'].error_messages = {'required': 'Please select a rating'}

    class Meta:
        model = Reviews
        fields = ["subject", "review", "rating"]

```


## Lighthouse Validation

The original lighthouse score for the index page was 80% so I had to add aria tags to my footer, add "defer" to some of the scripts in base.html, reduce the size of the images on the homepage plus save them as webp rather than png. The score increased to 90%. The remaining issue is the box at the top of the page with web content in it, which Lighthouse refers to as the "largest contentful paint".

***All pages scored 90% or above for accessibility.***

**Index Page:** Accessibility was given a score of 90% first time around because of a missing ```<ul>``` element in the mobile header. Once that was added the score increased to 100% but the navbar stopped working on larger screens so I removed it.

<img src="readme/testing/rm-lighthouse-accessibility.png" width="90%"><br><br>

<img src="readme/testing/rm-lighthouse.png" width="90%"><br><br>

SEO was given a 100% score overall

<img src="readme/testing/rm-lighthouse-seo.png" width="90%"><br><br>

**Registration Page**
<img src="readme/testing/rm-lighthouse-signup.png" width="90%"><br><br>

**Login Page:**
<img src="readme/testing/rm-lighthouse-login.png" width="90%"><br><br>

**Forgotten Password Page:**
<img src="readme/testing/rm-lighthouse-password-forgot.png" width="90%"><br><br>

**Products Page:** PNG images reduced score and can be changed to webp
Test results the same across all pages e.g. sort category price high to low, a-z, z-a, low to high price.
<img src="readme/testing/rm-lighthouse-products.png" width="90%"><br><br>

**Checkout Page:**
<img src="readme/testing/rm-lighthouse-checkout.png" width="90%"><br><br>

**Profile Page:**
<img src="readme/testing/rm-lighthouse-profile.png" width="90%"><br><br>

**About Page:**
<img src="readme/testing/rm-lighthouse-about.png" width="90%"><br><br>

**Contact Us Page:**
<img src="readme/testing/rm-lighthouse-contact-us.png" width="90%"><br><br>

**Newsletter Page:**
<img src="readme/testing/rm-lighthouse-newsletter.png" width="90%"><br><br>

**Event Page:**
<img src="readme/testing/rm-lighthouse-eventpage.png" width="90%"><br><br>



## Resources

- [Pep 8 for code standards](https://peps.python.org/pep-0008/)
- Web Development Tool - Google Lighthouse



<p align="right">(<a href="#table-of-content">back to top</a>)</p>
