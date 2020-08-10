import fluid_flow as ff
import fluid_flow_coefficients as ffc
import numpy as np
from fluid_flow_coefficients import calculate_oil_film_force

print('example long')
print('fornecendo o load')
nz = 8
ntheta = 16
nradius = 8
length = 0.03
omega = 157.1
p_in = 0.0
p_out = 0.0
radius_rotor = 0.0499
radius_stator = 0.05
load = 525
visc = 0.1
rho = 860.0
ff3 = ff.FluidFlow(
    nz,
    ntheta,
    nradius,
    length,
    omega,
    p_in,
    p_out,
    radius_rotor,
    radius_stator,
    visc,
    rho,
    load=load,
    immediately_calculate_pressure_matrix_numerically=False,
)

# calculo de como se fosse short

# print('antes')
# print('e:', ff3.eccentricity, 'w:', ff3.load, ff3.bearing_type)
# print('xi ', ff3.xi, 'yi ', ff3.yi)
# temp = ffc.find_equilibrium_position2(ff3, max_iterations=20, increment=1e-6)
# ffc.find_equilibrium_position2(ff3, max_iterations=20, increment=1e-6)
# print(temp)
# print('depois')
# ff3.eccentricity = np.sqrt(ff3.xi ** 2 + ff3.yi ** 2)
# print('e:', ff3.eccentricity, 'w:', ff3.load, ff3.bearing_type)
# print('xi ', ff3.xi, 'yi ', ff3.yi)

# ff3.calculate_coefficients()
# ff3.calculate_pressure_matrix_numerical()
# temp = calculate_oil_film_force(
#     ff3, force_type="numerical"
# )
# print(temp)

