# simpix

C++ starter code
* simpix_start.cpp
use make to build this example

Usage: simapix_start image1 image2 <output=out.png>

Python starter code
* simpix_start.py

Usage: simapix_start image1 image2 <output=out.png>

Here's my comments on the solution.

Well, my salesman code is kinda terrible, but here's what AI said for my simpix code!

My images are from Impressionism. The small versions are called imageA.jpg and imageB.jpg. They are pretty small (500 x 393).

I also tried for full-size versions, called large_imageA.jpg and large_imageB.jpg. They're quite large at 2200x1639 and 4719x3713, respectively.

The two codes (simpix.py and large_simpix.py) are mostly identical. All I changed was the names of the input and output files and I made the large_simpix.py version run hotter for longer, so that it could actually converge.

My results are called annealed_image_numba.jpg and large_annealed_image_numba.jpg.

How to run my code:

First, enter the phys56xx environment.

Then, run the following commands:

python simpix.py

python large_simpix.py

They run pretty fast! Simpix takes 1.9 s and large simpix takes 119 s.