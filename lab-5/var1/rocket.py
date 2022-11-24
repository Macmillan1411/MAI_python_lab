def main():
    r = Rocket(1000,500)
    for i in range(5):
        r.spend_fuel(100)
        print(r)
    
          
class Rocket:

    def __init__(self,mass,fuel,engine_on=False):
        '''this creates  a rocket with three  properties total mass,fuel an engine status
           if there is fuel in the engine the rocket immediately turns on
        '''
        self.fuel = fuel
        self.mass = mass
        if self.fuel > 0:
            self.engine_on = True


    def spend_fuel(self,count):
        '''this reduces the fuel by count a value passed to the method by the user kilograms
            if the fuel drops t below 0 the engine immediately stalls/stops running 
        '''
        self.fuel -= count 
        self.mass -= count
        if self.fuel > 0:
            return True
        else:
            self.engine_on = False
            return False
            

    def get_fuel_level(self):
        '''returns the current amount of fuel'''
        return self.fuel 


    def get_total_weight(self):
        '''returns the current total mass of the rocket'''
        return self.mass


    def get_is_engine_running(self):
        '''shows the current status of the engine on/off'''
        return self.engine_on 

    def __str__(self):
        engine_status = "Running" if self.get_is_engine_running() else "Stalled, no fuel left"
        return f"Current Total Mass of Rocket  and Fuel: {self.get_total_weight()}\n The Net Mass of the Rocket: {self.get_total_weight() - self.get_fuel_level()}\n Remaining fuel: {self.get_fuel_level()}\n The Engine is currently: {engine_status}\n -----------------"
        #print(f"Current Total Mass of Rocket  and Fuel: {self.mass}\n The Net Mass of the Rocket: {self.mass - self.fuel}\n Remaining fuel: {self.fuel}\n The Engine is currently: {engine_status}")

if __name__== "__main__":
    main()
