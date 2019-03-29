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
- Delete data currently held within the database regarding products, storage location, orders, and requisitions


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

## Differences between Product Types & Product Instances
**Product Type**
contains the meta data concerning a specific product. This includes details such as:
- Product Name
- Suppliers
- Product EROS
- Price (£)
- Lead Time Days)

*it does NOT contain information regarding the existence of a product within the laboratory*

**Product Instance**
contains information regarding the physical existence of a product within the laboratory. "Product Instance" pulls data from "Product Type", however adds extra data to link an "instance" of this product type with a laboratory team/location.
Extra data included in product Instance include:
- Associated Team
- Associated Storage Location
- Instance ID
- Date updated
- Current stock
- Minimum Stock

*n.b. Multiple "product instances" of the same "product type" can exist at any one time.*

---
## Stock Update


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

---

## Requisitions
Accessible via the Navigation Bar `/Lists/Requisitions`, this page displays a list of requisitions. This appears in a descending order using internal requisition numbers. Similar to the "Orders" page the "Requisitions" page is also ordered by the internal ID (#).
- "#"
  - Internal Requisition ID
  - Autoincrements on creation of a new Requisition
- EROS
  - Requisition EROS assigned to a requisition upon submission of orders via the EROS ordering system
  - NOT TO BE CONFUSED WITH PRODUCT EROS NUMBERS
- Requisitioned
  - Date orders held within this requisition were submitted via the EROS ordering system
- Created
  - Date Requisition was created
- Status
  - Current status of the Requisition

Colours of each row are linked to the status of the requisition
- `To Order` - Requisition created and currently available for orders to be attached
- `Sent` - Requisition has been submitted via the EROS ordering system
  - Orders can NO LONGER be added to requisitions with this Status

### Requisition - Detail (Update Requisition)
This page displays the chosen requisition in greater detail. It displays:
- Requisition internal ID
- Assigned Requisition EROS number
- Requisition Status (Coloured Text)
- Comments
- Orders assigned to the requisition
  - similar format to the Orders list page
  - please refer to `Orders` for information regarding the orders displayed here
- `Update Requisition`
  - used to update requisition with associated comments and date sent

*n.b. Associated `Product types`, `Suppliers` and `Teams` can be navigated to via clicking on the associated names within the "Orders" table*

## Orders
Accessible via the Navigation Bar ```/Lists/Orders```, this page shows a list of the most recent orders created (ordered by internal order number).

Each column defines the following:
- "#"
  - Internal order identification number
  - Auto-increments on the creation of a new order
- Flags
  - Displays flags
    - Triangle Flag - Urgent orders
    - Circular Flag - Orders with Issues
- Quantity
  - Amount of the product requested for order
- Product
  - Name of the Product on order
- EROS
  - Unique identification number provided for the item on the external EROS system (not this application)
- User
  - User who requested the order
- Team
  - Team in which this order was assigned to
- Requisition
  - Requisition in which this order is associated with
  - syntax = ```Internal_Req_Number(Requisition_EROS_number)```
- Date Requisitioned
  - Date which the associated requisition was sent for order
- Lead Time
  - estimated time until receipt of delivery
  - based upon previous experience and known times
- Status
  - Current status of the orders

The colours of each row are linked the current status of the orders themselves as to allow better visualisation
- ```BLUE```- Order Created
- ```YELLOW``` - Order Sent (Out for delivery)
- ```RED``` - Order Part Received
- ```GREEN``` - Order Completed and Received

Clicking upon the Order or Requisition number will take the user pages with greater details regarding either

*n.b. Fields for "Product" and "Team" also provide links regarding current stock for those areas*

### Orders - Detail (Update Order)
Accessed primarily via selecting the internal order ID number available on the "Orders List" Page. Similar to the previous page, this page  shows details pertaining to the order in question.

This page however shows further useful details such as "QC information" (blue), along with various useful dates to enable tracking of various stages of the order.

Orders can be updated on this page via the `Update Order` button. Selecting this option brings up the same form as that used to create the order. Further details or updates can then be added/made to the order such as:
- Updated order status
- Date Order completed
- QC information
  - Condition Received
  - Lot number
  - Expiry Date

*n.b. "associated requisition" can be accessed from this page via the `Requisition` link button.
Other products available from this supplier can also be viewed by the `Supplier` link button*

## Teams
Primarily accessible via the `/List/Teams` drop down menu option. This option brings up a list of current teams present within the application

### Team - Detail
This page displays all of the `Product Instances` which belong to the chosen team. Associated Product instances are displayed in a tabulature format. The table is organised alphabetically by product name.

Each row is colour coded according to the relationship between current/minimum stock levels.
- `RED` - Current stock is BELOW Minimum stock
- `GREEN` - Current stock is ABOVE Minimum stock

`Update Stock` please refer to the "Stock update" section of this guide

`Update Team` can be accessed from this page (Senior Laboratory Staff Access)

*n.b. `Product Types`, `Storage Location`, `ID` can be used as links to direct the user to further detail pages*

## Storage Locations
Primarily accessible via the `/List/Storage_Locations` drop down menu option. This option brings up a list of current storage locations present within the application. The list displays:
- Names of storage Locations
- Location of Storage
- Temperature range of Storage

### Storage Location - Detail
This page displays all of the `Product Instances` that are present in the chosen storage location. Associated Product instances are displayed in a tabulature format. The table is organised alphabetically by product name.

Each row is colour coded according to the relationship between current/minimum stock levels.
- `RED` - Current stock is BELOW Minimum stock
- `GREEN` - Current stock is ABOVE Minimum stock

`Update Stock` please refer to the "Stock update" section of this guide

`Update Storage Location` can be accessed from this page (Senior Laboratory Staff Access)

*n.b. `Product Types`, `Team`, `ID` can be used as links to direct the user to further detail pages*

## Product Types
This page displays a list of all "Product Types" held within the application organised alphabetically by product name. This includes various meta data surrounding the product such as:
- Suppliers (links to supplier detail page)
- Product Names
- Product EROS
- Price Per instance
- Estimated Lead Time (Days)

### Product Types - Detail
This page displays the product type meta data mentioned above, along with all of the instances of this product type. This is organised into a tabulature format and ordered alphabetically according to associated teams.

Each row is colour coded according to the relationship between current/minimum stock levels.
- `RED` - Current stock is BELOW Minimum stock
- `GREEN` - Current stock is ABOVE Minimum stock

`Update Stock` please refer to the "Stock update" section of this guide

`Update Product Type` can be accessed from this page (Senior Laboratory Staff Access)

*n.b. `Team`, `Storage Location`, `ID` can be used as links to direct the user to further detail pages*
