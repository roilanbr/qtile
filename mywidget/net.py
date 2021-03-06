from math import log
from typing import Tuple

import psutil

from libqtile.log_utils import logger
from libqtile.widget import base


class Net(base.ThreadPoolText):
    """
    Displays interface down and up speed. Widget requirements: psutil_.
    _psutil: https://pypi.org/project/psutil/
    """
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('format', '{interface}: {down} \u2193\u2191 {up}',
         'Display format of down-/upload speed of given interfaces'),
        ('interface', None, 'List of interfaces or single NIC as string to monitor, \
            None to displays all active NICs combined'),
        ('update_interval', 1, 'The update interval.'),
        ('use_bits', False, 'Use bits instead of bytes per second?'),
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(Net.defaults)
        if not isinstance(self.interface, list):
            if self.interface is None:
                self.interface = ["all"]
            elif isinstance(self.interface, str):
                self.interface = [self.interface]
            else:
                raise AttributeError("Invalid Argument passed: %s\nAllowed Types: List, String, None" % self.interface)
        self.stats = self.get_stats()

    def convert_b(self, num_bytes: float) -> Tuple[float, str]:
        """Converts the number of bytes to the correct unit"""
        factor = 1000.0

        if self.use_bits:
            letters = ["b", "kb", "Mb", "Gb", "Tb", "Pb", "Eb", "Zb", "Yb"]
            num_bytes *= 8
        else:
            letters = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

        if num_bytes > 0:
            power = int(log(num_bytes) / log(factor))
            power = max(min(power, len(letters) - 1), 0)
        else:
            power = 0

        converted_bytes = num_bytes / factor**power
        unit = letters[power]

        return converted_bytes, unit

    def get_stats(self):
        interfaces = {}
        if self.interface == ["all"]:
            net = psutil.net_io_counters(pernic=False)
            interfaces["all"] = {'down': net.bytes_recv, 'up': net.bytes_sent}
            return interfaces
        else:
            net = psutil.net_io_counters(pernic=True)
            for iface in net:
                down = net[iface].bytes_recv
                up = net[iface].bytes_sent
                interfaces[iface] = {'down': down, 'up': up}
            return interfaces

    def _format(self, down, down_letter, up, up_letter):
        max_len_down = 7 - len(down_letter)
        max_len_up = 7 - len(up_letter)
        down = '{val:{max_len}.1f}'.format(val=down, max_len=max_len_down)
        up = '{val:{max_len}.1f}'.format(val=up, max_len=max_len_up)
        return down[:max_len_down], up[:max_len_up]

    def poll(self):
        ret_stat = []
        try:
            new_stats = self.get_stats()
            for intf in self.interface:
                down = new_stats[intf]['down'] - \
                    self.stats[intf]['down']
                up = new_stats[intf]['up'] - \
                    self.stats[intf]['up']

                down = down / self.update_interval
                up = up / self.update_interval
                down, down_letter = self.convert_b(down)
                up, up_letter = self.convert_b(up)
                down, up = self._format(down, down_letter, up, up_letter)
                self.stats[intf] = new_stats[intf]
                ret_stat.append(
                    self.format.format(
                        **{
                            'interface': intf,
                            'down': down + down_letter,
                            'up': up + up_letter
                        }))

            return " ".join(ret_stat)
        except Exception as excp:
            logger.error('%s: Caught Exception:\n%s',
                         self.__class__.__name__, excp)