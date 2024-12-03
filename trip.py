def hotelCost(nights):
    return 140 * nights 

def planeRides(city):
    if "Alberta" == city:
        return 183
    elif "Manitoba" == city:
        return 220
    elif "Toronto" == city:
        return 222
    elif "Yukon" == city:
        return 475 
    
def carRental(days):
    if days>=7: 
        return 40*days - 5
    elif days>=3:
        return 40*days - 3
    else:
        return 40*days
    
def tripCost(city, days, spendingMoney):
    return carRental(days) + hotelCost(days) + planeRides(city) + spendingMoney

print("the cost of car rental:" , carRental(5))
print("the cost of plane ride:", planeRides("Toronto"))
print("the cost of hotel room:", hotelCost(7))
print("the total cost of the trip is:", tripCost("Toronto", 7, 5))