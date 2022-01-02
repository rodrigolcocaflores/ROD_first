cars = 100
space_in_a_car = 4.0
drivers = 30
car_passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = car_passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", car_passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

# Exercise

planes = 14
space_in_a_plane = 100.0
pilots = 5
passengers = 750
planes_not_flying = planes - pilots
planes_flying = pilots
plane_capaciy = planes_flying * space_in_a_plane
average_passengers_per_plane = passengers / planes_flying

print("There are", planes, "planes available.")
print("THere are only", pilots, "pilots available.")
print("There will be", planes_not_flying, "empty planes.")
print("We can transport", plane_capaciy, "people.")
print("we have", passengers, "passengers to fly.")
print("We need to put about", average_passengers_per_plane,
      "in each plane.")

