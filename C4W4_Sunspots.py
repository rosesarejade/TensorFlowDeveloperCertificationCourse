import wget
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import csv

""""
wget.downlohttps://storage.googleapis.com/tensorflow-1-public/course4/Sunspots.csv)

time_step = []
sunspots = []

with open('./Sunspots.csv') as csvfile:
    #initialize reader
    reader = csv.reader(csvfile, delimiter=',')
    #skip the header
    next(reader)

    #append number to lists
    for row in reader:
        time_step.append(int(row[0]))
        sunspots.append(float(row[2]))

#convert list to arrays
time = np.array(time_step)
series = np.array(sunspots)

plot_series(time, series, xlabel='Month', ylabel='Monthly mean total sunspot number')
"""
#building a model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(filters=64, kernel_size=5, strides=1, activation="relu", padding='causal', input_shape=[30, 1]),
    tf.keras.layers.Flatten()
])