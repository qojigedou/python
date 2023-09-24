import matplotlib.pyplot as plt
from matplotlib import animation

Mass_sun = 2.0e30
Gravity = 6.67e-11
astro_unit = 1.5e11
sec_in_day = 24.0*60*60
x_sun, y_sun, z_sun = 0, 0, 0
x_vel_sun, y_vel_sun, z_vel_sun = 0, 0, 0

t = 0.0
dt = 1*sec_in_day


class Planet:
    def __init__(self, velocity, mass, distance, name):
        self.mass = mass
        self.velocity = velocity
        self.mass = mass
        self.distance = distance
        self.name = name
        self.gravconst = Gravity*self.mass*Mass_sun
        self.position = [distance*astro_unit, 0, 0] 
        self.positional_velocity = [0, self.velocity, 0] 
        self.x_list = []
        self.y_list = []
        self.z_list = []

    def get_new_position(self):
        rx, ry, rz = self.position[0], self.position[1], self.position[2]
        modr3 = (rx**2 + ry**2 + rz**2)**1.5
        fx = -self.gravconst*rx/modr3
        fy = -self.gravconst*ry/modr3
        fz = -self.gravconst*rz/modr3
        self.positional_velocity[0] += fx*dt/self.mass
        self.positional_velocity[1] += fy*dt/self.mass
        self.positional_velocity[2] += fz*dt/self.mass
        self.position[0] += self.positional_velocity[0]*dt
        self.position[1] += self.positional_velocity[1]*dt
        self.position[2] += self.positional_velocity[2]*dt
        self.x_list.append(self.position[0])
        self.y_list.append(self.position[1])
        self.z_list.append(self.position[2])
        return (fx, fy, fz)



    def setup_render(self, color):
        self.color = color
        self.line = ax.plot([0], [0], [0], self.color, lw=1)[0]
        self.point = ax.plot([astro_unit], [0], [0], marker="o", markersize=4, markeredgecolor=color, markerfacecolor=color)[0]
        self.text = ax.text(astro_unit, 0, 0, self.name)
    
    def update(self, num):
        self.line.set_data_3d(self.x_list[:num], self.y_list[:num], self.z_list[:num])
        self.point.set_data_3d(self.x_list[num], self.y_list[num], self.z_list[num])
        self.text.set_position((self.x_list[num], self.y_list[num], self.z_list[num]))



earth = Planet(29780, 5.972e24, 1, "Earth")
mars = Planet(24100, 6.39e30, 1.52, "Mars")
mercury = Planet(47900, 3.285e23, 0.39, "Mercury")
venus = Planet(35000, 4.867e24, 0.72, "Venus")

x_sun_list = []
y_sun_list = []
z_sun_list = []


while t < 5*365*sec_in_day:

    fx_earth, fy_earth, fz_earth = earth.get_new_position()
    fx_mars, fy_mars, fz_mars = mars.get_new_position()
    fx_mercury, fy_mercury, fz_mercury = mercury.get_new_position()
    fx_venus, fy_venus, fz_venus = venus.get_new_position()

    x_vel_sun += -(fx_earth+fx_mars+fx_mercury+fx_venus)*dt/Mass_sun
    y_vel_sun += -(fy_earth+fy_mars+fy_mercury+fy_venus)*dt/Mass_sun
    z_vel_sun += -(fz_earth+fz_mars+fz_mercury+fz_venus)*dt/Mass_sun

    x_sun += x_vel_sun*dt
    y_sun += y_vel_sun*dt 
    z_sun += z_vel_sun*dt
    x_sun_list.append(x_sun)
    y_sun_list.append(y_sun)
    z_sun_list.append(z_sun)
    
    t +=dt

print('data ready')


fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.axis('auto')

axis_size = 1.3
ax.set_xlim(-axis_size*astro_unit,axis_size*astro_unit)
ax.set_ylim(-axis_size*astro_unit,axis_size*astro_unit)
ax.set_zlim(-axis_size*astro_unit,axis_size*astro_unit)

datadict = {}
dataset_sun = [x_sun_list,y_sun_list,z_sun_list]
datadict['s'] = dataset_sun
vis_dict = {}

# sun
line_s,     = ax.plot([0],[0],[0],'-y',lw=1)
point_s,    = ax.plot([astro_unit],[0],[0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s      = ax.text(astro_unit,0,0,'Sun')
vis_dict['s'] = [line_s,point_s,text_s]

earth.setup_render("#00ff00")
mars.setup_render("#ff0000")
mercury.setup_render("#9003fc")
venus.setup_render("#e377c2")


def update(num,data_dict,vis_dict):
    # sun 
    dataset_sun              = data_dict['s']
    line_s,point_s,text_s   = vis_dict['s'][0],vis_dict['s'][1],vis_dict['s'][2]
    line_s.set_data_3d(dataset_sun[0][:num],dataset_sun[1][:num],dataset_sun[2][:num])
    point_s.set_data_3d(dataset_sun[0][num],dataset_sun[1][num],dataset_sun[2][num])
    text_s.set_position((dataset_sun[0][num],dataset_sun[1][num],dataset_sun[2][num]))

    earth.update(num)
    mars.update(num)
    mercury.update(num)
    venus.update(num)


ani = animation.FuncAnimation(
    fig
    ,update
    ,len(earth.x_list)
    ,fargs=(datadict, vis_dict)
    ,interval=1
)

plt.show()

    