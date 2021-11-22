from mock_data import FleetGen
'''
The for loop below is an example of how you can access the data created by FleetGen()
'''

fleet = FleetGen()

fleet.make_truck()


for truck, stats in fleet.truck.items():
	print(f"{stats['year']}\t {stats['make']}\t {stats['model']} ")
