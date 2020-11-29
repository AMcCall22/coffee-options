# Alison McCallum - Coffee Choices



## Milestone 4 project - Full Stack Frameworks With Django

This website has been designed primarily as an e-commerce site which sells coffee from different regions of the world. It is a full-stack site utilising Django for database purposes.

It also incorporates a blog which allows the site owner to update a blog with coffee -related posts.  This allows the site owner to share their passion for coffee!

Deployed site - [Coffee Choices](https://coffee-choices.herokuapp.com/)



#### Home Scren Image
Link to [Home Screen](/Readme_files/Home_screen.png)



#### UX

##### User Stories

As a **coffee customer**,  I would like to see the following:

- As a customer I would like to view all available products by region, country and bag size

- As a customer I would like to  view the items in my basket

- As a customer I would like to remove items from my basket

- As a customer I would like to view my total spent so far

- As a customer I would like to register with the shop so that I can save my delivery address and view my order history. 

- As a customer I would like to purchase the items in my shopping bag through a seemless checkout experience

- As a customer, I would an email to confirm my order has been processed

- As a customer, I would like to read about the site owner's passion for coffee

  

As the **owner of a small shop**,  I would like to see the following: 

- As a small shop owner, I would like to be able to showcase my  coffee products 
- As a small  shop owner, I would like have a robust payment system in place
- As a small  shop owner, I would like to be able to showcase my coffee products
- As a small shop owner, I would like to share my passion for coffee through a blog on the site

##### Wireframes

##### 

Link to [Wireframes](/Readme_files/MS4_Wireframes.pdf)

##### 

#### Design

##### Background

I decide to choose a plain background colour to allow the images on both the regions and countries page stand out.

##### Colour

The colours were chosen to complement each other and to allow the images to stand out:

- A dark blue (\#2E56AC) for the nav bar

- A lighter blue for the body (\#c0dfe6)

- Standard bg-light class from Bootstrap4 for the footer

  

#### Features

Bootstrap4 was used as the basis of the design to provide a modern, standardised  and responsive layout throughout the site.

##### Nav-bar

The nav-bar includes the name of the site - Coffee Choices. This name indicates the site's purpose and if selected, will redirect the user back to homepage from wherever they are in the site.  The nav-bar also includes links to the following sections:

##### Buy Coffee Beans

This is a drop down menu which allows the user to select from the following:

- All Coffee Beans
- South America
- Asia
- Africa
- North America

Selecting one of these options takes the user through to a 'countries' page which offers the user a choice of different countries within that region.  The user can then select a country and is presented with a choice of bag sizes for that country.  These can then be added to the shopping basket.

##### Blog

A blog has been created which allows the site owner to add snippets of information regarding their passion for coffee. The user is presented with a list of blogs, can select one to ready the detail and can 'like' the blog post if they so wish.

##### Login

This allows an already registered user to login to the website, using their email address and password set up at registration.  It provides the user with the ability to sign up if they are not already registered, as well as a forgotten password option.

##### Register

Registration allows the user to save a default delivery address which is then visible on their checkout form when making a purchase. It also allows them to view a list of their previous orders.  

The user must add their email in twice, submit a user name and also a new password to be added twice.  Validation is on the form using the alluth prebuilt settings, and will also not allow an email address to be added twice to the Django database. An email is sent to the user to confirm they have signed up to the site before then can they login. A message appears to confirm that the user has successfully signed in to the site. 

##### Profile

The profile dropdown is split into 2 options - Profile and Logout. These options are only visible to users that are logged in.

The profile is split into 2 modals. 

Default delivery address which can be updated, and a message is visible when this is done. This delivery address will then be visible of the users checkout form.

Previous orders provide a list of all the customer's previous orders from Coffee Choices.

##### Shopping Bag/Current Total

The shopping bag icon and current total show the user the current total in their bag, and provide a link which takes the user through to the shopping bag.

#### Further functionality

##### Shopping Bag

If the shopping bag is empty, the user is provided with a message to confirm this and a back button to navigate back to the Beans page.

If the user has selected items, these will appear in the shopping bag. The user can remove an item from their shopping bag if they wish, but can otherwise proceed to the checkout from here.

##### Checkout

The checkout page allows the user to enter their personal and delivery details (if they have not been linked to their profile page/not a logged in user). The user should also enter their card details here, which will be verified and processed using Stripe. When this payment has gone through, a success page appears and an email confirmation is sent to the user.

##### Footer

The footer contains contact details for the site owner (these are fake details, only for the purpose of the project) as well as a disclaimer 'for educational purposes'.

##### Authentication

The prebuilt Django Allauth package has been utilised throughout this site which provides a robust authentication, registration and account management system for the site.

#### Technologies Used

###### 	Languages

- HTML5

- CSS3

- JavaScript

- Python

- Jinja

  ###### Frameworks and tools

- Bootstrap4

- Django 3.1

- Postgres

- sqlite3

- Django Allauth

- Gunicorn

- Pscopg2

- Crispy Forms

- Stripe

- Heroku

- AWS S3 Bucket

- Boto3

- Balsamiq

- Github/Gitpod

- Font Awesome

- Unicorn Revealer (https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln)



#### Testing

Please find a separate file detailing the testing undertaken here:

Link to [Testing](/Testing_MS4.md)



#### Issues faced and resolved

I had some issues ensuring that the emails were set up correctly using Gmail. I had to remove the 2 step verification process as suggested in the course material in order for emails to send.

I also had some issues setting up webhooks as I was keen to adapt the Boutique Ado code . This turned out to be too complex so the checkout app is primarily code from the tutorial.

Some lines of code are 81 characters long and therefore showing as too long in code validators. As they are only 1 character over the limit, I chose to keep the 'long lines' as the code appears neater that way.



#### Future Developments

**Blog**

This could be linked to the user's profile and allow them to add in or comment on blog posts.

**Stock Control**

This would be added in to ensure stock was definitely available for customers to buy, but was beyond the scope of this particular project.

**Search Form**

This could be added to enhance the user's experience of the site to quickly locate the bean that is required.



#### Deployment

**Locally**

​	To **clone** this project from GitHub, please follow the steps below:

1. Navigate to the correct repository - [here](https://github.com/AMcCall22/coffee-options)

2. Click the green button - `Clone or Download`.

3. Copy the clone URL that appears -https://github.com/AMcCall22/coffee-options

4. Change the current working directory to the location where you want the cloned directory to be made.

5. Type  `git clone` and paste the URL you copied in Step 3.

6. Press Enter to created your local clone.

7. In settings.py add in the following variables:

   ```
   SECRET_KEY = os.environ.get(your secret key)
   STRIPE_PUBLIC_KEY = os.getenv(your secret key
   STRIPE_SECRET_KEY = os.getenv(your secret key)
   STRIPE_WH_SECRET = os.getenv(your sec
   ```

8. Update Gitpod settings with the actual values as per the above 4 keys.

9. Install the project dependencies using `pip install -r requirements.txt`

10. Go to the terminal and run the following: `python3 manage.py makemigrations --dry-run`, then `python3 manage.py makemigrations` , then `python3 manage.py migrate` to migrate all existing migrations.

11. Create a superuser using the command`python3 manage.py createsuperuser`

12. Then run the applications with `python3 manage.py runserver`

13. Open `localhost:8000` on your browser

14. To access the admin panel add `/admin` to the url and enter your superuser details

**Heroku**

1. Create the following files, which are  required to be set up to run the Heroku app:

   1. Requirements.txt details the dependencies required to run the app. Create this file using `pip3 freeze --local > requirements.txt`
   2. Procfile signifies to Heroku which files run the app and also how to run the app. Create the file using `eco web: python app.py > Procfile`. Inside the file add`web: gunicorn coffee_options.wsgi:application`
   3. Run `pip3 install gunicorn` and add to `requirements.txt`

2. Add, commit and push the above files to Github. 

3. Create a new app on Heroku by selecting 'New.'  Give a unique name to it and choose the relevant region.

4. Select `create app`.

5. On the Resources tab in Heroku, then in the `Add-ons`search bar, search for `Heroku Postgres`, select `Hobby Dev — Free` and click `Provision` .

6. In `Settings` , click on the `Reveal Config Vars` button and copy the value of the`DATABASE_URL`

7. Run `pip3 install dj_database_url` and `pip3 install psycopg2 binary`. Run `pip3 freeze > requirements.txt`. Check these have been installed in requirements.txt.

8. In settings.py, add`import dj_database_url`

9. Within settings on Heroku, select Reveal Config Vars and set the following variables:

   1. DATABASE_URL
   2. SECRET_KEY
   3. STRIPE_PUBLIC_KEY
   4. STRIPE_SECRET_KEY
   5. STRIPE_WH_SECRET

10. In settings.py, comment out the existing code under Databases and temporarily add the following:

    ​	DATABASES = {

    ​		'default:' dj_database_url.parse('DATABASE URL')}

    *Note: DATABASE URL value can be found in config vars in heroku settings.*

11. Go to the terminal and run the following: `python3 manage.py makemigrations --dry-run`, then `python3 manage.py makemigrations` , then `python3 manage.py migrate` to migrate all existing migrations.

12. Load the fixtures by first loading the regions, countries then beans json files: 		`python3 manage.py loaddata regions` `python3 manage.py loaddata countries` and`python3 manage.py loaddata beans`

    

13. Create a superuser using the command`python3 manage.py createsuperuser`

14. Remove the text in settings.py that was added in step 9 above

15. Uncomment out the existing text under Databases

16. Go to `settings.py` and add `ALLOWED_HOSTS = ['coffee-choices.herokuapp.com', 'localhost']`

17. Add changes, commit and push to github

18. Select Deploy menu and within Deployment method, select GitHub.  Ensure the correct Github repository is linked to the app.

19. Select Deploy menu and Deploy branch button which initiates the building of the required packages.

20. Once the build is complete, and the app is successfully deployed, select view to view the app.

#### **AWS**

1. Logged in to `Amazon AWS`, select `S3` and created a new `S3` bucket.

2. Returned to terminal window and run ` pip3 install django-storages` and `pip3 install boto3`. Add `storages` to `INSTALLED_APPS` in settings.py

3. In settings.py also add:

   ```
   STATIC_URL = '/static/'
   STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
   
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   
   if 'USE_AWS' in os.environ:
       # Cache control
       AWS_S3_OBJECT_PARAMETERS = {
           'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
           'CacheControl': 'max-age=94608000',
       }
   # Bucket Config
   AWS_STORAGE_BUCKET_NAME = 'coffee-choices'
   AWS_S3_REGION_NAME = 'eu-west-2'
   AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
   AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
   
   # Static and media files
   STATICFILES_STORAGE = 'custom_storages.StaticStorage'
   STATICFILES_LOCATION = 'static'
   DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
   MEDIAFILES_LOCATION = 'media'
   
   # Override static and media URLs in production
   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
   MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
   ```

4. In Heroku config settings, add in:

   1. AWS_ACCESS_KEY_ID
   2. AWS_SECRET_ACCESS_KEY
   3. USE_AWS (set to True)

5. Create a  `custom_storages.py` 

   ```
   from django.conf import settings
   from storages.backends.s3boto3 import S3Boto3Storage
   
   
   class StaticStorage(S3Boto3Storage):
       location = settings.STATICFILES_LOCATION
   
   
   class MediaStorage(S3Boto3Storage):
       location = settings.MEDIAFILES_LOCATION
   ```

6. Git add, commit and push to trigger automatic deployment

   

#### Credits

##### Content

###### **Code**

- The Boutique Ado tutorial from Code Institute has been used throughout this project.  It has been modified to suit the needs of the project but the code from certain areas including Stripe, Emails and Checkout have generally been used as per the tutorial code

- Inspiration from the blog app was taken from a course on [Codemy](https://www.youtube.com/watch?v=B40bteAMM_M)

  

###### General

- The CI slack channel and tutor support
- Django documentation has been used for reference
- https://www.w3schools.com/




###### Media

​	The 4 regions images were created by my husband Peter McCallum from photos of real coffee beans

​	The bag image on the countries.html template was taken from [here](https://yellowimages.com/stock/glossy-kraft-coffee-bag-with-valve-mockup-halfside-view-13662)



##### Acknowledgements

Thanks to my mentor, Brian Macharia for his input and direction.

Thanks to student support at Code Institute.

Thanks to my peers at Code Institute, of whom I have called on for support during this project.

Thanks also to my husband, Peter McCallum for his support and patience throughout this project.



\------



Disclaimer



This site is currently for educational and practical use 