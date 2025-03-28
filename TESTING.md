# Bake Me Happy Testing

[Return to Main Readme](README.md)

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
    - [Browsing & Navigation](#browsing--navigation)
    - [Searching & Sorting](#searching--sorting)
    - [Account Management](#account-management)
    - [Basket & Checkout](#basket--checkout)
    - [Favorites](#favorites)
    - [Reviews](#reviews)
    - [Newsletter Signup](#newsletter-signup)
    - [Admin Access](#admin-access)
    - [Business Information](#business-information)
2. [Code Validation](#code-validation)
    - [HTML](#html-validation)
    - [CSS](#css-validation)
    - [JavaScript](#javascript-validation)
    - [Python](#python-validation)
    - [JSON](#json-validation)
3. [Manual Testing](#manual-testing)
4. [Device and Browser Testing](#device-and-browser-testing)
    - [Device Compatibility](#device-compatibility)
    - [Browser Compatibility](#browser-compatibility)
5. [Bugs](#bugs)
6. [Accessibility](#accessibility)


## Testing User Stories

### Browsing & Navigation

As a **shopper**, I can **view a list of products** so that **I can see all available options and make a selection**.
- A list of all products is available on the products page.
- Each product is represented by a clickable product card including an image as well as the name, price, and rating, if available.
- Products can be sorted by a variety of criteria, including price, rating, and name.
- Products can be added to the Basket or Favorites from the product page.
- Clicking on the product image will take the user to the product detail page.

As a **shopper**, I can **view detailed information about a specific product** so that **I can learn more about a product to make an informed purchasing decision**.
- The product detail page includes the product name, price and serving size, rating, description, and a list of allergens.
- Products can be added to the Basket or Favorites from the product detail page.
- Clicking on the product image will open the image in a new window.

As a **shopper**, I can **easily navigate between different pages** so that **I can find the information I need quickly**.
- The navigation bar is available on every page and kept consistent across all pages.
- The navigation bar includes links to all pages, including the Basket, Profile, and Shop / Product pages.
- The logo and title are clockable links, returning shoppers back to the home page.
- The footer is available on every page and kept consistent across all pages.
- The footer includes additional links, such as allergen information, privacy policy, and contact information.
- The footer includes links to the business' social media accounts.

As a **shopper**, I can **browse products by category** so that **I can easily find items within a specific area of interest**.
- Products can be sorted by category as well as by occasion.
- Product counts indicate how many products are available in each category / occasion.
- Clicking on the category / occasion displayed on the product detail page will filter the product list to only include products in that category / occasion.

As a **visually impaired  shopper**, I can **use a screen reader to access and understand the website content** so that **I can browse and interact with the site independently**.
- The website is fully accessible using a screen reader.
- Pages have been structured using semantic HTML elements, with appropriate use of headings, lists, and other elements to convey information in a clear and meaningful way.
- All images have alt text that describes the image content.
- Links and buttons have aria labels that describe their purpose.

### Searching & Sorting 

As a **shopper**, I can **search for products using keywords** so that **that I can quickly find items of interest**.
- The search bar is available in the product navigation bar.
- The search bar will return results for products that match the query in the title or description of the product.
- The search bar will return results for both German and English product names.

As a **shopper**, I can **sort search results by different criteria** so that **I can prioritize the products I'm most interested in**.
- The search results can be sorted by price, rating, and name.
- The search results can be sorted in ascending or descending order.
- The search results can be sorted by category or occasion.

As a **shopper**, I can **easily see if my search returns no results** so that **I am not left confused or frustrated. and can adjust my search criteria**.
- If no results are found, the user will be informed with a message.
- The user will be given the option to view all products.

### Account Management

As a **shopper**, I can **create an account** so that **I can access personalized features and services**.
- The user can create an account by providing their email address, and creating a password.
- The user will receive a confirmation email to verify their email address.
- The user will be redirected to the login page after conforming their email address.

As a **registered user**, I can **manage my profile information** so that **my information is accurate and up-to-date**.
- The user can access their profile page from the navigation bar.
- The user can update their profile information, including their name, email address, contact details.
- The user can view their order history, favorite products, and product reviews from theirr profile page.

As a **registered user**, I can **delete my account** so that **my data is removed from the system**.
- The user can delete their account from the profile page.
- The user will be asked to confirm their decision to delete their account.
- Deleting the account will remove all personal information from the system.

As a **registered user**, I can **log in to my account using my credentials** so that **I can access my personalized information and features**.
- The user can log in to their account using their email address and password.
- The user can choose the "Remember me" option to stay logged in during login.

As a **registered user**, I can **reset my password** so that **regain access to my account**.
- The user can update their password on the profile page.
- The user can request a password reset email during the log in process.
- The user will receive feedback once their password jas been updated.

### Basket & Checkout

As a **shopper**, I can **add products to my basket** so that **I can purchase them later**.
- Products can be added to the basket by clicking the "Add to Basket" button on the product detail page.
- Products can be added to the basket by clicking the "Add to Basket" icon on the product list page.

As a **shopper**, I can **view and update the contents of my basket** so that **I have control over my order before checkout**.
- The basket is accessible from the navigation bar.
- The basket displays the products added to it, along with their quantities and prices.
- The basket allows the user to update the quantities of products or remove them from the basket.
- The basket can be cleared completly with the "Clear Basket" button.

As a **shopper**, I can **proceed to checkout from my basket** so that **I can complete my purchase**.
- The checkout button is available in the basket.
- The checkout button will redirect the user to the checkout page.
- The checkout page will display the products in the basket, along with their quantities and prices.

As a **shopper**, I can **securely provide my payment information during checkout** so that **my transaction is processed safely**.
- The checkout page will display a secure payment form using Stripe.
- The user can enter their payment information securely.
- The user will receive a confirmation message after the payment is processed.
- The user will receive feedback for invalud payment informaiton.
- The user can choose to pay in cash on pickup, bypassing the payment process.

As a **new shopper**, I can **checkout as a guest without creating an account** so that **I can quickly complete my purchase**.
- The checkout page is available without requiring the user to create an account.
- The user can enter their payment information securely.
- The user will receive a confirmation message after the payment is processed.
- The user hs the option to create or log in to an account during checkout to save their information for future purchases.

### Favorites

As a **logged-in shopper**, I can **add products to my favorites list** so that **I can easily find them again later**.
- The user can add products to their favorites list by clicking the "Add to Favorites" button on the product detail page.
- The user can add products to their favorites list by clicking the "Add to Favorites" icon on the product list page.

As a **logged-in shopper**, I can **view my favorites list** so that **easily access products I've saved**.
- The user can view their favorites list by clicking the "Favorites" link in the profile navigation bar.
- The favorites list displays the products added to it as small product cards.
- Clicking on the product card will redirect the user to the product detail page.

As a **logged-in shopper**, I can **remove products from my favorites list** so that **I can keep the list organized and up-to-date**.
- The user can remove products from their favorites list by clicking the "Remove from Favorites" button on the product detail page.
- The user can remove products from their favorites list by clicking the "Remove from Favorites" icon on the product list page.
- The user can remove products from their favorites list by clicking the "Remove from Favorites" icon on the favorites list page.
- Adding and removing products from the favorites list will toggle a heart icon on the product card.

As a **logged-in shopper**, I can **add products from my favorites list directly to my basket** so that **I can quickly purchase them**.
- The user can add products from their favorites list to their basket by clicking the "Add to Basket" button on their favorite list page.
- Adding a product from the favorites list to the basket will not remove it from the favorites list.

### Reviews

As a **logged-in shopper**, I can **submit a review for a product I've purchased** so that **I can share my experience with other customers**.
- The user can submit a review by clicking the "Add Review" button on the product detail page.
- The "Add Review" button is only visible to logged-in users.

As a **shopper**, I can **review existing reviews** so that **I can make an educated purchasing decision**.
- Existing reviews are visible on the product detail page.
- Existing reviews are visible to all users, regardless of whether they are logged in.

As a **shopper**, I can **update my submitted reviews** so that **I can correct any mistakes I may have made**.
- The user can update their submitted reviews by clicking the "Edit Review" button on the review page in their profile.
- Updated reviews will appear in the review section of the product detail page.

As a **shopper**, I can **delete my published reviews** so that **I can remove information that is no longer relevant**.
- The user can delete their submitted reviews by clicking the "Delete Review" button on the review page in their profile.
- Deleted reviews will be removed from the review section of the product detail page.

### Newsletter Signup

As a **shopper**, I can **subscribe to the newsletter** so that **receive updates, promotions, and other relevant information**.
- The user can subscribe to the newsletter by entering their email address on the newsletter signup form.
- The user will receive a confirmation message after subscribing to the newsletter.
- The newsletter signup form is available on all pages, in the footer.
- Subscribting to the newsletter will add the user to the subscribers list.

### Admin Access

As a **site admin**, I can **add, edit, and delete products in the catalogue** so that **I can keep the product information up-to-date**.
- The admin user can add, edit, and delete products from the store management page.
- New and updated products will be visible on the product list page immediately
- Deleted products will be removed from the product list page.

As a **site admin**, I can **review product comments and ratings** so that **I can stay informed about my customers’ feedback**.
- The admin user can view and manage product comments and ratings on the store management page.
- The admin user can delete inappropriate reviews on the store management page.
- Reviews are displayed with detailed information, including the product name, the reviewer's name, the review text rating, and the date of the review.

As a **site admin**, I can **view my newsletter subscribers** so that **I can stay connected with my customers**.
- The admin user can view the newsletter subscribers list on the store management page.
- Subscribers are displayed with their email address and the date they subscribed.

As a **site admin**, I can **view and manage orders** so that **I can track order status, process shipments, and handle customer inquiries**.
- The admin user can view orders on the store management page.*
- The admin user can view order details, including the customer's name, email, shipping address, and order items.

*Note: For the purpose of this project, the admin user can view orders, but not manage them.

As a **site admin**, I can **manage the website’s content** so that ** I can keep the website up-to-date and engaging**.
- The admin user can add, edit, and delete content on the store management page.
- The site admin can manage product information as well as the content of the About Us, Allergen Informaiton, FAQ, and Privacy Policy pages.
- The site admin can update texts and, where applicable, images associated with these pages

### Business Information

As a **shopper with allergies**, I can **view clear allergen information on product pages** so that **I can make informed choices about what I can safely consume**.
- The allergen information is displayed on the product detail page.
- The allergen information is displayed in a clear and concise manner.
- The user can view a full list of allergens on the Allergen Information page.
- The Allergen Information page is accessible from the footer.

As a **shopper**, I can **easily access the privacy policy** so that **I can understand how my data is collected, used, and protected**.
- The privacy policy is accessible from the footer.
- The privacy policy is accesible by all users, regardless of whether they are logged in.
- The privacy lays out the company's data collection and usage practices.

As a **shopper**, I can **learn about the company's values and its team** so that **I can connect with the people that make it happen**.
- The About Us page provides information about the company's values and its team.
- The About Us page is accessible from both the header abd footer.
-  The About Us page is accessible by all users, regardless of whether they are logged in.

As a **shopper**, I can **easily find the company’s contact information** so that **I can get in touch if needed**.
- The contact information is displayed on the Contact Us page.
- The contact information is accessible from the footer.
- The contact information is accessible by all users, regardless of whether they are logged in.
- In addition to the contact information, the Contact Us page provides a form for users to submit their questions or comments.
- Contacts submitted through the form will appear in the site admin's store management panel.

As a **shopper**, I can **view detailed answers to frequently asked questions** so that **I can find solutions to common problems**.
- The FAQ page provides answers to frequently asked questions.
- The FAQ page is accessible from both the header and footer.
- The FAQ page is accessible by all users, regardless of whether they are logged in.

[Back to top ⇧](#bake-me-happy-testing)

## Code Validation

### HTML Validation

[W3C Markup Validator](https://validator.w3.org/) was used to validate the HTML code of each templated page. HTML validation was performed via source code text input.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|Home | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|About | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|FAQ | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Contact Us | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Allergen Information | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Privacy policy | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Products | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Product Details | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Basket | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Checkout | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Checkout Success | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Profile | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|My Orders | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|My Favorties | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|My Reviews | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Edit a Review | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Sign Up | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Sign In | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Sign Out | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Change Password | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Forgot Password | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Reset Password | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Set New Password | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Password Changed | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Store Management | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Manage Products | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Add a Product | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Edit a Product | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Manage Reviews | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|View a Review | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Manage Subscribers | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Manage Orders | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Manage Contacts | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|View a Contact | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Edit About Content | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Manage Baker Profiles | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Edit a Baker Profile | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Edit FAQ Content | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Edit Privacy Policy Content | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|Edit Allergen Information Content | Validation errors relate to Summernote Widget. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/summernote-errors-html-validation.png)</details>| Pass |
|404 | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |

### CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the custom CSS code.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|about.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|base.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|checkout.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|home.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|products.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|profiles.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |
|reviews.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the custom JavaScript code.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|Back to Top Button JS | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/btt-button-validation.png)</details>| Pass |
|delivery_toggle.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/delivery-toggle-validation.png)</details>| Pass |
|dropdown.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/dropdown-validation.png)</details>| Pass |
|mobile_product_search.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/mobile-product-search-validation.png)</details>| Pass |
|navigation.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/navigation-validation.png)</details>| Pass |
|product_sorting.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/product-sorting-validation.png)</details>| Pass |
|profile_toggle.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profile-toggle-validation.png)</details>| Pass |
|quantity_dropdown.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/quantity_dropdown-validation.png)</details>| Pass |
|star_rating.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/star-rating-validation.png)</details>| Pass |
|stripe_elements.js | One undefined variable (Stripe )* | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/stripe-elements-validation.png)</details>| Pass |
|Toasts JS | One undefined variable (Bootstrap)* | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/toasts-validation.png)</details>| Pass |

**Note:** These variables show up as undefined due to the modular nature of Django projects. They have no impact on the code and project functionality.

### Python Validation

[PEP8 Online Check](https://pep8ci.herokuapp.com) was used to validate the custom Python code.

#### About

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|about/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-admin-validation.png)</details> | Pass |
|about/apps.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-apps-validation.png)</details> | Pass |
|about/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-forms-validation.png)</details> | Pass |
|about/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-models-validation.png)</details> | Pass |
|about/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-urls-validation.png)</details>| Pass |
|about/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-views-validation.png)</details>| Pass |

#### Bake Me Happy

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|bake_me_happy/settings.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/bake-me-happy-settings-validation.png)</details> | Pass |
|bake_me_happy/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/bake-me-happy-urls-validation.png)</details> | Pass |
|bake_me_happy/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/bake-me-happy-views-validation.png)</details> | Pass |

#### Basket

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|basket/apps.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/basket-apps-validation.png)</details>| Pass |
|basket/contexts.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/basket-contexts-validation.png)</details>| Pass |
|basket/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/basket-urls-validation.png)</details>| Pass |
|basket/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/basket-views-validation.png)</details>| Pass |
|basket/basket-tools.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/basket-basket-tools-validation.png)</details>| Pass |


