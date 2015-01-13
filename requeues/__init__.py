# -*- coding: utf-8 -*-

import math
import redis

NUM_BLOCK_SIZE = 1000


class Tools(object):

    @staticmethod
    def get_block_slices(num_elements, num_block_size=None):

        block_slices = []

        if num_block_size is None:
            num_block_size = NUM_BLOCK_SIZE

        if num_block_size > num_elements or num_elements is 0:
            return [[0, num_elements]]

        for i in range(0, int(math.ceil(num_elements / float(num_block_size)))):
            position_from = i * num_block_size
            position_to = position_from + num_block_size
            block_slices.append([position_from, position_to])

        return block_slices
