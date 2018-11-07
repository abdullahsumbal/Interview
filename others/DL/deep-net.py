import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# 3 classes, 0-2

'''
one_hot
0 = [1,0,0]
1 = [0,1,0]
2 = [0,0,1]
'''
# we will have three layer in our network
# they dont have to identical
# feel free ot change
n_node_hl1 = 500
n_node_hl2 = 500
n_node_hl3 = 500

n_classes = 10
# this will take 100 images into the system at a time
batch_size = 100

#place holders
# height x width
# image size 28 * 28= 784
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

def neural_network_model(data):

    # (input_data * weights) + biases

    hidden_l_layer = {'weights':tf.Variable(tf.random_normal([784, n_node_hl1])),
                      'biases': tf.Variable(tf.random_normal([n_node_hl1]))}
    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_node_hl1, n_node_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_node_hl2]))}
    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_node_hl2, n_node_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_node_hl3]))}
    output_layer = {'weights':tf.Variable(tf.random_normal([n_node_hl3, n_classes])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}

    l1 = tf.add(tf.matmul(data, hidden_l_layer['weights']), hidden_l_layer['biases'])
    # pass through activation function
    #linear Rectifier: f(x) = max(0,x)
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    # pass through activation function
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    # pass through activation function
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights'])+ output_layer['biases']

    return output


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdadeltaOptimizer().minimize(cost)

    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict= {x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss:', epoch_loss)

        correct = tf.equal(tf.arg_max(prediction,1), tf.arg_max(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print("Accuracy:",accuracy.eval({x: mnist.test.images, y:mnist.test.labels}))

train_neural_network(x)