from random import randint

from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self.__device = device

    def write(self, address: int, data: int) -> None:
        if self.__device.read(address) != 0xFF:
            raise Exception

        self.__device.write(address, data)

    def read(self, address: int) -> int:
        result = self.read_five_times(address)

        self.assert_all_same(result)

        return result[0]

    def assert_all_same(self, result):
        for i in range(1, 5):
            if result[0] == result[i]:
                continue
            raise Exception

    def read_five_times(self, address):
        result = []
        for i in range(5):
            result.append(self.__device.read(address))
        return result
