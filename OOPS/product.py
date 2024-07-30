class Product:
    procount=0
    

    def __init__(self,pname,pprice,pdescription):
        Product.procount +=1
        self.__id=self.procount
        self._pname=pname
        self._pprice=pprice
        self._pdescription=pdescription


    def getProDetails(self):
        print('product id : ',self.__id)
        print('product name : ',self._pname)
        print('product price : ',self._pprice)
        print('product description : ',self._pdescription)


p1=Product(name,price,description)

p1.name=input('enter product name : ')
p1.price=input('enter product price : ')
p1.description=input('enter product description : ')

p1.getProDetails()
        