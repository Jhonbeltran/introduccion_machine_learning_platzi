from tensorflow.examples.tutorials.mnist import  input_data
import tensorflow as tf

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

#Matriz de ceros con 784 posiciones
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W)+b)
y_= tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)