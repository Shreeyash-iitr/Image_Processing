<h1> Canny Edge Detection </h1>
  <h4> - Algorithm with code in python </h4>


The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.</br>
I am using following image as my query image.
<img src='nobita.jpg'>
<h3>(1) Apply Gaussian filter to smooth the image in order to remove the noise</h3>
              After converting image to gray-scale and applying gaussian filter, image looks as following:
<img src='images/gaussian.jpg'>

<h3>(2) Find the intensity gradients of the image</h3>
calculate derivative in x and y directions, its magnitude and direction.
<h5>                   X-derivative</h5>
<img src='images/dx.jpg'>
<h5>                   Y-derivative</h5>
<img src='images/dy.png'>
<h5>                  Gradient Magnitude</h5>
<img src='images/grad_magnitude.png'>
<h3>(3)Apply non-maximum suppression to get rid of spurious response to edge detection</h3>
<img src='images/non_maximal.png'>
<h3>(4) Apply double threshold to determine potential edges and Track edge by hysteresis</h3>
Final output looks like : 
<img src='images/output.jpg'>
<h4> Output by cv2.Canny() function</h4>
<img src='images/cv2.Canny.jpg'>