#### Checkout

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|checkout/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-admin-validation.png)</details>| Pass |
|checkout/apps.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-apps-validation.png)</details>| Pass |
|checkout/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-forms-validation.png)</details>| Pass |
|checkout/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-models-validation.png)</details>| Pass |
|checkout/signals.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-signals-validation.png)</details>| Pass |
|checkout/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-urls-validation.png)</details>| Pass |
|checkout/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-views-validation.png)</details>| Pass |
|checkout/webook_handler.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-webhook-hander-validation.png)</details>| Pass |
|checkout/webhooks.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/checkout-webhooks-validation.png)</details>| Pass |

#### Contact

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|contact/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-admin-validation.png)</details>| Pass |
|contact/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-forms-validation.png)</details>| Pass |
|contact/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-models-validation.png)</details>| Pass |
|contact/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-urls-validation.png)</details>| Pass |
|contact/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-views-validation.png)</details>| Pass |

#### Favorites

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|favorites/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/favorites-models-validation.png)</details>| Pass |
|favorites/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/favorites-urls-validation.png)</details>| Pass |
|favorites/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/favorites-views-validation.png)</details>| Pass |

#### Home

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|home/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/home-urls-validation.png)</details>| Pass |
|home/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/home-views-validation.png)</details>| Pass |

