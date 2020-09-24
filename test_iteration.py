from matplotlib import pyplot as plt
from calculation import calc_reynolds_number, calc_pressure_loss


#parameters divff_5cm2_2ch
channel_width_anode = [i * 0.00001 for i in [40, 45, 45, 50, 50, 55, 55,
                                             60, 60, 65, 65]]
channel_heights = [x * 0.0001 for x in range(1000, 10000, 2)]
flowrate_anode = (1e-6/60)
number_of_channels = 2
fluid_density_anode = 974.7
fluid_viscosity_anode = 0.00055289
channel_length_anode = 0.234
channel_height = 0.48
segments = len(channel_width_anode)
channel_length_segment = channel_length_anode / segments



eps = 1

while eps > 0.001:

    for height in channel_heights:
        pressure_loss_per_segment = []
        segment_list = []
        pressure_loss_sum_list = []
        v_in_segment = []
        avg_v = []

        pressure_loss_sum = 0
        segment = 0
        average_velocity = 0

        for width in channel_width_anode:
            segment += 1
            channel_cross_section = float(width) * \
                                    float(height / 1000)

            cross_section = float(channel_cross_section) * int(number_of_channels)

            hydraulic_diameter_anode = 4 * (channel_cross_section /
                                            (2 * (float(width) +
                                                  float(height / 1000))))

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
            segment_list.append(segment)
            average_velocity = sum(v_in_segment) / len(segment_list)
        # print("1")
        eps = ((0.0331 - average_velocity)) ** 2.0
        #print(eps, average_velocity, height)

        # if eps < 1e-8:
        #     break

print(eps, average_velocity, height)

