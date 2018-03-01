class dog :
    def __init__(self,name = "",height = 0,weight = 0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
def  main():
    spot = dog("spot",66,26)
    spot.eat()


main()
