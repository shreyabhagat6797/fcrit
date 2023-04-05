'''
Freight cargo >>>>>>oops A3
'''

class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        id=str(self.__customer_id)
        if(id[0]=='1' and len(id)==6):
            return True
        else:
            return False

class Freight:
    counter=198
    def __init__(self,receipent_customer,from_customer,weight,distance):
        self.__receipent_customer=receipent_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__frieght_id=0
        self.__freight_charge=0

    def validate_weight(self):
        if self.__weight%5==0:
            return True
        else:
            return False

    def validate_distance(self):
        if self.__distance>=500 and self.__distance<=5000:
            return True
        else:
            return False

    def forward_cargo(self):
        if self.validate_distance() and self.validate_weight() and Customer.validate_customer_id(self.__from_customer) and Customer.validate_customer_id(self.__receipent_customer):
            self.__frieght_id=Freight.counter+2
            Freight.counter+=2
            self.__freight_charge=(self.__weight*150)+(self.__distance*60)
            return self.__frieght_id and self.__freight_charge
        else:
            self.__freight_charge=0

    def get_receipent_customer(self):
        return self.__receipent_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_freight_id(self):
        return self.__frieght_id

    def get_freight_charge(self):
        return self.__freight_charge

c1=Customer(123456,"ABC","CHennai")
c2=Customer(112233,"XYZ","Mumbai")
f=Freight(c1,c2,15,506)
print(f.forward_cargo())
print(f.get_freight_id())


'''
Apparel oop A4
'''

class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__item_type=item_type
        self.__price=price
        self.__item_id=item_type[0].upper()+str(Apparel.counter+1)
        Apparel.counter+=1

    def set_price(self,price):
        self.__price=price

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def get_item_id(self):
        return self.__item_id

    def calculate_price(self):
        self.__price*=1.05

class Cotton(Apparel):
    def __init__(self,price,discount):
        self.__discount=discount
        Apparel.__init__(self,price,"Cotton")  #invoking parent constructor

    def get_discount(self):
        return self.__discount

    def calculate_price(self):
        Apparel.calculate_price(self)
        price=Apparel.get_price(self)
        price*=(1-((self.__discount)/100))
        price*=1.05
        Apparel.set_price(self,price)
        return price

class Silk(Apparel):
    def __init__(self,price):
        self.__points=0
        Apparel.__init__(self,price,"Silk")

    def get_points(self):
        return self.__points

    def calculate_price(self):
        Apparel.calculate_price(self)
        price=Apparel.get_price(self)
        if price>10000:
            self.__points+=10
        else:
            self.__points+=3
        price*=1.10
        Apparel.set_price(self,price)
        return price
        
c=Cotton(1320,35)
s=Silk(1320)
print(c.calculate_price())
print(s.calculate_price())
print(s.get_points())

'''
Coorg fruit farm oop A4
'''

class FruitInfo:
    fruit_name_list=["Apple","Guava","Orange","Grape","SweetLime"]
    fruit_price_list=[200,80,70,110,60]

    def get_fruit_price_list():
        return FruitInfo.fruit_price_list

    def get_fruit_name_list():
        return FruitInfo.fruit_name_list

    def get_fruit_price(fruit_name):
        if fruit_name.title() in FruitInfo.fruit_name_list:
            return FruitInfo.fruit_price_list[FruitInfo.fruit_name_list.index(fruit_name.title())]

class Purchase:
    counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

    def calculate_price(self):
        each_fruit_price=FruitInfo.get_fruit_price(self.__fruit_name)
        if each_fruit_price>0:
            self.__purchase_id='P'+str(Purchase.counter)
            Purchase.counter+=1
            price=each_fruit_price*self.__quantity
            if each_fruit_price==max(FruitInfo.get_fruit_price_list()) and self.__quantity>1:
                price*=0.98
            if each_fruit_price==min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5:
                price*=0.95
            if Customer.get_cust_type(self.__customer)=='Wholesale':
                price*=0.90
            return price
        else:
            return -1

class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type

c=Customer("ABC","Wholesale")
p=Purchase(c,"Apple",5)
print(p.calculate_price())
