from main import *
earth=Planet(3650,1000,'люди')
bethelgeize=Star(1220000,100000,'красный гигант')
force = Calculation.calc_gravity_force(earth,bethelgeize,1)
print (force)