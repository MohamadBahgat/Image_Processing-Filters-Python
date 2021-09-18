# Image_Processing-Filters-Python
Smoothing, Sharpening, High-Pass Filter, Low-Pass Filter (Image Processing)

Question 1:
Implement the histogram smoothing algorithm. Your function should take as input the gray scaled image and
the value of K. The function should output the histogram of the image before smoothing and after smoothing.
Apply your function to the image “Sphinx.png”.
Apply K with two values, K = 3 and K = 11.
You should Do:
A plot of the histogram before smoothing for both values of K. Name the plot “Before_Smoothing.jpg”.
A plot of the histogram after smoothing for both values of K. Name the plot “After_Smoothing.jpg”.


Question 2:
Implement a function that applies a low-pass, a high-pass and a bandpass filter to an input gray-scale image.
Your low-pass filter should be the Butterworth filter, your high-pass filter should be the Gaussian filter and
your bandpass filter should use both. Implement a function for every filter.
The low-pass filter function should take as inputs the input image, the order of the filter, the cutoff distance
of the Butterworth filter D0. It should output the filtered image.
The high-pass filter function should take as inputs the input image, the cutoff distance of the Gaussian filter
D0 . It should output the filtered image.
In the Bandpass filter you should use the previous implemented functions.
Apply the filters to the image “cameraman.png”.
