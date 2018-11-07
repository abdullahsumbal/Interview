# Deep Learning

Deep learning uses Neural Networks.
Deep Learning is biologically Inspired. See the image below
![f](image1.JPG)

The artifical neural network uses something like this
![](image2.JPG)

There are some inputs (x_1, x_2, x_3) and ther=ir associated weights. they go through a function which gives an output y and then an activation or step function with a certain threshold determines what is the value. that value is fed into the input again. This is one neuron.

if you have one layer it is called neural network. if it has multiple layer it is called a deep neural network.
![](image3.JPG)

Neural networks can perform better than machine learning algorithms. But whats more interesting is the modeling aspect of the deep learning. We actually do not fully understand how they actually model.

Consider the following
jack is 12 years old
jane is 10 years old.
kate is older than jane and younger than jack.

To solve this you have to come up with a logic. until recently machine learning has not been able to come up and model logics. But what Neural network if you give it a bunch of example and keep matching it to the answer may like a million times

Once the input has gone through the layers. the output is compared with the input. > cost function.
Then we need to optimize the cost by minimizing it. The minimization function changes the weights and feeds back the output. this action is back propagation.

feedward + back prop = epoch (you can do this step 10 times , 20 times, a million times) 

each time we aim to lower the cost function, but eventually we will see law of demenising returns
