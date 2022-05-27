import numpy as np

def get_mask(n1, n2, r):
    arr = np.zeros((n1, n2))
    # arr = np.ones((n1, n2))
    center = (n1/2, n2/2)
    for i in range(n1):
        for j in range(n2):
            if (i-center[0])**2 + (j-center[1])**2 <= r**2:
                # arr[i][j] = 0
                # arr[i][j] = 0.0
                arr[i][j] = 1.0
            else:
                # pass
                arr[i][j] = 0.0
    return arr

mask = get_mask(224, 224, 80)


def fourier_transform_rgb(image, mask_size, R=None):
    f_size = 25
    if R is None:
        # Randomly get a R
        R = int(random.uniform(int(mask_size//2*0.8),int(mask_size//2* math.sqrt(2))+1))
    mask = get_mask(mask_size, mask_size, R)
    transformed_channels = []
    n1 = image.shape[-2]
    n2 = image.shape[-1]
    for i in range(3):
        rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i])))
        rgb_fft *= mask
        transformed_channels.append(abs(np.fft.ifft2(rgb_fft)))

    final_image = np.dstack([transformed_channels[0],
                             transformed_channels[1],
                             transformed_channels[2]])

    return final_image
