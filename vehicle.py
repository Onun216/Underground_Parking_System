from datetime import datetime, date, time, timedelta


class Vehicle:

    def __init__(self, handicap, vehicle_type, owner_ID, drivers_license, nr_plate, VIP, entry_time, exit_time):
        self.__handicap = handicap
        self.__vehicle_type = vehicle_type
        self.__owner_ID = owner_ID
        self.__drivers_license = drivers_license
        self.__nr_plate = nr_plate
        self.__VIP = VIP
        self.__entry_time = entry_time
        self.__exit_time = exit_time

    @property
    def handicap(self):
        return self.__handicap

    @handicap.setter
    def handicap(self, handicap):
        self.__handicap = bool

    @property
    def type(self):
        return self.__vehicle_type

    @type.setter
    def type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    @property
    def owner_ID(self):
        return self.__owner_ID

    @owner_ID.setter
    def owner_ID(self, owner_ID):
        self.__owner_ID = owner_ID

    @property
    def drivers_license(self):
        return self.__drivers_license

    @drivers_license.setter
    def drivers_license(self, drivers_license):
        self.__drivers_license = drivers_license

    @property
    def nr_plate(self):
        return self.__nr_plate

    @nr_plate.setter
    def nr_plate(self, nr_plate):
        self.__nr_plate = nr_plate

    @property
    def VIP(self):
        return self.__VIP

    @VIP.setter
    def VIP(self, VIP):
        self.__VIP = bool

    @property
    def entry(self):
        return self.__entry_time

    @entry.setter
    def entry(self, entry_time):
        self.__entry_time = entry_time

    @property
    def exit(self):
        return self.__exit_time

    @exit.setter
    def exit(self, exit_time):
        self.__exit_time = exit_time


# Vehicle examples:
v1 = Vehicle(False, 'car', 'João', 123456, 'AA-00-AA', True,
             entry_time=datetime(2023, 1, 14, 16, 00, 00, 00),
             exit_time=datetime(2023, 1, 14, 18, 00, 00, 00))

v2 = Vehicle(False, 'motorcycle', 'Marco', 654321, 'AA-99-AA', False,
             entry_time=datetime(2023, 1, 14, 14, 00, 00, 00),
             exit_time=datetime(2023, 1, 14, 18, 00, 00, 00))

v3 = Vehicle(True, 'car', 'Luis', 656511, 'AA-22-BB', False,
             entry_time=datetime(2023, 1, 10, 14, 00, 00, 00),
             exit_time=datetime(2023, 1, 14, 18, 30, 00, 00))

v4 = Vehicle(True, 'electric', 'Marta', 676544, 'AA-44-BB', False,
             entry_time=datetime(2023, 3, 10, 10, 00, 00, 00),
             exit_time=datetime(2023, 3, 10, 19, 00, 00, 00))

v5 = Vehicle(False, 'electric', 'Leandro', 765490, 'AA-88-BB', False,
             entry_time=datetime(2023, 3, 12, 14, 00, 00, 00),
             exit_time=datetime(2023, 3, 12, 15, 00, 00, 00))

v6 = Vehicle(False, 'motorcycle', 'Lina', 698512, 'AB-99-AB', False,
             entry_time=datetime(2023, 4, 3, 12, 00, 00, 00),
             exit_time=datetime(2023, 4, 3, 20, 30, 00, 00))

v7 = Vehicle(False, 'electric', 'Ana', 696871, 'BB-10-BB', True,
             entry_time=datetime(2023, 4, 4, 8, 00, 00, 00),
             exit_time=datetime(2023, 4, 4, 18, 30, 00, 00))

v8 = Vehicle(True, 'car', 'Márcio', 878676, 'BB-11-BB', False,
             entry_time=datetime(2023, 4, 5, 8, 00, 00, 00),
             exit_time=datetime(2023, 4, 5, 18, 30, 00, 00))

v9 = Vehicle(False, 'car', 'André', 777888, 'BB-88-BB', True,
             entry_time=datetime(2023, 4, 6, 8, 00, 00, 00),
             exit_time=datetime(2023, 4, 6, 18, 30, 00, 00))

v10 = Vehicle(False, 'car', 'Anabela', 576423, 'BC-10-BC', True,
              entry_time=datetime(2023, 4, 6, 9, 00, 00, 00),
              exit_time=datetime(2023, 4, 6, 19, 30, 00, 00))

v11 = Vehicle(False, 'motorcycle', 'Ernesto', 909878, 'BC-77-BA', False,
              entry_time=datetime(2023, 4, 6, 8, 45, 00, 00),
              exit_time=datetime(2023, 4, 6, 16, 30, 00, 00))

v12 = Vehicle(True, 'electric', 'Lídia', 900111, 'BA-88-BC', False,
              entry_time=datetime(2023, 4, 6, 12, 30, 00, 00),
              exit_time=datetime(2023, 4, 6, 18, 30, 00, 00))

v13 = Vehicle(False, 'car', 'Leonel', 142364, 'AC-99-AC', True,
              entry_time=datetime(2023, 4, 6, 10, 20, 00, 00),
              exit_time=datetime(2023, 4, 6, 19, 30, 00, 00))

v14 = Vehicle(False, 'car', 'Rita', 888112, 'AD-00-AD', True,
              entry_time=datetime(2023, 4, 6, 9, 15, 00, 00),
              exit_time=datetime(2023, 4, 6, 17, 00, 00, 00))

v15 = Vehicle(False, 'motorcycle', 'Anacleto', 898989, 'CD-00-AD', False,
              entry_time=datetime(2023, 4, 6, 9, 30, 00, 00),
              exit_time=datetime(2023, 4, 6, 17, 30, 00, 00))

v16 = Vehicle(False, 'car', 'Alberto', 500334, 'CC-17-CC', False,
              entry_time=datetime(2023, 4, 6, 10, 35, 00, 00),
              exit_time=datetime(2023, 4, 6, 18, 30, 00, 00))

v17 = Vehicle(False, 'car', 'Abel', 443556, 'CC-22-CC', True,
              entry_time=datetime(2023, 4, 6, 11, 30, 00, 00),
              exit_time=datetime(2023, 4, 6, 22, 00, 00, 00))

v18 = Vehicle(False, 'car', 'Nelo', 332211, 'CD-25-CE', False,
              entry_time=datetime(2023, 4, 6, 11, 35, 00, 00),
              exit_time=datetime(2023, 4, 6, 13, 30, 00, 00))

vehicle_list = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18]


def vehicles(list):
    for vehicle in list:
        print(vehicle.type)

# vehicles(vehicle_list)
