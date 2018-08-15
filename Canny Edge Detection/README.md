
# Canny Edge Detection

#### - Algorithm with [code](https://github.com/Shreeyash-iitr/Image_Processing/blob/master/Canny%20Edge%20Detection/code.py) in python

The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.  
I am using following image as my query image. ![](nobita.jpg)

### (1) Apply Gaussian filter to smooth the image in order to remove the noise

After converting image to gray-scale and applying gaussian filter, image looks as following: ![](images/gaussian.jpg)

### (2) Find the intensity gradients of the image

calculate derivative in x and y directions, its magnitude and direction.

##### X-derivative

![](images/dx.jpg)

##### Y-derivative

![](images/dy.png)

##### Gradient Magnitude

![](images/grad_magnitude.png)

### (3)Apply non-maximum suppression to get rid of spurious response to edge detection

![](images/non_maximal.png)

### (4) Apply double threshold to determine potential edges and Track edge by hysteresis

Final output looks like : ![](images/output.jpg)

#### Output by cv2.Canny() function (for comparision)

![](images/cv2.Canny.jpg)
