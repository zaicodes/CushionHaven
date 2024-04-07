# cushionhaven
 
Cushion Haven is an eCommerce store crafted with a blend of HTML, CSS, JavaScript, Python (Django), Bootstrap, jQuery, and PostgreSQL database technologies. Features include a user-friendly checkout process, an add-to-cart functionality, and convenient sorting and search features, allowing customers to easily find their desired products.The navbar features intuitive categories for effortless navigation, while the product detail page provides information about each item, ensuring a satisfying shopping experience from start to finish.

![am-i-responsive](https://github.com/)

Link to live site: []()

## CONTENTS

- [User Experience](#User-Experience-ux)
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

- [Testing](#Testing)

- [Deployment](#Deployment)

- [Credits](#Credits)
  - [Code Used](#Code-used)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgments](#Acknowledgments)

 -----

## User Experience (UX)

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

![colour-scheme]()

This color scheme combines soft and muted tones (lavender and plum) with a bold accent color (dark cyan) and neutral tones (white and black). The overall effect is a balance of elegance, sophistication, and stability, with a touch of creativity and mystery.

### Typography

The fonts used for this project are: Lobster, Cormorant Garamond and Roboto.

Lobster: Lobster is a script typeface known for its elegant and flowing cursive style. It exudes a sense of sophistication and was used for decorative purposes for the logo.

Cormorant Garamond: Cormorant Garamond is a classic serif typeface inspired by the timeless elegance of traditional Garamond fonts. It offers a balance of refinement and readability, making it suitable for body text and headings alike.

Roboto: Roboto is a modern sans-serif typeface designed for digital interfaces. Its clean and versatile appearance, along with excellent legibility, makes it a popular choice for web and mobile applications, as well as for body text on websites.

### Imagery

All website images are generated using Midjourney, focusing on products and color schemes against a white background to enhance the vibrancy of colours.The icons are from Font Awesome.

### Wireframes

### Data Model

### Security

Various security measures were implemented for this project:

- Use of .env file: Sensitive credentials like DATABASE_URL, SECRET_KEY, STRIPE keys, AWS ACCESS KEYS, and GMAIL passwords are stored in a .env file, which is then added to .gitignore to keep it secure. 

- Defensive Programming: The site includes measures to prevent unauthorized actions by users. For instance, only superusers can access the product admin panel. Users must be authenticated to access the profile page and cannot add reviews without authorization.

- Feedback to Users: Toast messages provide instant feedback to users about their actions, such as successful login or reasons for authentication failure.

## Features

### General Features



### Accessibility

I've been careful while coding to make sure the website is accessible-friendly. Here's how I've achieved that:

- I've used semantic HTML.
- I've included descriptive alt attributes on images.
- Information is provided for screen readers where icons are used without text.
- I've made sure there's enough contrast between colours across the site (details on colour choices can be found in the color scheme section).

### Responsiveness

The website's responsiveness across diverse screen sizes and browsers is achieved through the utilization of media queries and Bootstrap. These tools enable seamless adaptation of layout and functionality, ensuring a consistent and user-friendly experience across different devices and browsing environments.

### Future Implementations

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
- Midjourney: is an artificial intelligence program that was used for creating the images using prompts.
- Balsamiq: it's used to create wireframes.
- Favicon.io: it's used to create the favicon.
- Git: it's used for version control.
- GitHub: it's where the codebase is hosted.
- Heroku: it's used as our hosting platform.
- PostgreSQL: it's used as our hosting platform’s database. 
- Am I Responsive: to create responsive images of the website on variety of different device sizes.
- Coolors: to generate the colour palette used for the website. 


## Testing 
Please consult the [TESTING.md](https://github.com/zaicodes/CushionHaven/blob/main/TESTING.md) document for a comprehensive overview of all conducted tests.

## Deployment 


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