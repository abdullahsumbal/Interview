# K Nearest Neighbors

Imagine you have bunch of + and - on a graph and you can have random point. you need to classify the point as + or -. with k nearest neighbor algorithm you have to select k points closest to that random point. if you have more + points selected then the random point is + and vice versa.

## Accuracy vs Confidence
When you train the model and test it. Then you get the accuracy.
Confidence is associated with the each point predict. for eg 3 closest neighbor was ++-. confidence that it is a + is 2/3.

To find the shortest difference we use the Euclid distance. 

e.g breast cancer