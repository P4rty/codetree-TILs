class Product:
    def __init__(self, name="codetree",code = "50"):
        self.name = name
        self.code = code
product1 = Product()
a,c = tuple(input().split())
product2 = Product(a,c)
print("product {0} is {1}".format(product1.code,product1.name))
print("product {0} is {1}".format(product2.code,product2.name))