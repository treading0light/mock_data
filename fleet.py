from mock_data import FleetGen
'''
The for loops below are examples of how you can access the data created by FleetGen()
'''

fleet = FleetGen()

fleet.make_truck()


for truck, stats in fleet.truck.items():
	print(f"{stats['year']}\t {stats['make']}\t {stats['model']} ")


# truck_1 = fleet.truck[1]
# print(f"truck_1 is a {truck_1['make']} {truck_1['model']} and has {truck_1['mileage']} miles on it")

