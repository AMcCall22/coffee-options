## Testing

### Functionality



#### Home Page

###### 1 Test Description 

Ensure homepage loads correctly.

###### Test

Load https://coffee-choices.herokuapp.com/

#### Expected Outcome 

4 regions are visible on the page and can be selected to navigate to countries.html.

###### Pass/Fail

*Pass*



#### Buy Coffee Beans

###### 2 Test Description 

Ensure coffee beans are visible for purchase, either per region or all beans.

###### Test

Load https://coffee-choices.herokuapp.com/countries 

###### Expected Outcome 

Countries are visible on the page and can be selected to navigate to bean_detail page. 

###### Pass/Fail

*Pass*



###### 3 Test Description 

Ensure bag size options are available for selection(small and large).

###### Test

Select a bag size quantity and add to basket.

###### Expected Outcome 

Current total on nav bar updates to include item added.

 A message appears "Successfully added to your bag!"

###### Pass/Fail

*Pass*



###### 4 Test Description 

Ensure shopping bag is functioning as expected.

###### Test(s0

Add a product to the bag, and remove it.

Add a product to the bag, and select `checkout`

###### Expected Outcome 

The item can be removed from the basket if required.

 A page is rendered if the shopping basket is empty to confirm this and allows navigation back to products.

The checkout button navigates to the checkout page.

###### Pass/Fail

*Pass*



###### 5 Test Description 

Ensure checkout form is functioning as expected

###### Test

Complete the form using the saved address from the customer's profile is applicable, or enter the details manually.

Complete the purchase using Stripe test credentials 424242424242 in the card input.

###### Expected Outcome 

A saved address appears if the user is logged in and has an address in their profile saved.

A payment is processed through Stripe

Form validation is present.

A small update to warn the customer that their card will be charged a certain amount.

Successful webhooks are created. 

The complete order button triggers an email to the buyer and renders to a confirmation page.



###### Pass/Fail

*All Pass*



#### Profile/Register/Log In

###### 6 Test Description 

A new user can register with the site to allow profile information to be stored(delivery address and previous orders)

###### Test

Complete the signup form and submit.

Complete the confirmation email that is sent.

###### Expected Outcome 

The user completes the form with their details and receives a confirmation email.

A confirmation email is sent to allow user to then login.

Form validation exists.

###### Pass/Fail

*Pass*



###### 7 Test Description 

A user can sign in to view their saved information in the Profile page

###### Test

Sign in to site and navigate to modals on the Profile page

###### Expected Outcome 

Customer is signed in and a message appears to confirm this

Profile modals contain any previously saved info.

###### Pass/Fail

*Pass*



#### Registration

###### 8 Test Description 

Profile page saves information as required.

###### Test

Update the delivery address and save

View previous orders.

###### Expected Outcome 

Delivery address is updated and renders properly on Checkout page

Previous are visible to the customer.

###### Pass/Fail

*Pass*



###### 9 Test Description 

Log Out functionality works as expected.

###### Test

Logout of website.

###### Expected Outcome 

A page is rendered to ensure the customer does want to sign out.

The profile page is now unavailable to logged out customers.

###### Pass/Fail

*Pass*



#### Blog

###### 10 Test Description 

Blog posts can be used by site visitors

###### Test

Navigate to blog page and select a blog to view

Select the like button if required

###### Expected Outcome 

The blog detail is available for site visitors to view.

The blog posts can be liked once by a site visitor, if they so wish.

###### Pass/Fail

*Pass*



###### 11 Test Description 

Admin can add new blog posts

###### Test

Navigate to the Django admin page and add a new post

###### Expected Outcome 

The new post appears on the site.

###### Pass/Fail

*Pass*



### Browser compatibility

Ensure that the site loads correctly on each of the following web browsers

- Chrome - Passed

- Edge - Passed

- Firefox - Passed

- Safari - Passed



#### Code Validation/Beautifier

The code has been passed through the following validation tools:

[W3C Markup Validation](https://validator.w3.org/) 

[W3C CSS validation](https://jigsaw.w3.org/css-validator/) 

http://pep8online.com/



#### Responsiveness

Ensure that the site is responsive and loads correctly on each screen size using the chrome developer tools:

- Small devices - Passed

- Medium devices - Passed
- Large devices - Passed

- x-Large devices - Passed



#### Further testing

Chrome developer tools and Python debugger were used throughout the entirety of the project.

Family and friends have also tested the site for user experience and to aid mobile responsiveness testing.

