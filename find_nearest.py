#coding: utf8
"""
Module of function to search in arrays
"""
___author___   = 'Cédric Montero'
___contact___  = 'cedric.montero@esrf.fr'
___copyright__ = '2012, ESRF'
___version___  = '0'

#External modules:
import numpy

def find_nearest(value,array):
    """
    Return the nearest element in an array of a specified value
    @param value : value to look into data array
    @type  value : integer or float
    @param array : data array of numeric values ordered increasingly or decreasly
    @type  array : numpy 1D array
    """
    idx = numpy.abs(value-array).argmin()
    return idx,array[idx]


if __name__ == "__main__":
    data  = numpy.arange(-2.0,5.0,.5)
    point =  -1.6
    print find_nearest(point,data)
