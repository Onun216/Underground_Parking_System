from datetime import datetime, date, time, timedelta
import vehicle


class Park:

    def __init__(self, floor_list, charging_fee):
        self.floor_list = floor_list
        self.__charging_fee = charging_fee

    @property
    def fee(self):
        return self.__charging_fee

    @fee.setter
    def fee(self, charging_fee):
        self.__charging_fee = charging_fee

    def info(self):
        for floors in self.floor_list:
            print(f'Floor: {floors.floor_name}\nNumber of charging points: {floors.charging_points}\n'
                  f'Spaces for cars: {floors.spaces_cars}\nSpaces for motorcycles: {floors.spaces_motorcycles}')
            print()

    def park_availability(self, vehicle):
        i = 0
        for floor in self.floor_list:
            if floor.is_full(vehicle) == 100:
                i += 1
                continue
            # print(f'Floor name: {floor.floor_name}')
            return i
        return 1000


class Floor:

    def __init__(self, floor_name, spaces_cars, spaces_vip, spaces_handicap, spaces_motorcycles, charging_points):
        self.__floor_name = floor_name
        self.__spaces_cars = spaces_cars
        self.__spaces_vip = spaces_vip
        self.__spaces_handicap = spaces_handicap
        self.__spaces_motorcycles = spaces_motorcycles
        self.__charging_points = charging_points

    @property
    def floor_name(self):
        return self.__floor_name

    @floor_name.setter
    def floor_name(self, floor_name):
        self.__floor_name = floor_name

    @property
    def spaces_cars(self):
        return self.__spaces_cars

    @spaces_cars.setter
    def spaces_cars(self, spaces_cars):
        self.__spaces_cars = spaces_cars

    @property
    def spaces_vip(self):
        return self.__spaces_vip

    @spaces_vip.setter
    def spaces_vip(self, spaces_vip):
        self.__spaces_vip = spaces_vip

    @property
    def spaces_handicap(self):
        return self.__spaces_handicap

    @spaces_handicap.setter
    def spaces_handicap(self, spaces_handicap):
        self.__spaces_handicap = spaces_handicap

    @property
    def spaces_motorcycles(self):
        return self.__spaces_motorcycles

    @spaces_motorcycles.setter
    def spaces_motorcycles(self, spaces_motorcycles):
        self.__spaces_motorcycles = spaces_motorcycles

    @property
    def charging_points(self):
        return self.__charging_points

    @charging_points.setter
    def charging_points(self, charging_points):
        self.__charging_points = charging_points

    def is_full(self, vehicle):
        if vehicle.type == 'car' and vehicle.VIP:
            if len(self.__spaces_vip) != 0:
                print('Opening park gate...')
                return self.__floor_name
        elif vehicle.type == 'car' and vehicle.handicap:
            if len(self.__spaces_handicap) != 0:
                print('Opening park gate...')
                return self.__floor_name

        elif vehicle.type == 'electric' and vehicle.handicap:
            if len(self.__charging_points) != 0:
                print('Opening park gate...')
                return self.__floor_name

        elif vehicle.type == 'car' and not vehicle.VIP:
            if len(self.__spaces_cars) != 0:
                print('Opening park gate...')
                return self.__floor_name

        elif vehicle.type == 'electric' and not vehicle.handicap:
            if len(self.__charging_points) != 0:
                print('Opening park gate...')
                return self.__floor_name

        elif vehicle.type == 'electric' and not vehicle.VIP:
            if len(self.__charging_points) != 0:
                print('Opening park gate...')
                return self.__floor_name

        elif vehicle.type == 'motorcycle':
            if len(self.__spaces_motorcycles) != 0:
                print('Opening park gate...')
                return self.__floor_name

        return 100


# None represents an empty parking space
f1 = Floor(0, ([None] * 50), ([None] * 3), ([None] * 5), ([None] * 5), ([None] * 10))
f2 = Floor(-1, ([None] * 50), ([None] * 3), ([None] * 5), ([None] * 5), ([None] * 10))
f3 = Floor(-2, ([None] * 50), ([None] * 3), ([None] * 5), ([None] * 5), ([None] * 0))
f4 = Floor(-3, ([None] * 50), ([None] * 0), ([None] * 3), ([None] * 5), ([None] * 5))
f5 = Floor(-4, ([None] * 50), ([None] * 0), ([None] * 0), ([None] * 0), ([None] * 0))
floors = [f1, f2, f3, f4, f5]
