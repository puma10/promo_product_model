

"""
FEATURE WISHLIST

    * Creative Position - Coupling Industrial Design/Merchendiser with Graphic Designer for extremely original products. ** Differentiator
    * Creative Position - Product Research Team <--- love to shop ** Differentiator
    * Can auto calculate best place to source product from depening on the supplier pricing and promotions.

        ----------------- GENERAL CLASSES ---------------
      # This are not linear in the process
#v1
Product
    Size
    Quantity
    Color
    Other Variables
    Weight
    Dimensions

Product_Category
    Tag
    Material
    Event
    Purpose

Supply_Chain
    Vendor
        Decorator
        Supplier
        Manufacturer
    Broker
    Customer

Relationships
    # <-> means two way

    Broker <-> Customer
    Vendor <-> Broker
    Vendor -> Customer


------------------------------------------------------------
CRM
    Marketing
        SEO
        Email Drip - Lead warming
        Social Media
        Content Writing

    Inbound Sales
        Tele-services

    #v1
    Presentation
            Quote
                Mockup
                Pricing
                    adjustable <- module so they can change numbers
                        price_breaks

            Order_Logistics
                single vendor <-- everything done in one place
                    Shipping_Quote
                multi-vendor <-- multiple vendors and decorators
                    Shipping_Quote

            Order_Changes

------------------------------------------------------------
#v1
Pre-Production
    Order Details
        In Hands Date

    Sale
        Invoice/Receipt
            Credit Card Payment
            ACH Payment

------------------------------------------------------------
#v1
Order_Management

    #v1
    #we take the order before we check the supplier inventory
    #until we can get live inventory from supplier API's
    Check Supplier Inventory
        If supplier doesn't have inventory -> supplier B,C,D
        elif - when will there be inventory -> ask customer to delay order
            customer can't delay
                do refund
            customer can delay
                change Order_Dates

    Procure Product
        Intiate API Call
        Elif Initiat Email Order
        Else Initate Phone Call

    #v1
    Ship
        Location Starting
        Location Ending
        Carrier

        Ship_to_Final_Vendor    <- Sub Class
        Ship_to_Customer        <- Sub Class
        Shipping_Quote          <- Sub Class
            = Ship_to_Final_Vendor.cost + Ship_to_Customer.cost

    #v1
    Order_Check <- Can create a GUI
        Check_Order_Recieved
            - get_production_date #via automated email
            - get_ship_date
        Check_Pre_Production
        Check_In_Production
        Check_Finished_Production
        Check_Ship_Date <-- will ship on time?
        Check_Shipped

        Vendor recieve product
            confirmation
"""


class Artwork
    #type_of_artwork
    #of colors
    #cost of design
        #cost of conversion
            #vector
            #digitize
        #cost of creative design


class Product
    #Name
    #Type
    #Model
    #Price
    #Color
    #cost of good

#Inherits from the product class

class ProductCategory
    #type
    #weight
    #price break - an array, 2d [at what quantity break occurs, price at that quantity]
    #SKU
    #name
    #cost
    #suppliers (array)

class Order
    #product
    #artwork
    rec=0
    def autoIncrement():
         global rec
         pStart = 1
         pInterval = 1
         if (rec == 0):
          rec = pStart
         else:
          rec += pInterval
         return rec

class Company
    #Name


#Inherits from the company class
class Supplier
    #takes in a list of prouct product array

    #def add_product_to_inventory()


#Inherits from the company class
class Distibutor


class Customer
    #Name
    #Budget


class Order
    #artwork cost
    #artwork margin
    #artwork profit

class Shipping




