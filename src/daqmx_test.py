# Performs a daqmx device test.
# Analog output and input, Digital I/O or Counter I/O.

import nidaqmx
from devices import Devices

sys = Devices()

sys.set_current_device(10)

print(sys.get_devices_info())
print(sys.get_channels_types())