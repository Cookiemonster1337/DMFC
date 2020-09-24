from matplotlib import pyplot as plt
from calculation import calc_reynolds_number, calc_pressure_loss


#parameters divff_5cm2_2ch
channel_width_anode = [i * 0.00001 for i in [40, 45, 45, 50, 50, 55, 55,
                                             60, 60, 65, 65]]
print(channel_width_anode)
flowrate_anode = (1e-6/60)
number_of_channels = 2
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.234
channel_height = 0.48
segments = len(channel_width_anode)
channel_length_segment = channel_length_anode / segments

pressure_loss_per_segment = []
segment_list = []
pressure_loss_sum_list = []
v_in_segment = []
avg_v = []

pressure_loss_sum = 0
segment = 0
average_velocity = 0

for width in channel_width_anode:
    segment +=1
    channel_cross_section = float(width) * \
                            float(channel_height / 1000)

    cross_section = float(channel_cross_section) * int(number_of_channels)

    hydraulic_diameter_anode = 4 * (channel_cross_section /
                                    (2 * (float(width) +
                                          float(channel_height / 1000))))

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


    v_in_segment.append(fluid_velocity_anode)
    pressure_loss_per_segment.append(pressure_loss_segment_i)
    pressure_loss_sum_list.append(pressure_loss_sum)
    segment_list.append(segment)

    average_velocity = sum(v_in_segment) / len(segment_list)
    avg_v.append(average_velocity)


ax1=plt.subplot(2,2,1)
ax2=ax1.twinx()

ax2.hlines(0.0331, 1, max(segment_list), colors='black')
ax2.vlines(segments/2, 0, max(avg_v), colors='black')
ax1.plot(segment_list, v_in_segment, label='DIVFF-5cm2-2ch')
ax2.plot(segment_list, avg_v, linestyle='dashed')
ax1.set_ylim(0, max(v_in_segment)*1.1)
ax2.set_ylim(0, max(avg_v)*1.1)
ax1.set_xlabel('Channel-Segment')
ax1.set_ylabel('Velocity-Segment [m/s')
ax2.set_ylabel('Average-Velocity-Flowfield [m/s]')

plt.show()