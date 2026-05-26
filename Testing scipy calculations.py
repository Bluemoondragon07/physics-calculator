import scipy
import scipy.constants as const


# things to test

# 1. calculate momentum
# --> p = mv; Fnet = ma -> m = Fnet/a --> p = Fnet/a * v
# ----> variables: Fnet, m , a, v 
#       user select which variables to input -> determine appropriate formula to use
# include option for freefall, throwing/launching projectile from user-defined height 

# basic momentum calculator 

print("Welcome to momentum calculator.") 
mass = input("If the object's mass is known, enter it (kg). Press [Enter] if unknown");
velocity = input("Enter velocity (m/s). [Enter] to skip")

if not mass and not velocity: # if already have mass and velocity, don't need to ask for these
    acceleration = input("Enter acceleration (m/s^2). [Enter] to skip")
    Fnet = input("Enter net force (N). [Enter] to skip")


if mass and velocity:
    momentum = float(mass) * float(velocity)
elif Fnet and acceleration and velocity:
    mass = float(Fnet) / float(acceleration)
    momentum = mass * float(velocity)   
   
print(f"Momentum (p) = {momentum} kg*m/s")

