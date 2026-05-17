# import numpy as py
import matplotlib.pyplot as plt

# CONSTANTS
altitude = 100.0
velocity = 0.0
g = 9.81
dt = 0.01
thrust = 1.0
mass = 1.0

alt_history = []
time_history = []
t = 0.0

ignition_elapse_time = None
ignition_delay_time = 0.1

print("Starting Simulation..")

# simulation ends when the rocket hits the ground
while altitude > 0.0:
# via kinematics, where the final velocity must be equal to zero
    k = 0.95 # safety margin/factor that causes the engine to use more power during ignition to compensate for the delay
    accel_needed = -(velocity ** 2) / (2 * altitude) * k
# via f=ma
    accel_max = (15.0 - (mass * g)) / mass

# when this occurs, the rocket has reached the absolute last second it has to break, therefore ignition begins
    if abs(accel_needed) >= accel_max:
# capture the moment when ignition begins
        if ignition_elapse_time is None:
            ignition_elapse_time = t

# manage the thrust based on this timestamp
        if ignition_elapse_time != 0.0 and (t-ignition_elapse_time) >= ignition_delay_time:
                thrust = 15.0
        else:
            thrust = 0.0

# all these formula were derived from f=ma (Newton's 2nd)
    force = thrust - (mass * g) # the net force on the rocket
    acceleration = force / mass
    velocity = velocity + (acceleration * dt)
    altitude = altitude + (velocity * dt)

# "records" the history for both the altitude and time variables and stores them into a list
    alt_history.append(altitude)
    time_history.append(t)
    t += dt

print("Rocket landed/crashed")

# plot the data
plt.figure(figsize=(10, 5))
plt.plot(time_history, alt_history, label='Altitude (m)')
plt.axhline(0, color='black', linestyle='--') # Ground line
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('1D Rocket Drop Simulation')
plt.grid(True)
plt.legend()
plt.show()