#### Newsletter

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|newsletter/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-admin-validation.png)</details>| Pass |
|newsletter/contexts.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-contexts-validation.png)</details>| Pass |
|newsletter/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-forms-validation.png)</details>| Pass |
|newsletter/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-models-validation.png)</details>| Pass |
|newsletter/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-urls-validation.png)</details>| Pass |
|newsletter/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/newsletter-views-validation.png)</details>| Pass |

#### Products

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|products/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-admin-validation.png)</details>| Pass |
|products/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-forms-validation.png)</details>| Pass |
|products/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-models-validation.png)</details>| Pass |
|products/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-urls-validation.png)</details>| Pass |
|products/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-views-validation.png)</details>| Pass |
|products/widgets.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/products-widgets-validation.png)</details>| Pass |

#### Profiles

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|profiles/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profiles-admin-validation.png)</details>| Pass |
|profiles/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profiles-forms-validation.png)</details>| Pass |
|profiles/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profiles-models-validation.png)</details>| Pass |
|profiles/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profiles-urls-validation.png)</details>| Pass |
|profiles/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/profiles-views-validation.png)</details>| Pass |


#### Reviews

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|reviews/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/reviews-admin-validation.png)</details>| Pass |
|reviews/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/reviews-forms-validation.png)</details>| Pass |
|reviews/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/reviews-models-validation.png)</details>| Pass |
|reviews/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/reviews-urls-validation.png)</details>| Pass |
|reviews/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/reviews-views-validation.png)</details>| Pass |

