class Gear:
    def __init__(self, teeth, is_axle_connection=False, gear_type='spur', radius=1):
        self.teeth = teeth
        self.radius = radius
        self.gear_type = gear_type
        self.is_axle_connection = is_axle_connection

    def get_radius(self):
        return self.radius

    def get_teeth(self):
        return self.teeth

    def get_gear_type(self):
        return self.gear_type
    
    def get_axle_connection(self):
        return self.is_axle_connection

class GearTrain():
    def __init__(self):
        self.gears = []

    def add_gear(self, gear):
        self.gears.append(gear)

    def calculate_gear_ratio(self):
        '''
        Calculates the gear ratio.
        Considering the first gear as the driver gear and the last gear as the driven gear:
        A gear ratio greater than 1 indicates that it is a gear reduction system; 
        the output gear will spin slower, but will have more torque. A gear ratio lower
        than 1 indicates that it is an overdrive system. A gear equal to 1; 
        the output and input remains the same.
        '''
        i = []
        for index, gear in enumerate(self.gears):
            if gear.get_axle_connection():
                i.append(index)
        if not i:
            # print(self.gears[-1].get_teeth())
            gear_ratio = self.gears[-1].get_teeth() / self.gears[0].get_teeth()
        return gear_ratio

if __name__ == '__main__':
    driver_gear = Gear(10)
    middle_gear = Gear(30)
    driven_gear = Gear(20)
    gear_train = GearTrain()
    gear_train.add_gear(driver_gear)
    gear_train.add_gear(driven_gear)

    print(gear_train.calculate_gear_ratio())

