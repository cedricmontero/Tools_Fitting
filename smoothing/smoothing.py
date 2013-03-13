# -*- coding: utf-8 -*-
"""
 Module of interpolation methods
"""

__author__  = "Cédric Montero"
__contact__ = "cedric.montero@esrf.fr"
__version__ = "0.1_alpha"

# External modules (preliminary installation could be require):
import numpy

# Internal modules (lacal modules files):

# Program configurations:

# Preliminary functions definitions:
def request_order(vec):
	"""
	Check ordering of a numpy array (True : increasing ; False : decreasing)
	@param vec: 1 dimension array to check ordering
	#type  vec: numpy.ndarray (1,)
	"""
	return all(vec[:-2] < vec[1:-1])

# Main module functionality definitions:
def SmoothInterp(x0,y0,xi,wMin,nMin):
	"""Local interpolation by a 2nd order polynome
	@param x0,y0: Initials data in increasing or decreasing order
	@param xi: Abscissa of interpolated points
	@param wMin: Minimal width of the interpolated window
	@param nMin: Minimal number of points on one side of the interpolation window
	"""
	# Cheking parameters
	#	dimensions:
	if x0.ndim !=1 or y0.ndim !=1 or xi.ndim != 1:
		raise ValueError, "SmoothInterp only accepts 1 dimension arrays."
	#	order:
	if request_order(x0) == False:
		x0 = x0[::-1]# Reverse entry data
		y0 = y0[::-1]
	if request_order(xi) == False:
		xi = xi[::-1]
	#	out of range data
	if xi[0] < x0[0] or xi[-1] > x0[-1]:
		raise ValueError, "SmoothInterp do not accept extrapolation"
	
	# Initialization:
	n = len(xi)# Dimension of interpolation data domain.
	yi = []
	dyi=[]
	ddyi=[]
			
	#Define the interpolation window :
	for i in range(0,n):
		indx0 = numpy.abs(x0-xi[i]).argmin()#Nearest x0 index.
		#Define interpolation windows
		if indx0 < nMin or indx0+nMin > len(x0)-1:
			raise ValueError, "nMin value exceed initial domain"
		x_interp = numpy.r_[x0[indx0-nMin:indx0],x0[indx0],x0[indx0+1:indx0+1+nMin]]
		y_interp = numpy.r_[y0[indx0-nMin:indx0],y0[indx0],y0[indx0+1:indx0+1+nMin]]
		#Calculate interpolation matrix inversion :
		A = numpy.array([[len(x_interp),numpy.sum(x_interp),numpy.sum(x_interp**2)],\
		[numpy.sum(x_interp),numpy.sum(x_interp**2),numpy.sum(x_interp**3)],\
		[numpy.sum(x_interp**2),numpy.sum(x_interp**3),numpy.sum(x_interp**4)]])
		W = numpy.array([numpy.sum(y_interp),numpy.sum(y_interp*x_interp),numpy.sum(y_interp*x_interp**2)])
		C = numpy.linalg.solve(A,W)
		yi.append(C[0]+C[1]*xi[i]+C[2]*(xi[i]**2))
		dyi.append(C[1]+2*C[2]*xi[i])
		ddyi.append(2*C[2])
	return numpy.array(yi),numpy.array(dyi),numpy.array(ddyi)



"""
def smooth(x,window_len=11,window='hanning'):
   ##The signal is prepared by introducing reflected window-length copies of the signal at both ends so that boundary effect are minimized in the beginning and end part of the output signal.
   if x.ndim != 1:
      raise ValueError, "smooth only accepts 1 dimension arrays."
   if x.size < window_len:
      raise ValueError, "Input vector needs to be bigger than window size."
   if window_len<3:
      return x
   if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
      raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
   s=np.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
   if window == 'flat': #moving average
      w=np.ones(window_len,'d')
   else:
      w=eval('np.'+window+'(window_len)')
   y=np.convolve(w/w.sum(),s,mode='valid')
   y = y[int(window_len/2)-1:-1-int(window_len/2)+1]
   return y
"""

def LinInterp(x0,y0,xi):
	"Linear interpolation of (x0,y0) data at xi values"
	if xi[0]<x0[0] or xi[-1]>x0[-1]:
		print "Interpolation domain out of data range"
		yi = numpy.zeros_like(xi)
	else:
		yi = numpy.interp(xi,x0,y0)#Tested faster than scipy.interpolate.interp1d
	return yi
	
