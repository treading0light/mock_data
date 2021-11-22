from mock_data import FleetGen

v_fleet = FleetGen()

v_fleet.make_truck()


for truck, stats in v_fleet.truck.items():
	print(f"{stats['year']}\t {stats['make']}\t {stats['model']} ")

# truck = {'mileage': 150, 'year': 2016}

# print(truck['mileage'])