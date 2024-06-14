from unittest import TestCase
from unittest.mock import Mock
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):
    def test_successful_read(self):
        mk = Mock()
        driver = DeviceDriver(mk)

        mk.read.side_effect = [1, 1, 1, 1, 1]

        driver.read(0xAB)

        self.assertEqual(mk.read.call_count, 5)

    def test_read_exception(self):
        mk = Mock()
        driver = DeviceDriver(mk)

        mk.read.side_effect = [1, 1, 2, 1, 1]

        with self.assertRaises(Exception):
            driver.read(0xAB)

    def test_success_read(self):
        mk = Mock()
        driver = DeviceDriver(mk)

        mk.read.side_effect = [1, 1, 1, 1, 1]

        self.assertEqual(driver.read(0xAB), 1)

    def test_write_read(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0xFF

        driver.write(0xAB, 12)
        self.assertEqual(mk.read.call_count, 1)

    def test_write_exception(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0x12

        with self.assertRaises(Exception):
            driver.write(0xAB, 12)

    def test_write_success(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0xFF
        driver.write(0xAB, 12)

        self.assertEqual(mk.write.call_count, 1)
