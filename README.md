# Bake Me Happy

![Mock Up Image](assets/readme-files/images/mockup.png)

Bake Me Happy is an e-commerce website for a small, local online bakery. The shop offers a wide range of baked goods, mainly inspired by traditionally German recipes. Bake Me Happy is designed to provide a seamless shopping experience for customers, with a user-friendly interface and secure payment processing. It also features a user profile section for registered users, allowing them to manage their orders, reviews, and personal information, as well as a store management section for site admins to manage products, orders, customer contacts, and more.

Visit the deployed application [here](https://bake-me-happy-b9b73285e6cc.herokuapp.com).

## Table of Contents

1. [Project Planning](#project-planning)
    - [Agile Methodology](#agile-methodology)
        - [Sprints](#sprints)
        - [GitHub Projects](#github-projects)
    - [CRUD Functionality](#crud-functionality)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Structure](#structure)
2. [Marketing](#marketing)
    - [Search Engine Optimisation](#search-engine-optimisation)
    - [Business Model](#business-model)
3. [Design Choices](#design-choices)
    - [Color Palette](#color-palette)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
    - [Fixtures](#fixtures)
4. [User Experience (UX)](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
5. [Features](#features)
    - [General](#general)
    - [Pages](#pages)
    - [Future Features](#future-features)
6. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Tools](#tools)
    - [Libraries, Frameworks, and Packages](#libraries-frameworks-and-packages)
    - [Tools and Programs](#tools-and-programs)
7. [Deployment](#deployment)
    - [GitHub](#github)
    - [Heroku](#heroku)
8. [Testing](#testing)
9. [Finished Product](#finished-product)
10. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
11. [Acknowledgements](#acknowledgements)

[Back to top ⇧](#bake-me-happy)

## Project Planning

### Agile Methodology

Agile methodology played a crucial role in managing the development process. The project was divided into smaller sprints, each focusing on adding a specific feature or improving an existing function.

#### Sprints

**1st Sprint:**

The first sprint focused on setting up the basics of the application, including the base.html template which was used across all pages of the project.

**2nd Sprint:**

The second sprint focused on setting up the product app and its functionality. Bootstrap templates were customized to create a basic shop interface, including the different product views, as well as sorting and filtering functionality.

**3rd Sprint:**

The third sprint focused on setting up the basket app and its functionality. The basket provides a place for shoppers to view and update their planned purchases and easily access information about the costs associated with them.

**4th sprint:**

The fourth sprint focused on setting up the checkout app and its functionality. The checkout page uses Stripe to handle payments. This sprint relied heavily on webhook testing to ensure a smooth user experience.

**5th Sprint:**

The fifth sprint focussed on setting up the profile app and its functionality. Django allauth was implemented for user authentication, with customized tenplates to match the project's design.

**6th Sprint:**

The sixth sprint focused on setting up the favorites app and its functionality. Logged in users can easily add products to their favorites list and view them in a dedicated section within their profile.

**7th Sprint:**

The seventh sprint focused on setting up the basics of the store management app and its functionality. This sprint involved creating a dedicated section for store managers to manage products using a WYSIWYG editor.

**8th Sprint:**

The seventh sprint focused on setting up the reviews app and its functionality. Logged in users can create and update product reviews, which are displayed at the bottom of the relevant product detail page. Reviews may include ratings, which will update the existing product rating dynamically.

**9th Sprint:**

The ninth sprint focused on preparing the app for deployment with Heroku. A custom page was created to handle 404 errors. Email settings wer updated to allow Django to send out emails, as opposed to logging them to the terminal. The project was connected to AWS S3 to handle static and media files.

**10th Sprint:**

The tenth sprint focused on setting up the newsletter app and its functionality. Subscribers receive a confirmation email and are added to the subscribers list in the database. A context processor makes the newsletter accessible in the footer of every page of the project.

**11th Sprint:**

The eleventh sprint focused on setting up the contact app and its functionality. A contact page with several kinds of contact information as well as a contact form were created. Contacts via the form are added to the database.

**12th Sprint:**

The twelfth sprint focused on setting up the about app and its functionality, allowing users to learn more about the business and its staff. Separate models were created for the business and staff information.

**13th Sprint:**

The thirteenth sprint focused on improving on the store management app. A dashboard for admin users was created to easily manage products, contacts, subcribers, and the about content. The store management app brings a lot of the functionality from Django's */admin* panel to the front end, allowing store owners to maintain their website without the need to access backend pages. More pages were created for the about app, which can be managed from the store management dashboard.

**14th Sprint:**

The fourteenth sprint focused on implementing feedback from early user testing as well as initial code reviews. Improvements made included:
- Refactoring code that is being used in multiple places to avoid repetition.
- Updating page templates for improved screen reader compatibility and consistency.
- Improving page navigation.
- Updating the quantity selector to better suit the needs of the business.
- Creating additional account functionality with customized allauth templates.

**15th Sprint:**

The fifteenth sprint focused on improving the checkout process. Pickup and cash payment options were added, and address fields were updated to be more relevant to the business.

**16th Sprint:**

The final sprint focussed on polishing the project for submission. Code validation was performed alongside a final round of compatibility and feature testing.

#### GitHub Projects
 
GitHub Projects was an essential tool for tracking progress and managing tasks throughout the Agile development process. A Kanban-style board was used to track progress visually. Each issue was based on a user story and moved through the different phases of *To Do*, *In Progress*, and *Done*, following the corresponding sprints.
Custom labels were created to distinguish the issues visually. Labels were used to assign a priority, a functionality, and an Epic. 
<br>
A total of 37 user stories were created and completed across 9 Epics.

**Priorities, based on MOSCOW model of prioritization**
- *must-have*
- *should-have*
- *could-have* 
- *will-not-have*,

**Functionalities, based on CRUD model**
- C Create
- R read
- U update 
- D delete

**Epics** 
- Account Management
- Admin Access
- Basket & Checkout
- Browsing & Navigation
- Business Information 
- Favorites
- Newsletter
- Reviews
- Searching & Sorting

### CRUD Functionality

*CRUD* functionality has been implemented throughout the project to create an entirely usable experience for the user. Some examples of this include:
 
**Admin (superuser only)**
- *C*: Add new products. 
- *R*: View all products, subscribers, reviews, etc. 
- *U*: Update existing product listings. 
- *D*: Delete product listings and reviews. 
 
**Reviews (logged-in users only)**
- *C*: Create a new product review.
- *R*: View all reviews posted by this used. 
- *U*: Update reviews posted by this user.
- *D*: Delete reviews posted by this user.
 
**Basket (all users)**
- *C*: Add a new item to the basket.
- *R*: View basket contents.
- *U*: Update quantities of items in the basket.
- *D*: Delete basket contents or clear basket.

### Entity Relationship Diagram

[Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) was used to generate the ERD from Django models.<br>
[Graphviz](https://graphviz.org/) was used to render the ERD from the model relationships.

<details>
    <summary> Entity Relationship Diagram Image</summary>
    <img src = "assets/readme-files/images/erd.png">
</details>

### Structure
[Draw.io](https://www.draw.io) was used to visualize structure of the website and relationships between pages.

<details>
    <summary> Website Structure Image</summary>
    <img src = "assets/readme-files/images/sitemap.png">
</details>

[Back to top ⇧](#bake-me-happy)

## Marketing

### Search Engine Optimisation (SEO)

SEO is a crucial aspect of any website, and Bake Me Happy is no exception. To ensure Bake Me Happy ranks well on search engines such as Google and attracts the right audience, Bake Me Happy utilizes advanced Search Engine Optimization (SEO) techniques.
<br>
The following SEO strategies were implemented:

**Keyword Research:**

Tools like [Wordtracker](https://www.wordtracker.com/) were used to identify high-ranking keywords related to German baking, such as:
- "Authentic German bakery Ireland"
- "German bread delivery Ireland"
- "Traditional German cakes"
- "Online bakery Ireland"
 
These keywords will need to be reviewed and updated regularly, with tools like  [Google Analytics](https://developers.google.com/analytics).

**Content Optimisation:**

The website features high-quality, descriptive content that highlights the unique selling points of Bake Me Happy, such as its German heritage and fresh, handmade products.
The "About" section is rich in keywords and tells a compelling story that resonates with customers.

**Technical SEO:**

The website is mobile-friendly and responsive, ensuring a seamless user experience across devices.
Fast loading times are achieved through optimized images and efficient code.
A sitemap is submitted to search engines to ensure all pages are indexed.

**Local SEO:**

Bake Me Happy targets customers in Ireland, so local keywords like "German bakery Ireland" and "Irish online bakery" are prioritized.
As a real business, Bake Me Happy would be listed on Google My Business to improve visibility in local searches.

### Business Model

[Miro](https://miro.com) was used to create a business model canvas to visualize and define Bake Me Happy's key elements.

<details>
    <summary> Business Model Image</summary>
    <img src = "assets/readme-files/images/business-model-canvas.png">
</details>

#### Company Description

Bake Me Happy is a small, friend-run bakery based in Ireland, specializing in authentic German baked goods. Their mission is to provide high-quality, freshly baked goods made from traditional recipes. The business was founded by German expats who wanted to share the nostalgic flavors of their homeland with their new community. Bake Me Happy offers a wide range of products, including rye breads, brioche rolls, and classic German cakes, all made fresh to order using traditional recipes and high-quality ingredients.

#### Marketing Strategy

Bake Me Happy's marketing strategy focuses on building a strong online presence and fostering community engagement. The bakery aims to create a welcoming and inclusive environment for customers, emphasizing the importance of community and connection. 

**Social Media Presence:**

A dedicated [Facebook Business Page]() is used to engage with customers, share updates, and promote new products.

<details>
    <summary> Facebook Business Page Image</summary>
    <img src = "assets/readme-files/images/fb-business-page.png">
</details>
<br>

**Email Marketing:**

Regular newsletters are sent to subscribers, featuring exclusive discounts, seasonal specials, and baking tips.

**Local Partnerships:**

For a real business, collaborations with local cafes and food markets help increase brand visibility.
Partnerships with food bloggers and influencers drive traffic to the website.

#### Customer Analysis

Bake Me Happy's primary customers are German expats living in Ireland who crave a taste of home. Their products appeal to families and individuals who value fresh, made-to-order bakery items made from real ingredients.

**Target Audience:**

- Primary: German expats in Ireland who crave the nostalgic flavors of home.
- Secondary: Irish locals interested in exploring authentic German baking.
- Tertiary: Food enthusiasts and customers seeking high-quality, preservative-free baked goods.

**Customer Needs:**
- Authentic, high-quality baked goods.
- Convenient online ordering and delivery.
- A connection to German culture and traditions.

#### Competitor Analysis

While there are several bakeries in Ireland, Bake Me Happy stands out due to its focus on authentic German baking. The market will need to be monitored continously to stay ahead of trends and ensure Bake Me Happy's offerings remain competitive.

**Direct Competitors:**
- Other online bakeries in Ireland offering artisanal or specialty baked goods.
- Local bakeries with delivery options.

**Indirect Competitors:**
- Supermarkets offering mass-produced baked goods.
- International online bakeries shipping to Ireland.

**Competitive Advantages:**
- Authentic German recipes and techniques.
- Fresh, handmade products with no preservatives.
- A strong brand story rooted in tradition and nostalgia.

#### SWOT Analysis

**Strengths:**
- Unique selling point: Authentic German baked goods.
- High-quality, preservative-free products.
- Strong emotional connection with German expats.
- Convenient online ordering and delivery.

**Weaknesses:**
- Limited marketing budget for traditional advertising.
- Limited physical presence (online-only).
- Reliance on delivery services, which may affect customer experience.
- Niche market appeal may limit customer base.

**Opportunities:**
- Expanding product range to include seasonal or festive items.
- Partnering with local cafes and restaurants.
- Offering the subscription service for regular deliveries.
- Leveraging social media to reach a wider audience.

**Threats:**
- Competition from established local bakeries and supermarkets.
- Fluctuation in ingredient and delivery costs.
- Economic downturns affecting discretionary spending.
- Changes in consumer preferences.

[Back to top ⇧](#bake-me-happy)

## Design Choices

### Color Palette

The color palette is based on the colors of the logo and the hero image. Colors have been picked to resemble bread and flour, to create a cohesive atmosphere and invite users to explore the baked goods on the website.
The palette was generated using [Coolors](https://coolors.co/image-picker).

<details>
    <summary> Color Palette Image</summary>
    <img src = "assets/readme-files/images/color-palette.png">
</details>

The main colors used in the project are:

- 4f3527 (Cafè Noir): Used for the footer, navigation bars, action buttons, button outlines, and card headers.

- F9F5F1 (Isabeliine): Used for the backrgound of the body.

- F1D4C6 (Pale Dogwood): Used for call to action sections on the home page.

- FFC107 (Amber): Used to highlight active links and stars in review forms as well as allergens on the product detail pages.

### Typography
Fonts were paired and imported using [Google Fonts](https://fonts.google.com). <br>
*Playfair Display* was chosen as the font for  headings, card titles, and the navbar brand.

Open Sans, with a fallback of sans-serif, was applied to the body, buttons, and prices.

<details>
    <summary> Playfair Display</summary>
    <img src = "assets/readme-files/images/playfair-display.png">
    <br>
    <br>
    <summary> Open Sans</summary>
    <img src = "assets/readme-files/images/open-sans.png">
</details>

### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create wireframes to display the pages' appearance on both mobile and larger devices. Since a lot of pages were going to be very similar in layout and functionality, not every page is represented in the table below. The templates have been adapted for the following pages: 

**Allergen Information**:
- Privacy Policy

**Store Management Views:**
- Manage Bakers
- Manage Orders
- Manage Subscribers
- Manage Products
- Manage Reviews
- Manage Contacts

**User Management Views:**
- My Orders
- My Favorites
- My Reviews

**Add / Edit View:**
- Add / Edit a Product
- Add / Edit a Review
- Add / Edit a Baker
- Edit About Content
- Edit Allergen Information
- Edit Privacy Policy

**Allauth Forms:**
- Sign In
- Sign Out
- Sign Up

**Allauth Texts:**
- Verifification / Reset Email sent

 
Page | Desktop Version | Mobile Version
--- | --- | ---
Home | ![Desktop Home Image](assets/readme-files/wireframes/home-desktop-wf.png) | ![Mobile Home Image](assets/readme-files/wireframes/home-mobile-wf.png)
About | ![Desktop About Image](assets/readme-files/wireframes/about-desktop-wf.png)  | ![Mobile About Image](assets/readme-files/wireframes/about-mobile-wf.png)
Contact Us | ![Desktop Contact Image](assets/readme-files/wireframes/contact-desktop-wf.png) | ![Mobile Contact Image](assets/readme-files/wireframes/contact-mobile-wf.png)
FAQ | ![Desktop FAQ Image](assets/readme-files/wireframes/faq-desktop-wf.png) | ![Mobile FAQ Image](assets/readme-files/wireframes/faq-mobile-wf.png)
Allergen Information | ![Desktop Allergen Information Image](assets/readme-files/wireframes/allergen-desktop-wf.png) | ![Mobile Allergen Information Image](assets/readme-files/wireframes/allergen-mobile-wf.png)
Profile | ![Desktop Profile Image](assets/readme-files/wireframes/profile-desktop-wf.png) | ![Mobile Profile Image](assets/readme-files/wireframes/profile-mobile-wf.png)
Profile Views | ![Desktop List Overview Image](assets/readme-files/wireframes/profile-views-desktop-wf.png) | ![Mobile List Overview Image](assets/readme-files/wireframes/profile-views-mobile-wf.png)
Store Management | ![Desktop Store Management Image](assets/readme-files/wireframes/store-management-desktop-wf.png) | ![Mobile Store Management Image](assets/readme-files/wireframes/store-management-mobile-wf.png)
Store Management Views | ![Desktop Store Management Views Image](assets/readme-files/wireframes/store-management-views-desktop-wf.png) | ![Mobile Store Management Views Image](assets/readme-files/wireframes/store-management-views-mobile-wf.png)
Product List | ![Desktop Product List Image](assets/readme-files/wireframes/product-list-desktop-wf.png) | ![Mobile Product List Image](assets/readme-files/wireframes/product-list-mobile-wf.png)
Product Detail View | ![Desktop Product Details Image](assets/readme-files/wireframes/product-details-desktop-wf.png) | ![Mobile Product Details Image](assets/readme-files/wireframes/product-details-mobile-wf.png)
Add / Edit View | ![Desktop Edit / Create View Image](assets/readme-files/wireframes/add-edit-desktop-wf.png) | ![Mobile Edit / Create View Image](assets/readme-files/wireframes/add-edit-mobile-wf.png)
Allauth Forms | ![Desktop Sign In Image](assets/readme-files/wireframes/allauth-forms-desktop-wf.png) | ![Mobile Sign In Image](assets/readme-files/wireframes/allauth-forms-mobile-wf.png)
Allauth Texts | ![Desktop Sign In Image](assets/readme-files/wireframes/allauth-text-desktop-wf.png) | ![Mobile Sign In Image](assets/readme-files/wireframes/allauth-text-mobile-wf.png)
404 Page | ![Desktop 404 Page Image](assets/readme-files/wireframes/404-desktop-wf.png) | ![Mobile 404 Page Image](assets/readme-files/wireframes/404-mobile-wf.png)

### Fixtures

In order to create a realistic, immersive feeling for users, fixtures were created to upload products and product reviews.

- For the products app, three .json files were created - *occasions.json* to manage 6 occasions, *categories.json* to manage 3 categories, and *products.json* to manage 35 products.
- For the reviews app, one .json file - *reviews.json* -  was created to manage 23 product reviews.

[Back to top ⇧](#bake-me-happy)

## User Experience (UX)

### Project Goals

- The project incorporates a responsive design across different devices.
- The project provides an intuitive structure and navigation.
- The project has a pleasant, coherent design that invites users to explore the product range.
- The project allows users to register and access their profiles.
- The project allows users to have a pleasant shopping experience including a secure payment option.
- The project incorporates full *CRUD* functionality so the user can interact with the content.
- The project allows users to contact the site owners for questions and concerns.
- The project allows site admins to manage the pages content and contacts in one place.

### User Stories

#### Browsing & Navigation

- As a **shopper**, I can **view a list of products** so that **I can see all available options and make a selection**.

- As a **shopper**, I can **view detailed information about a specific product** so that **I can learn more about a product to make an informed purchasing decision**.

- As a **shopper**, I can **easily navigate between different pages** so that **I can find the information I need quickly**.

- As a **shopper**, I can **browse products by category** so that **I can easily find items within a specific area of interest**.

- As a **visually impaired  shopper**, I can **use a screen reader to access and understand the website content** so that **I can browse and interact with the site independently**.

#### Searching & Sorting 

- As a **shopper**, I can **search for products using keywords** so that **that I can quickly find items of interest**.

- As a **shopper**, I can **sort search results by different criteria** so that **I can prioritize the products I'm most interested in**.

- As a **shopper**, I can **easily see if my search returns no results** so that **I am not left confused or frustrated. and can adjust my search criteria**.

#### Account Management

- As a **shopper**, I can **create an account** so that **I can access personalized features and services**.

- As a **registered user**, I can **manage my profile information** so that **my information is accurate and up-to-date**.

- As a **registered user**, I can **delete my account** so that **my data is removed from the system**.

- As a **registered user**, I can **log in to my account using my credentials** so that **I can access my personalized information and features**.

- As a **registered user**, I can **reset my password** so that **regain access to my account**.

#### Basket & Checkout

- As a **shopper**, I can **add products to my basket** so that **I can purchase them later**.

- As a **shopper**, I can **view and update the contents of my basket** so that **I have control over my order before checkout**.

- As a **shopper**, I can **proceed to checkout from my basket** so that **I can complete my purchase**.

- As a **shopper**, I can **securely provide my payment information during checkout** so that **my transaction is processed safely**.

- As a **new shopper**, I can **checkout as a guest without creating an account** so that **I can quickly complete my purchase**.

#### Favorites

- As a **logged-in shopper**, I can **add products to my favorites list** so that **I can easily find them again later**.

As a **logged-in shopper**, I can **view my favorites list** so that **easily access products I've saved**.

- As a **logged-in shopper**, I can **remove products from my favorites list** so that **I can keep the list organized and up-to-date**.

- As a **logged-in shopper**, I can **add products from my favorites list directly to my basket** so that **I can quickly purchase them**.

#### Reviews

- As a **logged-in shopper**, I can **submit a review for a product I've purchased** so that **I can share my experience with other customers**.

- As a **shopper**, I can **review existing reviews** so that **I can make an educated purchasing decision**.

- As a **shopper**, I can **update my submitted reviews** so that **I can correct any mistakes I may have made**.

- As a **shopper**, I can **delete my published reviews** so that **I can remove information that is no longer relevant**.

#### Newsletter Signup

- As a **shopper**, I can **subscribe to the newsletter** so that **receive updates, promotions, and other relevant information**.

#### Admin Access

- As a **site admin**, I can **add, edit, and delete products in the catalogue** so that **I can keep the product information up-to-date**.

- As a **site admin**, I can **review product comments and ratings** so that **I can stay informed about my customers’ feedback**.

- As a **site admin**, I can **view my newsletter subscribers** so that **I can stay connected with my customers**.

- As a **site admin**, I can **view and manage orders** so that **I can track order status, process shipments, and handle customer inquiries**.

- As a **site admin**, I can **manage the website’s content** so that ** I can keep the website up-to-date and engaging**.


#### Business Information

- As a **shopper with allergies**, I can **view clear allergen information on product pages** so that **I can make informed choices about what I can safely consume**.

- As a **shopper**, I can **easily access the privacy policy** so that **I can understand how my data is collected, used, and protected**.

- As a **shopper**, I can **learn about the company's values and its team** so that **I can connect with the people that make it happen**.

-  As a **shopper**, I can **easily find the company’s contact information** so that **I can get in touch if needed**.

- As a **shopper**, I can **view detailed answers to frequently asked questions** so that ‘’I can find solutions to common problems**.

[Back to top ⇧](#bake-me-happy)

## Features

### General

A back to top button is available in the bottom right corner of every page to allow for easy navigation.

<details>
    <summary> Back to Top Button Image </summary>
    <img src = "assets/readme-files/images/btt-button.png">
</details>

#### Responsiveness

Most people access the internet through moile devices. With that in mind, this website was designed to maintain as much of its functionality on smaller screens. Changes between the mobile and desktop layout include:

- Single product card presentation (one card per row as opposed to multiple small cards)
- Fewer columns displayed in tables
- Main navigation is turned into an offscreen canvas
- Secondary navigations use icons to save space

<details>
    <summary> Mobile Menu Image </summary>
    <img src = "assets/readme-files/images/mobile-profile-navbar.png">
</details>

<details>
    <summary> Mobile Menu Image </summary>
    <img src = "assets/readme-files/images/mobile-menu.png">
</details>

#### Header & Navigation

The navigation bar is the same across all pages to provide users with a familiar layout and allow them to focus on the content of each page. It contains the logo in the top left, doubling as a home page link. It also includes links to the main pages across the top, which will take on a different color when active. Its dark color provides a visual framing for the website.
The navigation bar contains a dynamically updated visual indicator of the shopping basket, which serves as a link to the baset.
The navigation bar includes a collapsible profile menu with changing options depending on the status of the user - guest user vs. logged in user vs site admin.
<br>
Secondary navigation bars appear on product and profile pages to allow quick and easy access to related functions. The product navigation bar includes a search field for product searches.
<br>
The header includes the main background image, which displays a welcome message across the home page. The image is visible on all front-facing pages except the home page, to avoid visual clutter. However, it is not rendered on admin-related pages like store management to allow for better focus.

<details>
    <summary> Header Image </summary>
    <img src = "assets/readme-files/images/header.png">
</details>

<details>
    <summary> No Header Image </summary>
    <img src = "assets/readme-files/images/no-header.png">
</details>

<details>
    <summary> Profile Navigation Bar Image </summary>
    <img src = "assets/readme-files/images/profile-navbar.png">
</details>

#### Footer

The footer is the same across all pages to provide users with a familiar layout and allow them to focus on the content of each page. It has the same color as the navigation bars to provide the bottom frame of the content.
The footer contains business related links, including links to the proivacy policy and allergen informaiton pages which are only accessible from there. The footer also contains the business' contact information, including social media links. Lastly, the footer contains a simple newsletter signup fiels, allowing users to subscrbe by simply entering their email address.
<br>
Due to the density of informaiton in the footer, it appears quite large on mobile devices.

<details>
    <summary> Footer Image </summary>
    <img src = "assets/readme-files/images/footer.png">
</details>

#### Toasts

User feedback is provided via toasts that appear in the top right corner of the screen. These toasts are color coded to be easily distinguishable.

<details>
    <summary> Danger Toast Image </summary>
    <img src = "assets/readme-files/images/toast-danger.png">
</details>

<details>
    <summary> Success Toast Image </summary>
    <img src = "assets/readme-files/images/toast-success.png">
</details>

<details>
    <summary> Info Toast Image </summary>
    <img src = "assets/readme-files/images/toast-info.png">
</details>

### Pages

#### Home

The home page contains multiple buttons to take the user to the store, including buttons to go straight to a filtered products, if users are only interested in a certain category.
The home page contains a clearly visible call to action, to invite users to start shopping or contact the business with questions, as well as a carousel displaying customer testimonials to showcase the positive relationship between the business and its customers.

<details>
    <summary> Carousel Image </summary>
    <img src = "assets/readme-files/images/carousel.png">
</details>

<details>
    <summary> Call to Action Image </summary>
    <img src = "assets/readme-files/images/cta.png">
</details>

#### Contact Us

The contact us page contains multiple ways to contact the business, including a contact form. The contact form lets users select a subject from a predefined list to help sort and group incoming messages.

<details>
    <summary> Contact Us Form Image </summary>
    <img src = "assets/readme-files/images/contact-form.png">
</details>

#### FAQ

The FAQ page lists the most frequently asked questions in individual accordions, with the questions always visible and the answers hidden until the accordion is clicked. Only one answer can be revealed at a time. This allows users to quickly scan through the list of questions and focus on the answer they were looking for.

<details>
    <summary> Accordion Image </summary>
    <img src = "assets/readme-files/images/accordion.png">
</details>

#### Product List

Each product is presented in a card. On larger screens, these cards have hover effect to provide visual feedback to the user. When the card image is clicked, the user is taken to the product detail page. 
Products can be added to the shopping basket with a quantitsy of 1 by clicking the basket icon. The heart icon adds products to the user's favorites list, if they are logged in. The heart icon appears empty by default but will toggle to a filled in heart for items that are on the favorites list.

<details>
    <summary> Product Card Image </summary>
    <img src = "assets/readme-files/images/product-card.png">
</details>

#### Product Details

The product detail page contains allr elevant information about a product. Clicking the image will open it in a new tab. Products can be added to the cart up to the maximum quantity available. Products can also be toggled on/off the favorites list.
Allergens are displayed prominently to alert users with allergies. 
Logged in users have the optopn to leave a product review, while guest users can only view existing reviews.

<details>
    <summary> Product Info Image </summary>
    <img src = "assets/readme-files/images/product-info.png">
</details>

#### Basket

In the basket, users can see the products they have added to their basket, as well as the total cost of the items. Item quantitites can be adjusted up to the maximum quantity available. A messageUsers can remove individual items and clear their entire basket. Clicking on a product image will redirect users to the product detail page. From the basket, users can move to the checkout page.
Depending on the total of the basket, a delivery fee may be added. The delivery charge is clearly visible on the basket page. Users receive feedback about how much more they'd have to spend in order to receive free shiping.

<details>
    <summary> Basket Detail Image </summary>
    <img src = "assets/readme-files/images/basket-detail.png">
</details>

#### Checkout

The checkout page contains a form for users to enter their shipping information. For logged in users, these fields will be prepopulated with the information from their profile. Logged in users can tick a box to save the entered information to their profile, while guest users see a prompt to log in or create an account to save their information.
Users can choose between two delivery options via radio buttons - delivery, which is the default option, or pickup. The only option to pay fot delivery is by card via Stripe, using the field at the bottom of the screen. If ppickup is selected, no delivery charge is added to the total. Additionally, when users select to pickup their order, a seecond set of radio buttons becomes visible, allowing users to choose between card payment via Stripe or cash payment on pickup. If cash payment is selected, the checkout process via Stripe is bypassed and the order confirmtion is displayed.
The country field on the checkout page is set to Ireland and cannot be changed.

<details>
    <summary> Checkout Pickup Image </summary>
    <img src = "assets/readme-files/images/checkout-pickup-cash.png">
</details>

<details>
    <summary> Checkout Delivery Image </summary>
    <img src = "assets/readme-files/images/checkout-delivery-card.png">
</details>

#### Profile

In the profile page, users can view and update their personal information. By default, their information are read-only, and the editable form becomes visible by clicking the relevant button. The country field on the profile page is set to Ireland and cannot be changed, same as on the checkout page. Users can reset their password and delete their profile form this page as well.
A secondary navigation bar appears on the profile app to allow users to navigate between their relevant section and view their orders, favorite list, and product reviews. On mobile, the navigation bar uses icons to save space.
- The favorite list is presented as smaller product cards. Favorite products can be deleted from the list and added to the basket by clicking the corresponding buttons.
- Orders are displayed in a table. Clicking on the eye icon will open the oder confirmation in a new tab.
- Reviews are displayed in a table and can be viewed on the product page, edited, and deleted by clicking the correspondng button.

<details>
    <summary> Update Profile Image </summary>
    <img src = "assets/readme-files/images/profile-edit.png">
</details>

<details>
    <summary> Profile Table Image </summary>
    <img src = "assets/readme-files/images/profile-table.png">
</details>

#### Store Management

The store management page allows admin users to easily maintain the website's content and monitor customer interactions. A dashboard at the top provides an easy overview of the sites main stats, such as amount of products, subscribers, reviews, etc. Each of these cards is clickable and will bring site admins to a more detailed view of that section. The dashboard is collapsed on mobile screens to save space.
These sections can also be reached by clicking the links in the category cards. Where applicable, store admins can view a table for eah of these sections containing more details as well as action buttons. This is very similar to the way information is presented in the user profile tables. If no tables are neccessary, site admins are brought straight to the relevant editor, where they can use a WYSISYG editor to make changes to the content.

<details>
    <summary> Dashboard Image </summary>
    <img src = "assets/readme-files/images/dashboard.png">
</details>

<details>
    <summary> Store Management Table Image </summary>
    <img src = "assets/readme-files/images/store-management-table.png">
</details>

### Future Features

The following features could be implement in future versions of the site to improve both the user experience and site functionality:

- Social media sign in
- Additional payment options
- Dynamic order status updates for admins and users
- Recurring orders and subscriptions
- A newsletter signup pop up
- Promo codes at checkout
- Search options for admin views
- Search / sort by allergens and ingredients

[Back to top ⇧](#bake-me-happy)

## Technologies Used

### Languages

- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Tools and Programs

- [Amazon Web Services S3](https://aws.amazon.com/s3/) was used to store static and media files in production.
- [Am I Responsive](ami.responsivedesign.is) was used to preview the website across various popular devices.
- [Balsamiq](https://balsamiq.com/) was used to create wireframes.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used for code review and responsiveness testing.
- [Coolors](https://coolors.co) was used to create a color scheme for the website.
- [Draw.io](https://www.draw.io) was used to visualize the structure of the website and relationships between pages.
- [Favicon.io](https://favicon.io) was used to create the site favicon.
- [Gemini](https://gemini.google.com/) was used to help generate the product and review fixtures.
- [Getimg.ai](https://getimg.ai/) was used to generate the hero image.
- [Git](https://git-scm.com) was used for version control by committing and pushing code to GitHub.
- [GitHub](https://github.com) was used to store the project's code.
- [Grammalry](https://app.grammarly.com) was used to spell-check the contents of the Readme.
- [Heroku](https://www.heroku.com) was used to deploy the website.
- [Heroku Postgres](https://www.heroku.com/postgres) database was used in production, as a service based on PostgreSQL provided by Heroku.
- [JPG2PNG](https://jpg2png.com) was used to convert all images to PNG format.
- [JSHint](https://jshint.com/) was used to validate the site's JavaScript code.
- [JSON Formatter & Validator](https://jsonformatter.curiousconcept.com) was used to validate the JSON code.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) was used to measure the page's quality.
- [Silktide Accessibility Checker](https://chromewebstore.google.com/detail/silktide-accessibility-ch/mpobacholfblmnpnfbiomjkecoojakah?hl=en) was used to test the website's accessibility.
- [PEP8 Online Check](https://pep8ci.herokuapp.com) was used to validate the Python code.
- [SQLite](https://www.sqlite.com/index.html) was used as a single-file database during development.
- [Stripe](https://stripe.com/en-gb-nl) was used to process all online payment transactions.
- [Tiny PNG](https://tinypng.com) was used to reduce the file size of images.
- [Visual Studio Code](https://code.visualstudio.com) was used to write and edit the code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.
- [W3C Markup Validator](https://validator.w3.org/) was used to validate the HTML code.

### Libraries, Frameworks, and Packages

- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used throughout the website to help with styling and responsiveness.
- [CDNJS](https://cdnjs.com/) was used to deliver external libraries to the website.
- [Django](https://www.djangoproject.com/) was used as the web framework.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.
- [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for forms and models.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to control the rendering of forms.
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html) was used to generate the ERD from Django models.
- [Font Awesome](https://fontawesome.com) was used throughout the website to add icons for aesthetic and UX purposes.
- [Google Fonts](https://fonts.google.com) was used to import fonts into the HTML file and applied across the site.
- [Graphviz](https://graphviz.org/) was used to render the ERD from the model relationships.
- [Gunicorn](https://gunicorn.org/) was used as a Python WSGI HTTP Server for UNIX to support the deployment of the Django application.
- [jQuery 3.6.0](https://jquery.com/) was used as a JavaScript library to simplify JavaScript code.
- [Pillow](https://pypi.org/project/Pillow/) was used to add image processing capabilities.
- [Pixabay](https://pixabay.com/) was used to source images.
- [Summernote](https://summernote.org/) was used as a WYSIWYG editor.

[Back to top ⇧](#bake-me-happy)

## Deployment

The project was deployed using *Visual Studio Code* for writing code, *GitHub* for version control, and *Heroku* for hosting the live application. Below are the detailed steps for deploying the project, assuming you are working on your code in *Visual Studio Code*.

### GitHub

1. **Create a Repository**:
   - Log in to your [GitHub account](https://github.com/).
   - Click on the *New Repository* button.
   - Provide a name for your repository, add an optional description, and choose whether it should be public or private.
   - Click *Create Repository*.

2. **Clone the Repository in Visual Studio Code**:
   - Open *Visual Studio Code*.
   - Open the Command Palette (`Cmd + Shift + P` on Mac or `Ctrl + Shift + P` on Windows/Linux).
   - Search for and select *Git: Clone*.
   - Paste the repository URL and select a folder to clone the repository into.

3. **Work on Your Code**:
   - Open the cloned repository folder in Visual Studio Code.
   - Make changes to your code as needed.

4. **Commit and Push Changes**:
   - Open the *Source Control* tab in Visual Studio Code (the Git icon in the sidebar).
   - Stage your changes by clicking the `+` icon next to the files or clicking *Stage All Changes*.
   - Add a commit message in the text box and click the checkmark icon to commit the changes.
   - Push the changes to GitHub by clicking the three dots in the Source Control tab and selecting *Push*.

   Alternatively, you can stage, commit, and push your changes via the *Terminal*:
    ```bash
    git add .
    git commit -m "Description of the changes"
    git push origin my-new-branch
    ```
5. **Set Up GitHub Pages (Optional)**:
   - If you want to deploy a static version of your project, go to the repository's *Settings* on GitHub.
   - Under the *Pages* section, select the branch (e.g., `main`) and the folder (e.g., `/root`) to deploy.
   - Save the settings, and your project will be live on GitHub Pages.


### Heroku

1. **Create a Heroku Account**:
   - Sign up or log in to your [Heroku account](https://www.heroku.com/).

2. **Create a New Heroku App**:
    - In your Heroku account, select *Create New App* from the Dashboard.
    - Enter a unique app name and choose your region.
    - Click *Create App*.

3. **Set Up Environment Variables**:
   - Go to the *Settings* tab of your Heroku app on the Heroku dashboard.
   - Click on *Reveal Config Vars* and add the following environment variables:

   Varable | Key   
   --- | ---   
   DATABASE_URL | your_database_url   
   EMAIL_HOST_PASS | your_app_password_from_your_email   
   EMAIL_HOST_USER | your_email_address  
   SECRET_KEY | your_secret_key 
   STRIPE_PUBLIC_KEY | your_stripe_public_key  
   STRIPE_SECRET_KEY | your_stripe_secret_key  

4. **Prepare the Project for Deployment**:
   - Open the terminal in Visual Studio Code and ensure `gunicorn` and `psycopg2`are installed:
     ```bash
     pip3 install gunicorn
     pip3 install psycopg2
     ```
   - Create a [Procfile](http://_vscodecontentref_/0) in the root of your project and add the following line:
     ```plaintext
     web: gunicorn <project_name>.wsgi
     ```
    - Create a file named *python-version* in the root of your project and add the version of Python you are using.

    - Update your *requirements.txt* file:
        ```bash
        pip3 freeze > requirements.txt
        ```

    - Run any outstanding database migrations and collect static files:
        ```bash
        python3 makemigrations
        python3 migrate
        python3 manage.py collectstatic
        ````

    - Update your debug settings in your *settings.py* file:
        ```plaintext
        DEBUG = FALSE
        ```

    - Update your database configuration in your *settings.py* file:
        ```plaintext
            if 'DATABASE_URL' in os.environ:
                DATABASES = {
                    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
            else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
        ```
        - **Note**: This conditional statement defines that  app will connect to Postgres when running on Heroku, and connect to Sqlite when running locally.

5. **Push the Code to Heroku**:
   - Add Heroku as a remote repository:
     ```bash
     heroku git:remote -a <app-name>
     ```
   - Push the code to Heroku:
     ```bash
     git push heroku main
     ```

6. **Deploy the Project:**
    - On Heroku, go to *Deploy* and specify deployment details.
    - Select *GitHub* as the *Deployment Method*.
        - When prompted to *Connect to GitHub*, find your repository and click *Connect*.
    - Select either *Automatic Deploys* or *Manual Deploys* and click *Deploy Branch*.

7. **Access the Live Application**:
   - Once the deployment is complete, your application will be live at `https://<app-name>.herokuapp.com/`.

9. **Monitor the Application**:
   - Use the Heroku dashboard or CLI to monitor logs and performance. In the Visual Studio Code terminal, you can run:
     ```bash
     heroku logs --tail
     ```

### Amazon Web Services

1. **Create an AWS Account**
- Go to [AWS](https://aws.amazon.com/) and create an account if you don’t already have one.
- Once logged in, navigate to the *AWS Management Console*.

2. **Create an S3 Bucket**
- In the AWS Management Console, search for *S3* in the search bar and click on it.
- Click the *Create Bucket* button.
- Provide a unique name for your bucket (e.g., `my-django-static-media`).
- Choose a region closest to your location.
- Uncheck *Block all public access* (this is necessary to allow public access to your static and media files).
- Acknowledge the warning about public access and click *Create Bucket*.

3. **Configure Bucket Permissions**
- Go to your newly created bucket and click on the *Permissions* tab.
    - Set the appropriate permissions for the bucket.
    - Ensure that the bucket is not publicly accessible unless specifically required.
    - Configure the *Bucket Policy* and *Cross-origin resource sharing (CORS)* details.

4. **Install Required Packages**: 
- Install `boto3` and `django-storages` packages.
    ```bash
    pip3 install boto3 
    pip3 install django-storages
    ```

5. **Update Django Settings**:
- Add the following configurations to your `settings.py` file.
    ```bash
    # AWS S3 Settings
    AWS_STORAGE_BUCKET_NAME = '<your-bucket-name>'
    AWS_S3_REGION_NAME = '<your-region>'  # e.g., 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and Media Files
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # Static and Media URLs
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    ```
- Update your *INSTALLED_APPS* to include `storages`.

5. **Update Heroku Config Vars:**
- Add the following environment variables:

   Varable | Key   
   --- | ---
   AWS_ACCESS_KEY_ID | your_access_key_id_from_AWS   
   AWS_SECRET_ACCESS_KEY | your_secret_access_key_from_AWS  
   USE_AWS | True 



6. **Collect Static Files**: Run the `collectstatic` command to collect all static files and upload them to your S3 bucket.
    ```bash
    python manage.py collectstatic
    ```

[Back to top ⇧](#bake-me-happy)

## Testing

The testing documentation can be found [here ⇨](TESTING.md).

[Back to top ⇧](#bake-me-happy)

## Finished Product

Page | Desktop Version | Mobile Version
--- | --- | ---
Home | ![Result](assets/readme-files/images/home-desktop.png) | ![Result](assets/readme-files/images/home-mobile.png)
About | ![Result](assets/readme-files/images/about-desktop.png) | ![Result](assets/readme-files/images/about-mobile.png)
FAQ | ![Result](assets/readme-files/images/faq-desktop.png) | ![Result](assets/readme-files/images/faq-mobile.png)
Contact Us | ![Result](assets/readme-files/images/contact-desktop.png) | ![Result](assets/readme-files/images/contact-mobile.png)
Allergen Information | ![Result](assets/readme-files/images/allergen-info-desktop.png) | ![Result](assets/readme-files/images/allergen-info-mobile.png)
Profile | ![Result](assets/readme-files/images/profile-desktop.png) | ![Result](assets/readme-files/images/profile-mobile.png)
Favorites | ![Result](assets/readme-files/images/my-favorites-desktop.png) | ![Result](assets/readme-files/images/my-favorites-mobile.png)
Orders | ![Result](assets/readme-files/images/my-orders-desktop.png) | ![Result](assets/readme-files/images/my-orders-mobile.png)
Reviews | ![Result](assets/readme-files/images/my-reviews-desktop.png) | ![Result](assets/readme-files/images/my-reviews-mobile.png)
Product List | ![Result](assets/readme-files/images/product-list-desktop.png) | ![Result](assets/readme-files/images/product-list-mobile.png)
Product Detail | ![Result](assets/readme-files/images/product-details-desktop.png) | ![Result](assets/readme-files/images/product-details-mobile.png)
Store Management | ![Result](assets/readme-files/images/store-management-desktop.png) | ![Result](assets/readme-files/images/store-management-mobile.png)
Manage Products | ![Result](assets/readme-files/images/manage-products-desktop.png) | ![Result](assets/readme-files/images/manage-products-mobile.png)
Add Product | ![Result](assets/readme-files/images/add-product-desktop.png) | ![Result](assets/readme-files/images/add-product-mobile.png)
Edit About | ![Result](assets/readme-files/images/edit-about-desktop.png) | ![Result](assets/readme-files/images/edit-about-mobile.png)
Sign In | ![Result](assets/readme-files/images/sign-in-desktop.png) | ![Result](assets/readme-files/images/sign-in-mobile.png)
Sign Up | ![Result](assets/readme-files/images/sign-up-desktop.png) | ![Result](assets/readme-files/images/sign-up-mobile.png)
Sign Out | ![Result](assets/readme-files/images/sign-out-desktop.png) | ![Result](assets/readme-files/images/sign-out-mobile.png)
404 Page | ![Result](assets/readme-files/images/404-desktop.png) | ![Result](assets/readme-files/images/404-mobile.png)

**Note:** In the mobile screenshots, the banner image is displaying as a black background. However, when viewing the pages on a mobile device, the banner image is displaying correctly.

[Back to top ⇧](#bake-me-happy)

## Credits

### Content

All content was written by the developer.

The following resources were consulted frequently:

- [Django Documentation](https://docs.djangoproject.com/)
- [Stripe Documentation](https://docs.stripe.com/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Django-allauth Documentation](https://django-allauth.readthedocs.io/en/latest/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Developedbyed's *Learn Javascript* [Youtube Playlist](https://www.youtube.com/playlist?list=PLDyQo7g0_nsXlSfuoBpG5Fgz0Qe3IvWnA)
- Codemy's *Let's build an e-commerce website* [Youtube Playlist](https://www.youtube.com/watch?v=u6R4vBa7ZK4&list=PLCC34OHNcOtpRfBYk-8y0GMO4i1p1zn50)


### Media

- The hero image and logo were generated by Alex Büttner using [Getimg.ai](https://getimg.ai/).
- The product images were sourced from [Pixabay](https://pixabay.com/) and [Pinterest](https://www.pinterest.com/).
- The product descriptions and reviews were generated with the help of [Gemini](https://gemini.google.com/). 

### Code

- The code for *basket/contexts.py* has been adapted from Code Institute's "Boutique Ado" project.
- The desktop view of the basket has been adapted from Code Institute's "Boutique Ado" project.
- The product sorting functionality has been adapted from Code Institute's "Boutique Ado" project.
- The code for *custom_clearable_file_input.html* has been adapted from Code Institute's "Boutique Ado" project.
- The code for the county and subject dropdowns has been adapted from Code Institute's "Boutique Ado" project.
- The Back to Top button has been adapted from Code Institute's "Boutique Ado" project

- The product detail page has been adapted from Start Bootstrap's ["Shop Item" template](https://startbootstrap.com/template/shop-item).
- The product list page has been adapted from Start Bootstrap's ["Shop Homepage" template](https://startbootstrap.com/template/shop-homepage).
- The desktop view of the main navigation has been adapted from Start Bootstrap's ["Shop Homepage" template](https://startbootstrap.com/template/shop-homepage).

- The star rating has been adapted from CSS Tricks'["Star Rating Widget"](https://css-tricks.com/star-ratings/) tutorial and [Bootstrap Star Rating](https://github.com/kartik-v/bootstrap-star-rating).
- The mobile off-canvas navigation has been adapted from Bootstrap 5's [Off-Canvas](https://getbootstrap.com/docs/5.0/components/offcanvas/) component.
- The code for *products/widgets.py* has been adapted from https://github.com/django/django.
- The footer has been adapted from MDB's [Footer with newsletter section](https://mdbootstrap.com/docs/standard/navigation/footer/examples-and-customization/).


[Back to top ⇧](#bake-me-happy)

## Acknowledgements

- A heartfelt thank you to Code Institute, its incredible tutors, and the supportive Slack community for their invaluable guidance and encouragement throughout this journey.  
- To Marcel, my mentor, thank you for your insightful feedback and helping me stay on track.  
- A special shoutout to Nono for your endless patience and for being my go-to person for all things JavaScript.  
- And finally, to my husband, thank you for your constant encouragement, understanding, and support every step of the way — I couldn’t have done this without you.

[Back to top ⇧](#bake-me-happy)