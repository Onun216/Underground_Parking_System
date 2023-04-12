from datetime import datetime
from park_floors import Park, floors
from vehicle import Vehicle, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18

my_park = Park(floors, 10)

fl0, fl1, fl2, fl3, fl4, fl5 = [], [], [], [], [], []
park_floors = [fl0, fl1, fl2, fl3, fl4, fl5]


def price_parking(vehicle):
    result = vehicle.exit - vehicle.entry
    minutes = result.total_seconds() / 60
    if vehicle.VIP:
        price = minutes * 0.35
        return price
    else:
        if minutes > 180:
            extra_time = minutes - 180
            extra_time_fine = extra_time * 0.25
            price = extra_time_fine + minutes * 0.05
            return price
        else:
            price = minutes * 0.05
            return price


# Park.info(my_park)

def payment(park, vehicle):
    price_parking(vehicle)
    if vehicle.type == 'electric':
        price = price_parking(vehicle) + park.fee
        # print(f'Vehicle: {vehicle.nr_plate}\nPrice: €{price}')
    else:
        price = price_parking(vehicle)
        # print(f'Vehicle: {vehicle.nr_plate}\nPrice: €{price}')
    return price


def entry_park(park, vehicle):
    check = Park.park_availability(park, vehicle)
    if check == 100:
        print('The park is full!')
    else:
        park_vehicle = floors[check]
        if vehicle.type == 'car' and vehicle.VIP:
            park_vehicle.spaces_vip.pop()
        elif vehicle.type == 'car' and vehicle.handicap:
            park_vehicle.spaces_handicap.pop()
        elif vehicle.type == 'electric' and vehicle.handicap:
            park_vehicle.charging_points.pop()
        elif vehicle.type == 'electric' and not vehicle.handicap:
            park_vehicle.charging_points.pop()
        elif vehicle.type == 'car' and not vehicle.VIP:
            park_vehicle.spaces_cars.pop()
        elif vehicle.type == 'car' and not vehicle.handicap:
            park_vehicle.spaces_cars.pop()
        elif vehicle.type == 'car' and not vehicle.handicap and not vehicle.VIP:
            park_vehicle.spaces_cars.pop()
        elif vehicle.type == 'motorcycle':
            park_vehicle.spaces_motorcycles.pop()

        # Save all the vehicles that are/were parked in my_park
        park_floors[check].append(vehicle)

        print('Floor:', park_vehicle.floor_name, '|', len(park_vehicle.spaces_cars), len(park_vehicle.spaces_vip),
              len(park_vehicle.spaces_handicap),
              len(park_vehicle.spaces_motorcycles), len(park_vehicle.charging_points), '|', vehicle.nr_plate, '|',
              'VIP:', vehicle.VIP, 'Handicap:', vehicle.handicap, '|', vehicle.type)
        return park_vehicle


entry_park(my_park, v1)
new_request_5 = entry_park(my_park, v2)
entry_park(my_park, v3)
entry_park(my_park, v4)
entry_park(my_park, v5)
new_request_3 = entry_park(my_park, v6)
entry_park(my_park, v7)
entry_park(my_park, v8)
entry_park(my_park, v9)
entry_park(my_park, v10)
entry_park(my_park, v11)
entry_park(my_park, v12)
new_request_2 = entry_park(my_park, v13)
new_request_4 = entry_park(my_park, v14)
entry_park(my_park, v15)
entry_park(my_park, v16)
entry_park(my_park, v17)
new_request = entry_park(my_park, v18)
print()


def exit_park(request_update, vehicle):
    pay = payment(my_park, vehicle)
    if vehicle.type == 'car' and vehicle.VIP:
        request_update.spaces_vip.append('None')
    elif vehicle.type == 'car' and vehicle.handicap:
        request_update.spaces_handicap.append('None')
    elif vehicle.type == 'electric' and vehicle.handicap:
        request_update.charging_points.append('None')
    elif vehicle.type == 'electric' and not vehicle.handicap:
        request_update.charging_points.append('None')
    elif vehicle.type == 'car' and not vehicle.VIP:
        request_update.spaces_cars.append('None')
    elif vehicle.type == 'car' and not vehicle.handicap:
        request_update.spaces_cars.append('None')
    elif vehicle.type == 'car' and not vehicle.handicap and not vehicle.VIP:
        request_update.spaces_cars.append('None')
    elif vehicle.type == 'motorcycle':
        request_update.spaces_motorcycles.append('None')
    print(f'Vehicle: {vehicle.nr_plate}\nPrice: €{pay}')
    print(f'Payment validated!')
    print(f'Opening gate...')
    print('Floor:', request_update.floor_name, '|', len(request_update.spaces_cars), len(request_update.spaces_vip),
          len(request_update.spaces_handicap),
          len(request_update.spaces_motorcycles), len(request_update.charging_points))
    print()


exit_park(new_request, v18)
exit_park(new_request_2, v13)
exit_park(new_request_3, v6)
exit_park(new_request_4, v14)
exit_park(new_request_5, v2)
