import unittest
import sys
import time

import numpy as np

from urh.dev.native.RTLSDRTCP import RTLSDRTCP

class TestRTLSDRTCP(unittest.TestCase):

    def test_device_communication(self):
        error = 0
        sdr = RTLSDRTCP(0, 0, 0, device_number=0)
        sdr.open()
        if sdr.socket_is_open == False:
            error += 1
        if sdr.set_parameter("centerFreq", 927000000):
            error += 1
        if sdr.set_parameter("sampleRate", 2000000):
            error += 1
        if sdr.set_parameter("bandwidth", 2000000):
            error += 1
        if sdr.set_parameter("tunerGain", 200):
            error += 1
        data = sdr.read_sync()
        if len(data) < 1:
            error += 1
        sdr.close()
        self.assertEqual(error, 0)

