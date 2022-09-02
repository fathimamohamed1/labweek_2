
#TUPLES

city_state=[('Seattle','WA'),('Portland','OR'),('San Francisco', 'CA')]
print(len(city_state))

first_city_state=city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state =first_city_state
print(state)

def get_distance():
    miles= 4000
    km= miles * 2.2
    return miles, km 

distances=get_distance()  
print(distances[0]) 