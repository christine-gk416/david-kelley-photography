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
    - [Design](#design) 

+ [Database](#database-structure)

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
  + Cart will display total and change colour if there is content in the cart and link to cart

+ Footer
  + Branding link back to homepage
  + Footer navigation links to main pages
  + Contact button that links directly to form on About page

+ Toasts
  + Display messages when a specific change is made on the site
  + Display checkout information after product is added to cart

+ Home app
  + Call to action button: Shop Now to products page
  + Category navigation gallery that will short products by category if you click on an image
  + Featured blog posts that show 3 most recent blog posts -User story-

+ About app
  + Contact form that saves to database and sends email notification to site owner -User story-

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

+ Cart
  + Display up to date information about items in cart
  + Option to update product quantity
  + Option to remove item from cart
  + Show total, shipping, and subtitle
  + Button to checkout or return to products page

+ Checkout  
  + Main checkout
    + Display order information
    + Display checkout form
    + Give user the option to login or create account -User story-
    + Display shipping information if user is logged in
    + Stripe payment form
    + Button to make a purchase or return to products page -User story-
    + Loading modal while order goes through
  + Order confirmation
    + Display order information and send order confirmation -User story-
    + Button to blog page

+ Products 
  + All products
    + Display all products in masonry style
    + Search bar for products
    + Sort products by category links
    + Heart button to add items to wishlist if you're logged in -User story-
    + Button to product details page
  + Product details
    + Display specific product details
    + Inputs to add product quantity and choose mat card colour
    + Button to add items to wishlist -User story-
    + Buttons to add to cart or return to products page
  + Add product -Superuser-
    + Form to add new products posts -User story-
  + Edit product -Superuser-
    + Form to edit products -User story-

+ Profile 
  + Profile page -User story-
    + Give logged in user option to update shipping info
    + Display all order information
    + Button to Wishilist page
  + Wishlist page -User story-
    + Display wishlist items
    + Delete item or go to product details page

+ Register/Login
  + Allauth forms to allow users to create an account or login


### Future features

For future releases, I plan to make the products page more robust so that customers can customise their order such as adding more dimensions at different price points and add a photo frame to their order.

## Testing

Read testing file [here](static/docs/Testing.md).


## Technologies Used

### Languages
+ HTML5, CSS3, JavaScript, Python

### Planning site

+ [Figma](https://figma.com/) was used to create Wireframes and style system.
+ [Coolors](https://coolors.co/) was used to create site colour palettes.
+ [QuickDBD](https://www.quickdatabasediagrams.com/) was used to model database structure.
+ [Trello](https://trello.com/) was used to plan user stories and scope out features.
+ [Gimp](https://www.gimp.org/) was used to edit image dimensions and crop images.
+ [TinyJPG](https://tinypng.com/) used to minify image file sizes.
+ [Responsive Design Checker](https://responsivedesignchecker.com/) was used to check the site design and responsiveness on different devices.
+ [Lambda Test](https://www.lambdatest.com/) was used to check the site on different browsers and operating systems.
+ [WebAccessibility](https://www.webaccessibility.com/) was used to test how accessible the site is.
   
### Libraries and Frameworks

+ [Django](https://www.djangoproject.com/) was used to create templates and manage the project.

+ [Bootstrap 4](https://getbootstrap.com/) was used to format the site design with their built-in CSS and JS.

+ [FontAwesome 5.15.4](https://fontawesome.com/) is used for social links and the rating stars.

+ [Google Fonts](https://fonts.google.com/) is used for most fonts on the site.

+ [jQuery](https://jquery.com/) to easily manipulate the DOM and update Bootstrap tools that require initialization.

### Payment processors

+ [Stripe](https://stripe.com/ie) is used to process payments on the site. 

### Required modules

All modules required are located in the [requirements.txt](requirements.txt) file.

### Development tools

+ [Git](https://git-scm.com/) is used to track changes made to the repository and for version control.
+ [GitHub](https://github.com/) is used to store the project and to share the project.
+ [VS Code](https://code.visualstudio.com/) is used with the CI base template as an IDE (integrated development environment) to develop, commit, and push files to GitHub.


### Deployment/Hosting

+ [Heroku](https://id.heroku.com/login) is used to deploy and host the live site content.

### Static and media file storage

+ [AWS](https://aws.amazon.com/) was used to store static files and media files so that they work correctly on the deployed site

## Deployment

### Required technology

-   **Django**: to create multiple apps in the project and manage templates
-   **Python3**: write the code and run the project through Django
-   **PIP**: install packages
-   **Git**: version control
-   **VSC:** IDE used to create this project.
-   **Postgre**:  as the database to create content, add new content, and manage data
-   **Heroku**: to deploy the project and manage the app

### Deployment to Heroku

Create a new application in Heroku:

1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select Create New App.
4. Enter a uniquge app name.
5. Select your current region.

Set up connection to Github Repository:

1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a github repository to connect to will then be displayed.
3. Enter the repository name for the project and click search to find your repository.
4. Click the connect button.

Add PostgreSQL Database:

1. Click the Resources tab.
2. Under Add-ons seach for Heroku Postgres and then click on it when it appears.
3. Select Plan name Hobby Dev - Free and then click Submit Order Form.

Set environment variables:

Click on the Settings tab and then click reveal Config Vars.
Variables added:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

DATABASE_URL

EMAIL_HOST_PASS

EMAIL_HOST_USER

SECRET_KEY

STRIPE_PRICE_ID

STRIPE_PUBLIC_KEY

STRIPE_SECRET_KEY

STRIPE_WH_SECRET

USE_AWS

Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Clone and run locally

1. Go to the Github repository for Horror House Reviews and click the Code dropdown
2. Click Download Zip, unzip the files, and upload the files to the IDE of your choice. 
3. Upload these files to your IDE
4. In the terminal, install the requirements.txt file using:

        pip3 install -r requirements.txt

5. Create an env.py file in your IDE with this command:

        touch env.py 

6. Add your AWS, Stripe, and your email hidden keys to the env.py file.


7. Store the env.py file in your .gitignore file so that this sensitive information is hidden on your GitHub repository. 

8. You can now run the app on your IDE by running this command in your terminal: 

        python3 manage.py runserver

## Credits

### Code

+ The base code for this project is from the Code Institute Boutique Ado project
+ Site footer is based on free Bootstrap footer templates [here](https://mdbootstrap.com/docs/standard/navigation/footer/)
+ Mobile modal is based on [this Codepen project](https://codepen.io/Papawhoop/pen/bwXmxq)
+ Contact form on the About page is based on this [Bootstrap template](https://mdbootstrap.com/docs/b4/jquery/forms/contact/)
+ Blog app was built by following this tutorial from [Django Central](https://djangocentral.com/building-a-blog-application-with-django/)
+ The blog like button is based on this tutorial from [Codemy](https://www.youtube.com/watch?v=PXqRPqDjDgc)
+ Wishlist is based on the code in this [Very Academy walkthrough](https://www.youtube.com/watch?v=OgA0TTKAtqQ)
+ [StackOverflow](https://stackoverflow.com/) was used to solve coding issues and ask questions
+ [Medium](https://medium.com/) was used to search for fixes in code and find instructions
+ [Django documentation](https://docs.djangoproject.com/en/3.2/) was used to learn and implement Django template features
+ [W3Schools](https://www.w3schools.com/) was used for general reference
+ [CSSTricks](https://css-tricks.com/) was used for general reference on CSS

### Images

+ The favicon was created on [Free Favicon Maker](https://formito.com/tools/favicon)
+ Abstract image was created on [Sshape](https://fffuel.co/ssshape/)
+ All landscape photography on the site was created by David Kelley and this site is his portfolio

+ Freepik background image creators:
  + https://www.freepik.com/free-photo/explosion-colored-powder-white-background_1193983.htm#page=1&position=0&from_view=collections
  + https://www.freepik.com/freepik
  + https://www.freepik.com/free-vector/copy-space-abstract-green-background-with-shiny-elements_12235867.htm#page=1&position=1&from_view=collections
  + https://www.freepik.com/free-vector/abstract-background-with-watercolor-shapes-empty-space_18962624.htm#page=1&position=2&from_view=collections
  + https://www.freepik.com/free-vector/flat-geometric-background_13817744.htm#page=1&position=3&from_view=collections

### Acknowledgements
+ Thanks to my amazing mentor Mr. Spencer Barriball
+ My husband James for his support through this course
+ The Code Institute team and the Slack community
