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
    index,value = find_nearest(point,data)
    print "The closest value is at the index %i and the value at this index is %s" %(index,str(value))
    # Benchmark on MacBook 2.4GHz Intel Core 2 Duo 4Go 667MHz DDR2 SDRAM :
    # approx. 19 us for len(data) = 1000
    # approx. 536 us for len(data) = 100000
