import unittest

import numpy

import cupy
from cupy import testing


@testing.gpu
class TestBasic(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_scalar_constant_none(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = 2
        a = xp.pad(array, pad_width, mode='constant')
        return a

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_scalar_constant_scalar(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = 2
        a = xp.pad(array, pad_width, mode='constant', constant_values=1)
        return a

    # @testing.for_all_dtypes()
    # @testing.numpy_cupy_array_equal()
    # def test_pad_scalar_constant_sequence(self, xp, dtype):
    #     array = xp.arange(10).reshape([2, 5])
    #     pad_width = 2
    #     a = xp.pad(array, pad_width, mode='constant', constant_values=[1, 2])
    #     return a

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_sequence_constant_none(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = [2, 3]
        a = xp.pad(array, pad_width, mode='constant')
        return a

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_sequence_constant_scalar(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = [2, 3]
        a = xp.pad(array, pad_width, mode='constant', constant_values=1)
        return a

    # @testing.for_all_dtypes()
    # @testing.numpy_cupy_array_equal()
    # def test_pad_sequence_constant_sequence(self, xp, dtype):
    #     array = xp.arange(10).reshape([2, 5])
    #     pad_width = [2, 3]
    #     a = xp.pad(array, pad_width, mode='constant', constant_values=[1, 2])
    #     return a

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_1dsequence_constant_none(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = [2]
        a = xp.pad(array, pad_width, mode='constant')
        return a

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_pad_1dsequence_constant_scalar(self, xp, dtype):
        array = xp.arange(10).reshape([2, 5])
        pad_width = [2]
        a = xp.pad(array, pad_width, mode='constant', constant_values=1)
        return a

    # @testing.for_all_dtypes()
    # @testing.numpy_cupy_array_equal()
    # def test_pad_1dsequence_constant_sequence(self, xp, dtype):
    #    array = xp.arange(10).reshape([2, 5])
    #    pad_width = [2]
    #    a = xp.pad(array, pad_width, mode='constant', constant_values=[1, 2])
    #    return a