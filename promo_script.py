import Promo_Class

#order_num1 = Promo_Class.Order()
#order_num2 = Promo_Class.Order()

product_1 = Promo_Class.Product
print product_1

# our inventory is a reflection of the combined total of our suppliers
# our product selection is a combination of all our suppliers product selection
""" the_tee_shirt_bakery = Distributor()

sanmar = Supplier()
bodek = Supplier()

john = Customer(budget, purpose = event, product)
dave = Customer()

product = (name, supplier, [supplier_sku], [supplier_inventory], distributor_sku, quantity, artwork)

order = (product, customer, shipping_details, decorator, [supplier], [quantity])

print order_details
print customer

"""

"""

Order Details
------------------
Order # 0000001
Status: In Progress
In Hands Date: 1/2/2015
Description: Staff Shirts                       <-------- customer input
Customer: John Doe
Product: Gildan 5000

Total Quantity: 500

Sanmar Quantity: 300                 <-------- based on pricing and inventory
    S       M       L       XL      XXL
    $4.50   $4.50   $4.50   $4.50   $7.50
    50      100     100     50      0

Bodek Quantity: 200
    S       M       L       XL      XXL
    $4.60   $4.60   $4.60   $4.60   $7.60
    25      50      50      75      0

Contractor Pricing
    setup: $120 (4 * $30)
    print: $2000 (500 qty * $4.00)
    ------------------------------
    total: $2120

Order Margin: 40%
    Product Margin: 50%
    Print Margin: 20%
    Setup Margin: 0%


Artwork File: capital_one.jpg

"""

"""
Orders Overview
---------------
In progress     Order #0000001    Capital One           Staff Shirts
In progress     Order #0000002    Capital One           Staff Sweatshirts
Waiting         Order #0000003    Capital One           Promo Pens
Complete        Order #0000004    All Service Movers    Staff Sweatshirts
Complete        Order #0000005    All Service Movers    Promo Hats

"""


