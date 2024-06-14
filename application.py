from device_driver import DeviceDriver


class Application:
    def __init__(self, device_driver: DeviceDriver):
        self.__device_driver = device_driver

    def read_and_print(self, start_addr, end_addr):
        # start_addr ~ end_addr 까지 Read 수행 후 결과 출력
        result = []
        for addr in range(start_addr, end_addr + 1):
            result.append(self.__device_driver.read(addr))

        return result

    def write_all(self, value):
        # 0x00~ 0x04까지 모두 value 값으로 Write한다.
        self.__device_driver.write(0x00, value)
        self.__device_driver.write(0x01, value)
        self.__device_driver.write(0x02, value)
        self.__device_driver.write(0x03, value)
        self.__device_driver.write(0x04, value)
