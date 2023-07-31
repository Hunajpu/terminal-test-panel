# Retrive modular instruments and daqmx devices names, and its properties 
# from the system (channels, type of task, etc).

import nidaqmx

class Devices:
    def __init__(self) -> None:
        self._current_device = 0
        # Create a list of devices
        local_system = nidaqmx.system.System.local()
        self.devices = []
        for device in local_system.devices:
            self.devices.append(device)
        
    def get_devices_info(self):
        information_string = ""
        device_index = 0

        for device in self.devices:
            information_string = information_string + "{0} - Device Name: {1}, Product Category: {2}, Product Type: {3}".format(
            device_index, device.name, device.product_category, device.product_type) + "\n"
            device_index = device_index + 1
        return information_string
    
    def get_channels_types(self):
        # Retruns a string with the channels types of the current device
        channels_types_string = ""

        # Check if the device has analog input channels
        if self.devices[self._current_device].ai_physical_chans:
            channels_types_string = channels_types_string + "Analog Input Channels\n"

        # Check if the device has analog output channels
        if self.devices[self._current_device].ao_physical_chans:
            channels_types_string = channels_types_string + "Analog Output Channels\n"

        # Check if the device has digital I/O channels
        if self.devices[self._current_device].di_lines or self.devices[self._current_device].do_lines:
            channels_types_string = channels_types_string + "Digital I/O Channels\n"

        # Check if the device has counter I/O channels
        if self.devices[self._current_device].ci_physical_chans or self.devices[self._current_device].co_physical_chans:
            channels_types_string = channels_types_string + "Counter I/O Channels\n"
            
        return channels_types_string
    
    def get_options(self):
        pass

    def set_current_device(self, device_index):
        self._current_device = device_index
    
    @property
    def current_device(self):
        return self._current_device