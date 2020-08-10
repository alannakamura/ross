import fluid_flow as ff
import fluid_flow_coefficients as ffc
import numpy as np
from fluid_flow_coefficients import calculate_oil_film_force

print('exemplo1')
print('fornecendo a excentricidade')
ff1 = ff.FluidFlow(
        nz=8,
        ntheta=32*16,
        length=0.04,
        omega=100.0 * 2 * np.pi / 60,
        p_in=0.0,
        p_out=0.0,
        radius_rotor=0.2,
        radius_stator=0.2002,
        viscosity=0.015,
        density=860.0,
        eccentricity=0.0001,
        #attitude_angle=np.pi / 4,
        immediately_calculate_pressure_matrix_numerically=False,

    )

print('e:', ff1.eccentricity, 'w:', ff1.load, ff1.bearing_type)
ra=np.array(calculate_oil_film_force(ff1))
print('forca analitica', ra)
rn=np.array(calculate_oil_film_force(ff1, 'numerical'))
print('forca numerica', rn)
erro=(rn-ra)/rn
erro[2]=(rn[2]-ra[2])/rn[2]
print('erro relativo', abs(erro))
print('')
print('fornecendo o load calculado anteriormente')
ff2 = ff.FluidFlow(
        nz=8,
        ntheta=32*16,
        length=0.04,
        omega=100.0 * 2 * np.pi / 60,
        p_in=0.0,
        p_out=0.0,
        radius_rotor=0.2,
        radius_stator=0.2002,
        viscosity=0.015,
        density=860.0,
        load=ff1.load,
        attitude_angle=np.pi / 4,
        immediately_calculate_pressure_matrix_numerically=False,
    )

print('e:',ff2.eccentricity, 'w:', ff2.load, ff2.bearing_type)
ra=np.array(calculate_oil_film_force(ff2))
print('forca analitica', ra)
rn=np.array(calculate_oil_film_force(ff2, 'numerical'))
print('forca numerica', rn)
erro=(rn-ra)/rn
erro[2]=(rn[2]-ra[2])/rn[2]
print('erro relativo', abs(erro))
print('')
# exit(0)

# print('example 3')
# print('fornecendo a excentricidade')
# nz = 8  # 8
# ntheta = 32*8  # 32
# nradius = 8
# omega = 100.0 * 2 * np.pi / 60
# p_in = 0.0
# p_out = 0.0
# # radius_rotor = 0.1999996
# # radius_stator = 0.1999996 + 0.000194564
# radius_rotor=0.2
# radius_stator=0.2002
# length = (1 / 10) * (2 * radius_stator)
# eccentricity = 0.0001
# visc = 0.015
# rho = 860.0
# ff5 = ff.FluidFlow(
#     nz,
#     ntheta,
#     nradius,
#     length,
#     omega,
#     p_in,
#     p_out,
#     radius_rotor,
#     radius_stator,
#     visc,
#     rho,
#     eccentricity=eccentricity,
#     immediately_calculate_pressure_matrix_numerically=False,
# )
#
# print('e:',ff5.eccentricity, 'w:', ff5.load, ff5.bearing_type)
# ra=np.array(calculate_oil_film_force(ff5))
# print('forca analitica', ra)
# rn=np.array(calculate_oil_film_force(ff5, 'numerical'))
# print('forca numerica', rn)
# erro=(rn-ra)/rn
# erro[2]=(rn[2]-ra[2])/rn[2]
# print('erro relativo', abs(erro))
# print("")
#
# print('fornecendo o load calculado anteriormente')
# ff6 = ff.FluidFlow(
#     nz,
#     ntheta,
#     nradius,
#     length,
#     omega,
#     p_in,
#     p_out,
#     radius_rotor,
#     radius_stator,
#     visc,
#     rho,
#     load=ff5.load,
#     immediately_calculate_pressure_matrix_numerically=False,
# )
#
# print('e:',ff6.eccentricity, 'w:', ff6.load, ff6.bearing_type)
# ra=np.array(calculate_oil_film_force(ff6))
# print('forca analitica', ra)
# rn=calculate_oil_film_force(ff6, 'numerical')
# print('forca numerica', rn)
# erro=(rn-ra)/rn
# erro[2]=(rn[2]-ra[2])/rn[2]
# print('erro relativo', abs(erro))

# coefficients = [
    #     (1 - (modified_s ** 2) * (16 - np.pi ** 2)),
    #     -4,
    #     6 - (np.pi ** 2) * (modified_s ** 2),
    #     -4,
    #     1,
    # ]