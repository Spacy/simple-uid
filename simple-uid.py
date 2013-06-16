#-*- encoding: utf-8 -*-
import time
'''
生成32位的惟一ID，该ID具有以下特性:
1. 单进程内生成ID惟一
2. ID基本按照生成时间递增
'''
class Uniqid:
    def __init__(self, counter_bit=8, time_shift=2, time_diff=363139923):
        '''
        counter_bit: 计数器位数
        time_shift: 时间戳左移量,time_shift=1: 近70年不会重复，time_shift=2: 34年不会重复
        time_diff: 时间戳减去time_diff，防止时间戳过大
        '''
        self.time_shift = time_shift
        self.time_diff = time_diff
        self.counter_mask = -1 << counter_bit
        self.counter = -1

    def get_id(self):
        self.counter = (self.counter + 1) & ~self.counter_mask
        return (int(time.time() - self.time_diff) << self.time_shift) & self.counter_mask | self.counter

if __name__ == '__main__':
    generator = Uniqid()
    for i in range(1, 200):
        print generator.get_id()
