# Testing

+ [Code Validation](#code-validation)
+ [Features](#features)
+ [Defensive Design](#defensive-design)
+ [Minor Issues](#minor-issues)
+ [Responsiveness](#responsiveness)
+ [Browser and OS](#browser-and-os)
+ [Performance](#performance)

## Code validation
+ Python passes in PEP8 validator with no errors.
+ JavaScript passes in JShint with no errors.
+ CSS passes in Jigsaw with no errors. Third-party CSS does throw some warnings.
+ HTML passes in W3 Validator with no errors in my code. Errors and warnings from third party code is present

## Features 

+ Navigation Bar
  + Built with Bootstrap - Tested that navbar is working correctly and resizing on different screens.
  + Dropdowns for Account link and Category link - Tested that dropdowns display additional links when clicked on and aria-labels are set up properly.

+ Mobile nav modal
  + Open a modal when the hamburger icon is clicked on - Tested that modal opens over the screen with additional links on mobile.
  + Close modal on X button - Tested that modal closes on click
  + Display main navlinks, dropdowns, and account link in modal - Tested that dropdowns still work in the modal

+ Desktop and mobile navbar
  + Display specific Account links depending on if the user is logged out, logged in, or is a superuser - Register/Login appears when not logged in; Manage Profile/Wishlist appears when logged in; 
  all other options display when superuser is logged in
  + Cart will display total and change colour if there is content in the cart and link to cart - Tested that cart only displays total and changes colour when products are in cart

+ Footer
  + Branding link back to homepage - Tested that link directs to homepage on click
  + Footer navigation links to main pages - Tested that all all footer navlinks go to correct pages
  + Contact button that links directly to form on About page - Tested that contact button goes to About page and scrolls to the form

+ Toasts
  + Display messages when a specific change is made on the site - Tested that toasts appear when appropriate change is made
  + Display checkout information after product is added to cart - Tested that product information appears in cart after being added

+ Home app
  + Call to action button: Shop Now to products page - Tested that call to action button jumps to products page
  + Category navigation gallery that will short products by category if you click on an image - Tested that category links sort correct product category on products page
    - An issue was found on mobile, since the overlay buttons don't work as expected. To fix this, I added category captions to only display on small screens
  + Featured blog posts that show 3 most recent blog posts -User story- - Tested that only the 3 most recent posts are displayed and open blog post
    - Fixed an issue where blog drafts also appeared on this page

+ About app
  + Contact form that saves to database and sends email notification to site owner -User story- - Tested that contact form saves form to database and sends an email with information to site owner

+ Blog app
  + Blog page
    + Card that displays content from each blog post -User story- -Tested that correct blog post content for each post displays on card
    + Link to the full blog post - Tested that link opens correct blog post
    + Comment counter - Tested that the correct number or products appears per post
      - There is a slight issue here where moderated comments not yet approved are counted that I plan to handle in future releases
    + Option to edit/delete blog posts -Superuser- - Tested that blog posts can be edited and deleted successfully
  + Blog details
    + Full blog post content - Full blog post content is display and formatted with Django templating
    + Moderated comment section and comment form -User story- - Tested that users can create moderated comments and tested that superuser can approve comments in admin
      - Comments post after moderation and I fixed a small issue where the comments ran into each other on the page
    + Button to like blog post -User story- - Tested that button adds and removes likes, but only if user is logged in. I'd like to remove this gating in future releases.
    + Blog sidebar that links to products page - Tested that blog sidebar appears on the page with link that successfully opens products page
    + Option to edit/delete blog posts -Superuser- - Tested that blog posts can be edited and deleted successfully
  + Add blog -Superuser-
    + Form to add new blog posts -User story- - Tested that form creates new blog posts and sorts posts by drafts and published posts
      - A Tempus Dominus date picker was added to fix errors with date formatting from general form input and user author is set to logged in user to limit to superusers
    + Display draft blog posts to edit or delete - Draft blog post displays on this page if the post is set to be a draft
  + Edit blog -Superuser-
    + Form to edit blog posts -User story- - Tested that a blog post can be edited successfully and updated on date is used when published

+ Cart
  + Display up to date information about items in cart - Tested that cart shows updated information
  + Option to update product quantity - Tested that it's possible to update product quantity and fixed input issue from mobile code refactor
  + Option to remove item from cart - Item is removed from cart if product quantity is set to 0
  + Show total, shipping, and subtitle - Total displays with shipping, only if less than $100 spent
  + Button to checkout or return to products page - Checkout button goes to the checkout page and return button goes to products page

+ Checkout  
  + Main checkout
    + Display order information - Tested that correct order information is displayed
    + Display checkout form - Tested that checkout form is displayed, takes information, and throws an error if the wrong info is entered or required info isn't provided
    + Give user the option to login or create account -User story- - Tested that a logged out user can create an account
    + Display shipping information if user is logged in - Tested that saved shipping information displays if user is logged in
    + Stripe payment form - Tested that Stripe payment form appears on page and accepts test orders
    + Button to make a purchase or return to products page -User story- - Tested that purchase button creates an order and directs to order confirmation page
    + Loading modal while order goes through - Tested that modal works
      - Spinner didn't work on FontAwesome 6, so I used an earlier version
  + Order confirmation
    + Display order information and send order confirmation -User story- - Tested that order confirmation goes through as expected
    + Button to blog page - Tested that button opens blog page

+ Products 
  + All products
    + Display all products in masonry style - Tested that all products display and that masonry works if I stagger image sizes
      - For future releases I plan to use the Masonry JS tool with Bootstrap
    + Search bar for products - Tested that search bar displays products that match search or show no products if search doesn't match
    + Sort products by category links - Tested that category links sort products by category
    + Heart button to add items to wishlist if you're logged in -User story- - Tested that the heart button adds/removes items from wishlist
    + Button to product details page - Tested that button for each product opensn correct details page
  + Product details
    + Display specific product details - Tested that all product details display as expected
    + Inputs to add product quantity and choose mat card colour - Tested that a mat colour must be selected and that a non-zero quantity can be added
    + Button to add items to wishlist -User story- Tested that the button adds/removes items from wishlist
    + Buttons to add to cart or return to products page - Tested that add to cart button adds item to cart and return button goes to main products page
  + Add product -Superuser-
    + Form to add new products posts -User story- -Tested that form successfully adds new products and throws errors only if requirements aren't met
  + Edit product -Superuser-
    + Form to edit products -User story- -Tested that form successfully edits new products and throws errors only if requirements aren't met

+ Profile 
  + Profile page -User story-
    + Give logged in user option to update shipping info - Tested that shipping information can be successfully updated
    + Display all order information - Tested that all order information appears on this page and can be opened from a custom link
    + Button to Wishilist page - Tested that button opens wishlist page
  + Wishlist page -User story-
    + Display wishlist items - Tested that wishlist items are added per correct user
    + Delete item or go to product details page - Tested that delete button will remove item from wishlist and that details button opens specific product details page

+ Register/Login
  + Allauth forms to allow users to create an account or login - Tested that user can successfully create an account, receive confirmation email, and login

## Defensive design

- I've tested the validation on all site forms to make sure correct information type is inputted and required fields are met.
- I've tested that only a .png or .jpg can be added to the image field on a form.
- I've tested that an error message or warning appears if a user makes an invalid form input.
- I've tested login/sign up forms to confirm that only a session user with an account can access the Profile and Wishlist pages.
- I've tested that only superusers can access the pages to edit/delete blog posts and products. Only superusers can access Product Management and Manage Blog Post pages.
- I've tested that an error will appear if a user with incorrect permissions tries to access a gated page.

 ## Minor issues
 1. I meant to allow blog post likes to be available to all and will update in future releases.
 2. Some Bootstrap default buttons used don't have high level contrast with the background and I intend to fix this in future releases.

 ## Responsiveness

 My main aim when building a site is to design with mobile responsiveness and accessibility for older users. While developing, I regularly checked the site responsiveness on Chrome and Firefox dev tools, and built my media queries accordingly.

 To test the site responsive design further, I used [Responsive Design Checker](https://responsivedesignchecker.com/checker.php?url=https%3A%2F%2Fhorror-house-reviews.herokuapp.com%2F&width=1400&height=700). With this tool, I reviewed how my site will look on desktop screens from 10-24 inches in width. I also tested it on iPad and Kindle tablet views. The site was tested on all iPhone and Android mobile devices availble. 

 It tested well across all the sample devices.

 I regularly tested my site on desktop, my iPhoneSE2 and my Kindle Fire

 ## Browser and Os
 -  I used [Lambda test](https://www.lambdatest.com/) to test out the site on different browsers and Windows devices (I develop on a MacBook Air).

## Performance

- I've implemented SEO features--general site metadata metadata, unique page titles--on every page so that the site scores above 90% on Lighthouse's SEO rating. I'd like to add custon page titles and slugify product names in future releases.
- The site scores above 90% on all pages for accessibility for Lighthouse in Chrome. I kept the text size large on small screens, created contrast between colours, included Aria labels and tab indexes where appropriate.
- The site scores above 95% on all pages when run through https://www.webaccessibility.com/
- The site scores above 87% in Best Practices on all pages in Lighthouse when all browser extensions are disabled.

