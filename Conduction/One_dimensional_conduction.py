# In this problem we want to calculate heat transfer and the heat flux for any one dimensinal conduction with steady state

# Getting the inputs from the user
wall_thichness = float(
    input('Please enter the thickness of wall in meters: '))
thermal_conductivity = float(
    input('Please enter the thermal conductivity(W/m.K): '))
inside_temperature = float(
    input('Please enter the temperature of inside: '))
outside_temperature = float(
    input('Please enter the temperature of outside: '))
# creating a function to check if an input can be a float or not


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# check if we have the Area or not
while True:
    Area = input(
        'Please enter the area of wall in meters(if you do not have the area type no): ')
    if Area == 'no'.lower():
        break
    elif is_float(Area) is True:
        Area = float(Area)
        break
    else:
        print('Please enter a VALID answer.')


# checking the temperature unit
while True:    # We use while here to avoid the user see syntax error if user enter wrong input for temp_unit
    temp_unit = input(
        'What is the unit of the temperature(for kelvin type K, celcius type C, farenheit type F): ')
    temp_unit = temp_unit.upper()
    if temp_unit == 'C':
        inside_temperature = inside_temperature + 273.15
        outside_temperature = outside_temperature + 273.15
        print('The temperatre of inside is ' + str(inside_temperature) + 'K')
        print('The temperatre of outside is ' + str(outside_temperature) + 'K')
        # Change Celcius to Kelvin and show it to user
        break
    elif temp_unit == 'F':
        inside_temperature = (5 / 9) * (inside_temperature - 32) + 273.15
        outside_temperature = (5 / 9) * (outside_temperature - 32) + 273.15
        print('The temperatre of inside is ' + str(inside_temperature) + 'K')
        print('The temperatre of outside is ' + str(outside_temperature) + 'K')
        # Change Farenheit to Kelvin and show it to user
        break
    elif temp_unit == 'K':
        print('Thank you for using Kelvin!')
        break
    else:
        print('Please enter a Valid answer.')


# checking the heat flow through the wall.
if inside_temperature > outside_temperature:
    temp_diff = inside_temperature - outside_temperature
    heat_flow = 'the heat flow is from inside to outside'
elif inside_temperature == outside_temperature:
    temp_diff = inside_temperature - outside_temperature
    heat_flow = 'there is no heat flow since the temperature difference is zero'
else:
    temp_diff = outside_temperature - inside_temperature
    heat_flow = 'the heat flow is from outside to inside'


# calculating the final answer and show it to user.
heat_flux = thermal_conductivity * (temp_diff / wall_thichness)
if Area == 'no'.lower():
    print('Since we do not have the area of wall we can not calculate heat transfer but heat flux is' +
          str(heat_flux) + 'W/m2 and the heat flow is' + heat_flow)
else:
    heat_transfer = heat_flux * Area
    print('The heat transfer is ' + str(heat_transfer) + ' (W) and heat flux is' +
          str(heat_flux) + '(W/m2) and the heat flow is' + heat_flow)
