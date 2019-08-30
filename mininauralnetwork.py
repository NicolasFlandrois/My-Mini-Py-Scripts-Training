#!/usr/bin/python3.7
# UTF8
# date: Fri 30 Aug 2019 21:46:04 CEST
# Author: Nicolas Flandrois
# Description: Short exercices, build a neural network of 1 neurone, to predict Pi


def predict(inputs, weights, pred_goal):
    pred = sum([inputs[k]*weights[k] for k in range(len(inputs))])
    return pred, (pred-pred_goal)**2

def gradient_descend(inputs, weights, pred_goal, alpha=0.01, steps=100):
    for _ in range(steps):
        pred, err = predict(inputs, weights, pred_goal)
        delta = pred-pred_goal
        weight_deltas = [i*delta for i in inputs]
        weights = [weights[k]-weight_deltas[k]*alpha for k in range(len(weight_deltas))]
    return weights

import math
inputs = [1, 3, 2]
weights = [0.5, 2, -3]
pred_goal = math.pi
p = predict(inputs, weights, pred_goal)
print("Before training")
print(f"pred={p}")
print(weights)
weights = gradient_descend(inputs, weights, pred_goal)
p = predict(inputs, weights, pred_goal)
print("After training")
print(f"pred={p}")
print(weights)