### JSON Validation

[JSON Formatter & Validator](https://jsonformatter.curiousconcept.com) was used to validate the JSON code of the fixtures.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|categories.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |
|occasions.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |
|products.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |
|faq.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |
|bakers.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |
|reviews.json | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/json-validation.png)</details>| Pass |

[Back to top ⇧](#bake-me-happy-testing)

## Manual Testing

### General

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Responsive Design | Website is responsive on various screen sizes| Pass | Tested on multiple devices |
| Accessibility | Website is accessible using a screen reader | Pass | Semantic HTML and alt text implemented |
| Toast Messages | Toast messages provide feedback on user actions | Pass | |
| Deletion confirmation | Before deleting an item, a confirmation dialog is displayed | Pass | Dellete product / review, account |

### Contact Form

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Contact Form | Submitting the form adds the contact to the admin's store management panel | Pass | |
| Contact Form | Users can chose from predefined subjects | Pass | |

### Header & Navigation

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Logo| Click on logo redirects user to homepage | Pass | |
| Main Navigation Bar | Click on the page name redirects the user to the corresponding page | Pass | |
| Main Navigation Bar | Active page is highlighted | Pass | |
| Main Navigation Bar | Profile dropdown options depend on user status | Pass | Log in / Log out toggle, only logged-in users see profile option, only site admins see store managemend option |
| Secondary Navigation Bar | On product pages, a secondary product navigation bar is displayed | Pass | |
| Secondary Navigation Bar | On profile pages, a secondary profile navigation bar is displayed | Pass | |
| Header Image | The header image is not rendered on admin pages | Pass | |

### Footer

| Element | Expected Outcome | Pass /Fail | Notes| 
|---|---|---|---|
| Newsletter Signup| Users can subscribe to the newsletter | Pass | |
| Newsletter Signup| Users receive a confirmation email after subscribing | Pass | |
| External Footer Links | Links open in a new tab | Pass | |
| Internal Footer Links | Links navigate to the respective pages | Pass | |

### Search & Sort Functionality

| Element | Expected Outcome | Pass /Fail | Notes| 
|---|---|---|---|
| Search Bar| Users can search for products using keywords | Pass | Search queries product title and description |
| Search Bar| Users can search for products using German keywords | Pass | Titles have German translations that can be searched |
| Search Bar| Search results are displayed correctly| Pass | |
| Search Bar | Returns product(s) matching the search query | Pass | |
| Search Bar | Displays a message if no results are found | Pass | |
| Sorting Options | Allows sorting products by different criteria | Pass | |

### Product Listings & Details

| Element | Expected Outcome | Pass /Fail | Notes| 
|---|---|---|---|
| Product List | Products are displayed in a responsive grid format | Pass | |
| Product List | Products are displayed as cards with name, price, rating, and action buttons | Pass | |
| Product Card | Clicking on a product card redirects to the product detail page | Pass | |
| Product Details | Product details are displayed correctly | Pass | |
| Add to Basket button | Add to Basket button adds the product to the basket | Pass | |
| Add to Favorites button | Add to Favorites button toggles the product in the favorites list | Pass | |
| Quantity Dropdown | Allows users to select the quantity of the product | Pass | |
| Quantity Feedback | Provides feedback if the maximum quantity is reached | Pass | Users are asked to contact the store for more than 5 items of any product |
| Reviews Section | Displays all reviews for a product | Pass | |
| Reviews Section | Allows logged-in users to add, edit, or delete reviews | Pass | |

### Basket

| Element | Expected Outcome | Pass /Fail | Notes| 
|---|---|---|---|
| Basket | All items added to the basket are displayed | Pass | |
| Basket | Displays delivery fee and total cost dynamically | Pass | Free delivery for orders over € 50 |
| Quantity Dropdown | Users can update the quantity of items in the basket | Pass | The same maximum quantity applies as in the product details page |
| Remove from Basket button | Users can remove items from the basket | Pass | |
| Clear Basket button | Users can clear the entire basket | Pass | |

### Checkout

| Element | Expected Outcome | Pass /Fail | Notes| 
|---|---|---|---|
| Checkout Form | Users can enter shipping information | Pass | |
| Checkout Form | Users can select payment method | Pass | |
| Checkout Form | Users can select delivery method | Pass | |
| Checkout Form | Users receive an order confirmation email | Pass | |
| Checkout Form | Displays pre-filled user information for logged-in users | Pass | |
| Checkout Form | Offers a county dropdown with all counties in Ireland | Pass | |
| Checkout Form | The country field is set to Ireland by default and non-editable | Pass | |
| Save my Details checkbox | Allows logged-in users to save payment information for future orders | Pass | |
| Checkout Form | Allows guest checkout without requiring account creation | Pass | |
| Sign in / Sign up option | Provides guest users with a link to create or sign in to an account | Pass | |
| Stripe Element | Securely processes payments via Stripe | Pass | |
| Stripe Element | Bypassed when selecting cash payment | Pass | |
| Delivery Fee | Updates delivery fee dynamically | Pass | |
| Order Summary | Displays items and total cost of the order | Pass | |

### User Registration & Login

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| User Registration | Users can create a new account using a valid email and password | Pass | |
| Email Verification | Users receive a verification email | Pass | |
| Change Password | Users can change their password | Pass | |
| Delete Profile | Users can delete their profile | Pass | |
| User Login | Users can log in with their credentials | Pass | |
| User Profile | Users can view and update their profile information | Pass | |
| User Profile | The country field is set to Ireland by default and non-editable | Pass | |
| Order History | Users can view their order history | Pass | |
| My Favorites | Users can view and manage their favorite products | Pass | |
| My Favorites | Users can add products to the basket directly from the favorites list | Pass | |
| Favorites List | Displays all favorited products as cards | Pass | |
| My Favorites | Clicking on a product card navigates to the product details page | Pass | |
| My Reviews | Users can view and manage their reviews | Pass | |

### Admin Dashboard

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Admin Dashboard | Admins can view site statistics | Pass | |
| Admin Dashboard | Admins can add, edit, and delete products | Pass | |
| Admin Dashboard | Admins can manage user view and delete user reviews | Pass | |
| Admin Dashboard | Admins can view and manage orders | Pass | |
| Admin Dashboard | Admins can view and manage subscribers | Pass | |
| Admin Dashboard | Admins can view and manage page contents | Pass | |

[Back to top ⇧](#bake-me-happy-testing)

## Device and Browser Testing

The project was tested on multiple deviced and browsers to ensure compatibility and functionality.

### Device Compatibility

Device | Outcome | Pass/Fail
| --- | --- | --- |
| iPhone 13 Mini | No appearance, responsiveness, or functionality issues. | TBA |
| iPad 9th Generation | No appearance, responsiveness, or functionality issues. | TBA |
| iPad Pro (9.7-inch) | No appearance, responsiveness, or functionality issues. | TBA |
| MacBook Air 13" | No appearance, responsiveness, or functionality issues. | TBA |
| Asus Vivobook Pro 15 | No appearance, responsiveness, or functionality issues. | TBA |
| Black Shark PAR-HOA | No appearance, responsiveness, or functionality issues. | TBA |
| Samsung Galaxy S23 | No appearance, responsiveness, or functionality issues. | TBA |

### Browser Compatibility

Browser | Outcome | Pass/Fail
| --- | --- | --- |
| Safari | No appearance, responsiveness, or functionality issues. | TBA |
| Google Chrome | No appearance, responsiveness, or functionality issues. | TBA |
| Microsoft Edge | No appearance, responsiveness, or functionality issues. | TBA |
| Mozilla Firefox | No appearance, responsiveness, or functionality issues. | TBA |
| JoyUI Native Browsers | No appearance, responsiveness, or functionality issues. | TBA |

[Back to top ⇧](#bake-me-happy-testing)

## Bugs

| Feature | Bug | Fix |
|---|---|---|
| Adding a product review | Ratings added through the website rather than through fixtures override rather than update ratings declared in the fixtures | Not fixed |
| Adding / Editing a product / Allergens| Allergens of products added / edited on the website are split by letter, e.g. "milk" turning into "m", "i", "l", "k" | Not fixed |
| Adding a product | Products added through the website do not show up in alphabetical order on the manage products page, but rather at the end of the list | Fixed |
| Summernote Editor | The editor does not resize correctly on mobile devices | Fixed |

[Back to top ⇧](#bake-me-happy-testing)

## Accessibility

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) in [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to measure the page's quality, focusing on performance, accessibility, best practices, and SEO scores.
<br>
The scores are ordered as *Performance* - *Accessibility* - *Best Practices* - *SEO*.

| Tested | Result | View Result | Pass/Fail |
| --- | --- | --- | --- |
| Home | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/home-lighthouse.png)</details> | TBA |
| About | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/about-lighthouse.png)</details> | TBA |
| FAQ | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/faq-lighthouse.png)</details> | TBA |
| Contact Us | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/contact-lighthouse.png)</details> | TBA |
| Allergen Information | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/allergen-info-lighthouse.png)</details> | TBA |
| Profile | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/profile-lighthouse.png)</details> | TBA |
| Favorites | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/my-favorites-lighthouse.png)</details> | TBA |
| Orders | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/my-orders-lighthouse.png)</details> | TBA |
| Reviews | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/my-reviews-lighthouse.png)</details> | TBA |
| Product List | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/product-list-lighthouse.png)</details> | TBA |
| Product Detail | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/product-details-lighthouse.png)</details> | TBA |
| Store Management | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/store-management-lighthouse.png)</details> | TBA |
| Manage Products | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/manage-products-lighthouse.png)</details> | TBA |
| Add Product | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/add-product-lighthouse.png)</details> | TBA |
| Edit About | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/edit-about-lighthouse.png)</details> | TBA |
| Sign In | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-in-lighthouse.png)</details> | TBA |
| Sign Up | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-up-lighthouse.png)</details> | TBA |
| Sign Out | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-out-lighthouse.png)</details> | TBA |
| 404 Page | TBA | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/404-lighthouse.png)</details> | TBA |

[Back to top ⇧](#bake-me-happy-testing)

[⇦ Return to Main Readme](README.md)
