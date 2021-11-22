# mock_data
Randomly generate a fleet of vehicles and their stats.

fleet.py is a brief example of how mock_data can be used

to use mock_data:

                  import FleetGen from mock_data.py

                  create an instance of FleetGen

                  call the make_truck() method

There are various print() functions commented out that might be helpful when changing things in the code.


To change the number of vehicles in the fleet:
                                              
                                              change the range in the make_truck() for loop.

To add new makes and models to be chosen:

  Add to the FLeetGen init: 
  
                            self.{make}_models = ['model', 'model', 'etc']
  
  in choose_make(): 
                    
                    increase the randint range to match the number of makes
  
                    add an elif statement that returns the make as a str       
                    
  in choose_model(): 
                    
                    add an elif statement to assign the new list of models to var "model_list"
