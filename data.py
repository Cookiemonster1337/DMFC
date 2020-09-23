import pandas as pd
from calculation import calc_reynolds_number, calc_pressure_loss, \
    calc_faradaic_stoichiometry
from matplotlib import pyplot as plt


fluid_viscosity_anode = 0.999
fluid_density_anode = 0.999

# import water_methanol_viscosity (csv) °C <--> mPas
df_water_methanol_viscosity = \
    pd.read_csv('feed_data/methanol_water_viscosity.txt', delimiter='\t',
                decimal=',')

# import water_methanol_density (csv) °C <--> g/cm3
df_water_methanol_density = \
    pd.read_csv('feed_data/methanol_water_density.txt', delimiter='\t',
                decimal=',')

# import methanol_spec_1bar (csv)
df_methanol_1bar_spec = \
    pd.read_csv('feed_data/nist_methanol_properties_1bar.txt', delimiter='\t',
                decimal='.')

df_water_1bar_spec = pd.read_csv('feed_data/nist_water_properties_1bar.txt', delimiter='\t',
                decimal='.')


# dictionary of physical constants needed in calculations
physical_constants = {'faradaic_constant': 96485.3        # As/mol
                      }

# dictionaries of specific fluid values
methanol_specific_values = {'molar_mass': 0.03204,       # kg/mol
                            'stoichiometric_air_requirement': 6.43
                            }

water_specific_values = {'molar_mass': 0.01801528          # kg/mol
                         }

# dictionary of dmfc specific values:
dmfc_specific_values = {'charge_number': 6
                        }

# dictionary to store calculated data:
result = {}

