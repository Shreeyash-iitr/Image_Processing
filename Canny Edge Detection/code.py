import numpy
from scipy import misc
from scipy.ndimage import filters


#>>(0)<<   loading query image and getting its gray-scaled image=============================
img = misc.imread('nobita.jpg', mode='L')
# mode = 'L' converts RGB image to gray-scale
img = numpy.array(img, dtype=float)

#>>(1)<<   Noise reduction, May be performed by Gaussian filter.=================================
gauss = filters.gaussian_filter(img, sigma=2)  # value of sigma can be changed


#>>(2)<<   calculating derivative, gradient magnitude and direction===================================
dx = filters.convolve(gauss, [[-1,0,1],[-2,0,2],[-1,0,1]])        #differentiation mask
dy = filters.convolve(gauss, [[-1,-2,-1],[0,0,0],[1,2,1]])        #differentiation mask
grad_mag = numpy.power(numpy.power(dx,2)+numpy.power(dy,2),0.5)
grad = numpy.arctan2(dy, dx)                                      # returns values in range [-pi,pi]
grad_dir = numpy.round(grad*(180/numpy.pi))+180     # converting angle range to [0,360] (in degree)
temp = grad_mag.copy()


#>>3<< Non-maximal supression=========================================================================
for r in range(img.shape[0]):
    for c in range(img.shape[1]):
        if r==0 or r==img.shape[0]-1 or c==0 or c==img.shape[1]-1: # making image boundry pixels black
            temp[r,c] = 0
            continue
        x = grad_dir[r,c]


        if any([x<=5, x>=175 and x<=185, x>=355]): # means for horizontal gradient direction
            if grad_mag[r,c]<=grad_mag[r,c+1] or grad_mag[r,c]<=grad_mag[r,c-1]:
                temp[r,c] = 0
        if any([x>=85 and x<=95, x>=265 and x<=275]):# vertical direction
            if grad_mag[r,c]<=grad_mag[r+1,c] or grad_mag[r,c]<=grad_mag[r-1,c]:
                temp[r,c] = 0
        if any([x>5 and x<85, x>185 and x<265]):# line having <45 from +X-axis
            if grad_mag[r,c]<=grad_mag[r-1,c+1] or grad_mag[r,c]<=grad_mag[r+1,c-1]:
                temp[r,c] = 0
        if any([x>95 and x<175, x>185 and x<265]):# line having <-45 from +X-axis
            if grad_mag[r,c]<=grad_mag[r-1,c-1] or grad_mag[r,c]<=grad_mag[r+1,c+1]:
                temp[r,c] = 0
#===========  The values of upper threshold and lower threshold are defined here ======================
t_upper = 91
t_lower = 31

edges = temp.copy()
current_pix = []
final_edges = numpy.zeros((img.shape[0],img.shape[1]))

#>>4<<  Tracing edges with hysteresis  ===============================================================
for r in range(1,img.shape[0]-1):
    for c in range(1,img.shape[1]-1):
        if edges[r,c] <= t_lower:
            final_edges[r,c] = 0
        if edges[r,c] >= t_upper:
            final_edges[r,c] = 255
        if all([edges[r,c]<t_upper,edges[r,c]>t_lower]):
            patch = edges[r-1:r+2,c-1:c+2]   #  3x3 matrix surrounding pixel whose value lies inbetween t_upper and t_lower
            if patch.max() == 255:
                current_pix.append((r,c))
                final_edges[r,c] = 255


while len(current_pix) > 0:
    new_pix = []
    for r,c in current_pix:
        for dr in range(-1,2):
            for dc in range(-1,2):
                R = r+dr
                C = c+dc
                if all([R!=r,C!=c]):
                    if all([edges[r, c] < t_upper, edges[r, c] > t_lower]):
                        final_edges[R,C] = 255
                        new_pix.append((R,C))
    current_pix = new_pix

    
# displaying final output
misc.imshow(final_edges)
