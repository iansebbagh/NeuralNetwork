import numpy as np

# Sigmoid Function
def act(x):
    return 1/(1+np.exp(-x))

# datasets
x = np.array([[0, 0, 1], 
              [0, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]])
y = np.array([[1, 0, 0, 1]]).T     # xor
print(x,y)

# parameters
input_size = x.shape[1] # original input + bias
hidden_size = 4
output_size = 1
alpha = 0.8    # learning rate

# weights
w1 = np.random.randn(input_size, hidden_size)
w2 = np.random.randn(hidden_size, output_size)

# training
for iter in range(1000):
    if(iter%100 == 0):
        alpha *= 0.99;
    # forward
    z1 = np.dot(x, w1)
    a1 = act(z1)
    z2 = np.dot(a1, w2)
    Y = act(z2)
    
    # back propagation
    delta2 = (Y-y) * (Y * (1-Y))
    delta1 = np.dot(delta2, w2.T) * (a1 * (1-a1))
    w2 -= alpha * np.dot(a1.T, delta2)
    w1 -= alpha * np.dot(x.T, delta1)

# test
z1 = np.dot(x, w1)
a1 = act(z1)
z2 = np.dot(a1, w2)
Y = act(z2)
print ("Ouput after training...")
print (Y)

