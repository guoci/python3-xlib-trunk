#!/usr/bin/env python3

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import string
import unittest
from Xlib.protocol import request, rq, event
import Xlib.protocol.event

import struct
import array

class CmpArray:
    def __init__(self, *args, **kws):
        self.array = array.array(*args, **kws)

    def __len__(self):
        return len(self.array)

    def __getslice__(self, x, y):
        return list(self.array[x:y])

    def __getattr__(self, attr):
        return getattr(self.array, attr)

    def __eq__(self, other):
        return self.array.tolist() == other

    def __ne__(self, other):
        return self.array.tolist() != other

rq.array = CmpArray

def tohex(bin):
    bin = ''.join('\\x%02x' % c for c in bin])

    bins = []
    for i in range(0, len(bin), 16):
        bins.append(bin[i:i+16])

    bins2 = []
    for i in range(0, len(bins), 2):
        try:
            bins2.append("'%s' '%s'" % (bins[i], bins[i + 1]))
        except IndexError:
            bins2.append("'%s'" % bins[i])

    return ' \\\n            '.join(bins2)

class DummyDisplay:
    def get_resource_class(self, x):
        return None

    event_classes = Xlib.protocol.event.event_class
dummy_display = DummyDisplay()


def check_endian():
    if struct.unpack('BB', struct.pack('H', 0x0100))[0] != 1:
        sys.stderr.write('Big-endian tests, skipping on this system.\n')
        sys.exit(0)



class TestCreateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 38608,
            'window_class': 0,
            'border_width': 34451,
            'visual': 398069779,
            'x': -20771,
            'y': -4049,
            'parent': 1960526158,
            'attrs': {'backing_pixel': 561400151, 'cursor': 1442692293, 'background_pixmap': 1583833923, 'border_pixmap': 1992559786, 'backing_planes': 1454152605, 'win_gravity': 3, 'backing_store': 2, 'event_mask': 368242204, 'save_under': 0, 'background_pixel': 209127175, 'colormap': 377416705, 'border_pixel': 2135465356, 'bit_gravity': 0, 'do_not_propagate_mask': 597142897, 'override_redirect': 0},
            'wid': 1828913444,
            'depth': 186,
            'width': 51466,
            }
        self.req_bin_0 = b'\x01\xba\x00\x17' b'\x6d\x03\x01\x24' \
            b'\x74\xdb\x41\x4e' b'\xae\xdd\xf0\x2f' \
            b'\xc9\x0a\x96\xd0' b'\x86\x93\x00\x00' \
            b'\x17\xba\x10\x13' b'\x00\x00\x7f\xff' \
            b'\x5e\x67\x63\x43' b'\x0c\x77\x07\x07' \
            b'\x76\xc4\x0c\xaa' b'\x7f\x48\x9d\x8c' \
            b'\x00\x00\x00\x00' b'\x03\x00\x00\x00' \
            b'\x02\x00\x00\x00' b'\x56\xac\x9b\x9d' \
            b'\x21\x76\x49\x57' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x15\xf2\xee\x1c' \
            b'\x23\x97\xad\x71' b'\x16\x7e\xec\x01' \
            b'\x55\xfd\xbc\xc5'


    def testPackRequest0(self):
        bin = request.CreateWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeWindowAttributes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1813552124,
            'attrs': {'backing_pixel': 59516078, 'cursor': 1682969315, 'background_pixmap': 370313360, 'border_pixmap': 1158771722, 'backing_planes': 1432315664, 'win_gravity': 3, 'backing_store': 1, 'event_mask': 1054128649, 'save_under': 0, 'background_pixel': 1953340842, 'colormap': 1462101672, 'border_pixel': 287436510, 'bit_gravity': 10, 'do_not_propagate_mask': 1283834625, 'override_redirect': 0},
            }
        self.req_bin_0 = b'\x02\x00\x00\x12' b'\x6c\x18\x9b\xfc' \
            b'\x00\x00\x7f\xff' b'\x16\x12\x88\x90' \
            b'\x74\x6d\x9d\xaa' b'\x45\x11\x74\x0a' \
            b'\x11\x21\xee\xde' b'\x0a\x00\x00\x00' \
            b'\x03\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x55\x5f\x67\x10' b'\x03\x8c\x24\xae' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x3e\xd4\xba\x09' b'\x4c\x85\xc3\x01' \
            b'\x57\x25\xe6\xa8' b'\x64\x50\x12\xe3'


    def testPackRequest0(self):
        bin = request.ChangeWindowAttributes._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetWindowAttributes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1931593850,
            }
        self.req_bin_0 = b'\x03\x00\x00\x02' b'\x73\x21\xc8\x7a'

        self.reply_args_0 = {
            'sequence_number': 60057,
            'backing_pixel': 136561993,
            'your_event_mask': 1332399119,
            'map_is_installed': 0,
            'visual': 687387929,
            'backing_bit_planes': 990144409,
            'backing_store': 147,
            'win_class': 18284,
            'map_state': 185,
            'save_under': 0,
            'all_event_masks': 270223628,
            'colormap': 1161384334,
            'win_gravity': 157,
            'bit_gravity': 253,
            'do_not_propagate_mask': 33787,
            'override_redirect': 0,
            }
        self.reply_bin_0 = b'\x01\x93\xea\x99' b'\x00\x00\x00\x03' \
            b'\x28\xf8\xb5\x19' b'\x47\x6c\xfd\x9d' \
            b'\x3b\x04\x67\x99' b'\x08\x23\xc5\x49' \
            b'\x00\x00\xb9\x00' b'\x45\x39\x51\x8e' \
            b'\x10\x1b\x49\x0c' b'\x4f\x6a\xcc\x0f' \
            b'\x83\xfb\x00\x00'


    def testPackRequest0(self):
        bin = request.GetWindowAttributes._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetWindowAttributes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetWindowAttributes._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetWindowAttributes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestDestroyWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1622184267,
            }
        self.req_bin_0 = b'\x04\x00\x00\x02' b'\x60\xb0\x91\x4b'


    def testPackRequest0(self):
        bin = request.DestroyWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.DestroyWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestDestroySubWindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1000376476,
            }
        self.req_bin_0 = b'\x05\x00\x00\x02' b'\x3b\xa0\x88\x9c'


    def testPackRequest0(self):
        bin = request.DestroySubWindows._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.DestroySubWindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeSaveSet(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1577523459,
            'mode': 0,
            }
        self.req_bin_0 = b'\x06\x00\x00\x02' b'\x5e\x07\x19\x03'


    def testPackRequest0(self):
        bin = request.ChangeSaveSet._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeSaveSet._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestReparentWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'parent': 72188776,
            'window': 1300734112,
            'x': -5207,
            'y': -22675,
            }
        self.req_bin_0 = b'\x07\x00\x00\x04' b'\x4d\x87\xa0\xa0' \
            b'\x04\x4d\x83\x68' b'\xeb\xa9\xa7\x6d'


    def testPackRequest0(self):
        bin = request.ReparentWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ReparentWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 61469476,
            }
        self.req_bin_0 = b'\x08\x00\x00\x02' b'\x03\xa9\xf3\x24'


    def testPackRequest0(self):
        bin = request.MapWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.MapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestMapSubwindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 818738118,
            }
        self.req_bin_0 = b'\x09\x00\x00\x02' b'\x30\xcc\xf3\xc6'


    def testPackRequest0(self):
        bin = request.MapSubwindows._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.MapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUnmapWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1923663468,
            }
        self.req_bin_0 = b'\x0a\x00\x00\x02' b'\x72\xa8\xc6\x6c'


    def testPackRequest0(self):
        bin = request.UnmapWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UnmapWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUnmapSubwindows(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 999740194,
            }
        self.req_bin_0 = b'\x0b\x00\x00\x02' b'\x3b\x96\xd3\x22'


    def testPackRequest0(self):
        bin = request.UnmapSubwindows._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UnmapSubwindows._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConfigureWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 190634459,
            'attrs': {'height': 57788, 'stack_mode': 2, 'border_width': -320, 'width': 53674, 'x': -2248, 'y': -29960, 'sibling': 1012823324},
            }
        self.req_bin_0 = b'\x0c\x00\x00\x0a' b'\x0b\x5c\xd9\xdb' \
            b'\x00\x7f\x00\x00' b'\xf7\x38\x00\x00' \
            b'\x8a\xf8\x00\x00' b'\xd1\xaa\x00\x00' \
            b'\xe1\xbc\x00\x00' b'\xfe\xc0\x00\x00' \
            b'\x3c\x5e\x75\x1c' b'\x02\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ConfigureWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ConfigureWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCirculateWindow(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1712979067,
            'direction': 1,
            }
        self.req_bin_0 = b'\x0d\x01\x00\x02' b'\x66\x19\xfc\x7b'


    def testPackRequest0(self):
        bin = request.CirculateWindow._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CirculateWindow._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetGeometry(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 680179490,
            }
        self.req_bin_0 = b'\x0e\x00\x00\x02' b'\x28\x8a\xb7\x22'

        self.reply_args_0 = {
            'height': 64954,
            'sequence_number': 39469,
            'root': 609586545,
            'border_width': 496,
            'x': -1253,
            'y': -11180,
            'depth': 204,
            'width': 38433,
            }
        self.reply_bin_0 = b'\x01\xcc\x9a\x2d' b'\x00\x00\x00\x00' \
            b'\x24\x55\x8d\x71' b'\xfb\x1b\xd4\x54' \
            b'\x96\x21\xfd\xba' b'\x01\xf0\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetGeometry._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetGeometry._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetGeometry._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetGeometry._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryTree(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 2052496265,
            }
        self.req_bin_0 = b'\x0f\x00\x00\x02' b'\x7a\x56\x9b\x89'

        self.reply_args_0 = {
            'sequence_number': 33887,
            'children': [1795767666, 1494491557, 748301378, 729512097, 1262057849, 64238195, 1088261715],
            'root': 1856577120,
            'parent': 2105827407,
            }
        self.reply_bin_0 = b'\x01\x00\x84\x5f' b'\x00\x00\x00\x07' \
            b'\x6e\xa9\x1e\x60' b'\x7d\x84\x60\x4f' \
            b'\x00\x07\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x6b\x09\x3d\x72' b'\x59\x14\x21\xa5' \
            b'\x2c\x9a\x2c\x42' b'\x2b\x7b\x78\xa1' \
            b'\x4b\x39\x79\x79' b'\x03\xd4\x32\x73' \
            b'\x40\xdd\x8e\x53'


    def testPackRequest0(self):
        bin = request.QueryTree._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryTree._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryTree._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryTree._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestInternAtom(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'only_if_exists': 0,
            'name': 'fuzzy_prop',
            }
        self.req_bin_0 = b'\x10\x00\x00\x05' b'\x00\x0a\x00\x00' \
            b'\x66\x75\x7a\x7a' b'\x79\x5f\x70\x72' \
            b'\x6f\x70\x00\x00'

        self.reply_args_0 = {
            'atom': 48723297,
            'sequence_number': 35223,
            }
        self.reply_bin_0 = b'\x01\x00\x89\x97' b'\x00\x00\x00\x00' \
            b'\x02\xe7\x75\x61' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.InternAtom._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.InternAtom._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.InternAtom._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.InternAtom._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetAtomName(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'atom': 1022286544,
            }
        self.req_bin_0 = b'\x11\x00\x00\x02' b'\x3c\xee\xda\xd0'

        self.reply_args_0 = {
            'sequence_number': 22699,
            'name': 'WM_CLASS',
            }
        self.reply_bin_0 = b'\x01\x00\x58\xab' b'\x00\x00\x00\x02' \
            b'\x00\x08\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x57\x4d\x5f\x43' b'\x4c\x41\x53\x53'


    def testPackRequest0(self):
        bin = request.GetAtomName._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetAtomName._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetAtomName._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetAtomName._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            'data': (8, ''),
            'property': 2085394193,
            'window': 266197951,
            'type': 1343008022,
            }
        self.req_bin_0 = b'\x12\x00\x00\x06' b'\x0f\xdd\xdb\xbf' \
            b'\x7c\x4c\x97\x11' b'\x50\x0c\xad\x16' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_1 = {
            'mode': 2,
            'data': (8, 'foo'),
            'property': 449719979,
            'window': 1522118044,
            'type': 121096013,
            }
        self.req_bin_1 = b'\x12\x02\x00\x07' b'\x5a\xb9\xad\x9c' \
            b'\x1a\xce\x2e\xab' b'\x07\x37\xc7\x4d' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x66\x6f\x6f\x00'

        self.req_args_2 = {
            'mode': 2,
            'data': (8, 'zoom'),
            'property': 1009841498,
            'window': 286324270,
            'type': 1547457396,
            }
        self.req_bin_2 = b'\x12\x02\x00\x07' b'\x11\x10\xf6\x2e' \
            b'\x3c\x30\xf5\x5a' b'\x5c\x3c\x53\x74' \
            b'\x08\x00\x00\x00' b'\x00\x00\x00\x04' \
            b'\x7a\x6f\x6f\x6d'

        self.req_args_3 = {
            'mode': 0,
            'data': (16, []),
            'property': 426983104,
            'window': 1964921608,
            'type': 692879036,
            }
        self.req_bin_3 = b'\x12\x00\x00\x06' b'\x75\x1e\x53\x08' \
            b'\x19\x73\x3e\xc0' b'\x29\x4c\x7e\xbc' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_4 = {
            'mode': 0,
            'data': (16, [1, 2, 3]),
            'property': 801006756,
            'window': 560040176,
            'type': 2030208993,
            }
        self.req_bin_4 = b'\x12\x00\x00\x08' b'\x21\x61\x88\xf0' \
            b'\x2f\xbe\x64\xa4' b'\x79\x02\x87\xe1' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x00'

        self.req_args_5 = {
            'mode': 0,
            'data': (16, [1, 2, 3, 4]),
            'property': 1401687842,
            'window': 2016421454,
            'type': 434059096,
            }
        self.req_bin_5 = b'\x12\x00\x00\x08' b'\x78\x30\x26\x4e' \
            b'\x53\x8c\x0f\x22' b'\x19\xdf\x37\x58' \
            b'\x10\x00\x00\x00' b'\x00\x00\x00\x04' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x04'

        self.req_args_6 = {
            'mode': 2,
            'data': (32, []),
            'property': 1008934075,
            'window': 461926013,
            'type': 613217208,
            }
        self.req_bin_6 = b'\x12\x02\x00\x06' b'\x1b\x88\x6e\x7d' \
            b'\x3c\x23\x1c\xbb' b'\x24\x8c\xf3\xb8' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x00'

        self.req_args_7 = {
            'mode': 1,
            'data': (32, [1, 2, 3]),
            'property': 1472503640,
            'window': 367636986,
            'type': 1085552939,
            }
        self.req_bin_7 = b'\x12\x01\x00\x09' b'\x15\xe9\xb1\xfa' \
            b'\x57\xc4\x9f\x58' b'\x40\xb4\x39\x2b' \
            b'\x20\x00\x00\x00' b'\x00\x00\x00\x03' \
            b'\x00\x00\x00\x01' b'\x00\x00\x00\x02' \
            b'\x00\x00\x00\x03'


    def testPackRequest0(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest1(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_1)
        try:
            assert bin == self.req_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_1
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest2(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_2)
        try:
            assert bin == self.req_bin_2
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest2(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_2, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_2
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest3(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_3)
        try:
            assert bin == self.req_bin_3
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest3(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_3, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_3
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest4(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_4)
        try:
            assert bin == self.req_bin_4
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest4(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_4, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_4
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest5(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_5)
        try:
            assert bin == self.req_bin_5
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest5(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_5, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_5
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest6(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_6)
        try:
            assert bin == self.req_bin_6
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest6(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_6, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_6
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest7(self):
        bin = request.ChangeProperty._request.to_binary(*(), **self.req_args_7)
        try:
            assert bin == self.req_bin_7
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest7(self):
        args, remain = request.ChangeProperty._request.parse_binary(self.req_bin_7, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_7
        except AssertionError:
            raise AssertionError(args)


class TestDeleteProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'property': 506897017,
            'window': 381870530,
            }
        self.req_bin_0 = b'\x13\x00\x00\x03' b'\x16\xc2\xe1\xc2' \
            b'\x1e\x36\xa2\x79'


    def testPackRequest0(self):
        bin = request.DeleteProperty._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.DeleteProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetProperty(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'delete': 0,
            'long_offset': 1563462862,
            'type': 1556454304,
            'property': 1007774483,
            'window': 1477792536,
            'long_length': 1346507413,
            }
        self.req_bin_0 = b'\x14\x00\x00\x06' b'\x58\x15\x53\x18' \
            b'\x3c\x11\x6b\x13' b'\x5c\xc5\x9b\xa0' \
            b'\x5d\x30\x8c\xce' b'\x50\x42\x12\x95'

        self.reply_args_0 = {
            'value': (8, ''),
            'sequence_number': 30606,
            'property_type': 1392423916,
            'bytes_after': 2046056935,
            }
        self.reply_bin_0 = b'\x01\x08\x77\x8e' b'\x00\x00\x00\x00' \
            b'\x52\xfe\xb3\xec' b'\x79\xf4\x59\xe7' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_1 = {
            'value': (8, 'foo'),
            'sequence_number': 44279,
            'property_type': 186441230,
            'bytes_after': 469299413,
            }
        self.reply_bin_1 = b'\x01\x08\xac\xf7' b'\x00\x00\x00\x01' \
            b'\x0b\x1c\xde\x0e' b'\x1b\xf8\xf0\xd5' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x66\x6f\x6f\x00'

        self.reply_args_2 = {
            'value': (8, 'zoom'),
            'sequence_number': 12674,
            'property_type': 1802804296,
            'bytes_after': 1968158856,
            }
        self.reply_bin_2 = b'\x01\x08\x31\x82' b'\x00\x00\x00\x01' \
            b'\x6b\x74\x9c\x48' b'\x75\x4f\xb8\x88' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7a\x6f\x6f\x6d'

        self.reply_args_3 = {
            'value': (16, []),
            'sequence_number': 25311,
            'property_type': 536196393,
            'bytes_after': 1874157309,
            }
        self.reply_bin_3 = b'\x01\x10\x62\xdf' b'\x00\x00\x00\x00' \
            b'\x1f\xf5\xb5\x29' b'\x6f\xb5\x5e\xfd' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_4 = {
            'value': (16, [1, 2, 3]),
            'sequence_number': 22665,
            'property_type': 1046879880,
            'bytes_after': 1952710167,
            }
        self.reply_bin_4 = b'\x01\x10\x58\x89' b'\x00\x00\x00\x02' \
            b'\x3e\x66\x1e\x88' b'\x74\x63\xfe\x17' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x00'

        self.reply_args_5 = {
            'value': (16, [1, 2, 3, 4]),
            'sequence_number': 19028,
            'property_type': 1014173132,
            'bytes_after': 1791090668,
            }
        self.reply_bin_5 = b'\x01\x10\x4a\x54' b'\x00\x00\x00\x02' \
            b'\x3c\x73\x0d\xcc' b'\x6a\xc1\xdf\xec' \
            b'\x00\x00\x00\x04' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x01\x00\x02' b'\x00\x03\x00\x04'

        self.reply_args_6 = {
            'value': (32, []),
            'sequence_number': 47226,
            'property_type': 2053870497,
            'bytes_after': 1727548898,
            }
        self.reply_bin_6 = b'\x01\x20\xb8\x7a' b'\x00\x00\x00\x00' \
            b'\x7a\x6b\x93\xa1' b'\x66\xf8\x4d\xe2' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'

        self.reply_args_7 = {
            'value': (32, [1, 2, 3]),
            'sequence_number': 37094,
            'property_type': 704363625,
            'bytes_after': 1957409055,
            }
        self.reply_bin_7 = b'\x01\x20\x90\xe6' b'\x00\x00\x00\x03' \
            b'\x29\xfb\xbc\x69' b'\x74\xab\xb1\x1f' \
            b'\x00\x00\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x01' b'\x00\x00\x00\x02' \
            b'\x00\x00\x00\x03'


    def testPackRequest0(self):
        bin = request.GetProperty._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetProperty._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply1(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_1)
        try:
            assert bin == self.reply_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_1
        except AssertionError:
            raise AssertionError(args)

    def testPackReply2(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_2)
        try:
            assert bin == self.reply_bin_2
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply2(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_2, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_2
        except AssertionError:
            raise AssertionError(args)

    def testPackReply3(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_3)
        try:
            assert bin == self.reply_bin_3
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply3(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_3, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_3
        except AssertionError:
            raise AssertionError(args)

    def testPackReply4(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_4)
        try:
            assert bin == self.reply_bin_4
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply4(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_4, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_4
        except AssertionError:
            raise AssertionError(args)

    def testPackReply5(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_5)
        try:
            assert bin == self.reply_bin_5
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply5(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_5, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_5
        except AssertionError:
            raise AssertionError(args)

    def testPackReply6(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_6)
        try:
            assert bin == self.reply_bin_6
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply6(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_6, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_6
        except AssertionError:
            raise AssertionError(args)

    def testPackReply7(self):
        bin = request.GetProperty._reply.to_binary(*(), **self.reply_args_7)
        try:
            assert bin == self.reply_bin_7
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply7(self):
        args, remain = request.GetProperty._reply.parse_binary(self.reply_bin_7, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_7
        except AssertionError:
            raise AssertionError(args)


class TestListProperties(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 91262675,
            }
        self.req_bin_0 = b'\x15\x00\x00\x02' b'\x05\x70\x8e\xd3'

        self.reply_args_0 = {
            'atoms': [580972634, 926488735, 714741529, 408777797, 679906858, 705092899, 2063243279, 893967755, 1591182471, 571137996, 1677110101, 1783836762, 1678219148, 1992402577, 871298793, 1182885899, 1155013854, 1822076326, 2117552706, 1972668469, 1660227078, 1523268962, 694042433],
            'sequence_number': 42191,
            }
        self.reply_bin_0 = b'\x01\x00\xa4\xcf' b'\x00\x00\x00\x17' \
            b'\x00\x17\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x22\xa0\xf0\x5a' b'\x37\x39\x18\x9f' \
            b'\x2a\x9a\x17\x19' b'\x18\x5d\x74\x45' \
            b'\x28\x86\x8e\x2a' b'\x2a\x06\xdd\x23' \
            b'\x7a\xfa\x98\x0f' b'\x35\x48\xdd\x8b' \
            b'\x5e\xd7\x84\x87' b'\x22\x0a\xdf\xcc' \
            b'\x63\xf6\xab\x55' b'\x6a\x53\x30\x5a' \
            b'\x64\x07\x97\x8c' b'\x76\xc1\xa6\x91' \
            b'\x33\xee\xf6\xe9' b'\x46\x81\x68\x0b' \
            b'\x44\xd8\x1c\xde' b'\x6c\x9a\xad\xa6' \
            b'\x7e\x37\x4a\x42' b'\x75\x94\x88\x35' \
            b'\x62\xf5\x0e\x06' b'\x5a\xcb\x3d\x62' \
            b'\x29\x5e\x3f\x41'


    def testPackRequest0(self):
        bin = request.ListProperties._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListProperties._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListProperties._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetSelectionOwner(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'selection': 2071258139,
            'window': 1190911777,
            'time': 1606660593,
            }
        self.req_bin_0 = b'\x16\x00\x00\x04' b'\x46\xfb\xdf\x21' \
            b'\x7b\x74\xe4\x1b' b'\x5f\xc3\xb1\xf1'


    def testPackRequest0(self):
        bin = request.SetSelectionOwner._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetSelectionOwner(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'selection': 819576555,
            }
        self.req_bin_0 = b'\x17\x00\x00\x02' b'\x30\xd9\xbe\xeb'

        self.reply_args_0 = {
            'sequence_number': 14152,
            'owner': 1922331178,
            }
        self.reply_bin_0 = b'\x01\x00\x37\x48' b'\x00\x00\x00\x00' \
            b'\x72\x94\x72\x2a' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetSelectionOwner._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetSelectionOwner._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetSelectionOwner._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetSelectionOwner._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestConvertSelection(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'property': 2137791927,
            'time': 1594653142,
            'target': 1972273672,
            'selection': 125139929,
            'requestor': 300355135,
            }
        self.req_bin_0 = b'\x18\x00\x00\x06' b'\x11\xe7\x0e\x3f' \
            b'\x07\x75\x7b\xd9' b'\x75\x8e\x82\x08' \
            b'\x7f\x6c\x1d\xb7' b'\x5f\x0c\x79\xd6'


    def testPackRequest0(self):
        bin = request.ConvertSelection._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ConvertSelection._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSendEvent(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'event': Xlib.protocol.event.Expose(height = 64784, sequence_number = 0, type = 12, x = 52546, y = 56316, window = 1322187412, width = 16612, count = 14164),
            'propagate': 1,
            'destination': 1369243800,
            'event_mask': 1594482936,
            }
        self.req_bin_0 = b'\x19\x01\x00\x0b' b'\x51\x9d\x00\x98' \
            b'\x5f\x09\xe0\xf8' b'\x0c\x00\x00\x00' \
            b'\x4e\xce\xfa\x94' b'\xcd\x42\xdb\xfc' \
            b'\x40\xe4\xfd\x10' b'\x37\x54\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SendEvent._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SendEvent._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGrabPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 2104857020,
            'confine_to': 1988278615,
            'event_mask': 2075,
            'pointer_mode': 0,
            'time': 1316427724,
            'keyboard_mode': 1,
            'cursor': 17101598,
            }
        self.req_bin_0 = b'\x1a\x01\x00\x06' b'\x7d\x75\x91\xbc' \
            b'\x08\x1b\x00\x01' b'\x76\x82\xb9\x57' \
            b'\x01\x04\xf3\x1e' b'\x4e\x77\x17\xcc'

        self.reply_args_0 = {
            'sequence_number': 47539,
            'status': 149,
            }
        self.reply_bin_0 = b'\x01\x95\xb9\xb3' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabPointer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GrabPointer._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GrabPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUngrabPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 209008422,
            }
        self.req_bin_0 = b'\x1b\x00\x00\x02' b'\x0c\x75\x37\x26'


    def testPackRequest0(self):
        bin = request.UngrabPointer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UngrabPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGrabButton(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 526402184,
            'confine_to': 1843948635,
            'event_mask': 16279,
            'pointer_mode': 1,
            'modifiers': 15589,
            'button': 208,
            'keyboard_mode': 1,
            'cursor': 1070323643,
            }
        self.req_bin_0 = b'\x1c\x01\x00\x06' b'\x1f\x60\x42\x88' \
            b'\x3f\x97\x01\x01' b'\x6d\xe8\x6c\x5b' \
            b'\x3f\xcb\xd7\xbb' b'\xd0\x00\x3c\xe5'


    def testPackRequest0(self):
        bin = request.GrabButton._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUngrabButton(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 795414150,
            'button': 240,
            'modifiers': 51717,
            }
        self.req_bin_0 = b'\x1d\xf0\x00\x03' b'\x2f\x69\x0e\x86' \
            b'\xca\x05\x00\x00'


    def testPackRequest0(self):
        bin = request.UngrabButton._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UngrabButton._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeActivePointerGrab(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 891337572,
            'event_mask': 23423,
            'cursor': 1696594928,
            }
        self.req_bin_0 = b'\x1e\x00\x00\x04' b'\x65\x1f\xfb\xf0' \
            b'\x35\x20\xbb\x64' b'\x5b\x7f\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeActivePointerGrab._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeActivePointerGrab._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGrabKeyboard(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 0,
            'grab_window': 76132199,
            'time': 1562605785,
            'pointer_mode': 1,
            'keyboard_mode': 1,
            }
        self.req_bin_0 = b'\x1f\x00\x00\x04' b'\x04\x89\xaf\x67' \
            b'\x5d\x23\x78\xd9' b'\x01\x01\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 9648,
            'status': 129,
            }
        self.reply_bin_0 = b'\x01\x81\x25\xb0' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabKeyboard._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GrabKeyboard._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GrabKeyboard._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUngrabKeyboard(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 1352311886,
            }
        self.req_bin_0 = b'\x20\x00\x00\x02' b'\x50\x9a\xa4\x4e'


    def testPackRequest0(self):
        bin = request.UngrabKeyboard._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UngrabKeyboard._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGrabKey(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'owner_events': 1,
            'grab_window': 1467490800,
            'pointer_mode': 0,
            'keyboard_mode': 0,
            'modifiers': 28819,
            'key': 193,
            }
        self.req_bin_0 = b'\x21\x01\x00\x04' b'\x57\x78\x21\xf0' \
            b'\x70\x93\xc1\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GrabKey._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUngrabKey(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'grab_window': 769929659,
            'key': 215,
            'modifiers': 60588,
            }
        self.req_bin_0 = b'\x22\xd7\x00\x03' b'\x2d\xe4\x31\xbb' \
            b'\xec\xac\x00\x00'


    def testPackRequest0(self):
        bin = request.UngrabKey._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UngrabKey._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestAllowEvents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'time': 342147129,
            'mode': 1,
            }
        self.req_bin_0 = b'\x23\x01\x00\x02' b'\x14\x64\xc0\x39'


    def testPackRequest0(self):
        bin = request.AllowEvents._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.AllowEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGrabServer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x24\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.GrabServer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUngrabServer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x25\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.UngrabServer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UngrabServer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 561336799,
            }
        self.req_bin_0 = b'\x26\x00\x00\x02' b'\x21\x75\x51\xdf'

        self.reply_args_0 = {
            'win_y': -25733,
            'same_screen': 0,
            'sequence_number': 41448,
            'root': 1599238998,
            'root_x': -4185,
            'root_y': -6112,
            'mask': 35955,
            'child': 1075058918,
            'win_x': -18858,
            }
        self.reply_bin_0 = b'\x01\x00\xa1\xe8' b'\x00\x00\x00\x00' \
            b'\x5f\x52\x73\x56' b'\x40\x14\x18\xe6' \
            b'\xef\xa7\xe8\x20' b'\xb6\x56\x9b\x7b' \
            b'\x8c\x73\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryPointer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryPointer._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryPointer._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetMotionEvents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 843681780,
            'start': 1520150500,
            'stop': 11115313,
            }
        self.req_bin_0 = b'\x27\x00\x00\x04' b'\x32\x49\x8f\xf4' \
            b'\x5a\x9b\xa7\xe4' b'\x00\xa9\x9b\x31'

        self.reply_args_0 = {
            'sequence_number': 52222,
            'events': [{'time': 2107444516, 'x': -649, 'y': -11631}, {'time': 1827536960, 'x': -18061, 'y': -2301}, {'time': 554175146, 'x': -32111, 'y': -13522}, {'time': 608168588, 'x': -5963, 'y': -24618}, {'time': 590416221, 'x': -3325, 'y': -19656}],
            }
        self.reply_bin_0 = b'\x01\x00\xcb\xfe' b'\x00\x00\x00\x0a' \
            b'\x00\x00\x00\x05' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7d\x9d\x0d\x24' b'\xfd\x77\xd2\x91' \
            b'\x6c\xee\x00\x40' b'\xb9\x73\xf7\x03' \
            b'\x21\x08\x0a\xaa' b'\x82\x91\xcb\x2e' \
            b'\x24\x3f\xea\x8c' b'\xe8\xb5\x9f\xd6' \
            b'\x23\x31\x09\x5d' b'\xf3\x03\xb3\x38'


    def testPackRequest0(self):
        bin = request.GetMotionEvents._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetMotionEvents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetMotionEvents._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetMotionEvents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestTranslateCoords(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_y': -27247,
            'src_x': -25331,
            'src_wid': 257619448,
            'dst_wid': 1238981863,
            }
        self.req_bin_0 = b'\x28\x00\x00\x04' b'\x0f\x5a\xf5\xf8' \
            b'\x49\xd9\x5c\xe7' b'\x9d\x0d\x95\x91'

        self.reply_args_0 = {
            'child': 2050350678,
            'same_screen': 1,
            'sequence_number': 38657,
            'x': -18096,
            'y': -5252,
            }
        self.reply_bin_0 = b'\x01\x01\x97\x01' b'\x00\x00\x00\x00' \
            b'\x7a\x35\xde\x56' b'\xb9\x50\xeb\x7c' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.TranslateCoords._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.TranslateCoords._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.TranslateCoords._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.TranslateCoords._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestWarpPointer(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_height': 56634,
            'src_window': 1335081711,
            'dst_window': 675547124,
            'src_width': 21809,
            'src_y': -26071,
            'src_x': -27119,
            'dst_x': -30516,
            'dst_y': -24204,
            }
        self.req_bin_0 = b'\x29\x00\x00\x06' b'\x4f\x93\xba\xef' \
            b'\x28\x44\x07\xf4' b'\x96\x11\x9a\x29' \
            b'\x55\x31\xdd\x3a' b'\x88\xcc\xa1\x74'


    def testPackRequest0(self):
        bin = request.WarpPointer._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.WarpPointer._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetInputFocus(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'revert_to': 1,
            'time': 1079702500,
            'focus': 1026400247,
            }
        self.req_bin_0 = b'\x2a\x01\x00\x03' b'\x3d\x2d\x9f\xf7' \
            b'\x40\x5a\xf3\xe4'


    def testPackRequest0(self):
        bin = request.SetInputFocus._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetInputFocus(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x2b\x00\x00\x01'

        self.reply_args_0 = {
            'revert_to': 152,
            'sequence_number': 16002,
            'focus': 2024022965,
            }
        self.reply_bin_0 = b'\x01\x98\x3e\x82' b'\x00\x00\x00\x00' \
            b'\x78\xa4\x23\xb5' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetInputFocus._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetInputFocus._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetInputFocus._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetInputFocus._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryKeymap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x2c\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 16233,
            'map': [186, 167, 191, 213, 241, 231, 234, 175, 154, 169, 132, 146, 215, 191, 196, 212, 158, 156, 177, 233, 220, 192, 130, 226, 181, 233, 238, 141, 129, 215, 245, 215],
            }
        self.reply_bin_0 = b'\x01\x00\x3f\x69' b'\x00\x00\x00\x02' \
            b'\xba\xa7\xbf\xd5' b'\xf1\xe7\xea\xaf' \
            b'\x9a\xa9\x84\x92' b'\xd7\xbf\xc4\xd4' \
            b'\x9e\x9c\xb1\xe9' b'\xdc\xc0\x82\xe2' \
            b'\xb5\xe9\xee\x8d' b'\x81\xd7\xf5\xd7'


    def testPackRequest0(self):
        bin = request.QueryKeymap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryKeymap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryKeymap._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryKeymap._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestOpenFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fid': 1728036313,
            'name': 'foofont',
            }
        self.req_bin_0 = b'\x2d\x00\x00\x05' b'\x66\xff\xbd\xd9' \
            b'\x00\x07\x00\x00' b'\x66\x6f\x6f\x66' \
            b'\x6f\x6e\x74\x00'


    def testPackRequest0(self):
        bin = request.OpenFont._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.OpenFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCloseFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 1139770507,
            }
        self.req_bin_0 = b'\x2e\x00\x00\x02' b'\x43\xef\x84\x8b'


    def testPackRequest0(self):
        bin = request.CloseFont._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CloseFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryFont(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 1867659050,
            }
        self.req_bin_0 = b'\x2f\x00\x00\x02' b'\x6f\x52\x37\x2a'

        self.reply_args_0 = {
            'sequence_number': 8877,
            'properties': [{'value': 2110348825, 'name': 1450586355}],
            'min_byte1': 190,
            'max_byte1': 168,
            'char_infos': [{'descent': -331, 'ascent': -14454, 'character_width': -28521, 'left_side_bearing': -4521, 'right_side_bearing': -9875, 'attributes': 55191}, {'descent': -18739, 'ascent': -6278, 'character_width': -4532, 'left_side_bearing': -20397, 'right_side_bearing': -25187, 'attributes': 29476}, {'descent': -18381, 'ascent': -2378, 'character_width': -21855, 'left_side_bearing': -20068, 'right_side_bearing': -906, 'attributes': 34385}],
            'max_char_or_byte2': 2516,
            'default_char': 8994,
            'min_char_or_byte2': 49360,
            'draw_direction': 143,
            'min_bounds': {'descent': -29813, 'ascent': -27033, 'character_width': -5286, 'left_side_bearing': -20740, 'right_side_bearing': -21698, 'attributes': 11392},
            'all_chars_exist': 1,
            'font_ascent': -15646,
            'font_descent': -23067,
            'max_bounds': {'descent': -24292, 'ascent': -26972, 'character_width': -19286, 'left_side_bearing': -16363, 'right_side_bearing': -3149, 'attributes': 35968},
            }
        self.reply_bin_0 = b'\x01\x00\x22\xad' b'\x00\x00\x00\x12' \
            b'\xae\xfc\xab\x3e' b'\xeb\x5a\x96\x67' \
            b'\x8b\x8b\x2c\x80' b'\x00\x00\x00\x00' \
            b'\xc0\x15\xf3\xb3' b'\xb4\xaa\x96\xa4' \
            b'\xa1\x1c\x8c\x80' b'\x00\x00\x00\x00' \
            b'\xc0\xd0\x09\xd4' b'\x23\x22\x00\x01' \
            b'\x8f\xbe\xa8\x01' b'\xc2\xe2\xa5\xe5' \
            b'\x00\x00\x00\x03' b'\x56\x76\x30\xf3' \
            b'\x7d\xc9\x5e\x19' b'\xee\x57\xd9\x6d' \
            b'\x90\x97\xc7\x8a' b'\xfe\xb5\xd7\x97' \
            b'\xb0\x53\x9d\x9d' b'\xee\x4c\xe7\x7a' \
            b'\xb6\xcd\x73\x24' b'\xb1\x9c\xfc\x76' \
            b'\xaa\xa1\xf6\xb6' b'\xb8\x33\x86\x51'


    def testPackRequest0(self):
        bin = request.QueryFont._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryFont._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryFont._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryFont._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryTextExtents(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'font': 1562125736,
            'string': (102, 111, 111),
            }
        self.req_bin_0 = b'\x30\x01\x00\x04' b'\x5d\x1c\x25\xa8' \
            b'\x00\x66\x00\x6f' b'\x00\x6f\x00\x00'

        self.reply_args_0 = {
            'overall_width': -1378352414,
            'draw_direction': 219,
            'sequence_number': 6791,
            'font_ascent': -16915,
            'overall_ascent': -22910,
            'overall_descent': -1795,
            'overall_right': -530284310,
            'overall_left': -1046976699,
            'font_descent': -14179,
            }
        self.reply_bin_0 = b'\x01\xdb\x1a\x87' b'\x00\x00\x00\x00' \
            b'\xbd\xed\xc8\x9d' b'\xa6\x82\xf8\xfd' \
            b'\xad\xd8\x02\xe2' b'\xc1\x98\x67\x45' \
            b'\xe0\x64\x80\xea' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryTextExtents._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryTextExtents._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryTextExtents._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryTextExtents._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestListFonts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 53961,
            'pattern': 'bhazr',
            }
        self.req_bin_0 = b'\x31\x00\x00\x04' b'\xd2\xc9\x00\x05' \
            b'\x62\x68\x61\x7a' b'\x72\x00\x00\x00'

        self.reply_args_0 = {
            'fonts': ['fie', 'fuzzy', 'foozooom'],
            'sequence_number': 38267,
            }
        self.reply_bin_0 = b'\x01\x00\x95\x7b' b'\x00\x00\x00\x05' \
            b'\x00\x03\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x03\x66\x69\x65' b'\x05\x66\x75\x7a' \
            b'\x7a\x79\x08\x66' b'\x6f\x6f\x7a\x6f' \
            b'\x6f\x6f\x6d\x00'


    def testPackRequest0(self):
        bin = request.ListFonts._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListFonts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListFonts._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListFonts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestListFontsWithInfo(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'max_names': 46571,
            'pattern': 'bhazr2',
            }
        self.req_bin_0 = b'\x32\x00\x00\x04' b'\xb5\xeb\x00\x06' \
            b'\x62\x68\x61\x7a' b'\x72\x32\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 20014,
            'properties': [{'value': 2110430409, 'name': 435956656}],
            'min_byte1': 214,
            'max_byte1': 217,
            'max_char_or_byte2': 2479,
            'default_char': 17041,
            'min_char_or_byte2': 26638,
            'draw_direction': 192,
            'replies_hint': 1985190562,
            'min_bounds': {'descent': -27837, 'ascent': -14775, 'character_width': -13026, 'left_side_bearing': -29767, 'right_side_bearing': -31908, 'attributes': 2465},
            'all_chars_exist': 0,
            'name': 'fontfont',
            'font_ascent': -30550,
            'font_descent': -28978,
            'max_bounds': {'descent': -20692, 'ascent': -6999, 'character_width': -15180, 'left_side_bearing': -7789, 'right_side_bearing': -5339, 'attributes': 1068},
            }
        self.reply_bin_0 = b'\x01\x08\x4e\x2e' b'\x00\x00\x00\x0b' \
            b'\x8b\xb9\x83\x5c' b'\xcd\x1e\xc6\x49' \
            b'\x93\x43\x09\xa1' b'\x00\x00\x00\x00' \
            b'\xe1\x93\xeb\x25' b'\xc4\xb4\xe4\xa9' \
            b'\xaf\x2c\x04\x2c' b'\x00\x00\x00\x00' \
            b'\x68\x0e\x09\xaf' b'\x42\x91\x00\x01' \
            b'\xc0\xd6\xd9\x00' b'\x88\xaa\x8e\xce' \
            b'\x76\x53\x9a\xa2' b'\x19\xfc\x2b\xb0' \
            b'\x7d\xca\x9c\xc9' b'\x66\x6f\x6e\x74' \
            b'\x66\x6f\x6e\x74'


    def testPackRequest0(self):
        bin = request.ListFontsWithInfo._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListFontsWithInfo._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListFontsWithInfo._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListFontsWithInfo._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetFontPath(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'path': ['foo', 'bar', 'gazonk'],
            }
        self.req_bin_0 = b'\x33\x00\x00\x06' b'\x00\x03\x00\x00' \
            b'\x03\x66\x6f\x6f' b'\x03\x62\x61\x72' \
            b'\x06\x67\x61\x7a' b'\x6f\x6e\x6b\x00'

        self.req_args_1 = {
            'path': [],
            }
        self.req_bin_1 = b'\x33\x00\x00\x02' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetFontPath._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest1(self):
        bin = request.SetFontPath._request.to_binary(*(), **self.req_args_1)
        try:
            assert bin == self.req_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
        args, remain = request.SetFontPath._request.parse_binary(self.req_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_1
        except AssertionError:
            raise AssertionError(args)


class TestGetFontPath(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x34\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 21510,
            'paths': ['path1', 'path2232'],
            }
        self.reply_bin_0 = b'\x01\x00\x54\x06' b'\x00\x00\x00\x04' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x05\x70\x61\x74' b'\x68\x31\x08\x70' \
            b'\x61\x74\x68\x32' b'\x32\x33\x32\x00'

        self.reply_args_1 = {
            'sequence_number': 62463,
            'paths': [],
            }
        self.reply_bin_1 = b'\x01\x00\xf3\xff' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetFontPath._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetFontPath._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetFontPath._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply1(self):
        bin = request.GetFontPath._reply.to_binary(*(), **self.reply_args_1)
        try:
            assert bin == self.reply_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
        args, remain = request.GetFontPath._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_1
        except AssertionError:
            raise AssertionError(args)


class TestCreatePixmap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 65515,
            'drawable': 162261202,
            'pid': 926490960,
            'depth': 145,
            'width': 5641,
            }
        self.req_bin_0 = b'\x35\x91\x00\x04' b'\x37\x39\x21\x50' \
            b'\x09\xab\xe8\xd2' b'\x16\x09\xff\xeb'


    def testPackRequest0(self):
        bin = request.CreatePixmap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreatePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestFreePixmap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'pixmap': 213012851,
            }
        self.req_bin_0 = b'\x36\x00\x00\x02' b'\x0c\xb2\x51\x73'


    def testPackRequest0(self):
        bin = request.FreePixmap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FreePixmap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cid': 1060658282,
            'drawable': 456876463,
            'attrs': {'dashes': 183, 'fill_rule': 0, 'clip_mask': 620422624, 'plane_mask': 1797423280, 'line_style': 1, 'tile': 77620460, 'arc_mode': 0, 'clip_y_origin': -7419, 'dash_offset': 62459, 'line_width': 50494, 'background': 44336037, 'clip_x_origin': -32045, 'join_style': 2, 'graphics_exposures': 0, 'font': 95118395, 'tile_stipple_y_origin': -17619, 'stipple': 631657813, 'fill_style': 0, 'cap_style': 0, 'subwindow_mode': 0, 'tile_stipple_x_origin': -12494, 'foreground': 2096879871, 'function': 10},
            }
        self.req_bin_0 = b'\x37\x00\x00\x1b' b'\x3f\x38\x5c\x6a' \
            b'\x1b\x3b\x61\xaf' b'\x00\x7f\xff\xff' \
            b'\x0a\x00\x00\x00' b'\x6b\x22\x80\xb0' \
            b'\x7c\xfb\xd8\xff' b'\x02\xa4\x83\xa5' \
            b'\xc5\x3e\x00\x00' b'\x01\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x04\xa0\x64\xec' b'\x25\xa6\x55\x55' \
            b'\xcf\x32\x00\x00' b'\xbb\x2d\x00\x00' \
            b'\x05\xab\x64\x3b' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x82\xd3\x00\x00' \
            b'\xe3\x05\x00\x00' b'\x24\xfa\xe5\xe0' \
            b'\xf3\xfb\x00\x00' b'\xb7\x00\x00\x00' \
            b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.CreateGC._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreateGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'dashes': 249, 'fill_rule': 1, 'clip_mask': 496525721, 'plane_mask': 1467281901, 'line_style': 2, 'tile': 1713935374, 'arc_mode': 0, 'clip_y_origin': -24572, 'dash_offset': 46636, 'line_width': 61036, 'background': 1598773587, 'clip_x_origin': -19725, 'join_style': 1, 'graphics_exposures': 0, 'font': 429323306, 'tile_stipple_y_origin': -11767, 'stipple': 1365263649, 'fill_style': 2, 'cap_style': 1, 'subwindow_mode': 1, 'tile_stipple_x_origin': -23501, 'foreground': 1272378077, 'function': 11},
            'gc': 518903558,
            }
        self.req_bin_0 = b'\x38\x00\x00\x1a' b'\x1e\xed\xd7\x06' \
            b'\x00\x7f\xff\xff' b'\x0b\x00\x00\x00' \
            b'\x57\x74\xf1\xed' b'\x4b\xd6\xf2\xdd' \
            b'\x5f\x4b\x59\x53' b'\xee\x6c\x00\x00' \
            b'\x02\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x02\x00\x00\x00' \
            b'\x01\x00\x00\x00' b'\x66\x28\x94\x0e' \
            b'\x51\x60\x45\x21' b'\xa4\x33\x00\x00' \
            b'\xd2\x09\x00\x00' b'\x19\x96\xf4\x2a' \
            b'\x01\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xb2\xf3\x00\x00' b'\xa0\x04\x00\x00' \
            b'\x1d\x98\x61\x99' b'\xb6\x2c\x00\x00' \
            b'\xf9\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeGC._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCopyGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mask': 1039948946,
            'src_gc': 1958847367,
            'dst_gc': 1311353896,
            }
        self.req_bin_0 = b'\x39\x00\x00\x04' b'\x74\xc1\xa3\x87' \
            b'\x4e\x29\xac\x28' b'\x3d\xfc\x5c\x92'


    def testPackRequest0(self):
        bin = request.CopyGC._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CopyGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetDashes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'dashes': [169, 241, 158, 238, 173, 159, 182, 139, 139],
            'dash_offset': 51693,
            'gc': 1639787502,
            }
        self.req_bin_0 = b'\x3a\x00\x00\x06' b'\x61\xbd\x2b\xee' \
            b'\xc9\xed\x00\x09' b'\xa9\xf1\x9e\xee' \
            b'\xad\x9f\xb6\x8b' b'\x8b\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetDashes._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetDashes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetClipRectangles(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'rectangles': [{'height': 59391, 'x': -15430, 'width': 46673, 'y': -3009}, {'height': 9883, 'x': -14046, 'width': 7782, 'y': -24857}],
            'gc': 1105675380,
            'x_origin': -22760,
            'y_origin': -16557,
            'ordering': 3,
            }
        self.req_bin_0 = b'\x3b\x03\x00\x07' b'\x41\xe7\x44\x74' \
            b'\xa7\x18\xbf\x53' b'\xc3\xba\xf4\x3f' \
            b'\xb6\x51\xe7\xff' b'\xc9\x22\x9e\xe7' \
            b'\x1e\x66\x26\x9b'

        self.req_args_1 = {
            'rectangles': [],
            'gc': 291514811,
            'x_origin': -29867,
            'y_origin': -10293,
            'ordering': 0,
            }
        self.req_bin_1 = b'\x3b\x00\x00\x03' b'\x11\x60\x29\xbb' \
            b'\x8b\x55\xd7\xcb'


    def testPackRequest0(self):
        bin = request.SetClipRectangles._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest1(self):
        bin = request.SetClipRectangles._request.to_binary(*(), **self.req_args_1)
        try:
            assert bin == self.req_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
        args, remain = request.SetClipRectangles._request.parse_binary(self.req_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_1
        except AssertionError:
            raise AssertionError(args)


class TestFreeGC(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 371787524,
            }
        self.req_bin_0 = b'\x3c\x00\x00\x02' b'\x16\x29\x07\x04'


    def testPackRequest0(self):
        bin = request.FreeGC._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FreeGC._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestClearArea(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'exposures': 0,
            'height': 53776,
            'width': 63821,
            'window': 1253992673,
            'x': -1843,
            'y': -32148,
            }
        self.req_bin_0 = b'\x3d\x00\x00\x04' b'\x4a\xbe\x68\xe1' \
            b'\xf8\xcd\x82\x6c' b'\xf9\x4d\xd2\x10'


    def testPackRequest0(self):
        bin = request.ClearArea._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ClearArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCopyArea(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_drawable': 321720617,
            'dst_drawable': 252019697,
            'src_y': -8372,
            'src_x': -25544,
            'gc': 126071392,
            'width': 49414,
            'height': 61502,
            'dst_x': -19068,
            'dst_y': -4602,
            }
        self.req_bin_0 = b'\x3e\x00\x00\x07' b'\x13\x2d\x11\x29' \
            b'\x0f\x05\x83\xf1' b'\x07\x83\xb2\x60' \
            b'\x9c\x38\xdf\x4c' b'\xb5\x84\xee\x06' \
            b'\xc1\x06\xf0\x3e'


    def testPackRequest0(self):
        bin = request.CopyArea._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CopyArea._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCopyPlane(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_drawable': 1988650265,
            'bit_plane': 2052065832,
            'dst_drawable': 2120887972,
            'src_y': -22401,
            'src_x': -4542,
            'gc': 1266180573,
            'width': 41241,
            'height': 33787,
            'dst_x': -24940,
            'dst_y': -13009,
            }
        self.req_bin_0 = b'\x3f\x00\x00\x08' b'\x76\x88\x65\x19' \
            b'\x7e\x6a\x2e\xa4' b'\x4b\x78\x61\xdd' \
            b'\xee\x42\xa8\x7f' b'\x9e\x94\xcd\x2f' \
            b'\xa1\x19\x83\xfb' b'\x7a\x50\x0a\x28'


    def testPackRequest0(self):
        bin = request.CopyPlane._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CopyPlane._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyPoint(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 206266633,
            'points': [{'x': -22449, 'y': -16714}, {'x': -16465, 'y': -12850}, {'x': -19616, 'y': -13131}],
            'drawable': 1008674,
            'coord_mode': 1,
            }
        self.req_bin_0 = b'\x40\x01\x00\x06' b'\x00\x0f\x64\x22' \
            b'\x0c\x4b\x61\x09' b'\xa8\x4f\xbe\xb6' \
            b'\xbf\xaf\xcd\xce' b'\xb3\x60\xcc\xb5'


    def testPackRequest0(self):
        bin = request.PolyPoint._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyPoint._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyLine(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1355594189,
            'points': [{'x': -11743, 'y': -18781}, {'x': -21373, 'y': -22722}, {'x': -17579, 'y': -13699}, {'x': -26545, 'y': -19353}, {'x': -11779, 'y': -26488}],
            'drawable': 1668889192,
            'coord_mode': 1,
            }
        self.req_bin_0 = b'\x41\x01\x00\x08' b'\x63\x79\x3a\x68' \
            b'\x50\xcc\xb9\xcd' b'\xd2\x21\xb6\xa3' \
            b'\xac\x83\xa7\x3e' b'\xbb\x55\xca\x7d' \
            b'\x98\x4f\xb4\x67' b'\xd1\xfd\x98\x88'


    def testPackRequest0(self):
        bin = request.PolyLine._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyLine._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolySegment(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'segments': [{'y1': -24252, 'y2': -22523, 'x1': -12610, 'x2': -25770}],
            'drawable': 146511635,
            'gc': 53385255,
            }
        self.req_bin_0 = b'\x42\x00\x00\x05' b'\x08\xbb\x97\x13' \
            b'\x03\x2e\x98\x27' b'\xce\xbe\xa1\x44' \
            b'\x9b\x56\xa8\x05'


    def testPackRequest0(self):
        bin = request.PolySegment._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolySegment._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyRectangle(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1927481661,
            'gc': 410140275,
            'rectangles': [{'height': 63567, 'x': -16992, 'width': 11122, 'y': -21320}, {'height': 34652, 'x': -18051, 'width': 59622, 'y': -30426}, {'height': 45646, 'x': -1111, 'width': 46231, 'y': -25261}],
            }
        self.req_bin_0 = b'\x43\x00\x00\x09' b'\x72\xe3\x09\x3d' \
            b'\x18\x72\x3e\x73' b'\xbd\xa0\xac\xb8' \
            b'\x2b\x72\xf8\x4f' b'\xb9\x7d\x89\x26' \
            b'\xe8\xe6\x87\x5c' b'\xfb\xa9\x9d\x53' \
            b'\xb4\x97\xb2\x4e'


    def testPackRequest0(self):
        bin = request.PolyRectangle._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyArc(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 37549, 'angle1': -16979, 'x': -4943, 'angle2': -25650, 'width': 65448, 'y': -9205}, {'height': 9322, 'angle1': -20781, 'x': -13865, 'angle2': -8498, 'width': 62173, 'y': -22862}, {'height': 63266, 'angle1': -1231, 'x': -12693, 'angle2': -809, 'width': 63732, 'y': -7550}],
            'drawable': 718777148,
            'gc': 1127021391,
            }
        self.req_bin_0 = b'\x44\x00\x00\x0c' b'\x2a\xd7\xab\x3c' \
            b'\x43\x2c\xfb\x4f' b'\xec\xb1\xdc\x0b' \
            b'\xff\xa8\x92\xad' b'\xbd\xad\x9b\xce' \
            b'\xc9\xd7\xa6\xb2' b'\xf2\xdd\x24\x6a' \
            b'\xae\xd3\xde\xce' b'\xce\x6b\xe2\x82' \
            b'\xf8\xf4\xf7\x22' b'\xfb\x31\xfc\xd7'


    def testPackRequest0(self):
        bin = request.PolyArc._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestFillPoly(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'shape': 1,
            'gc': 1070496026,
            'points': [{'x': -18749, 'y': -19415}, {'x': -8904, 'y': -26948}, {'x': -13336, 'y': -9462}],
            'drawable': 1326525185,
            'coord_mode': 0,
            }
        self.req_bin_0 = b'\x45\x00\x00\x07' b'\x4f\x11\x2b\x01' \
            b'\x3f\xce\x79\x1a' b'\x01\x00\x00\x00' \
            b'\xb6\xc3\xb4\x29' b'\xdd\x38\x96\xbc' \
            b'\xcb\xe8\xdb\x0a'


    def testPackRequest0(self):
        bin = request.FillPoly._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FillPoly._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyFillRectangle(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'drawable': 1708671692,
            'gc': 1965498255,
            'rectangles': [{'height': 36920, 'x': -2965, 'width': 26437, 'y': -3568}, {'height': 44383, 'x': -18327, 'width': 37730, 'y': -26752}],
            }
        self.req_bin_0 = b'\x46\x00\x00\x07' b'\x65\xd8\x42\xcc' \
            b'\x75\x27\x1f\x8f' b'\xf4\x6b\xf2\x10' \
            b'\x67\x45\x90\x38' b'\xb8\x69\x97\x80' \
            b'\x93\x62\xad\x5f'


    def testPackRequest0(self):
        bin = request.PolyFillRectangle._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyFillRectangle._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyFillArc(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'arcs': [{'height': 64114, 'angle1': -28360, 'x': -10754, 'angle2': -6712, 'width': 53819, 'y': -19555}],
            'drawable': 2083870696,
            'gc': 414470877,
            }
        self.req_bin_0 = b'\x47\x00\x00\x06' b'\x7c\x35\x57\xe8' \
            b'\x18\xb4\x52\xdd' b'\xd5\xfe\xb3\x9d' \
            b'\xd2\x3b\xfa\x72' b'\x91\x38\xe5\xc8'


    def testPackRequest0(self):
        bin = request.PolyFillArc._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyFillArc._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPutImage(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 9883,
            'data': 'bit map data',
            'drawable': 1534678783,
            'left_pad': 147,
            'format': 1,
            'dst_x': -3284,
            'gc': 209913475,
            'depth': 173,
            'width': 62850,
            'dst_y': -30693,
            }
        self.req_bin_0 = b'\x48\x01\x00\x09' b'\x5b\x79\x56\xff' \
            b'\x0c\x83\x06\x83' b'\xf5\x82\x26\x9b' \
            b'\xf3\x2c\x88\x1b' b'\x93\xad\x00\x00' \
            b'\x62\x69\x74\x20' b'\x6d\x61\x70\x20' \
            b'\x64\x61\x74\x61'


    def testPackRequest0(self):
        bin = request.PutImage._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PutImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetImage(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 42657,
            'plane_mask': 1756278272,
            'drawable': 1329487747,
            'x': -27672,
            'y': -30859,
            'format': 1,
            'width': 58993,
            }
        self.req_bin_0 = b'\x49\x01\x00\x05' b'\x4f\x3e\x5f\x83' \
            b'\x93\xe8\x87\x75' b'\xe6\x71\xa6\xa1' \
            b'\x68\xae\xae\x00'

        self.reply_args_0 = {
            'sequence_number': 54997,
            'data': 'this is real ly imag e b-map',
            'visual': 1108632607,
            'depth': 181,
            }
        self.reply_bin_0 = b'\x01\xb5\xd6\xd5' b'\x00\x00\x00\x07' \
            b'\x42\x14\x64\x1f' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x74\x68\x69\x73' b'\x20\x69\x73\x20' \
            b'\x72\x65\x61\x6c' b'\x20\x6c\x79\x20' \
            b'\x69\x6d\x61\x67' b'\x20\x65\x20\x62' \
            b'\x2d\x6d\x61\x70'


    def testPackRequest0(self):
        bin = request.GetImage._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetImage._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetImage._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetImage._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyText8(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 1481564777,
            'x': -13548,
            'drawable': 1550998666,
            'items': [{'delta': 2, 'string': 'zoo'}, 16909060, {'delta': 0, 'string': 'ie'}],
            'y': -8902,
            }
        self.req_bin_0 = b'\x4a\x00\x00\x08' b'\x5c\x72\x5c\x8a' \
            b'\x58\x4e\xe2\x69' b'\xcb\x14\xdd\x3a' \
            b'\x03\x02\x7a\x6f' b'\x6f\xff\x01\x02' \
            b'\x03\x04\x02\x00' b'\x69\x65\x00\x00'


    def testPackRequest0(self):
        bin = request.PolyText8._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestPolyText16(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'gc': 400697368,
            'x': -31614,
            'drawable': 1591407092,
            'items': [{'delta': 2, 'string': (4131, 18)}, 16909060],
            'y': -2741,
            }
        self.req_bin_0 = b'\x4b\x00\x00\x07' b'\x5e\xda\xf1\xf4' \
            b'\x17\xe2\x28\x18' b'\x84\x82\xf5\x4b' \
            b'\x02\x02\x10\x23' b'\x00\x12\xff\x01' \
            b'\x02\x03\x04\x00'


    def testPackRequest0(self):
        bin = request.PolyText16._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.PolyText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestImageText8(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'string': 'showme',
            'gc': 1393590305,
            'drawable': 1823595869,
            'x': -16077,
            'y': -4873,
            }
        self.req_bin_0 = b'\x4c\x06\x00\x06' b'\x6c\xb1\xdd\x5d' \
            b'\x53\x10\x80\x21' b'\xc1\x33\xec\xf7' \
            b'\x73\x68\x6f\x77' b'\x6d\x65\x00\x00'


    def testPackRequest0(self):
        bin = request.ImageText8._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ImageText8._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestImageText16(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'string': (115, 104, 111, 119, 109, 111, 114, 101),
            'gc': 1702299870,
            'drawable': 33607184,
            'x': -21343,
            'y': -24237,
            }
        self.req_bin_0 = b'\x4d\x08\x00\x08' b'\x02\x00\xce\x10' \
            b'\x65\x77\x08\xde' b'\xac\xa1\xa1\x53' \
            b'\x00\x73\x00\x68' b'\x00\x6f\x00\x77' \
            b'\x00\x6d\x00\x6f' b'\x00\x72\x00\x65'


    def testPackRequest0(self):
        bin = request.ImageText16._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ImageText16._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mid': 157536683,
            'alloc': 0,
            'visual': 813982403,
            'window': 698475631,
            }
        self.req_bin_0 = b'\x4e\x00\x00\x04' b'\x09\x63\xd1\xab' \
            b'\x29\xa1\xe4\x6f' b'\x30\x84\x62\xc3'


    def testPackRequest0(self):
        bin = request.CreateColormap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreateColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestFreeColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1296514923,
            }
        self.req_bin_0 = b'\x4f\x00\x00\x02' b'\x4d\x47\x3f\x6b'


    def testPackRequest0(self):
        bin = request.FreeColormap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FreeColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCopyColormapAndFree(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'src_cmap': 1049336329,
            'mid': 1237242690,
            }
        self.req_bin_0 = b'\x50\x00\x00\x03' b'\x49\xbe\xd3\x42' \
            b'\x3e\x8b\x9a\x09'


    def testPackRequest0(self):
        bin = request.CopyColormapAndFree._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CopyColormapAndFree._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestInstallColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 1539075582,
            }
        self.req_bin_0 = b'\x51\x00\x00\x02' b'\x5b\xbc\x6d\xfe'


    def testPackRequest0(self):
        bin = request.InstallColormap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.InstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestUninstallColormap(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 959493342,
            }
        self.req_bin_0 = b'\x52\x00\x00\x02' b'\x39\x30\xb4\xde'


    def testPackRequest0(self):
        bin = request.UninstallColormap._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.UninstallColormap._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestListInstalledColormaps(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'window': 1517864638,
            }
        self.req_bin_0 = b'\x53\x00\x00\x02' b'\x5a\x78\xc6\xbe'

        self.reply_args_0 = {
            'cmaps': [2146327722, 1361260227],
            'sequence_number': 61652,
            }
        self.reply_bin_0 = b'\x01\x00\xf0\xd4' b'\x00\x00\x00\x02' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x7f\xee\x5c\xaa' b'\x51\x23\x2e\xc3'


    def testPackRequest0(self):
        bin = request.ListInstalledColormaps._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListInstalledColormaps._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListInstalledColormaps._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListInstalledColormaps._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestAllocColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'red': 39725,
            'green': 49854,
            'cmap': 523356125,
            'blue': 49580,
            }
        self.req_bin_0 = b'\x54\x00\x00\x04' b'\x1f\x31\xc7\xdd' \
            b'\x9b\x2d\xc2\xbe' b'\xc1\xac\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 10904,
            'red': 43784,
            'green': 3170,
            'pixel': 1067923656,
            'blue': 14525,
            }
        self.reply_bin_0 = b'\x01\x00\x2a\x98' b'\x00\x00\x00\x00' \
            b'\xab\x08\x0c\x62' b'\x38\xbd\x00\x00' \
            b'\x3f\xa7\x38\xc8' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocColor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.AllocColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.AllocColor._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.AllocColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestAllocNamedColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 128217824,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x55\x00\x00\x05' b'\x07\xa4\x72\xe0' \
            b'\x00\x07\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 19971,
            'pixel': 1324239222,
            'screen_green': 50499,
            'screen_red': 33379,
            'exact_green': 29067,
            'exact_blue': 58811,
            'screen_blue': 43109,
            'exact_red': 64213,
            }
        self.reply_bin_0 = b'\x01\x00\x4e\x03' b'\x00\x00\x00\x00' \
            b'\x4e\xee\x49\x76' b'\xfa\xd5\x71\x8b' \
            b'\xe5\xbb\x82\x63' b'\xc5\x43\xa8\x65' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocNamedColor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.AllocNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.AllocNamedColor._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.AllocNamedColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestAllocColorCells(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'planes': 32867,
            'colors': 58698,
            'cmap': 675372338,
            'contiguous': 1,
            }
        self.req_bin_0 = b'\x56\x01\x00\x03' b'\x28\x41\x5d\x32' \
            b'\xe5\x4a\x80\x63'

        self.reply_args_0 = {
            'masks': [733927381, 1023311668, 595898647],
            'pixels': [693075497, 1294879029, 1478712895, 1781963728, 1442185575, 1654003869, 787619123, 1049825849, 1773935772, 1689075922, 1626562257, 177731275, 661046122, 1970509470, 1918486395, 688539096, 41044851],
            'sequence_number': 54025,
            }
        self.reply_bin_0 = b'\x01\x00\xd3\x09' b'\x00\x00\x00\x14' \
            b'\x00\x11\x00\x03' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x29\x4f\x7e\x29' b'\x4d\x2e\x49\x35' \
            b'\x58\x23\x5e\x3f' b'\x6a\x36\x9b\xd0' \
            b'\x55\xf6\x01\x67' b'\x62\x96\x18\x9d' \
            b'\x2e\xf2\x1d\x33' b'\x3e\x93\x12\x39' \
            b'\x69\xbc\x1c\x9c' b'\x64\xad\x40\xd2' \
            b'\x60\xf3\x5e\xd1' b'\x0a\x97\xf6\xcb' \
            b'\x27\x66\xc3\x6a' b'\x75\x73\x96\x9e' \
            b'\x72\x59\xc7\x7b' b'\x29\x0a\x45\xd8' \
            b'\x02\x72\x4b\x73' b'\x2b\xbe\xd7\xd5' \
            b'\x3c\xfe\x7f\x34' b'\x23\x84\xb1\x17'

        self.reply_args_1 = {
            'masks': [],
            'pixels': [],
            'sequence_number': 6273,
            }
        self.reply_bin_1 = b'\x01\x00\x18\x81' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.AllocColorCells._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.AllocColorCells._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.AllocColorCells._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply1(self):
        bin = request.AllocColorCells._reply.to_binary(*(), **self.reply_args_1)
        try:
            assert bin == self.reply_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply1(self):
        args, remain = request.AllocColorCells._reply.parse_binary(self.reply_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_1
        except AssertionError:
            raise AssertionError(args)


class TestAllocColorPlanes(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'red': 22876,
            'colors': 58275,
            'green': 9425,
            'cmap': 308019811,
            'contiguous': 0,
            'blue': 23880,
            }
        self.req_bin_0 = b'\x57\x00\x00\x04' b'\x12\x5c\x02\x63' \
            b'\xe3\xa3\x59\x5c' b'\x24\xd1\x5d\x48'

        self.reply_args_0 = {
            'green_mask': 265888391,
            'sequence_number': 36175,
            'pixels': [491961865, 1301906366, 1604705021, 1418751120],
            'blue_mask': 44676180,
            'red_mask': 734623206,
            }
        self.reply_bin_0 = b'\x01\x00\x8d\x4f' b'\x00\x00\x00\x04' \
            b'\x00\x04\x00\x00' b'\x2b\xc9\x75\xe6' \
            b'\x0f\xd9\x22\x87' b'\x02\xa9\xb4\x54' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x1d\x52\xbe\x09' b'\x4d\x99\x83\xbe' \
            b'\x5f\xa5\xda\xfd' b'\x54\x90\x6c\x90'


    def testPackRequest0(self):
        bin = request.AllocColorPlanes._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.AllocColorPlanes._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.AllocColorPlanes._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.AllocColorPlanes._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestFreeColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 727008216,
            'pixels': [61281082, 398475082, 1660604639, 1516738417, 1211104329, 105034864, 884930615, 902914796, 288637231, 2097165249, 1171127263, 1027274519, 806213035, 1485898709, 542709465, 169067149, 1230881159],
            'plane_mask': 1204733200,
            }
        self.req_bin_0 = b'\x58\x00\x00\x14' b'\x2b\x55\x43\xd8' \
            b'\x47\xce\xc5\x10' b'\x03\xa7\x13\x3a' \
            b'\x17\xc0\x3f\x4a' b'\x62\xfa\xd0\xdf' \
            b'\x5a\x67\x97\x71' b'\x48\x2f\xfc\x49' \
            b'\x06\x42\xb4\x70' b'\x34\xbe\xf8\x37' \
            b'\x35\xd1\x62\xec' b'\x11\x34\x41\x2f' \
            b'\x7d\x00\x33\xc1' b'\x45\xcd\xfb\xdf' \
            b'\x3d\x3a\xf7\x17' b'\x30\x0d\xd5\xab' \
            b'\x58\x91\x03\xd5' b'\x20\x59\x16\xd9' \
            b'\x0a\x13\xc2\x8d' b'\x49\x5d\xc1\x87'


    def testPackRequest0(self):
        bin = request.FreeColors._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FreeColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestStoreColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 501035281,
            'items': [{'red': 27925, 'pixel': 1094971765, 'green': 3673, 'flags': 189, 'blue': 31593}, {'red': 41633, 'pixel': 1330003189, 'green': 56186, 'flags': 178, 'blue': 30263}, {'red': 36007, 'pixel': 1813524037, 'green': 29697, 'flags': 224, 'blue': 14071}, {'red': 45716, 'pixel': 1987610486, 'green': 55405, 'flags': 200, 'blue': 35734}],
            }
        self.req_bin_0 = b'\x59\x00\x00\x0e' b'\x1d\xdd\x31\x11' \
            b'\x41\x43\xf1\x75' b'\x6d\x15\x0e\x59' \
            b'\x7b\x69\xbd\x00' b'\x4f\x46\x3c\xf5' \
            b'\xa2\xa1\xdb\x7a' b'\x76\x37\xb2\x00' \
            b'\x6c\x18\x2e\x45' b'\x8c\xa7\x74\x01' \
            b'\x36\xf7\xe0\x00' b'\x76\x78\x87\x76' \
            b'\xb2\x94\xd8\x6d' b'\x8b\x96\xc8\x00'


    def testPackRequest0(self):
        bin = request.StoreColors._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.StoreColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestStoreNamedColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'name': 'blue',
            'flags': 186,
            'cmap': 2061119590,
            'pixel': 1846011298,
            }
        self.req_bin_0 = b'\x5a\xba\x00\x05' b'\x7a\xda\x30\x66' \
            b'\x6e\x07\xe5\xa2' b'\x00\x04\x00\x00' \
            b'\x62\x6c\x75\x65'


    def testPackRequest0(self):
        bin = request.StoreNamedColor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.StoreNamedColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryColors(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 596369797,
            'pixels': [1018587496, 1553480933, 952694607, 341816269, 306591348, 1178729919, 173027853, 875811363],
            }
        self.req_bin_0 = b'\x5b\x00\x00\x0a' b'\x23\x8b\xe1\x85' \
            b'\x3c\xb6\x69\x68' b'\x5c\x98\x3c\xe5' \
            b'\x38\xc8\xf7\x4f' b'\x14\x5f\xb3\xcd' \
            b'\x12\x46\x36\x74' b'\x46\x41\xfd\xbf' \
            b'\x0a\x50\x32\x0d' b'\x34\x33\xd2\x23'

        self.reply_args_0 = {
            'colors': [{'red': 6715, 'blue': 40144, 'green': 56664}, {'red': 5799, 'blue': 22078, 'green': 35523}, {'red': 60111, 'blue': 58654, 'green': 25206}, {'red': 7433, 'blue': 60908, 'green': 14468}, {'red': 31213, 'blue': 9298, 'green': 27481}],
            'sequence_number': 60323,
            }
        self.reply_bin_0 = b'\x01\x00\xeb\xa3' b'\x00\x00\x00\x0a' \
            b'\x00\x05\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x1a\x3b\xdd\x58' b'\x9c\xd0\x00\x00' \
            b'\x16\xa7\x8a\xc3' b'\x56\x3e\x00\x00' \
            b'\xea\xcf\x62\x76' b'\xe5\x1e\x00\x00' \
            b'\x1d\x09\x38\x84' b'\xed\xec\x00\x00' \
            b'\x79\xed\x6b\x59' b'\x24\x52\x00\x00'

        self.req_args_1 = {
            'cmap': 79317049,
            'pixels': [],
            }
        self.req_bin_1 = b'\x5b\x00\x00\x02' b'\x04\xba\x48\x39'


    def testPackRequest0(self):
        bin = request.QueryColors._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryColors._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackRequest1(self):
        bin = request.QueryColors._request.to_binary(*(), **self.req_args_1)
        try:
            assert bin == self.req_bin_1
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest1(self):
        args, remain = request.QueryColors._request.parse_binary(self.req_bin_1, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_1
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryColors._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryColors._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestLookupColor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cmap': 789574750,
            'name': 'octarin',
            }
        self.req_bin_0 = b'\x5c\x00\x00\x05' b'\x2f\x0f\xf4\x5e' \
            b'\x00\x07\x00\x00' b'\x6f\x63\x74\x61' \
            b'\x72\x69\x6e\x00'

        self.reply_args_0 = {
            'sequence_number': 21040,
            'screen_green': 65314,
            'screen_red': 51033,
            'exact_green': 59546,
            'exact_blue': 61512,
            'screen_blue': 29893,
            'exact_red': 41875,
            }
        self.reply_bin_0 = b'\x01\x00\x52\x30' b'\x00\x00\x00\x00' \
            b'\xa3\x93\xe8\x9a' b'\xf0\x48\xc7\x59' \
            b'\xff\x22\x74\xc5' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.LookupColor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.LookupColor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.LookupColor._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.LookupColor._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'x': 14199,
            'fore_red': 65323,
            'back_green': 5090,
            'mask': 420188900,
            'back_blue': 49879,
            'y': 32780,
            'cid': 2022028217,
            'fore_blue': 63540,
            'fore_green': 43028,
            'back_red': 31899,
            'source': 794739749,
            }
        self.req_bin_0 = b'\x5d\x00\x00\x08' b'\x78\x85\xb3\xb9' \
            b'\x2f\x5e\xc4\x25' b'\x19\x0b\x92\xe4' \
            b'\xff\x2b\xa8\x14' b'\xf8\x34\x7c\x9b' \
            b'\x13\xe2\xc2\xd7' b'\x37\x77\x80\x0c'


    def testPackRequest0(self):
        bin = request.CreateCursor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreateCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestCreateGlyphCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fore_red': 56306,
            'source_char': 7568,
            'mask': 2018599719,
            'back_blue': 6500,
            'cid': 1999539964,
            'mask_char': 46124,
            'fore_blue': 30793,
            'fore_green': 16989,
            'back_red': 64484,
            'source': 1412345132,
            'back_green': 52966,
            }
        self.req_bin_0 = b'\x5e\x00\x00\x08' b'\x77\x2e\x8e\xfc' \
            b'\x54\x2e\xad\x2c' b'\x78\x51\x63\x27' \
            b'\x1d\x90\xb4\x2c' b'\xdb\xf2\x42\x5d' \
            b'\x78\x49\xfb\xe4' b'\xce\xe6\x19\x64'


    def testPackRequest0(self):
        bin = request.CreateGlyphCursor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.CreateGlyphCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestFreeCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'cursor': 553262138,
            }
        self.req_bin_0 = b'\x5f\x00\x00\x02' b'\x20\xfa\x1c\x3a'


    def testPackRequest0(self):
        bin = request.FreeCursor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.FreeCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestRecolorCursor(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'fore_red': 44718,
            'fore_green': 33104,
            'back_blue': 49533,
            'back_green': 12163,
            'fore_blue': 17246,
            'back_red': 64013,
            'cursor': 295995276,
            }
        self.req_bin_0 = b'\x60\x00\x00\x05' b'\x11\xa4\x87\x8c' \
            b'\xae\xae\x81\x50' b'\x43\x5e\xfa\x0d' \
            b'\x2f\x83\xc1\x7d'


    def testPackRequest0(self):
        bin = request.RecolorCursor._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.RecolorCursor._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryBestSize(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'height': 34743,
            'drawable': 503496990,
            'item_class': 1,
            'width': 27916,
            }
        self.req_bin_0 = b'\x61\x01\x00\x03' b'\x1e\x02\xc1\x1e' \
            b'\x6d\x0c\x87\xb7'

        self.reply_args_0 = {
            'height': 60728,
            'sequence_number': 34070,
            'width': 35970,
            }
        self.reply_bin_0 = b'\x01\x00\x85\x16' b'\x00\x00\x00\x00' \
            b'\x8c\x82\xed\x38' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryBestSize._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryBestSize._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryBestSize._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryBestSize._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestQueryExtension(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'name': 'XTRA',
            }
        self.req_bin_0 = b'\x62\x00\x00\x03' b'\x00\x04\x00\x00' \
            b'\x58\x54\x52\x41'

        self.reply_args_0 = {
            'sequence_number': 39952,
            'major_opcode': 195,
            'first_error': 150,
            'present': 1,
            'first_event': 202,
            }
        self.reply_bin_0 = b'\x01\x00\x9c\x10' b'\x00\x00\x00\x00' \
            b'\x01\xc3\xca\x96' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.QueryExtension._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.QueryExtension._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.QueryExtension._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.QueryExtension._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestListExtensions(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x63\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 20200,
            'names': ['XTRA', 'XTRA-II'],
            }
        self.reply_bin_0 = b'\x01\x02\x4e\xe8' b'\x00\x00\x00\x04' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x04\x58\x54\x52' b'\x41\x07\x58\x54' \
            b'\x52\x41\x2d\x49' b'\x49\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ListExtensions._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListExtensions._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListExtensions._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListExtensions._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeKeyboardMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'keysyms': [[707837223, 99294840, 1205405602], [67157514, 879853050, 2059131033], [1139736188, 578113249, 1525786315], [1335349176, 246731334, 277761436], [1386594542, 1676932187, 1862777168], [535892916, 342718655, 195574000], [5712156, 1820472637, 848853860], [1123197289, 1664064022, 94999154], [380150420, 402902535, 1061375041], [510686316, 502245882, 422893644], [1423643601, 194077695, 403885178], [1571826296, 529249772, 623556591], [720045879, 37553034, 955963792], [513407882, 861125615, 219940695], [184890179, 472466494, 1649347894], [1679171989, 1991748404, 1674460475], [1762342934, 276695222, 1941684480], [886658026, 1860690072, 577030090], [227169721, 1390318675, 321524615], [2144591365, 545119116, 404205206]],
            'first_keycode': 250,
            }
        self.req_bin_0 = b'\x64\x14\x00\x3e' b'\xfa\x03\x00\x00' \
            b'\x2a\x30\xbd\x27' b'\x05\xeb\x1e\x78' \
            b'\x47\xd9\x07\xa2' b'\x04\x00\xbe\x0a' \
            b'\x34\x71\x7d\xfa' b'\x7a\xbb\xd8\x99' \
            b'\x43\xee\xfe\x7c' b'\x22\x75\x4e\xe1' \
            b'\x5a\xf1\xa6\xcb' b'\x4f\x97\xcf\xb8' \
            b'\x0e\xb4\xd2\x46' b'\x10\x8e\x4d\x9c' \
            b'\x52\xa5\xc0\xee' b'\x63\xf3\xf4\x5b' \
            b'\x6f\x07\xb9\x50' b'\x1f\xf1\x13\xb4' \
            b'\x14\x6d\x78\xbf' b'\x0b\xa8\x38\xf0' \
            b'\x00\x57\x29\x1c' b'\x6c\x82\x35\x3d' \
            b'\x32\x98\x7b\x64' b'\x42\xf2\xa1\x69' \
            b'\x63\x2f\x9a\x16' b'\x05\xa9\x92\x72' \
            b'\x16\xa8\xa2\x94' b'\x18\x03\xce\x07' \
            b'\x3f\x43\x4c\x41' b'\x1e\x70\x74\x6c' \
            b'\x1d\xef\xa9\xfa' b'\x19\x34\xd8\x4c' \
            b'\x54\xdb\x13\xd1' b'\x0b\x91\x63\xff' \
            b'\x18\x12\xcc\x7a' b'\x5d\xb0\x2a\x78' \
            b'\x1f\x8b\xb5\xec' b'\x25\x2a\xb7\xef' \
            b'\x2a\xeb\x07\x37' b'\x02\x3d\x03\x8a' \
            b'\x38\xfa\xd9\x90' b'\x1e\x99\xfb\x8a' \
            b'\x33\x53\xbb\xef' b'\x0d\x1c\x07\x57' \
            b'\x0b\x05\x33\x43' b'\x1c\x29\x44\x3e' \
            b'\x62\x4f\x0d\x36' b'\x64\x16\x21\x95' \
            b'\x76\xb7\xab\x34' b'\x63\xce\x3d\x3b' \
            b'\x69\x0b\x38\x16' b'\x10\x7e\x08\xb6' \
            b'\x73\xbb\xc1\x00' b'\x34\xd9\x53\xea' \
            b'\x6e\xe7\xe0\x98' b'\x22\x64\xc7\xca' \
            b'\x0d\x8a\x55\xb9' b'\x52\xde\x94\x53' \
            b'\x13\x2a\x13\x87' b'\x7f\xd3\xde\x05' \
            b'\x20\x7d\xdb\x8c' b'\x18\x17\xae\x96'


    def testPackRequest0(self):
        bin = request.ChangeKeyboardMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetKeyboardMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'count': 131,
            'first_keycode': 206,
            }
        self.req_bin_0 = b'\x65\x00\x00\x02' b'\xce\x83\x00\x00'

        self.reply_args_0 = {
            'keysyms': [[1550369014, 1683205347, 1879538861], [452613596, 1132022246, 357271408], [528724632, 2118423140, 640580111], [1981239140, 195173082, 497130901], [2001675011, 809172000, 1577756130], [739794769, 1774524806, 787951551], [1784021539, 1998872082, 1747812414], [396316053, 1525431160, 1808906812], [1676662850, 1222579650, 1205117622], [396026453, 1956747483, 1762026309], [1222502216, 1488139702, 1799119214], [1504675136, 1414564657, 419659384], [1934768917, 2095924224, 590955729], [582168798, 383228141, 1552516537], [1482483262, 1041896520, 1047041873], [1932705867, 292473490, 226147737], [780322016, 1965031752, 1481062205], [89811542, 1313413666, 686267194], [237776128, 1310737228, 792176733], [849034415, 1592538831, 837355505]],
            'sequence_number': 61409,
            }
        self.reply_bin_0 = b'\x01\x03\xef\xe1' b'\x00\x00\x00\x3c' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x5c\x68\xc0\xf6' b'\x64\x53\xac\xe3' \
            b'\x70\x07\x7c\xad' b'\x1a\xfa\x55\xdc' \
            b'\x43\x79\x49\xe6' b'\x15\x4b\x87\x70' \
            b'\x1f\x83\xb2\x98' b'\x7e\x44\x92\x64' \
            b'\x26\x2e\x7a\x0f' b'\x76\x17\x4f\x64' \
            b'\x0b\xa2\x1a\xda' b'\x1d\xa1\x9d\x95' \
            b'\x77\x4f\x23\x03' b'\x30\x3a\xfc\x20' \
            b'\x5e\x0a\xa5\xe2' b'\x2c\x18\x5f\x51' \
            b'\x69\xc5\x19\x86' b'\x2e\xf7\x2f\xbf' \
            b'\x6a\x56\x02\x23' b'\x77\x24\x5e\x12' \
            b'\x68\x2d\x80\x3e' b'\x17\x9f\x4d\x95' \
            b'\x5a\xec\x3b\x78' b'\x6b\xd1\xba\x3c' \
            b'\x63\xef\xd8\x42' b'\x48\xdf\x15\xc2' \
            b'\x47\xd4\xa2\xb6' b'\x17\x9a\xe2\x55' \
            b'\x74\xa1\x98\xdb' b'\x69\x06\x63\x45' \
            b'\x48\xdd\xe7\x48' b'\x58\xb3\x35\xb6' \
            b'\x6b\x3c\x61\x6e' b'\x59\xaf\x85\x40' \
            b'\x54\x50\x8b\x31' b'\x19\x03\x7e\x78' \
            b'\x73\x52\x3b\x15' b'\x7c\xed\x44\x00' \
            b'\x23\x39\x44\xd1' b'\x22\xb3\x30\xde' \
            b'\x16\xd7\x98\xed' b'\x5c\x89\x85\xb9' \
            b'\x58\x5c\xe6\x3e' b'\x3e\x1a\x14\x48' \
            b'\x3e\x68\x97\x51' b'\x73\x32\xc0\x4b' \
            b'\x11\x6e\xca\x92' b'\x0d\x7a\xbd\x99' \
            b'\x2e\x82\xc4\xe0' b'\x75\x20\x01\x48' \
            b'\x58\x47\x37\x3d' b'\x05\x5a\x6a\x56' \
            b'\x4e\x49\x1a\x22' b'\x28\xe7\x9b\x3a' \
            b'\x0e\x2c\x2d\x00' b'\x4e\x20\x43\x4c' \
            b'\x2f\x37\xa8\x5d' b'\x32\x9b\x3c\xaf' \
            b'\x5e\xec\x36\xcf' b'\x31\xe9\x07\xf1'


    def testPackRequest0(self):
        bin = request.GetKeyboardMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetKeyboardMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetKeyboardMapping._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetKeyboardMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeKeyboardControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'attrs': {'key_click_percent': -35, 'bell_percent': -53, 'led_mode': 1, 'bell_pitch': -17390, 'auto_repeat_mode': 2, 'bell_duration': -30281, 'key': 235, 'led': 192},
            }
        self.req_bin_0 = b'\x66\x00\x00\x0a' b'\x00\x00\x00\xff' \
            b'\xdd\x00\x00\x00' b'\xcb\x00\x00\x00' \
            b'\xbc\x12\x00\x00' b'\x89\xb7\x00\x00' \
            b'\xc0\x00\x00\x00' b'\x01\x00\x00\x00' \
            b'\xeb\x00\x00\x00' b'\x02\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangeKeyboardControl._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetKeyboardControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x67\x00\x00\x01'

        self.reply_args_0 = {
            'key_click_percent': 206,
            'sequence_number': 30149,
            'bell_percent': 251,
            'bell_pitch': 13779,
            'auto_repeats': [217, 171, 167, 167, 243, 163, 129, 239, 168, 153, 225, 199, 189, 155, 228, 149, 148, 237, 139, 150, 211, 133, 135, 250, 191, 166, 146, 212, 239, 183, 214, 250],
            'global_auto_repeat': 0,
            'led_mask': 438224369,
            'bell_duration': 20235,
            }
        self.reply_bin_0 = b'\x01\x00\x75\xc5' b'\x00\x00\x00\x05' \
            b'\x1a\x1e\xc5\xf1' b'\xce\xfb\x35\xd3' \
            b'\x4f\x0b\x00\x00' b'\xd9\xab\xa7\xa7' \
            b'\xf3\xa3\x81\xef' b'\xa8\x99\xe1\xc7' \
            b'\xbd\x9b\xe4\x95' b'\x94\xed\x8b\x96' \
            b'\xd3\x85\x87\xfa' b'\xbf\xa6\x92\xd4' \
            b'\xef\xb7\xd6\xfa'


    def testPackRequest0(self):
        bin = request.GetKeyboardControl._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetKeyboardControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetKeyboardControl._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetKeyboardControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestBell(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'percent': -19,
            }
        self.req_bin_0 = b'\x68\xed\x00\x01'


    def testPackRequest0(self):
        bin = request.Bell._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.Bell._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangePointerControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'accel_denum': -32484,
            'accel_num': -9346,
            'do_accel': 0,
            'do_thresh': 0,
            'threshold': -8309,
            }
        self.req_bin_0 = b'\x69\x00\x00\x03' b'\xdb\x7e\x81\x1c' \
            b'\xdf\x8b\x00\x00'


    def testPackRequest0(self):
        bin = request.ChangePointerControl._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangePointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetPointerControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6a\x00\x00\x01'

        self.reply_args_0 = {
            'accel_denom': 63793,
            'sequence_number': 59946,
            'threshold': 46060,
            'accel_num': 53419,
            }
        self.reply_bin_0 = b'\x01\x00\xea\x2a' b'\x00\x00\x00\x00' \
            b'\xd0\xab\xf9\x31' b'\xb3\xec\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetPointerControl._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetPointerControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetPointerControl._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetPointerControl._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'allow_exposures': 0,
            'timeout': -12675,
            'interval': -12318,
            'prefer_blank': 2,
            }
        self.req_bin_0 = b'\x6b\x00\x00\x03' b'\xce\x7d\xcf\xe2' \
            b'\x02\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetScreenSaver._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6c\x00\x00\x01'

        self.reply_args_0 = {
            'allow_exposures': 1,
            'timeout': 1865,
            'sequence_number': 14674,
            'prefer_blanking': 1,
            'interval': 60559,
            }
        self.reply_bin_0 = b'\x01\x00\x39\x52' b'\x00\x00\x00\x00' \
            b'\x07\x49\xec\x8f' b'\x01\x01\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetScreenSaver._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetScreenSaver._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetScreenSaver._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestChangeHosts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'host': [188, 226, 135, 199],
            'mode': 1,
            'host_family': 1,
            }
        self.req_bin_0 = b'\x6d\x01\x00\x03' b'\x01\x00\x00\x04' \
            b'\xbc\xe2\x87\xc7'


    def testPackRequest0(self):
        bin = request.ChangeHosts._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ChangeHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestListHosts(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x6e\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 31662,
            'mode': 1,
            'hosts': [{'family': 0, 'name': [34, 23, 178, 12]}, {'family': 0, 'name': [130, 236, 254, 15]}],
            }
        self.reply_bin_0 = b'\x01\x01\x7b\xae' b'\x00\x00\x00\x04' \
            b'\x00\x02\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x04' b'\x22\x17\xb2\x0c' \
            b'\x00\x00\x00\x04' b'\x82\xec\xfe\x0f'


    def testPackRequest0(self):
        bin = request.ListHosts._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ListHosts._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.ListHosts._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.ListHosts._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetAccessControl(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            }
        self.req_bin_0 = b'\x6f\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.SetAccessControl._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetAccessControl._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetCloseDownMode(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 0,
            }
        self.req_bin_0 = b'\x70\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.SetCloseDownMode._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetCloseDownMode._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestKillClient(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'resource': 1679944210,
            }
        self.req_bin_0 = b'\x71\x00\x00\x02' b'\x64\x21\xea\x12'


    def testPackRequest0(self):
        bin = request.KillClient._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.KillClient._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestRotateProperties(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'delta': -27095,
            'window': 109899869,
            'properties': [1758270592, 1474783027, 1362037883, 19212066, 1095428186, 1435857629, 337040311, 1202859364, 1426187239, 725785004, 1722986690, 435243112],
            }
        self.req_bin_0 = b'\x72\x00\x00\x0f' b'\x06\x8c\xf0\x5d' \
            b'\x00\x0c\x96\x29' b'\x68\xcd\x14\x80' \
            b'\x57\xe7\x67\x33' b'\x51\x2f\x0c\x7b' \
            b'\x01\x25\x27\x22' b'\x41\x4a\xe8\x5a' \
            b'\x55\x95\x72\xdd' b'\x14\x16\xd3\xb7' \
            b'\x47\xb2\x2d\x64' b'\x55\x01\xe3\xe7' \
            b'\x2b\x42\x99\xac' b'\x66\xb2\xb0\xc2' \
            b'\x19\xf1\x48\x68'


    def testPackRequest0(self):
        bin = request.RotateProperties._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.RotateProperties._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestForceScreenSaver(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'mode': 1,
            }
        self.req_bin_0 = b'\x73\x01\x00\x01'


    def testPackRequest0(self):
        bin = request.ForceScreenSaver._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.ForceScreenSaver._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetPointerMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'map': [218, 142, 195, 250, 194],
            }
        self.req_bin_0 = b'\x74\x05\x00\x03' b'\xda\x8e\xc3\xfa' \
            b'\xc2\x00\x00\x00'

        self.reply_args_0 = {
            'sequence_number': 11995,
            'status': 187,
            }
        self.reply_bin_0 = b'\x01\xbb\x2e\xdb' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetPointerMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.SetPointerMapping._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.SetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetPointerMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x75\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 35825,
            'map': [165, 233, 136, 197, 230],
            }
        self.reply_bin_0 = b'\x01\x05\x8b\xf1' b'\x00\x00\x00\x02' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\xa5\xe9\x88\xc5' b'\xe6\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.GetPointerMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetPointerMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetPointerMapping._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetPointerMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestSetModifierMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            'keycodes': [[72, 169], [161, 154], [26, 10], [108, 187], [110, 198], [225, 88], [33, 66], [189, 147]],
            }
        self.req_bin_0 = b'\x76\x02\x00\x05' b'\x48\xa9\xa1\x9a' \
            b'\x1a\x0a\x6c\xbb' b'\x6e\xc6\xe1\x58' \
            b'\x21\x42\xbd\x93'

        self.reply_args_0 = {
            'sequence_number': 44526,
            'status': 188,
            }
        self.reply_bin_0 = b'\x01\xbc\xad\xee' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00'


    def testPackRequest0(self):
        bin = request.SetModifierMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.SetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.SetModifierMapping._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.SetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestGetModifierMapping(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x77\x00\x00\x01'

        self.reply_args_0 = {
            'sequence_number': 58377,
            'keycodes': [[3, 183], [213, 173], [9, 97], [35, 60], [249, 78], [175, 62], [237, 11], [26, 119]],
            }
        self.reply_bin_0 = b'\x01\x02\xe4\x09' b'\x00\x00\x00\x04' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x00\x00\x00\x00' b'\x00\x00\x00\x00' \
            b'\x03\xb7\xd5\xad' b'\x09\x61\x23\x3c' \
            b'\xf9\x4e\xaf\x3e' b'\xed\x0b\x1a\x77'


    def testPackRequest0(self):
        bin = request.GetModifierMapping._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.GetModifierMapping._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)

    def testPackReply0(self):
        bin = request.GetModifierMapping._reply.to_binary(*(), **self.reply_args_0)
        try:
            assert bin == self.reply_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackReply0(self):
        args, remain = request.GetModifierMapping._reply.parse_binary(self.reply_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.reply_args_0
        except AssertionError:
            raise AssertionError(args)


class TestNoOperation(unittest.TestCase):
    def setUp(self):
        self.req_args_0 = {
            }
        self.req_bin_0 = b'\x7f\x00\x00\x01'


    def testPackRequest0(self):
        bin = request.NoOperation._request.to_binary(*(), **self.req_args_0)
        try:
            assert bin == self.req_bin_0
        except AssertionError:
            raise AssertionError(tohex(bin))

    def testUnpackRequest0(self):
        args, remain = request.NoOperation._request.parse_binary(self.req_bin_0, dummy_display, 1)
        try:
            assert len(remain) == 0
        except AssertionError:
            raise AssertionError(tohex(remain))
        try:
            assert args == self.req_args_0
        except AssertionError:
            raise AssertionError(args)


if __name__ == "__main__":
    check_endian()
    unittest.main()
