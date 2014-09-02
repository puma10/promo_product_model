
"""
class Order(object):

    products_in_order = {}

    def __init__(self, name, customer):
        # a unie order ID
        # ***I wanted this to autoincrement by 1 but couldn't figure out how to do so.
        self.order_id = id(self)
        #a short description of the order
        self.name = name
        #set the status of the order -> can be updated later
        self.order_status = "new"
        #identify the customer
        self.customer = customer


    def add_item(self, product_ID):
        # add this
        #Quantity = {S : 20, M : 40, L : 60, XL: 80}
        if not product_ID in self.products_in_order
            self.products_in_order[product_ID] = price
            print product + " added."
        else:
            print product + " is already in the cart."



    def remove_item(self, productID):

    def ship(self,inhand_date):
        self.inhand_date = inhand_date



    #product
    #artwork
"""

class Product(object):

    def __init__():

    #weight is in grams
    #dimensions in inches - L = length, W = width, H = height


        product_name = raw_input("What is the name of this product : ")

        colors = raw_input("What color options does this product come in? Comma seperate all options : ")

        sizes = raw_input("What sizes does this come in? Comma seperate all sizes : ")

        weight = raw_input ("how much does this product weigh in grams(for shipping) : ")

        length = raw_input ("What is the length of this product (for shipping) : ")

        width = raw_input ("What is the width of this product (for shipping) : ")

        height = raw_input ("What is the height of this product (for shipping) : ")

        sku = id(self)

        return "hello"

        """self.product = {product_name : {"sku" : sku, "colors" : colors, "weight" : weight, "sizes" : sizes, "length" : length, "width" : width, "height" : height}}"""

  #  def print_product_list():
   #     pass

'''
#Should print this
    name: Gildan 5000
    sku: 23515
    Sizes: S, M, L, XL
    Color: Blue, Green, Red
    Weight: 2.4 oz
    Dimensions: Length = 10", Width = 12", Height = 14"
'''









"""def autoincrement_order(self):
         global rec
         pStart = 1
         pInterval = 1
         if (rec == 0):
          rec = pStart
         else:
          rec += pInterval
         return rec"""



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


#------------------------------------------------------------------------

"""

class Artwork:
    pass
    #type_of_artwork
    #of colors
    #cost of design
        #cost of conversion
            #vector
            #digitize
        #cost of creative design


class Product:
    pass
    #Name
    #Type
    #Model
    #Price
    #Color
    #cost of good

#Inherits from the product class

class ProductCategory:
    pass
    #type
    #weight
    #price break - an array, 2d [at what quantity break occurs, price at that quantity]
    #SKU
    #name
    #cost
    #suppliers (array)

class Company:
    pass
    #Name


#Inherits from the company class
class Supplier:
    pass
    #takes in a list of prouct product array

    #def add_product_to_inventory()


#Inherits from the company class
class Distibutor:
    pass


class Customer:
    pass
    #Name
    #Budget


class Order:
    pass
    #artwork cost
    #artwork margin
    #artwork profit

class Shipping:
    pass



"""
