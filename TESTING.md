# cushionhaven
 
Link to live site: [Cushion-Haven](https://cushionhaven-e17d4f9ff625.herokuapp.com/)

Link to README file [README](https://github.com/zaicodes/CushionHaven)

## CONTENTS

- [Validation Testing](#Validation-Testing)
  - [HTML](#HTML)
  - [CSS](#CSS)
  - [JavaScript](#JavaScript)
  - [Python](#Python)

- [Lighthouse](#Lighthouse)
- [Responsiveness Testing](#Responsiveness-Testing)

- [Manual Testing](#Manual_Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Full Testing](#Full_Testing)

- [Bugs](#Bugs)
  - [Solved Bugs](#Solved-Bugs)
  - [Known Bugs](#Known-Bugs)

## Validation Testing

The website underwent validation using W3C, WC3 CSS, JSHint JavaScript validator, and [CI PEP8 validator](https://pep8ci.herokuapp.com/).

### HTML

- HTML W3C Validator Regarding the HTML Validator, it flagged information messages about trailing slashes on void elements, a result of the automatically added /> close tag by Prettier. Manual removal will be addressed in the next file save to rectify this issue. 

![HTML-Validator](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/html-validator.png)

- Furthermore, there were two errors indicating a stray script tag. Upon investigation, I couldn't locate any such tag. However, upon rechecking the error, I observed that it was actually appearing in the console. I realized that the script tag is related to the Stripe public key in Python files, which cannot be altered through an HTML file.



### CSS

CSS Validator (JigSaw) The CSS Validator Jigsaw was used to validate all the CSS files. There were no errors found.

![CSS-Validator](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/css-validator.png)


### JavaScript

JSLint was used to check  for any syntax errors in the JS files, and there were couple of warnings found:
This was something I couldn't resolve, as it could break the code making the var let statements not work as expected.

![JSLint](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/jslint.png)


### Python

I had to rectify certain issues such as characters exceeding 79 and ensuring that there are two lines present between functions. Upon running the Python files through the PEP8 validator, no errors were detected.

![pep8-py](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/pep8-py.png)

## Lighthouse

Google's Lighthouse tool was used to test performance, accessibility, SEO, and PWA aspects of the site. 
The result is as follow:

![lighouse](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/lighthouse.png)

- I encountered some issues while using the Lighthouse tool to check the website. These included problems with contrast and slow-loading images. To fix this, I converted the images from PNG to WebP format and adjusted the background colour to better complement the white text. Additionally, I cleaned up redundant code in both the CSS and HTML, which improved the overall performance.

- However, there were a few unresolved issues, such as errors in the console related to core code like Stripe and certain buttons in the toast code. 

![console](https://github.com/zaicodes/CushionHaven/blob/main/documentation/testing/console-error.png)

Fixing these errors could potentially break the functionality, so I decided to leave them as is. Another challenge was enabling text compression, but I couldn't find clear instructions on how to do this after following the provided [link](https://developer.chrome.com/docs/lighthouse/performance/uses-text-compression).


## Responsiveness and Mobile-Friendliness Testing

Thorough testing was performed on the following devices:

Laptop:
- HP Envy 360

Mobile Devices:
- iPhone 13 Pro
- Samsung Galaxy S23 Ultra

In addition, the website was tested on the following browsers:
- Google Chrome
- Safari
- Firefox

All tests showed that the website is fully responsive and adaptable to different screen sizes.

## Manual Testing

### Testing User Stories

| User Story ID                	| As a/an      	| I want to be able to.....                                                        	| So that I can....                                                                           	| How is this achieved?                                                                                                                                                                                                                                                                                                                                              	|
|------------------------------	|--------------	|----------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| VIEWING &  NAVIGATION        	|              	|                                                                                  	|                                                                                             	|                                                                                                                                                                                                                                                                                                                                                                    	|
| 1                            	| SHOPPER      	| Easily Navigate the site                                                         	| Find information or products I'm looking for.                                               	| A top navbar offers users convenient access to their account, shopping bag, search bar and categories  enhancing navigation across all the pages.                                                                                                                                                                                                                  	|
| 2                            	| SHOPPER      	| View list of products and categories.                                            	| Find the items based on their type easily without having to scroll through all products.    	| Upon clicking a category in navbar, users encounter a dropdown presenting a breakdown of items within chosen category.                                                                                                                                                                                                                                             	|
| 3                            	| SHOPPER      	| Be able to identify the type of products and their ratings                       	| Get information of the products and make an informed decision before decising to purchase.  	| Users selecting a product are directed to a detailed page with essential information like item name, rating, price and description.                                                                                                                                                                                                                                	|
| 4                            	| SHOPPER      	| Easily view the total of my purchases.                                           	| be assured I don't overspend and be able to track down the total.                           	| After adding a product to the cart, users receive a toast confirming the addition, showing item detail and total value. In addition, the  shopping bag icon on the navbar updates with their total during their visit.                                                                                                                                             	|
| REGISTRATION & USER ACCOUNTS 	|              	|                                                                                  	|                                                                                             	|                                                                                                                                                                                                                                                                                                                                                                    	|
| 5                            	| SHOPPER      	| Easily be able to register and login for an account.                             	| Checkout my profile, view my purchase history and keep my account login information secure. 	| Users can register for an account via the account icon in the navbar, accessible on all site pages. During checkout, those without an account can opt to create one. Logging in and out is facilitated through the  same navbar icon.                                                                                                                              	|
| 6                            	| SHOPPER      	| Easily recover my password                                                       	| Be able to access my account in the case I forgot the  login details.                       	| If a user has forgotten their password, they can click on the forgotten password button during login to reset their password.                                                                                                                                                                                                                                      	|
| 7                            	| SHOPPER      	| Receive an email confirmation stating of successful registration.                	| Make sure my account was created successfully.                                              	| Users are sent an email requesting them to verify their email address by clicking on the enclosed link to finalise the registration process.                                                                                                                                                                                                                       	|
| SORTING & SEARCHING          	|              	|                                                                                  	|                                                                                             	|                                                                                                                                                                                                                                                                                                                                                                    	|
| 8                            	| SHOPPER      	| Easily sort categories of products                                               	| Easily identify and find products by rating, price and type.                                	| Users can filter products by price, rating or category from the navbar  and then choosing their desired option from the dropdown. Additionally, users have the option to sort and filter products directly  from the product page by clicking on the dropdown sort menu.                                                                                           	|
| 9                            	| SHOPPER      	| Be able to search for a product by name or description                           	| Easily find specific product                                                                	| A search bar in the navbar enables users to search for items, with the  search function examining both the product name and description for the entered term.                                                                                                                                                                                                      	|
| PURCHASING & CHECKOUT        	|              	|                                                                                  	|                                                                                             	|                                                                                                                                                                                                                                                                                                                                                                    	|
| 10                           	| SHOPPER      	| Easily select the quantity of a product when purchasing it.                      	| Be able to select the right quantity that I'm after.                                        	| On the product detail page, users encounter a quantity input box allowing them to adjust the desired quantity using plus or minus buttons.  These buttons are color-coded for clear visual indication of their function.                                                                                                                                           	|
| 11                           	| SHOPPER      	| View the items in my bag to be purchased.                                        	| Easily check the items I bought and their total cost.                                       	| Upon viewing their bag, users encounter a list of selected items for purchase. Information includes item image, name, quantity selected, unit price and subtotal. At the bottom, users find the subtotal for all items, delivery fee(if applicable) and the grand total of their order.                                                                            	|
| 12                           	| SHOPPER      	| Be able to adjust and update the quantity of items in my bag.                    	| Ensure I can make changes to the quantity of items before  checkout.                        	| In the bag, users can adjust item quantities using familiar selectors and update them with a click. They can also remove items entirely, receiving confirmation via a toast message.                                                                                                                                                                               	|
| 13                           	| SHOPPER      	| Easily enter my payment information                                              	| Easily checkout with no problems.                                                           	| The checkout page is divided into three sections, user details, delivery information and payment details, with feedback provided for any invalid information input.                                                                                                                                                                                                	|
| 14                           	| SHOPPER      	| Be assured that my personal and payment information are safe and secure.         	| Ensure I'm providing the required information to make a  purchase.                          	| Cushion Haven utilizes Stripe for its checkout services.                                                                                                                                                                                                                                                                                                          	|
| 15                           	| SHOPPER      	| View an order confirmation after the checkout and receive an email confirmation. 	| Ensure I have given the correct information and keep a record  of my order.                 	| During checkout, users reach an order confirmation page showing order details,  delivery address and billing information, including total and grand total.  After a successful checkout, users receive a confirmation email at the provided email address to confirm their order.                                                                                  	|
| ADMIN & STORE MANAGEMENT     	|              	|                                                                                  	|                                                                                             	|                                                                                                                                                                                                                                                                                                                                                                    	|
| 16                           	| STORE  OWNER 	| Add a product                                                                    	| Add new items to my web store.                                                              	| Admins, when logged in as superusers, can add new products to the store directly  from the website. This option is accessible under the account icon in the navbar, labelled "product management". Clicking this link directs admins to the add product page, where they can input details for a new item to be added to the store.                                	|
| 17                           	| STORE OWNER  	| Edit and update a product                                                        	| Adjust and change product details such as prices, descriptions, images etc.                 	| Superusers, upon logging in, have access to an "edit" button beneath each products  page, as well as when viewing an indivdual product. Clicking this button directs them to a page resembling the "add product" layout, ensuring continuity and  familiarity, where they can edit the product's information.                                                      	|
| 18                           	| STORE OWNER  	| Delete a product                                                                 	| Remove the items that are no longer for sale.                                               	| Superusers, upton login, see a "delete" button below each product on the products page and when viewing individual products. Clicking it triggers a modal confirming the deletion, emphasizing that this action is irreversible. They can choose to  proceed with deletion or cancel. This modal adds an extra layer of protection  against accidental deletions.  	|

### Full Testing


## Bugs

### Solved Bugs


### Known Bugs


