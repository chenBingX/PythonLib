import tensorflow as tf

num1 = raw_input("num1:")
num2 = raw_input("num2:")
tf_num1 = tf.constant(num1)
tf_num2 = tf.constant(num2)
with tf.Session() as sess:
    with tf.device("/cpu:0"):
        result = sess.run(tf_num1 + tf_num2)
        print result

