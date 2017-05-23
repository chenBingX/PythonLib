import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

# sess = tf.Session()  # 打开会话Session
# result = sess.run(product)
# print result
# sess.close() # Session使用后需要关闭

with tf.Session() as sess2:
    with tf.device("/gpu:1"): # 选择启用GPU
        result2 = sess2.run(product)
        print result2
