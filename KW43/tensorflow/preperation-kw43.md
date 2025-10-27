# Notes from prep for next Lecture (30.10.2025)
## Videos

- [Neural Networks Explained - Machine Learning Tutorial for Beginners](https://www.youtube.com/watch?v=GvQwE2OhL8I)

- [Machine Learning Explained in 100 Seconds](https://www.youtube.com/watch?v=PeMlggyqz0Y)

- [What is a Loss Function? Understanding How AI Models Learn](https://www.youtube.com/watch?v=v_ueBW_5dLg)

- [Backpropagation, intuitiv | DL3](https://www.youtube.com/watch?v=Ilg3gGewQ5U&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6)

- [Parameters vs Hyperparameters ( Parameter vs Hyperparameter ) in Machine Learning Detailed](https://www.youtube.com/watch?v=32tNAhQ8x7M)

- [Validation data: How it works and why you need it - Machine Learning Basics Explained](https://www.youtube.com/watch?v=NPWlj9G1Si8)

- [TensorFlow Tutorial 3 - Neural Networks with Sequential and Functional API](https://www.youtube.com/watch?v=pAhPiF3yiXI&list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb&index=5)

- [TensorFlow Tutorial 14 - Callbacks with Keras and Writing Custom Callbacks](https://www.youtube.com/watch?v=WUzLJZCKNu4)

## I. Loss Function

- Feedback Algorithm
- Score Keeper
- Guide for Improving Predictions

(Linear) Regression & Calssification

### Regression LF

#### MSE
- Mean Square Error

#### MAE
- Mean Average Error

#### Huber Loss
- 

### Classification

#### Cross Entropy Loss (CEL)
- Entropy: uncertainty of possible outcome
- High Entropy: A Dice Roll (6 Outcomes Possible)
- Low Entropy: A Coin Flip (2 Outcome Possible)


#### Hinge Loss
- support vector machines
- correct predictions with certain level of confidence
- max margin between calsses
- confidentally correct
- particullary usefull for binary classification classes


## II. Back Propagation
- Hebbian Theory 'Neurons that fire together, wire together.'
- Sigmoid or R funciton
- weights, activation & bias
- Gradient Decent
- Stochastic GRadient Decent (Drunk Man)

### Types:
- Learning Rate
- Momentum


### last layer

- increasing weight proportinally to activation
 - False High > a lot 'Down'; False Low > a little 'Down'
 - Right High > a little 'Up'; Right low > a lot 'Up'


## III. Training
- Mini Batch
- Hyperparmeters
- Parameter

### Test Data Sets
- Training Data ('overfitting' possible)
- Validation Data
    - Qualifying the mdoel, Hyper Parameter
- Test Data
- Mixing Data Sets > Data Leakage (to be avoided at all times)

### Parameters

### Hyper Parameters (no algorithm to choose HP > 'trial and error')
- Model Type
- Model Architecture
- Training Parameters
    - Learning Rate
    - Batch Size
    - Epochs #Number (repitions)
