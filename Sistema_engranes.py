import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

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

    def set_rpm(self, initial_rpm):
        self.initial_rpm = initial_rpm

    def visualize_rotation(self, num_frames=100):
        gear_ratio = self.calculate_gear_ratio()
        num_teeth = [gear.get_teeth() for gear in self.gears]

        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        # Define gear sizes and positions
        gear_sizes = np.array(num_teeth) * 0.1
        gear_positions = np.cumsum(gear_sizes)
        gear_centers = np.insert(gear_positions[:-1], 0, 0)

        gears = [plt.Circle((pos, 0), size, fill=False) for pos, size in zip(gear_centers, gear_sizes)]
        for gear in gears:
            ax.add_patch(gear)

        # Connect gears with lines
        for i in range(len(gears) - 1):
            ax.plot([gear_centers[i], gear_centers[i + 1]], [0, 0], 'k-')

        def update(frame):
            angle = 2 * np.pi * gear_ratio * frame / 100
            for gear, pos in zip(gears, gear_centers):
                x, y = gear.center
                x = pos * np.cos(angle)
                y = pos * np.sin(angle)
                gear.center = (x, y)
            return gears

        anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

        plt.xlim(-1, np.sum(gear_sizes) + 1)
        plt.ylim(-np.sum(gear_sizes) / 2, np.sum(gear_sizes) / 2)
        plt.title('Gear Rotation Animation')
        plt.show()
        gear_ratio = self.calculate_gear_ratio()

        fig, ax = plt.subplots()

        # Define the angles for rotation
        rotations = 2  # Number of full rotations
        angles = np.linspace(0, 2 * np.pi * rotations * gear_ratio, num_frames)

        # Positions of gears in the plot
        positions = np.array([[0, 0], [3, 0], [6, 0]])  # Adjust positions as needed

        for angle in angles:
            ax.clear()

            # Draw gears
            for i, gear in enumerate(self.gears):
                circle = plt.Circle(positions[i], gear.get_radius(), fill=False)
                ax.add_patch(circle)

            # Connect gears with lines
            for i in range(len(positions) - 1):
                ax.plot([positions[i][0], positions[i + 1][0]], [positions[i][1], positions[i + 1][1]], 'k-')

            # Update positions for rotation
            positions[1:] = self.rotate_gears(positions[1:], angle)

            ax.set_xlim(-3, 9)  # Adjust plot limits as needed
            ax.set_ylim(-3, 3)  # Adjust plot limits as needed
            ax.set_aspect('equal')
            ax.set_title(f"Frame {angle/(2*np.pi):.2f} of {rotations}")

            plt.pause(0.01)  # Pause to show each frame

    @staticmethod
    def rotate_gears(positions, angle):
        # Rotate gear positions around the origin
        rot_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return np.dot(positions, rot_matrix)


if __name__ == '__main__':
    driver_gear = Gear(10)
    middle_gear = Gear(30)
    driven_gear = Gear(30)

    gear_train = GearTrain()
    gear_train.add_gear(driver_gear)
    gear_train.add_gear(driven_gear)
    gear_train.set_rpm(5)
    print(gear_train.calculate_gear_ratio())

    gear_train.visualize_rotation()
