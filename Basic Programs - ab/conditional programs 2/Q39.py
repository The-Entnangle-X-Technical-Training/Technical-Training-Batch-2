#Write a program that calculates shipping cost based on: weight (kg) and distance (km). 
#Base cost: ₹50. Add ₹10/kg if weight > 5kg. Add ₹5/km if distance > 100km. If both conditions 
#true, add ₹20 extra. Display total shipping cost.
weight=float(input("Enter the weight: "))
distance=float(input("Enter the distance: "))
base_cost=50
if(weight>5):
    extra_weight=weight-5
    base_cost += extra_weight*10
if(distance>100):
    extra_distance=distance-100
    base_cost += extra_distance*5
if(weight>5 and distance>100):
    base_cost += 20
print("Total cost: ", base_cost)