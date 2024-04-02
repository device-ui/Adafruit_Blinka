# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""fake_mcp2221 pin names"""
import random


class Pin:
    """A basic Pin class for use with a "fake" MCP2221."""

    # pin modes
    OUT = 0
    IN = 1
    ADC = 2
    DAC = 3
    # pin values
    LOW = 0
    HIGH = 1

    def __init__(self, pin_id=None):
        self.id = pin_id
        self._mode = None
        self._prv_val = False

    def init(self, mode=IN, pull=None):
        """Initialize the Pin"""
        if self.id is None:
            raise RuntimeError("Can not init a None type pin.")
        if pull is not None:
            raise NotImplementedError(
                "Internal pullups and pulldowns not supported on the MCP2221"
            )
        if mode == Pin.ADC:
            # ADC only available on these pins
            if self.id not in (1, 2, 3):
                raise ValueError("Pin does not have ADC capabilities")
            # Do nothing
        elif mode == Pin.DAC:
            # DAC only available on these pins
            if self.id not in (2, 3):
                raise ValueError("Pin does not have DAC capabilities")
        else:
            raise ValueError("Incorrect pin mode: {}".format(mode))
        self._mode = mode

    def value(self, val=None):
        """Set or return the Pin Value"""
        # Digital In / Out
        if self._mode in (Pin.IN, Pin.OUT):
            # digital read
            if val is None:
                # The returned value toggles between True and false
                self._prv_val = not self._prv_val
                return self._prv_val
            # digital write
            if val in (Pin.LOW, Pin.HIGH):
                # We don't need to do anything here - no data is produced
                return None
            # nope
            raise ValueError("Invalid value for pin.")
        # Analog In
        if self._mode == Pin.ADC:
            if val is None:
                # Returned value is between 0 and 65535 inclusive
                # https://docs.circuitpython.org/en/latest/shared-bindings/analogio/index.html#analogio.AnalogIn.value
                self._prv_val = random.randint(0, 65535)
                return self._prv_val
            # read only
            raise AttributeError("'AnalogIn' object has no attribute 'value'")
        # Analog Out
        if self._mode == Pin.DAC:
            if val is None:
                # write only
                raise AttributeError("unreadable attribute")
            # We don't write to the DAC as this is a "fake" implementation
            return None
        raise RuntimeError(
            "No action for mode {} with value {}".format(self._mode, val)
        )


# create pin instances for each pin
G0 = Pin(0)
G1 = Pin(1)
G2 = Pin(2)
G3 = Pin(3)

SCL = Pin()
SDA = Pin()
