
import numpy as np
from PIL import Image
import math
from numba import njit

# Load and preprocess images
image_a = Image.open("imageA.jpg").convert("RGB")
image_b = Image.open("imageB.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)

pixels_a = np.array(image_a)
pixels_b = np.array(image_b)

flat_a = pixels_a.reshape(-1, 3)
flat_b = pixels_b.reshape(-1, 3)
num_pixels = len(flat_a)

perm = np.arange(num_pixels)
np.random.shuffle(perm)

@njit
def anneal(flat_a, flat_b, perm, T, alpha, iterations):
    num_pixels = len(flat_a)
    current_cost = np.sum((flat_a[perm] - flat_b) ** 2) / num_pixels

    for i in range(iterations):
        idx1 = np.random.randint(0, num_pixels)
        idx2 = np.random.randint(0, num_pixels)

        old_cost = (np.sum((flat_a[perm[idx1]] - flat_b[idx1]) ** 2) +
                    np.sum((flat_a[perm[idx2]] - flat_b[idx2]) ** 2)) / num_pixels

        perm[idx1], perm[idx2] = perm[idx2], perm[idx1]

        new_cost = (np.sum((flat_a[perm[idx1]] - flat_b[idx1]) ** 2) +
                    np.sum((flat_a[perm[idx2]] - flat_b[idx2]) ** 2)) / num_pixels

        delta = new_cost - old_cost
        arg = -delta / T

        # Overflow-safe acceptance
        if delta < 0 or (arg > -700 and np.random.random() < math.exp(arg)):
            current_cost += delta
        else:
            perm[idx1], perm[idx2] = perm[idx2], perm[idx1]

        T *= alpha

    return perm

# Run annealing
T = 2000.0
alpha = 0.999
iterations = 2000000

perm = anneal(flat_a, flat_b, perm, T, alpha, iterations)

# Build final image
mapped_pixels = flat_a[perm].reshape(pixels_a.shape)
mapped_image = Image.fromarraymapped_image = Image.fromarray(mapped_pixels.astype('uint8'), 'RGB')
mapped_image.save("annealed_image_numba.jpg")
