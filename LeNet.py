"""
LeNet design to impliment a CNN to differentiate between cat pictures and not cat pictures
data from: https://www.kaggle.com/crawford/cat-dataset
LeNet design from: https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/
sources:
https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks/
steps:
1) converting an RGB image into numpy array
the shape of the formed numpy array:(rows, coloumns, colours)
2) initialize filters
here I am choosing to use a filter of (10*10*3), randomly initialized matrix that is eventually
learned.
"""
#initial imports
from matplotlib.image import imread
import numpy as np

if __name__ == '__main__':
    # print out the image as a numpy array
    img = imread('CAT_00/1.jpg') #(500,375,3)
    # print(img.shape)
    img_tuple = img.shape
    filter = np.random.rand(10,10,3)
    # print(filter)
    