def convert_data(cell_temperature_anode, molarity, flowrate_anode,
                 channel_width_anode, channel_height_anode,
                 channel_length_anode, number_of_channels,
                 current_density, active_area, output_key, output_value,
                 output_unit):

    fluid_density_anode = \
        df_water_methanol_density[df_water_methanol_density['Temperatur'] ==
                                  int(cell_temperature_anode)][molarity + '_M']
    fluid_density_anode = float(fluid_density_anode) * 1000  # kg/m^3
    result['fluid_density_anode'] = [fluid_density_anode, 'kg/m³']
    print('fluid_density_anode ' + str(fluid_density_anode) + ' kg/m^3')

    fluid_viscosity_anode = \
        df_water_methanol_viscosity[df_water_methanol_viscosity['Temperatur'] ==
                                    int(cell_temperature_anode)][molarity + '_M']
    fluid_viscosity_anode = float(fluid_viscosity_anode) / 1000  # Pas
    result['fluid_viscosity_anode'] = [fluid_viscosity_anode*1000, 'mPas']
    print('fluid_viscosity_anode ' + str(fluid_viscosity_anode) + ' Pas')


    cell_temperature_anode = float(cell_temperature_anode) + 273.15  # K
    result['cell_temperature_anode'] = [cell_temperature_anode, 'K']
    print('cell_temperature_anode ' + str(cell_temperature_anode) + ' K')
    flowrate_anode = float(flowrate_anode) / (60 * 1000 * 1000)  # m^3 / s
    result['flowrate_anode'] = [flowrate_anode*1000*1000, 'cm³/s']
    print('flowrate_anode ' + str(flowrate_anode) + 'm^3/s')
    mass_flow_anode = float(flowrate_anode) * float(fluid_density_anode)
    result['mass_flow_anode'] = [mass_flow_anode*1000, 'g/s']
    print('mass_flow_anode ' + str(mass_flow_anode) + ' kg/s')
    channel_width_anode = float(channel_width_anode) / 1000  # m
    result['channel_width_anode'] = [channel_width_anode, 'm']
    print('channel_width_anode ' + str(channel_width_anode) + ' m')
    channel_height_anode = float(channel_height_anode) / 1000  # m
    result['channel_height_anode'] = [channel_height_anode, 'm']
    print('channel_height_anode ' + str(channel_height_anode) + ' m')
    channel_length_anode = float(channel_length_anode) / 1000  # m
    result['channel_length_anode'] = [channel_length_anode, 'm']
    print('channel_length_anode ' + str(channel_length_anode) + ' m')

    molar_volume_methanol = methanol_specific_values['molar_mass'] / \
                            float(fluid_density_anode)
    result['molar_volume_methanol'] = [molar_volume_methanol*1000*1000, 'cm³/mol']
    print('molar_volume_methanol ' + str(molar_volume_methanol) + ' m^3/mol')
    molar_volume_water = water_specific_values['molar_mass'] / \
                            float(fluid_density_anode)
    result['molar_volume_water'] = [molar_volume_water*1000*1000, 'cm³/mol']
    print('molar_volume_water ' + str(molar_volume_water) + ' m^3/mol')

    mass_methanol = float(molarity) * methanol_specific_values['molar_mass']
    result['mass_methanol'] = [mass_methanol*1000, 'g/kg']
    print('mass_methanol ' + str(mass_methanol) + ' kg/kg electrolyte')
    mass_water = 1 - (mass_methanol)
    result['mass_water'] = [mass_water*1000, 'g/kg']
    print('mass_water ' + str(mass_water) + ' kg/kg electrolyte')

    amount_of_methanol = float(mass_methanol) / methanol_specific_values['molar_mass']
    result['amount_of_methanol'] = [amount_of_methanol, 'mol']
    print('amount_of_methanol ' + str(amount_of_methanol) + ' mol')

    amount_of_water = float(mass_water) / water_specific_values['molar_mass']
    result['amount_of_water'] = [amount_of_water, 'mol']
    print('amount_of_water ' + str(amount_of_water) + ' mol')

    amount_of_electrolyte = float(amount_of_methanol) + float(amount_of_water)
    result['amount_of_electrolyte'] = [amount_of_electrolyte, 'mol']
    print('amount_of_electrolyte ' + str(amount_of_electrolyte) + ' mol')

    substance_fraction_methanol = float(amount_of_methanol) / \
                                  float(amount_of_electrolyte)
    result['substance_fraction_methanol'] = [substance_fraction_methanol, '']
    print('substance_fraction_methanol ' + str(substance_fraction_methanol))
    substance_fraction_water = float(amount_of_water) / \
                                  float(amount_of_electrolyte)
    result['substance_fraction_water'] = [substance_fraction_water, '']
    print('substance_fraction_water ' + str(substance_fraction_water))
    molar_mass_mixture = float(substance_fraction_methanol) * \
                         methanol_specific_values['molar_mass'] + \
                         float(substance_fraction_water) * \
                         water_specific_values['molar_mass']
    result['molar_mass_mixture'] = [molar_mass_mixture, 'mol']
    print('molar_mass_mixture ' + str(molar_mass_mixture) + ' mol')

    substance_flow_anode = float(mass_flow_anode) / float(molar_mass_mixture)
    result['substance_flow_anode'] = [substance_flow_anode, 'mol/s']
    print('substance_flow_anode ' + str(substance_flow_anode) + ' mol/s')

    substance_flow_methanol = float(substance_flow_anode) * \
                              float(substance_fraction_methanol)
    result['substance_flow_methanol'] = [substance_flow_methanol*60, 'mol/min']
    print('substance_flow_methanol ' + str(substance_flow_methanol) + ' mol/s')

    substance_flow_water = float(substance_flow_anode) * float(
        substance_fraction_water)
    result['substance_flow_water'] = [substance_flow_water*60, 'mol/min']
    print('substance_flow_water ' + str(substance_flow_water) + ' mol/s')

    mass_flow_methanol = float(substance_flow_methanol) * \
                         methanol_specific_values['molar_mass']
    result['mass_flow_methanol'] = [mass_flow_methanol*1000*1000, 'mg/s']
    print('mass_flow_methanol ' + str(mass_flow_methanol) + ' kg/s')

    mass_flow_water = float(substance_flow_water) * \
                         methanol_specific_values['molar_mass']
    result['mass_flow_water'] = [mass_flow_water*1000*1000, 'mg/s']
    print('mass_flow_water ' + str(mass_flow_water) + ' kg/s')
    
    channel_cross_section = float(channel_width_anode) * \
                            float(channel_height_anode)               # m^2
    result['channel_cross_section'] = [channel_cross_section*100*100, 'cm²']
    print('channel_cross_section ' + str(channel_cross_section) + ' m^2')

    fluid_velocity_anode = float(flowrate_anode) / \
                           (channel_cross_section * int(
                               number_of_channels))                   # m/s
    result['fluid_velocity_anode'] = [fluid_velocity_anode, 'm/s']
    print('fluid_velocity_anode ' + str(fluid_velocity_anode) + ' m/s')

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(channel_width_anode) +
                                    float(channel_height_anode))))    # m
    result['hydraulic_diameter_anode'] = [hydraulic_diameter_anode*100, 'cm']
    print('hydraulic_diameter_anode ' + str(hydraulic_diameter_anode) + ' m')

    re_anode = calc_reynolds_number(fluid_density_anode, fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)
    result['re_anode'] = [re_anode, ' ']
    print('re_anode ' + str(re_anode))

    pressure_loss_anode = calc_pressure_loss(re_anode, channel_length_anode,
                                             hydraulic_diameter_anode,
                                             fluid_density_anode,
                                             fluid_velocity_anode,
                                             number_of_channels)    # Pa
    result['pressure_loss_anode'] = [pressure_loss_anode, 'Pa']
    print('pressure_loss_anode ' + str(pressure_loss_anode) + ' Pa')

    current_density = int(current_density) / 1000
    result['current_density'] = [current_density*1000, 'mA/cm²']
    print('current density ' + str(current_density) + ' A/cm2')

    current = float(current_density) * int(active_area)
    result['current '] = [current, 'A']
    print('current ' + str(current) + ' A')

    faradaic_mf_anode, stoichiometry_anode = calc_faradaic_stoichiometry(
        dmfc_specific_values['charge_number'],
        physical_constants['faradaic_constant'],
        methanol_specific_values['molar_mass'],
        fluid_density_anode, current, flowrate_anode)

    result['faradaic_mf_anode'] = [faradaic_mf_anode*1000*1000*1000*60, 'µl/min']
    print('faradaic_mf_anode ' + str(faradaic_mf_anode) + ' m3/s')
    result['stoichiometry_anode'] = [stoichiometry_anode, '']
    print('stoichiometry_anode ' + str(stoichiometry_anode))

    result_key = ''
    result_value = ''
    result_unit = ''
    for key, value_list in result.items():
        result_key += key + ': \n'
        print(value_list)
        result_value += str(round(value_list[0],4)) + '\n'
        result_unit += str(value_list[1]) + '\n'


    output_key.set(result_key)
    output_value.set(result_value)
    output_unit.set(result_unit)

    #presssure_loss over channel height


