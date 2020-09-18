import pandas as pd
from calculation import calc_reynolds_number, calc_pressure_loss

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


def convert_data(cell_temperature_anode, molarity, flowrate_anode,
                 channel_width_anode, channel_height_anode,
                 channel_length_anode, number_of_channels):
    fluid_viscosity_anode = \
        df_water_methanol_density[df_water_methanol_density['Temperatur'] ==
                                  int(cell_temperature_anode)][molarity + '_M']
    fluid_viscosity_anode = float(fluid_viscosity_anode) / 1000  # Pas
    print('fluid_viscosity_anode ' + str(fluid_viscosity_anode) + ' Pas')

    fluid_density_anode = \
        df_water_methanol_viscosity[df_water_methanol_viscosity['Temperatur'] ==
                                    int(cell_temperature_anode)][
            molarity + '_M']
    fluid_density_anode = float(fluid_density_anode) * 1000  # kg/m^3
    print('fluid_density_anode ' + str(fluid_density_anode) + ' kg/m^3')

    cell_temperature_anode = float(cell_temperature_anode) + 273.15   # K
    print('cell_temperature_anode ' + str(cell_temperature_anode) + ' K')
    flowrate_anode = float(flowrate_anode) / (60 * 1000 * 1000)       # m^3 / s
    print('flowrate_anode ' + str(flowrate_anode) + 'm^3/s')
    channel_width_anode = float(channel_width_anode) / 1000           # m
    print('channel_width_anode ' + str(channel_width_anode) + ' m')
    channel_height_anode = float(channel_height_anode) / 1000         # m
    print('channel_height_anode ' + str(channel_height_anode) + ' m')
    channel_length_anode = float(channel_length_anode) / 1000         # m
    print('channel_length_anode ' + str(channel_length_anode) + ' m')

    channel_cross_section = float(channel_width_anode) * \
                            float(channel_height_anode)               # m^2
    print('channel_cross_section ' + str(channel_cross_section) + ' m^2')

    fluid_velocity_anode = float(flowrate_anode) / \
                           (channel_cross_section * float(
                               number_of_channels))                   # m/s
    print('fluid_velocity_anode ' + str(fluid_velocity_anode) + ' m/s')

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(channel_width_anode) +
                                    float(channel_height_anode))))    # m
    print('hydraulic_diameter_anode ' + str(hydraulic_diameter_anode) + ' m')

    re_anode = calc_reynolds_number(fluid_density_anode, fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)
    print('re_anode ' + str(re_anode))

    pressure_loss_anode = calc_pressure_loss(re_anode, channel_length_anode,
                                             hydraulic_diameter_anode,
                                             fluid_density_anode,
                                             fluid_velocity_anode,
                                             number_of_channels)    # Pa
    print('pressure_loss_anode ' + str(pressure_loss_anode) + ' Pa')
