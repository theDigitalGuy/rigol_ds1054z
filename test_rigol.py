from rigol_ds1054z import rigol_ds1054z
import time
import matplotlib.pyplot as plt
import numpy as np

# rigol_ds1054z class functions were writen to allow the high-level script
#  to be easy to read. Values with units are passed as strings, where the
#  unit can be stripped and converted to a base-10 value to be multiplied
#  by the value passed with it. This script sets up I2C decoding on the scope
#  to demonstrate triggering on SDA data (you don't need a slave device,
#  the scope is just observing the master write out to the bus)

plt.close('all')
scope = rigol_ds1054z()
# scope.print_info()
# scope.reset()
scope.run_trigger()
scope.setup_mem_depth(memory_depth=6e3)

scope.setup_channel(channel=1,on=1,offset_divs=0.0, volts_per_div=1.0, probe=1.0)
scope.setup_channel(channel=2,on=1,offset_divs=0.0,volts_per_div=1.0, probe=1.0)
scope.setup_timebase(time_per_div='100us',delay='0us')
scope.setup_trigger(channel=2, slope_pos=1, level='500mv')
time.sleep(1)
scope.single_trigger()

# time.sleep(3)
# for measurement in scope.single_measurement_list:
# 	scope.get_measurement(channel=1, meas_type=measurement)

# scope.get_measurement(channel=1, meas_type=scope.max_voltage)
# scope.write_screen_capture(filename='rigol.png')

(time_data, data) = scope.get_raw_waveform_data(channel=1)
plt.plot(time_data, data)

(time_data, data) = scope.get_raw_waveform_data(channel=2)
plt.plot(time_data, data)
plt.show()
plt.grid()

# scope.write_waveform_data(channel=1) # write to csv file
# scope.write_waveform_data(channel=2)
# scope.close()
