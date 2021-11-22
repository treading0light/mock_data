from random import randint

class FleetGen:
        ''' generate mock data to represent a fleet '''

        def __init__(self):
                ''' set up initial data to pick from '''

                self.ford_models = ["E350", "f150", "f350"]
                self.chevy_models = ["1500", "2500", "3500"]
                self.truck = {}


        def make_truck(self):
                ''' create a number of trucks equal to range '''

                for num in range(1,20):
                        year = randint(1990,2020)
                        make = self.choose_make()
                        model = self.choose_model(make)
                        mileage = randint(90_000,160_000)
                        num = str(num)
                        stats = {'year': year, 'make': make, 'model': model,
                                 'mileage': mileage}               
                        self.truck[num] = stats
                        # print(f"added {self.truck[num]} to dict")
                

        def choose_make(self):
                ''' randomly choose either ford or chevy '''

                choice = randint(1,2)
                
                if choice == 1:
                        return "ford"
                if choice == 2:
                        return "chevy"


        def choose_model(self, make):
                '''
                randomly choose from a list of models depending on
                chosen make
                '''

                if make == "chevy":
               
                        model_max = len(self.chevy_models) -1
                        # print(f"model max is {model_max}")
                        model_choice = randint(1,model_max)
                        # print(f"model choice is {model_choice}")
                        model = self.chevy_models[model_choice]
                        return model
                
                elif make == "ford":

                        model_max = len(self.ford_models) -1
                        # print(f"model max is {model_max}")
                        model_choice = randint(1,model_max)
                        # print(f"model choice is {model_choice}")
                        model = self.ford_models[model_choice]
                        return model