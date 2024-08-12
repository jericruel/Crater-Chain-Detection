import numpy as np
import h5py
import os
import matplotlib.pyplot as plt

train_imgs_path = 'data/train_images.hdf5'
test_imgs_path = 'data/test_images.hdf5'

train_imgs = h5py.File(train_imgs_path, 'r')

fig = plt.figure(figsize=[12, 6])
[ax1, ax2] = fig.subplots(1,2)
ax1.imshow(train_imgs['input_images'][3][...], origin='upper', cmap='Greys_r', vmin=120, vmax=200)
ax2.imshow(train_imgs['target_masks'][3][...], origin='upper', cmap='Greys_r')
plt.show()