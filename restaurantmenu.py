'''
create an program which replicates restaurants menu :
for ordering Veg or Non Veg menu

program shouldn't exit before uses wishes to
'''

class Restaurant:
    def Menu(self):
        ques=input("Do you want to order? (Y/N)")
        if (ques=='Y'):
            self.item=[]
            self.quantity=[]
            self.cost=0
            self.counter=0
            self.totalbill=0
            h.order()
        else:
            print("Thank you ! Please visit us again.")
    def order(self):
        opt=int(input(("Enter option whether Veg/Non-Veg/No-order : (1/2/3)")))
        if (opt==1):
            h.Veg()
        elif(opt==2):              
            h.NonVeg()
        elif(opt==3):
            print("Moving to Order summary !!")
            h.ordersummary()     
    def Veg(self):
        print("Please find below Veg Items :")
        print("SrNo--------Name---------------------Value")
        print("******************************************")
        print("1-----------Poha---------------------50")
        print("2----------Pav Bhaaji----------------80")
        print("3----------Masala Dosa---------------70")
        print("4----------Veg Pizza-----------------90")
        print("5----------Paneer Chili-------------100")
        order1=input("Press Y to enter Veg item order OR any other key to go back to previous menu :")
        if (order1=='Y'):
            i=int(input("Enter no of items you want to order : "))
            for j in range(self.counter,(self.counter+i)):
                y=int(input("Enter SrNo of the Item you want to order : "))
                self.item.append(y)
                z=int(input("No of quantity of the item you want to order : "))
                self.quantity.append(z)
            self.counter=self.counter+i
            x=input("Do you want to continue ordering? (Y/N) : ")
            if (x=='Y'):
                h.order()
            elif(x=='N'):
                h.ordersummary()
            else:
                print("Wrong Input ! Moving back to order screen.")
                h.order()
        elif(order1=='N'):
            h.order()
        else:
            print("Wrong Input ! Moving back to order screen.")
            h.order()
    def NonVeg(self):
        print("Please find below Non Veg Items :")
        print("SrNo--------Name---------------------Value")
        print("******************************************")
        print("6---------Tandoori Chicken-----------100")
        print("7---------Mutton Biryani--------------90")
        print("8---------Prawns Fry------------------70")
        print("9---------Lamb Roast-----------------100")
        print("10--------Fish Fry-------------------110")
        order2=input("Press Y to enter Non Veg item order OR any other key to go back to previous menu :")
        if (order2=='Y'):
            k=int(input("Enter no of items you want to order : "))
            for l in range(self.counter,(self.counter+k)):
                a=int(input("Enter SrNo of the Item you want to order : "))
                self.item.append(a)
                b=int(input("No of quantity of the item you want to order : "))
                self.quantity.append(b)
            self.counter=self.counter+k
            c=input("Do you want to continue ordering? (Y/N) : ")
            if (c=='Y'):
                h.order()
            elif(c=='N'):
                h.ordersummary()
            else:
                print("Wrong Input ! Moving back to order screen.")
                h.order()
        elif(order2=='N'):
            h.order()
        else:
            print("Wrong Input ! Moving back to order screen.")
            h.order()
    def ordersummary(self):
        if (len(self.item)==0):
            print("No items bought. Thank you ! Please visit us again.")
        else:
            items=("Poha","Pav Bhaaji","Dosa","Veg Pizza","Paneer Chili","Tandoori Chicken","Mutton Biryani","Prawns Fry","Lamb Roast","Fish Fry")
            prices=[50,80,70,90,100,100,90,70,100,110]
            print("Bill Summary : ")
            print("--------------------------------------------------------------------------------")
            for n in range(0,self.counter):
                print("Item Ordered : ",items[(self.item[n]-1)])
                print("Quantity Ordered :",self.quantity[n])
                print("Price per plate : ",prices[(self.item[n]-1)])
                self.cost= prices[(self.item[n]-1)]*self.quantity[n]
                print("Item Cost :",self.cost)
                print("************************")
                self.totalbill=self.totalbill + self.cost
            print("Total Bill :")
            print("--------------------------------------------------------------------------------")
            print(self.totalbill)
h=Restaurant()
h.Menu()
