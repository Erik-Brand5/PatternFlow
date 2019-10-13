# -*- coding: utf-8 -*-
# Author: Tianjie Shi 
# Last update: 13/10/2019
import histogram_matching as hm
import matplotlib.pyplot as plt
from skimage import data
import tensorflow as tf
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def plot(image1,image2):
    #for the source image and reference, convert them to tensor first
    image1  = tf.convert_to_tensor(image1)
    image2 = tf.convert_to_tensor(image2)
    matched = hm.match_histograms(image1, image2, multichannel=True)
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
    for aa in (ax1, ax2, ax3):
        aa.set_axis_off()

    ax1.imshow(image1)
    ax1.set_title('Source')
    ax2.imshow(image2)
    ax2.set_title('Reference')
    ax3.imshow(matched)
    ax3.set_title('Matched')
    plt.tight_layout()
    plt.show()
##Driver script

if __name__ == "__main__":
    #load the images
    reference = data.coffee()
    image = data.astronaut()
    #plot 
    plot(image,reference)
    