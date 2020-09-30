from matplotlib import pyplot as plt
from calculation import calc_reynolds_number, calc_pressure_loss

#variable_height(0.1,1mm) --> Result
channel_heights = [x * 0.01 for x in range(10, 100, 2)]

cs_fff_5cm2_2ch = []
v_fff_5cm2_2ch = []
re_fff_5cm2_2ch = []
pressure_losses_fff_5cm2_2ch = []

# parameters sff_5cm2_3ch
channel_width_anode = 0.0004
flowrate_anode = (1e-6/60)
number_of_channels = 2
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.240

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
    print(fluid_velocity_anode)
    re_fff_5cm2_2ch.append(re_anode)
    pressure_losses_fff_5cm2_2ch.append(pressure_loss_i)



# fixed width --> channel_length
name = 'FFF 5cm2'
channel_width_anode = 0.0004
flowrate_anode = (1e-6/60)
number_of_channels = 2
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.179
channel_height = 0.00063
segments = [i for i in range(1, 14, 1)]
channel_length_segment = float(channel_length_anode) / len(segments)

pressure_loss_per_segment = []
segment_list = []
pressure_loss_sum_list = []
v_in_segment = []
avg_v = []
reynolds_number_per_segment = []
cross_section_segment = []
cross_section_segment_per_channel = []

pressure_loss_sum = 0
average_velocity = 0

width = channel_width_anode

for segment in segments:
    channel_cross_section = float(width) * \
                            float(channel_height)

    cross_section = float(channel_cross_section) * int(number_of_channels)

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(width) +
                                          float(channel_height))))

    fluid_velocity_anode = float(flowrate_anode) / float(cross_section)

    re_anode = calc_reynolds_number(fluid_density_anode,
                                    fluid_velocity_anode,
                                    hydraulic_diameter_anode,
                                    fluid_viscosity_anode)

    pressure_loss_segment_i = calc_pressure_loss(re_anode, channel_length_segment,
                                         hydraulic_diameter_anode,
                                         fluid_density_anode,
                                         fluid_velocity_anode,
                                         number_of_channels)

    pressure_loss_sum += pressure_loss_segment_i

    cross_section_segment.append(channel_cross_section * number_of_channels * 1000000)
    cross_section_segment_per_channel.append(channel_cross_section * 1000000)
    v_in_segment.append(fluid_velocity_anode)
    pressure_loss_per_segment.append(pressure_loss_segment_i)
    reynolds_number_per_segment.append(re_anode)
    pressure_loss_sum_list.append(pressure_loss_sum)
    segment_list.append(segment)

    average_velocity = sum(v_in_segment) / len(segment_list)
    avg_v.append(average_velocity)


#Graph A
ax1 = plt.subplot(2, 2, 1)
ax2 = ax1.twinx()

ax1.title.set_text(name + ' channel depth')
ax1.vlines(0.63, 0, max(v_fff_5cm2_2ch), colors='red')
ax1.hlines(0.0331, 0, max(channel_heights), colors='black', linestyle='dashed')
ax1.plot(channel_heights, v_fff_5cm2_2ch, label='flowfield-velocity ', color='green')
ax2.plot(channel_heights, pressure_losses_fff_5cm2_2ch, linestyle='dashed',
         label='pressure_loss', color='blue')
ax1.set_ylim(0, max(v_fff_5cm2_2ch)*1.1)
ax2.set_ylim(0, max(pressure_losses_fff_5cm2_2ch)*1.1)
ax1.set_xlim(0.1, max(channel_heights))
ax1.set_xlabel('Channel Depth [mm]', labelpad=10)
ax1.set_ylabel('Velocity [m/s]', labelpad=20)
ax2.set_ylabel('Pressure Loss [Pa]', labelpad=20)
ax1.legend(bbox_to_anchor=(0.5, 0.5, 0.5, 0.5))
ax2.legend(bbox_to_anchor=(0.5, 0.4, 0.5, 0.5))

ax3 = plt.subplot(2, 2, 3)
ax4 = ax3.twinx()

ax3.vlines(0.63, 0, max(pressure_losses_fff_5cm2_2ch), colors='black', linestyle='dashed')
ax3.hlines(880, 0, max(channel_heights), colors='red')
ax4.hlines(28.5, 0, max(channel_heights), colors='red')
ax3.plot(channel_heights, pressure_losses_fff_5cm2_2ch, label='pressure_loss', color='green')
ax4.plot(channel_heights, re_fff_5cm2_2ch, linestyle='dashed', label='reynolds_number', color='blue')
ax3.set_ylim(0, 5000)
ax4.set_ylim(0, max(re_fff_5cm2_2ch)*1.1)
ax3.set_xlim(0.53, 0.73)
ax3.set_xlabel('Channel Depth [mm]', labelpad=10)
ax3.set_ylabel('Pressure Loss [Pa]', labelpad=20)
ax4.set_ylabel('Reynolds Number', labelpad=20)
ax3.legend(bbox_to_anchor=(0.5, 0.5, 0.5, 0.5))
ax4.legend(bbox_to_anchor=(0.5, 0.4, 0.5, 0.5))


#Graph B
ax5 = plt.subplot(2, 2, 2)
ax6 = ax5.twinx()


#ax2.hlines(0.0331, 1, max(segment_list), colors='black')
#ax2.vlines(segments/2, 0, max(avg_v), colors='black')
ax5.title.set_text(name + ' along channel (0.63mm depth)')
ax5.plot(segments, v_in_segment, label='velocity', color='green')
ax6.plot(segments, pressure_loss_sum_list, linestyle='dashed', label='pressure_loss', color='blue')
ax5.set_ylim(0, max(v_in_segment)*1.1)
ax6.set_ylim(0, max(pressure_loss_sum_list)*1.1)
ax5.set_xlabel('Channel-Segment', labelpad=10)
ax5.set_ylabel('Velocity [m/s]', labelpad=20)
ax6.set_ylabel('Pressure Loss [Pa]', labelpad=20)
ax5.legend(bbox_to_anchor=(0.5, 0.2, 0.5, 0.5))
ax6.legend(bbox_to_anchor=(0.5, 0.1, 0.5, 0.5))



ax7 = plt.subplot(2, 2, 4)
ax8 = ax7.twinx()


#ax2.hlines(0.0331, 1, max(segment_list), colors='black')
#ax2.vlines(segments/2, 0, max(avg_v), colors='black')
ax7.plot(segments, cross_section_segment, label='flowfield_cross_section', color='green')
ax7.plot(segments, cross_section_segment_per_channel, label='cross_section_channel', color='green', linestyle='dashed')
ax8.plot(segments, reynolds_number_per_segment, linestyle='dashed', label='reynolds_number', color='blue')
ax7.set_ylim(0, max(cross_section_segment)*1.1)
ax8.set_ylim(0, max(reynolds_number_per_segment)*1.1)
ax7.set_xlabel('Channel-Segment', labelpad=10)
ax7.set_ylabel('Area [mm²]', labelpad=20)
ax8.set_ylabel('Reynolds Number', labelpad=20)
ax7.legend(bbox_to_anchor=(0.57, 0.05, 0.5, 0.5))
ax8.legend(bbox_to_anchor=(0.5, -0.15, 0.5, 0.5))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=None)

plt.show()