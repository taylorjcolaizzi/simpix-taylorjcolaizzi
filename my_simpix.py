
import numpy as np
from PIL import Image
import random
import math

# Load and preprocess images
image_a = Image.open("imageA.jpg").convert("RGB")
image_b = Image.open("imageB.jpg").convert("RGB")
image_a = image_a.resize(image_b.size)

pixels_a = np.array(image_a)
pixels_b = np.array(image_b)

flat_a = pixels_a.reshape(-1, 3)
flat_b = pixels_b.reshape(-1, 3)

perm = np.arange(len(flat_a))
np.random.shuffle(perm)

# Precompute initial cost
mapped = flat_a[perm]
current_cost = np.sum((mapped - flat_b) ** 2)

# Simulated annealing parameters
T = 1e6
alpha = 0.995
iterations = 200000

for i in range(iterations):
    idx1, idx2 = random.sample(range(len(perm)), 2)

    # Compute old contributions
    old_cost = np.sum((flat_a[perm[idx1]] - flat_b[idx1]) ** 2) + \
               np.sum((flat_a[perm[idx2]] - flat_b[idx2]) ** 2)

    # Swap
    perm[idx1], perm[idx2] = perm[idx2], perm[idx1]

    # Compute new contributions
    new_cost = np.sum((flat_a[perm[idx1]] - flat_b[idx1]) ** 2) + \
               np.sum((flat_a[perm[idx2]] - flat_b[idx2]) ** 2)

    delta = new_cost - old_cost

    # Accept or revert
    if delta < 0 or random.random() < math.exp(-delta / T):
        current_cost += delta
    else:
        perm[idx1], perm[idx2] = perm[idx2], perm[idx1]  # revert

    T *= alpha

    if i % 10000 == 0:
        print(f"Iteration {i}, Cost: {current_cost}, Temp: {T}")

# Build final image
mapped_pixels = flat_a[perm].reshape(pixels_a.shape)
mapped_image = Image.fromarray(mapped_pixels.astype('uint8'), 'RGB')
mapped_image.save("annealed_image_optimized.jpg")
mapped_image.show()