# EROS POD (Product Ordering Database)

A Django application developed to manage and keep track of current stock, product orders,  and requisitions at Bristol Genetics Laboratory. This was developed as part of the Clinical Scientist (Bioinformatics Genomics) HCPC Registration portfolio, module "Computing for Clinical Scientists (SBI101)"

## Author
- **Andrew Smith**

Development start date: 1st February 2019

Available at: https://github.com/Fyodir/POD

## Prerequisites
- Python (3.6.x)
- Modules
  - Django (2.1.5)


## User Administration
Before a prospective user can interact with the POD system they will require an authorised account to access any other page apart from the application home page. Therefore users must first be created before data can be be entered or viewed through the HTML browser.

### User creation
Staff must contact an individual with administrator rights to the POD system. This will typically be the developer or the one responsible for maintenance of the system.

### Forgotten Passwords
If a user has forgotten their password to the system they must contact the individual with administrator rights. The administrator will then be able to reset the password of the user in question

>*n.b. currently no function exists to email the user with a link to reset their password*


## Access Privileges
### Laboratory Staff
The standard user will possess this level of activity. This access level allows users to do the following:
- View all Lists
- Update Product Stock Levels
- Create/Update Product Instance
- Create an Order
- Create Requisition
- Update Orders
- Update Requisitions

General Laboratory Staff CANNOT:
- Delete ANYTHING from  the database
- Update
  - Product Type
  - Supplier
  - Storage Locations
  - Temperature ranges
  - Team Names

### Senior Laboratory Staff
More senior levels of staff will possess further access to that given to general laboratory staff. In general staff with this level possess the ability to:
- View all Lists
- Create any of the entries available under the ```New``` navigation bar drop down
- Update any of the data currently held within the database regarding products, storage location, orders, and requisitions
- Delete any of the data currently held within the database regarding products, storage location, orders, and requisitions


## Navigation Bar
All users are required to login to their account via the ```Login``` button before they unlock access to navigate the EROS POD system.

- POD/Home icon
  - Redirects the user back to the ```Home Page```
- Create Order
  - Allows users to create orders for a given Product
  - A Requisition (with status "To Order") must exist prior to order creation
- Create Requisition
  - Allows users to create requisitions for orders to be added to
- List
  - Reveals a variation of lists in which data held within POD such as current stock, orders, product and supplier details can be visualised under different filters
- New
  - Allows for the creation of new database entries
  - General Laboratory staff will possess limited access to this section
- Login/Logout{User}


## Home page
This page is set up to display a collection of potentially useful information for the user. Among containing the title and application description a number of useful statistics are displayed.

These statistics include general numbers of Products and Suppliers contained within the application, and numbers to highlight orders at key stages of requisition or any that contain certain flags.

Counters for "Order Statistics" are designed to display colours to highlight the presence of orders within these counters

- ```BLUE``` - "Unsent Requisitions" and "Created Orders"
  - Number of orders/Requisitions that have been created but not yet submitted on the EROS ordering system
- ```YELLOW``` - "Awaiting Orders"
  - Number of orders that are submitted and out for order
- ```RED``` - "Part-Received Orders" and "Order Issues"
  - Number of orders that have either been part-received or currently have issues pertaining them (more detail can be found on specific order page)


**Note**
"Order Statistics" counters show ```BLACK``` if their counts are ZERO


## Create Requisition
A requisition is used to group together multiple orders. A Requisition with a current status of "To Order" is required to create orders. Once Requisition status is changed to "Sent", orders can no longer be attached to the requisition.

To Create a Requisition please follow these steps:
1. Click ```Create Requisition```
2. None of the fields are mandatory to complete on creation of a Requisition
  1. Requisition status (Default = To Order")
3. Click ```Submit```

*n.b. Once the requisition has been sent via the EROS ordering system a user is required to fill in these fields via the ```Update Requisition``` button (See Requisitions)*


## Create Order
It must be reminded that a ```Requisition``` with a status of "To Order" must be present before a new order can be made. If this is not the case, please refer to ```Create Requisition``` before carrying on with this section. This is because ONLY requisitions with a status of "To Order" will be displayed to add an order to on the ```Create Order``` screen. Requisitions that have been sent can no longer be added to.

To Create an order please follow these steps:
1. Click ```Create Order```
2. Complete the Required Fields
  1. Team
  2. Requisition ID
  3. Product Type
  4. Quantity
  5. Urgency (Default = Non-Urgent)
3. Complete Optional fields if Required
  1. Order Issue (Default = No)
  2. Order Status (Default = Created)
  3. Comments
4. Check entered fields are correct
5. Click ```Submit```

*n.b. the remaining fields on the Create Order page are completed upon receipt of the order*


## Orders
Accessible via the Navigation Bar ```/Lists/Orders```, this page shows a list of the most recent orders created (ordered by internal order number).

Each column defines the following:
- #
  - Internal Order identification number
  - auto-increments on the creation of a new order
- Flags
  - displays given Flags
  -   <i class="fab fa-rebel"></i>
- Quantity
- Product
- EROS
- User
- Team
- Requisition
- Date Requisitioned
- Lead Time
- Status
