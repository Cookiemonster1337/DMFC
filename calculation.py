

# reynolds_number (anode - methanol-water feed)
def calc_reynolds_number(fluid_density_anode, fluid_velocity_anode,
                         char_length_anode, fluid_viscosity_anode):

    re_anode = (float(fluid_density_anode) * float(fluid_velocity_anode) *
                float(char_length_anode)) \
           / float(fluid_viscosity_anode)

    return re_anode

# pressure_loss along all channels (anode)
def calc_pressure_loss(re, channel_length, char_length,fluid_density,
                       fluid_velocity, number_of_channels):

    drag_coefficient_channel = 64 / re

    pressure_loss = drag_coefficient_channel * \
                          (float(channel_length) / float(char_length)) * \
                          ((fluid_density * fluid_velocity**2) / 2)
    pressure_loss = float(pressure_loss) * int(number_of_channels)

    return pressure_loss