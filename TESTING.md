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

## Features Testing

The following manual tests have taken place. I went through the procedure myself and three other people tested the site and the checkout process as well as adding a review and using the wishlist. Below are the results

Admin Area - Role based access control successful - users are unable to log into the admin area

<img src="readme/testing/rm-testing-admin.png" width="90%"><br><br>



Registration
Email received
Confirmation of email
Add product to cart
increase and decrease product amounts
delete product
checkout process
Log in
Log out
wishlist
review

Admin area
Adding products
viewing messages
viewing orders


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


## Lighthouse

The original lighthouse score was 80% so I had to add aria tags to my footer, add "defer" to some of the scripts in base.html, reduce the size of the images on the homepage plus save them as webp rather than png. The score increased to 90%. The remaining issue is the box at the top of the page with web content in it, which Lighthouse refers to as the "largest contentful paint".

<img src="readme/testing/rm-lighthouse.png" width="90%"><br><br>

SEO was given a 100% score

<img src="readme/testing/rm-lighthouse-seo.png" width="90%"><br><br>

## Accessibility

All pages scored 90% or above for accessibility:

**Index Page:** Accessibility was given a score of 90% first time around because of a missing <ul></ul> element in the mobile header. Once that was added the score increased to 100%.

<img src="readme/testing/rm-lighthouse-accessibility.png" width="90%"><br><br>

**Product:**

<img src="readme/testing/rm-lighthouse-products.png" width="90%"><br><br>

**About Page:**

<img src="readme/testing/rm-lighthouse-about.png" width="90%"><br><br>

**Newsletter Page:**

<img src="readme/testing/rm-lighthouse-newsletter.png" width="90%"><br><br>

**Event Page:**

<img src="readme/testing/rm-lighthouse-eventpage.png" width="90%"><br><br>



## Resources

- [Pep 8 for code standards](https://peps.python.org/pep-0008/)
- Web Development Tool - Google Lighthouse



<p align="right">(<a href="#table-of-content">back to top</a>)</p>




## Automated Testing

I watched a video on submitting project five where the assessor spoke about automated testing and only including information on it if it went very well. Mine did not and as this is a learning process for me I decided to include it.

Hopefully, years from now I can look back and realise why it didn't work and reflect upon how much I have improved since creating this project 🤞🏿

One aspect of automated testing I do understand is the need to include two databases. The local one for testing and the production database for deployment. Information from [Very Academy](https://www.youtube.com/c/veryacademy)

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

I added a few basic tests to the project at the beginning that I


