# Performs a daqmx device test.
# Analog output and input, Digital I/O or Counter I/O.

import nidaqmx
import numpy as np

# Analog output test
def ao_test(device_name, channel_name, voltage):
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(device_name + '/' + channel_name)
        task.write(voltage, auto_start=True)

def ai_test(device_name, channel_name):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(device_name + '/' + channel_name)