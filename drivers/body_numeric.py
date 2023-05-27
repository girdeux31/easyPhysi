
import math
import matplotlib.pyplot as plt


class Body2D:

    dimensions = 2

    def __init__(self):

        # initial values
        self.position = None
        self.velocity = None

        # constants
        self.gravity = None
        self.mass = None

    def set_position(self, x, y):
        
        self.position = (x, y)

    def set_velocity(self, vx, vy):

        self.velocity = (vx, vy)

    def set_gravity(self, gx, gy):

        self.gravity = (gx, gy)

    def set_mass(self, m):

        self.mass = m

    def calc_position_at_time(self, t):

        # p = p0 + v0*t + 1/2*g*t**2

        position = tuple()

        for axis in range(self.dimensions):
            position.append(self.position[axis] + self.velocity[axis]*t + self.gravity[axis]/2*t**2)

        return position

    def calc_velocity_at_time(self, t):

        # v = v0 + g*t
  
        velocity = tuple()

        for axis in range(self.dimensions):
            velocity.append(self.velocity[axis] + self.gravity[axis]*t)

        return velocity

    def calc_time_at_position(self, p, axis):

        # if gravity
        #     g/2*t**2 + v0*t + (p0-p) = 0 -> t = (-v0 +- sqrt(v0**2 - 2*g*(p0-p))) / g
        # else
        #     p = p0 + v0*t -> t = (p-p0)/v0

        if axis >= self.dimensions:
            raise ValueError(f'Parameter \'axis\' must be less than {self.dimensions}')
        
        if self.gravity[axis] != 0.0:

            discriminant = self.velocity[axis]**2 - 2*self.gravity[axis]*(self.position[axis]-p)

            if discriminant < 0.0:
                raise ValueError('Solution in the imaginary domain')
            
            time = ((-self.velocity[axis] + math.sqrt(discriminant)) / self.gravity[axis],
                    (-self.velocity[axis] - math.sqrt(discriminant)) / self.gravity[axis])
            
        else:

            time = ((p-self.position[axis])/self.velocity[axis])
        
        return time
    
    def calc_time_at_velocity(self, v, axis):

        # v = v0 + g*t

        if axis >= self.dimensions:
            raise ValueError(f'Parameter \'axis\' must be less than {self.dimensions}')
        
        if self.gravity[axis] != 0.0:
            time = (v-self.velocity[axis])/self.gravity[axis]
        else:
            raise ValueError(f'There is no gravity in axis {axis}, thus its velocity is constant')
        
        if time < 0.0:
            raise ValueError(f'A negative time is calculated')
        
        return time

    def calc_flying_time(self, h=0.0):

        time = self.calc_time_at_position(h, axis=1)  # time to reach level 0.0 in the axis 1

        return time

    def calc_max_height(self):
    
        time = self.calc_time_at_velocity(0.0, axis=1)  # time to reach velocity 0.0 in axis 1
        position = self.calc_position_at_time(time)[1]

        return position

    def calc_landing_position(self, h=0.0):

        time = self.calc_time_at_position(h, axis=1)  # time to reach level 0.0 in axis 1
        position = self.calc_position_at_time(time)

        return position

    def calc_landing_velocity(self, h=0.0):

        time = self.calc_time_at_position(h, axis=1)  # time to reach level 0.0 in axis 1
        velocity = self.calc_velocity_at_time(time)

        return velocity
    
    def plot_position(self, ts=0.01, file=None):

        t = 0.0
        points = list()
        max_time = self.calc_flying_time()

        while t < max_time:
            
            points.append(self.calc_position_at_time(t))
            t += ts

        x_points = [point[0] for point in points]
        y_points = [point[1] for point in points]

        plt.plot(x_points, y_points)
        plt.title('Position (y = f(x))')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()

        if file:
            plt.savefig(file)

        plt.show()

    def plot_velocity(self, ts=0.01, file=None):

        t = 0.0
        t_points = list()
        v_points = [list() for _ in self.dimensions]
        max_time = self.calc_flying_time()

        while t < max_time:
            
            point = self.calc_velocity_at_time(t)

            for axis in range(self.dimensions):
                v_points[axis].append(point[axis])

            t_points.append(t)
            t += ts

        plt.plot(t_points, v_points)
        plt.title('Velocity (v = f(t))')
        plt.xlabel('Time')
        plt.ylabel('Velocity')
        plt.legend(['$v_x$', '$v_y$'])
        plt.grid()

        if file:
            plt.savefig(file)

        plt.show()
