# cushionhaven
 
Cushion Haven is an eCommerce store crafted with a blend of HTML, CSS, JavaScript, Python (Django), Bootstrap, jQuery, and PostgreSQL database technologies. Features include a user-friendly checkout process, an add-to-cart functionality, and convenient sorting and search features, allowing customers to easily find their desired products.The navbar features intuitive categories for effortless navigation, while the product detail page provides information about each item, ensuring a satisfying shopping experience from start to finish.

![am-i-responsive](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/am-i-responsive.png)


Link to live site: [Cushion-Haven](https://cushionhaven-e17d4f9ff625.herokuapp.com/)

## CONTENTS

- [User Experience](#User-Experience-ux)
  - [Project Goal](#Project-Goal)
  - [User Stories](#user-Stories)

- [Design](#design)
  - [Colour Scheme](#Colour-Scheme)
  - [Typography](#Typography)
  - [Imagery](#Imagery)
  - [Data Model](#Data-Model)
  - [Security](#Security)

- [Features](#Features)
  - [General features](#General-Features)
  - [Accessibility](#Accessibility)
  - [Responsiveness](#Responsiveness)
  - [Future Implementations](#Future-Implementations)

- [Technologies used](#Technologies-Used)
  - [Languages used](#Languages-Used)
  - [Frameworks/Tools Used](#frameworkstools-used)
  - [Libraries Used](#libraries-used)
  - [Stripe](#stripe)

- [Testing](#Testing)

- [Deployment](#Deployment)

- [Credits](#Credits)
  - [Code Used](#Code-used)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgments](#Acknowledgments)

 -----

## User Experience (UX)

### Project Goal

Cushion Haven is a Business to Consumer (B2C) e-commerce platform tailored for individuals passionate about interior decoration and home styling. Its primary audience comprises homeowners, interior enthusiasts, and decorators, ranging from novices to seasoned professionals. It offers a diverse selection of cushions, pillows, and blankets across various price ranges, catering to different preferences and budgets. Cushion Haven aims to provide customers with a one-stop destination for all their home decor needs, simplifying the process of finding the perfect accents for their living spaces. Understanding the demand for a platform like this within the community, it strives to meet the needs of home decor enthusiasts.

### User Stories

| User Story ID                	| As a/an      	| I want to be able to.....                                                        	| So that I can....                                                                           	|
|------------------------------	|--------------	|----------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------	|
| VIEWING &  NAVIGATION        	|              	|                                                                                  	|                                                                                             	|
| 1                            	| SHOPPER      	| Easily Navigate the site                                                         	| Find information or products I'm looking for.                                               	|
| 2                            	| SHOPPER      	| View list of products and categories.                                            	| Find the items based on their type easily without having to scroll through all products.    	|
| 3                            	| SHOPPER      	| Be able to identify the type of products and their ratings                       	| Get information of the products and make an informed decision before decising to purchase.  	|
| 4                            	| SHOPPER      	| Easily view the total of my purchases.                                           	| be assured I don't overspend and be able to track down the total.                           	|
| REGISTRATION & USER ACCOUNTS 	|              	|                                                                                  	|                                                                                             	|
| 5                            	| SHOPPER      	| Easily be able to register and login for an account.                             	| Checkout my profile, view my purchase history and keep my account login information secure. 	|
| 6                            	| SHOPPER      	| Easily recover my password                                                       	| Be able to access my account in the case I forgot the  login details.                       	|
| 7                            	| SHOPPER      	| Receive an email confirmation stating of successful registration.                	| Make sure my account was created successfully.                                              	|
| SORTING & SEARCHING          	|              	|                                                                                  	|                                                                                             	|
| 8                            	| SHOPPER      	| Easily sort categories of products                                               	| Easily identify and find products by rating, price and type.                                	|
| 9                            	| SHOPPER      	| Be able to search for a product by name or description                           	| Easily find specific product                                                                	|
| PURCHASING & CHECKOUT        	|              	|                                                                                  	|                                                                                             	|
| 10                           	| SHOPPER      	| Easily select the quantity of a product when purchasing it.                      	| Be able to select the right quantity that I'm after.                                        	|
| 11                           	| SHOPPER      	| View the items in my bag to be purchased.                                        	| Easily check the items I bought and their total cost.                                       	|
| 12                           	| SHOPPER      	| Be able to adjust and update the quantity of items in my bag.                    	| Ensure I can make changes to the quantity of items before  checkout.                        	|
| 13                           	| SHOPPER      	| Easily enter my payment information                                              	| Easily checkout with no problems.                                                           	|
| 14                           	| SHOPPER      	| Be assured that my personal and payment information are safe and secure.         	| Ensure I'm providing the required information to make a  purchase.                          	|
| 15                           	| SHOPPER      	| View an order confirmation after the checkout and receive an email confirmation. 	| Ensure I have given the correct information and keep a record  of my order.                 	|
| ADMIN & STORE MANAGEMENT     	|              	|                                                                                  	|                                                                                             	|
| 16                           	| STORE  OWNER 	| Add a product                                                                    	| Add new items to my web store.                                                              	|
| 17                           	| STORE OWNER  	| Edit and update a product                                                        	| Adjust and change product details such as prices, descriptions, images etc.                 	|
| 18                           	| STORE OWNER  	| Delete a product                                                                 	| Remove the items that are no longer for sale.                                               	|


## Design

### Colour Scheme

![colour-scheme](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/colour-scheme.png)

This color scheme combines soft and muted tones (lavender and plum) with a bold accent color (dark cyan) and neutral tones (white and black). The overall effect is a balance of elegance, sophistication, and stability, with a touch of creativity and mystery.

### Typography

The fonts used for this project are: Lobster, Cormorant Garamond and Roboto.

Lobster: Lobster is a script typeface known for its elegant and flowing cursive style. It exudes a sense of sophistication and was used for decorative purposes for the logo.

Cormorant Garamond: Cormorant Garamond is a classic serif typeface inspired by the timeless elegance of traditional Garamond fonts. It offers a balance of refinement and readability, making it suitable for body text and headings alike.

Roboto: Roboto is a modern sans-serif typeface designed for digital interfaces. Its clean and versatile appearance, along with excellent legibility, makes it a popular choice for web and mobile applications, as well as for body text on websites.

### Imagery

All website images are generated using Midjourney, focusing on products and color schemes against a white background to enhance the vibrancy of colours.The icons are from Font Awesome.

### Wireframes

For wireframes, please refer to the documentation [wireframes](https://github.com/zaicodes/CushionHaven/tree/main/documentation/wireframes)

### Data Model

![models](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/models.png)

The following data models were used:

- Orders: Stores details about users' orders.
- Order Line Items: Manages information about items in the user's shopping basket.
- Products: Contains information about the products available on the site.
- Users: Used for user registration purposes.
- comment box: Stores comments submitted through the comment box in product detail page.
- Profiles: Enables users to access their order history and update default delivery information.
- Address: Stores information about user addresses in address book during the checkout. This model enables users to save multiple addresses for their history which they can edit and delete.

These tables establish relationships between entities such as products, users, orders, and addresses, allowing for efficient storage and retrieval of data. Additionally, foreign key constraints ensure data integrity and consistency within the database.

I have also used the snowflake icon to show fields that are a foreign key.

Overall, these tables form a relational database schema that allows Cushion Haven to efficiently manage product inventory, user information, orders, and other essential data for its e-commerce platform.


### Security

Various security measures were implemented for this project:

- Use of .env file: Sensitive credentials like DATABASE_URL, SECRET_KEY, STRIPE keys, AWS ACCESS KEYS, and GMAIL passwords are stored in a .env file, which is then added to .gitignore to keep it secure. 

- Defensive Programming: The site includes measures to prevent unauthorized actions by users. For instance, only superusers can access the product admin panel. Users must be authenticated to access the profile page and cannot add reviews without authorization.

- Feedback to Users: Toast messages provide instant feedback to users about their actions, such as successful login or reasons for authentication failure.

## Features

### General Features

- Favicon: Created using Favicon.io, the site's favicon bears the initials of Cushion Haven, mirroring the font and colors of the website.

- Navbar: The navbar is divided into sections for easy navigation. It includes the logo and search bar, website pages, and account and bag icons. It is responsive, featuring a hamburger menu toggle on smaller screens.


![navbar](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/navbar.png)


![navbar](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/navbar-small.png)


- Footer: Also split into sections, the footer includes the logo, website pages, and social links. It is responsive and stacks sections on small screens.


![footer](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/footer.png)


- Home Page: The home page features a hero section with an image, message, and call-to-action button. It also includes an About section with three parts, each providing information about the designer, collection, and products. Additionally, there's a Contact Us section with contact information and a form.


![hero-section](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/hero-section.png)


![about-section](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/about-section.png)


![about-designer](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/about-designer.png)


![about-products](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/about-products.png)


![about-categories](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/about-categories.png)


![contact-form](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/contact-form.png)


![costumer-service](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/costumer-service.png)


- Products Page: Displays product images, names, prices, tags, and star ratings. Superusers have the option to update or delete products. It includes a sorting function and shows the number of items on the page.


![products](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/products.png)



- Product Detail Page: Provides detailed information about a selected item, including an image, title, price, description, tags, and quantity selector. Users can add items to their bag and receive a success toast notification. This page also includes comment box where users can leave a comment under the product.


![product-detail](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/product-detail.png)


![comment-box](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/comment-box.png)



- Bag Page: Lists all items in the user's bag with images, names, SKUs, prices, quantities, and subtotals. Users can adjust quantities or delete items. It displays bag totals and offers a secure checkout option.

![bag](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/bag.png)



- Checkout Page: Divided into delivery and order summary sections. Users can enter delivery information, with pre-populated details for registered users. It includes payment information and buttons for adjusting the bag or completing the order. Additionally, it contains address book where the user's different addresses will be saved. This is editable and can be deleted too.

![checkout](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/checkout.png)



- Checkout Success Page: Displays a summary of the order and notifies users of a confirmation email. It also includes a button to view latest deals and shows a success toast.


![checkout-success](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/checkout-success.png)



- Profile Page: Contains sections for default delivery information and order history. Users can update their inf

![profile](https://github.com/zaicodes/CushionHaven/blob/main/documentation/readme/profile.png)



### Accessibility

I've been careful while coding to make sure the website is accessible-friendly. Here's how I've achieved that:

- I've used semantic HTML.
- I've included descriptive alt attributes on images.
- I've made sure there's enough contrast between colours across the site (details on colour choices can be found in the color scheme section).

### Responsiveness

The website's responsiveness across diverse screen sizes and browsers is achieved through the utilization of media queries and Bootstrap. These tools enable seamless adaptation of layout and functionality, ensuring a consistent and user-friendly experience across different devices and browsing environments.

### Future Implementations

In future implementations, I would like to:

- Add user reviews for products with a rating facility.
- Introduce coupons which can be accepted in the checkout.
- Create a fully functioning stock management system that updates the stock value upon insertion to the bag and returns the value to the stock if the bag session ends.
- Introduce wish list functionality for users to add and remove products from their wish list, this is something I was planning to implement before but due to running out of time, I wasn't able to.
- Send newsletters to users.
- Create groups of users on the admin page to enable sending out specific emails, such as birthday coupons or loyal customer coupons. This section could also be used to create different mailing groups for newsletters depending on users' preferences.


## Technologies Used

### Languages Used

- HTML5: is utilized for crafting the markup for the website content. 
- CSS: is used for styling the individual pages. 
- JavaScript: is used to toggle the visibility of specific aspects of the site 
- Python: powers the application's functionality.

### Frameworks/Tools Used

- Bootstrap: is used to build completely responsive mobile-first websites.
- JQuery: is a JavaScript library that makes it easier to work with HTML elements, handle events, create animations, and perform AJAX requests on web pages. 
- Font Awesome: it's used to add icons to the site. We got it by linking to a CDN.
- Django Allauth: it's used for authentication, registering, and managing accounts on the site.
- Visual Studio Code: to code my project.
- Midjourney: is an artificial intelligence program that was used for creating the images using prompts.
- Balsamiq: it's used to create wireframes.
- Favicon.io: it's used to create the tab icons for the website.
- Git: it's used for version control.
- GitHub: it's where the codebase is hosted.
- Google Dev Tools: it's used to test features, and responsiveness and to troubleshoot.
- Google fonts: to get typography with free, customizable fonts.
- Heroku: it's used as our hosting platform.
- PostgreSQL: it's used as our hosting platform’s database. 
- Am I Responsive: to create responsive images of the website on variety of different device sizes.
- cloudconvert: to convert images from png or jpg to webp.
- img2go.com : to resize images to any size.
- Coolors: to generate the colour palette used for the website. 


### Libraries Used

- Django Allauth: Utilized for authentication, registration, and account management.
- Django-countries: library that provides a comprehensive list of world countries and their associated data, such as country codes, names, and flags.
- Django_crispy_forms: Provides a tag and filter for rendering forms quickly.
- Gunicorn: A Python WSGI HTTP Server.
- Pillow: Python imaging library.
- dj_database_url: Enables the utilization of the DATABASE_URL variable.
- psycopg2: Postgres database adapter facilitating connection with a postgres database.
- django-storages: A storage backend library.


### Stripe

[Stripe](https://stripe.com/gb) is utilized in the project to integrate the payment system.

Currently, Stripe for the website is in developer mode, enabling us to process test payments and ensure the site's functionality.


## Testing 
Please consult the [TESTING.md](https://github.com/zaicodes/CushionHaven/blob/main/TESTING.md) document for a comprehensive overview of all conducted tests.

## Deployment 

To deploy the application using Heroku, follow these steps:
- Create a requirements.txt file.
- Generate a Procfile by running the command echo web: python app.py > Procfile, ensuring it starts with a capital P.
- Log in to Heroku or create an account if needed.
- Click the 'New' button and select 'Create new app'.
- Provide a unique name for your project without capital letters or spaces, and choose your region. Click 'Create App'.
- Navigate to the Resources tab within your project and create a Heroku Postgres Database.
- Go to the 'Settings' tab in your project. Scroll down and click 'Reveal Config Vars'.
- Add the following variables:
-- SECRET_KEY: Your secret key
-- DATABASE_URL: Your PostgreSQL database URL
-- STRIPE_PUBLIC_KEY: Your Stripe public key
-- STRIPE_SECRET_KEY: Your Stripe secret key
-- USE_AWS: Set to 'True'
-- AWS_ACCESS_KEY_ID: Add your AWS access key ID
-- AWS_SECRET_ACCESS_KEY: Add your AWS secret access key
-- GMAIL_PASSWORD: Add the Gmail password from the selected account for email confirmation.
- Deploy your project by going to the Deploy tab and selecting 'Connect to GitHub'.
- Find your repository name and connect it.
-	Create a new repository on GitHub.
-	Add the necessary files to the repository.
-	Go to the settings page of the repository, then scroll down to the GitHub Pages section located at the bottom of the 'Code and automation' sub-section.
-	Select the main branch and the root folder, then click save.
-	The website will now be live at the URL provided in the GitHub Pages section.

How to clone the repository

Go to the [Cushion-Haven](https://github.com/zaicodes/CushionHaven) repository on GitHub.
Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
Open a GitBash terminal and navigate to the directory where you want to locate the clone.
On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.

How to Fork the repository

Go to the [Cushion-Haven](https://github.com/zaicodes/CushionHaven) repository on GitHub.
Click on the 'Fork' option towards the top left of the page.
Click the dropdown button and click 'create a new fork'.
This will bring up a page with details of the repository, fill in boxes as required.
Click 'create fork'.

## Credits

### Code Used

The project code is sourced from the following:

- Code Institute's Boutique Ado walkthrough project
- Django documentation
- Stripe Documentation

### Content

I authored the content of the website, drawing inspiration from the design of this particular website [here](https://mariela.webflow.io/)

### Media
All the images have been generated using Midjourney's prompts, refer to Imagery above for more details.

### Acknowledgments

I want to give a big thanks to those who helped me a lot with my project:

Narender S. - my mentor, who checked on my progress and gave me useful feedback.

Jessica I. - for the weekly stand-up meetings that were really helpful and informative.