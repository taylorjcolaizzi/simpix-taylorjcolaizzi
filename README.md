# simpix

C++ starter code
* simpix_start.cpp
use make to build this example

Usage: simapix_start image1 image2 <output=out.png>

Python starter code
* simpix_start.py

Usage: simapix_start image1 image2 <output=out.png>

### Taylor's work

Here's my comments on the solution.

In the simpix folder, I've laid out a few images. My first two are from the Impressionism Wikipedia page and are named imageA.jpg, large_imageA.jpg, imageB.jpg, and large_imageB.jpg. The imageX.jpg are pretty small (500 x 400 ish), but the large_imageX.jpg are full size (2200 x 1639 and 4719 x 3713). I also have a second set of images I pulled from the National Gallery of Art's free download site (I had no idea this existed until starting this project!). Those are called large_imageC.jpg and large_imageD.jpg, and their sizes are (4000 x 3000 ish).

The two codes (simpix.py and large_simpix.py) are mostly identical. simpix.py is what you should run first, just to check that all the code is working as expected. It only operates on the small images imageA.jpg and imageB.jpg. To make large_simpix.py, all I changed was the names of the input and output files and I made it run hotter for longer, so that it could actually converge for the larger images. I also hardcoded in the other images, so this code is just copy-pasted 4 times in a row!

The results of simpix.py are called annealed_image_numba.jpg and the results of large_simpix.py are called large_annealed_image_numba_A->B, ...B->A, ...C->D, ...D->C.jpg. These just represent the four transformations we did in this assignment.

How to run my code:

First, enter the phys56xx environment.

Then, run the following commands:

For the short version (2.1 s runtime approximately with 4 cores and 16 Gb ram on Rivanna):

python simpix.py

For the large version (8 min runtime approximately with 4 cores and 16 Gb ram on Rivanna): 

python large_simpix.py

They run pretty fast! Here, I'll just write my results verbatim:

simpix: 2.1 s

large_simpix: 118.9 s, 108.1 s, 114.3 s, 114.5 s.