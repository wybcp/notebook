#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Disk = namedtuple(
    'Disk',
    'major_number minor_number device_name '
    'read_count read_merged_count read_sections time_spent_reading '
    'write_count write_merged_count write_sections time_spent_write '
    'io_requests time_spent_doing_io weighted_time_spent_doing_io',
)


def get_disk_info(device):
    """
    从 /proc/diskstats 中读取磁盘的 IO 信息
    $ cat /proc/diskstats
    253       0 vda 13782022 2143 1636326514 207082488 6214221 3768592 174494280 56962460 0 18483856 264041352
    """
    with open("/proc/diskstats") as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))
    raise RuntimeError("device({0}) not found !".format(device))


def main():
    disk_info = get_disk_info('vda')
    print(disk_info)
    print("磁盘写次数: {0}".format(disk_info.write_count))
    print("磁盘写字节数: {0}".format(float(disk_info.write_sections) * 512))
    print("磁盘写延时:{0} ".format(disk_info.time_spent_write))


if __name__ == '__main__':
    main()
