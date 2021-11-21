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
+ Purchase products securly over Stripe and recieve a confirmation email
+ Create an account to save shopper details
+ Save products for later in a wishlist
+ Access all order details



Site Owner

+ Recieve contact forms through Django admin and direct email message
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

Existing customers will have the option to login, view order and shipping information in their profile, and save products in a wishlist. This will keep exisiting customers engaged with the site content and encourage them to come back and make more purchases.

Superusers can make updates to the site on pages that regular users won't have access to. The superusers can add/update/delete products and content on the blog.

### Structure


### Wireframes

Note: I combined the wireframs for some forms since their design is similar

| All Wireframs from Figma |     
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
