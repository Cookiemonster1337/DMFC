from matplotlib import pyplot as plt
from calculation import calc_reynolds_number, calc_pressure_loss

channel_heights = [x * 0.01 for x in range(10, 100, 2)]

cs_fff_5cm2_3ch = []
v_fff_5cm2_3ch = []
re_fff_5cm2_3ch = []
pressure_losses_fff_5cm2_3ch = []

# parameters sff_5cm2_3ch
channel_width_anode = 0.0004
flowrate_anode = (1e-6/60)
number_of_channels = 3
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.179

for i in channel_heights:
    channel_cross_section = float(channel_width_anode) * \
                            float(i/1000)

    cross_section = float(channel_cross_section) * int(number_of_channels)

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(channel_width_anode) +
                                          float(i/1000))))

    fluid_velocity_anode = float(flowrate_anode) / float(cross_section)

    re_anode = calc_reynolds_number(fluid_density_anode,
                                    fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)

    pressure_loss_i = calc_pressure_loss(re_anode, channel_length_anode,
                                         hydraulic_diameter_anode,
                                         fluid_density_anode,
                                         fluid_velocity_anode,
                                         number_of_channels)

    cs_fff_5cm2_3ch.append(cross_section*1000*1000)
    v_fff_5cm2_3ch.append(fluid_velocity_anode)
    re_fff_5cm2_3ch.append(re_anode)
    pressure_losses_fff_5cm2_3ch.append(pressure_loss_i)


cs_fff_5cm2_2ch = []
v_fff_5cm2_2ch = []
re_fff_5cm2_2ch = []
pressure_losses_fff_5cm2_2ch = []

# parameters sff_5cm2_2ch
channel_width_anode = 0.0004
flowrate_anode = (1e-6/60)
number_of_channels = 2
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.266

for i in channel_heights:
    channel_cross_section = float(channel_width_anode) * \
                            float(i/1000)

    cross_section = float(channel_cross_section) * int(number_of_channels)

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(channel_width_anode) +
                                          float(i/1000))))

    fluid_velocity_anode = float(flowrate_anode) / float(cross_section)

    re_anode = calc_reynolds_number(fluid_density_anode,
                                    fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)

    pressure_loss_i = calc_pressure_loss(re_anode, channel_length_anode,
                                         hydraulic_diameter_anode,
                                         fluid_density_anode,
                                         fluid_velocity_anode,
                                         number_of_channels)

    cs_fff_5cm2_2ch.append(cross_section*1000*1000)
    v_fff_5cm2_2ch.append(fluid_velocity_anode)
    re_fff_5cm2_2ch.append(re_anode)
    pressure_losses_fff_5cm2_2ch.append(pressure_loss_i)



cs_fff_25cm2_7ch = []
v_fff_25cm2_7ch = []
re_fff_25cm2_7ch = []
pressure_losses_fff_25cm2_7ch = []

# parameters_fff_25cm2_7ch
channel_width_anode = 0.0004
flowrate_anode = (5e-6/60)
number_of_channels = 7
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.429

for i in channel_heights:
    channel_cross_section = float(channel_width_anode) * \
                            float(i/1000)

    cross_section = float(channel_cross_section) * int(number_of_channels)

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(channel_width_anode) +
                                          float(i/1000))))

    fluid_velocity_anode = float(flowrate_anode) / float(cross_section)

    re_anode = calc_reynolds_number(fluid_density_anode,
                                    fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)

    pressure_loss_i = calc_pressure_loss(re_anode, channel_length_anode,
                                         hydraulic_diameter_anode,
                                         fluid_density_anode,
                                         fluid_velocity_anode,
                                         number_of_channels)

    cs_fff_25cm2_7ch.append(cross_section*1000*1000)
    v_fff_25cm2_7ch.append(fluid_velocity_anode)
    re_fff_25cm2_7ch.append(re_anode)
    pressure_losses_fff_25cm2_7ch.append(pressure_loss_i)

ax1 = plt.subplot(2, 1, 1)
ax2 = ax1.twinx()

ax1.vlines(0.9, 0, 20000, colors='black', label='FFF-25cm2-Design')
ax1.vlines(0.63, 0, 20000, colors='red', label='5cm2-eq. velocity')
ax1.plot(channel_heights, pressure_losses_fff_25cm2_7ch, label='25cm² - 7channels')
ax2.plot(channel_heights, re_fff_25cm2_7ch, linestyle='dashed')
ax1.plot(channel_heights, pressure_losses_fff_5cm2_2ch, label='5cm² - 2channels')
ax2.plot(channel_heights, re_fff_5cm2_2ch, linestyle='dashed')
ax1.plot(channel_heights, pressure_losses_fff_5cm2_3ch, label='5cm² - 3channels')
ax2.plot(channel_heights, re_fff_5cm2_3ch, linestyle='dashed')
ax1.set_ylim(0, 20000)
ax1.set_xlabel('Channel Depth [mm]')
ax1.set_ylabel('Pressure Loss [Pa]')
ax2.set_ylabel('Reynolds Number')
ax1.legend(loc=2, bbox_to_anchor=(0, 0.8, 0.5, 0.5), ncol=2)


ax3 = plt.subplot(2, 1, 2)
ax4 = ax3.twinx()

ax4.hlines(0.504, 0, 1)
ax3.vlines(0.9, 0, 0.3, colors='black', label='FFF-25cm2-Design')
#ax3.vlines(0.00063, 0, 0.3, colors='red', label='5cm2-eq. velocity')
ax3.plot(channel_heights, v_fff_25cm2_7ch, label='25cm² - 7channels')
ax4.plot(channel_heights, cs_fff_25cm2_7ch, linestyle='dashed')
ax3.plot(channel_heights, v_fff_5cm2_2ch, label='5cm² - 2channels')
ax4.plot(channel_heights, cs_fff_5cm2_2ch, linestyle='dashed')
ax3.plot(channel_heights, v_fff_5cm2_3ch, label='5cm² - 3channels')
ax4.plot(channel_heights, cs_fff_5cm2_3ch, linestyle='dashed')
ax3.set_ylim(0, 0.3)
ax3.set_xlabel('Channel Depth [mm]')
ax3.set_ylabel('Fluid Velocity [m/s]')
ax4.set_ylabel('Cross Section [mm²]')

plt.show()

