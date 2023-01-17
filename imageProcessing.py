# # Lab03, Dor Shukrun 203841697
# # Image Processing

import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np

# ############################################
#
##### (2, 3, 4, 5) #############
img = matplotlib.image.imread('colors.png')
print(type(img))
print(img.shape)
#
#
# Exc 6:
plt.imshow(img)
plt.show()

# # Exc 7:
# plt.imshow(img[:, :, 0], cmap='gray')
# plt.show()
# plt.imshow(img[:, :, 1], cmap='gray')
# plt.show()
# plt.imshow(img[:, :, 2], cmap='gray')
# plt.show()
# plt.imshow(img[:, :, 3], cmap='gray')
# plt.show()
# #####################################
#
# # Exc 8:
# img[:, :, 3] = np.random.uniform(size=(1000, 1000))
#
# # Exc 9:
# img = img[:, :, :3]
#
# # Exc 10:
# plt.imshow((img[::-1,:,:]))
#
# Exc 11:
# plt.imshow((img[:, ::-1, :]))
# plt.show()

# Exc 12:
plt.imshow(img[:, :, 0].T, cmap="gray")
plt.show()

# Exc 13:
zeroImg = np.zeros((1000, 1000, 3))

# Exc 14:
zeroImg[:, :, 0] += img[:, :, 0].T

# Exc 15:
zeroImg[:, :, 1] += img[:, ::-1, 1]

# Exc 16:
zeroImg[:, :, 2] += img[::-1, :, 2]

# Exc 17:
plt.imshow(zeroImg)
plt.show()

# # Exc 18:
# plt.imshow((img[1:, :, :]) - (img[:-1, :, :]))
# plt.show()
#
# # Exc 19:
# plt.imshow((img[:-1, :, :]) - (img[1:, :, :]))
# plt.show()
#
# # Exc 20:
# plt.imshow((img[:-1, :, :] - img[1:, :, :]) + (img[1:, :, :] - img[:-1, :, :]))
# plt.show()

# Exc 21

# Exc 22:
zeroImg2 = np.zeros((1000, 1000, 3))
zeroImg2[:, :, 0] += img[:, ::-1, 0]
zeroImg2[:, :, 0] += img[:, ::, 0]
zeroImg2[:, :, 1] += img[::-1, :, 1]
plt.imshow(zeroImg2)
plt.show()
