# David Kelley Photography

View live site: [David Kelley Photography](https://david-kelley-photography.herokuapp.com/)

![David Kelley Photography Mockup](https://i.ibb.co/h1YLrSt/david-kelley-responsive.png)

From [Techsini](http://techsini.com/)

------

## About this project:

David Kelley Photography is a business to consumer (B2C) site intended for site users to purchase landscape photography directly from the shop owner. This site was created as a project (Milestone 4) for the Code Institute, but I plan to launch it live online after assessment. The site sells photography created by David Kelley (my father) from over 15 years of travel in the US and abroad. I created the site so that my father can turn his hobby into a way to sell his photography and communicate directly with his customers through a personal blog. In this case, I designed the site to fit and showcase the landscape photography; I used a retro 1970s aesthetic on the site to match my dad's preferred style. The proceeds from the photography when the site goes live online will be donated to local charities in Harrisburg, PA. 

The project is developed using Django, Python, JavaScript, HTML, CSS, and the Bootstrap framework.

**This is currently a test project and the products aren't available for sale**

To make test payments use this Stripe test card:

credit card: 4242 4242 4242 4242

expiration date: 04 / 24

CVC: 424

ZIP: 42424

------

## Table of Contents

  

+  [Ux](#ux-planning)

    - [User Stories](#user-stories)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
    - [Database](#database-structure)
    - [Design](#design-choices) 

+  [Features](#features)

+  [Technologies used](#technologies-used)

+  [Testing](#testing)

+  [Deployment](#deployment)

+  [Credits](#credits)


------


## UX Planning
  

### Project Goals:

Users

+ To easily navigation the site and understand its purpose
+ Learn about the site owner and the charities purchase proceeds go to
+ Contact the site owner directly through a form
+ Learn about the photography in the site's blog
+ Comment on and like blog posts
+ Browse landscape photographs by category
+ See related products in the same category
+ Choose a mat colour to back the photograph
+ Purchase products securely over Stripe and receive a confirmation email
+ Create an account to save shopper details
+ Save products for later in a wishlist
+ Access all order details



Site Owner

+ Receive contact forms through Django admin and direct email message
+ Add/edit/delete products
+ Add/edit/delete blog posts
+ Access blog post drafts on the site
+ Design focus on owner's personal style and taste


### User Stories:


You can view an organised board with all user stories here:


[User Stories for Milestone 4 Trello Board](https://trello.com/b/e7RIsmL0/milestone-4-user-stories)

### Scope

For this project, the main aim was to create a simply Ecommerce site to sell landscape photography from the site owner directly to customers so that proceeds from purchases can be donated to charities like Hospice of Central Pennsylvania and Bethesda Mission. This site was built desktop first with older users in mind. Elegant mobile and tablet design was also considered for all users. 

To convert general users into customers, a blog was planned with information about the photographer, his artwork, and meditations on different landscapes. All users can engage with this blog and there's a call to action sidebar to help direct these users to make purchases. 

Existing customers will have the option to login, view order and shipping information in their profile, and save products in a wishlist. This will keep existing customers engaged with the site content and encourage them to come back and make more purchases.

Superusers can make updates to the site on pages that regular users won't have access to. The superusers can add/update/delete products and content on the blog.

### Structure


### Wireframes

Note: I combined the wireframes for some forms since their design is similar

| All Wireframes from Figma |     
| ----------- | 
| [Home](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=106%3A2)     | 
| [About](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A870)  |
| [All Products](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A595) |  
| [Product Details](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A273) |  
| [Wishlist](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A1032) |  
| [Cart](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A398) |  
| [Checkout](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A498) |  
| [Add/Edit Products/Blogs](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A786) |  
| [Profile](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A948) |  
| [Blog](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=106%3A138) |  
| [Blog post](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A681) |  
| [Register/Login](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=107%3A1099) |  


### Design


#### Colours

The colours for this site are autumnal/earth tones that match the aesthetic of the store owner. The palette was created on [Coolors](https://coolors.co/):

![David Kelley Photography colour palette](https://i.ibb.co/ZYDPY1j/David-Kelley-palette.png)

### Fonts

The branding font for the site is David Libre.

The main headings are Goudy Bookletter 1911 and Zen Antique Soft. Paragraph sections are Lato font. The navlinks in the header and footer are Aleo and custom buttons are Ubuntu. 

These fonts were chose to be easy to read and have a vintage/artistic look.


The full style pack was planned out in Figma and you can view the style pack [here](https://www.figma.com/file/dZz9h1LTx9RT6xNIFdwAZb/Milestone-4-styles?node-id=2%3A4).


## Database structure

### Databases used

For development, I used the sqlite3 database that comes with Djanga. A PostgreSQL database through Heroku is in use for the deployed live site. 

### Django apps and models

Home
About
Blog
Cart
Checkout
David_kelley
Products
Profiles

## Features

### Existing features

+ Navigation Bar
  + Built with Bootstrap
  + Dropdowns for Account link and Category link

+ Mobile nav modal
  + Open a modal when the hamburger icon is clicked on
  + Close modal on X button
  + Display main navlinks, dropdowns, and account link in modal

+ Desktop and mobile navbar
  + Display specific Account links depending on if the user is logged out, logged in, or is a superuser
  + Cart will display total and change colour if there is content in the cart

+ Footer
  + Branding link back to homepage
  + Footer navigation links to main pages
  + Contact button that links directly to form on About page

+ Home app
  + Call to action button: Shop Now to products page
  + Category navigation gallery that will short products by category if you click on an image
  + Featured blog posts that show 3 most recent blog posts -User story-

+ About app
  + Contact form that saves to database and sends email notifcation to site owner -User story-

+ Blog app
  + Blog page
    + Card that displays content from each blog post -User story-
    + Link to the full blog post
    + Comment counter
    + Option to edit/delete blog posts -Superuser-
  + Blog details
    + Full blog post content 
    + Moderated comment section and comment form -User story-
    + Button to like blog post -User story-
    + Blog sidebar that links to products page
    + Option to edit/delete blog posts -Superuser-
  + Add blog -Superuser-
    + Form to add new blog posts -User story-
    + Display draft blog posts to edit or delete
  + Edit blog -Superuser-
    + Form to edit blog posts -User story-







