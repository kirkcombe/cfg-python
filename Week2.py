#Name= input("What is your name? ")
#Age= input("How old are you? ")
#print ("Hello {}, {} is a good age".format(Name,Age))

#HowManyPeople= int(input("How many people are there?  "))
#HowMuch= 0.5
#Pizza=HowManyPeople*HowMuch
#print("you need {} pizzas".format(Pizza))

store_capacity = 5
while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1 #---> imagine that we forgot to add this logic!!!
print("\nPlease wait for someone to exit the store.")

