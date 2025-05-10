def hotel_cost(nights):
    return 140*nights
def plane_ride(city):
    if "California" == city:
        return 183
    elif "Phoenix" == city:
        return 220
    elif "Edinburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
def rental_car(days):
    if days >= 7:
        return 40*days - 50
    if days >= 3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car(days) + hotel_cost(days) + plane_ride(city) + spending_money
print("Cost of car rental :", rental_car(6))
print("Cost of plane tickets :", plane_ride("California"))
print("Cost of hotel room :", hotel_cost(7))
print("Total cost of  the trip :", trip_cost("California", 7,500))
print(trip_cost("Phoenix", 6,500))