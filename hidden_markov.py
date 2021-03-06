# -*- coding: utf-8 -*-
"""hidden markov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h7QIQJ9Iy707w3Zm23y02SIjotddnaCA
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x

!pip install --upgrade tensorflow-probability

import tensorflow_probability as tfp
import tensorflow as tf

#model distrbution
tfd=tfp.distributions
initial_distribution=tfd.Categorical(probs=[0.8,0.2])#80 percent chance of being hot and 20 percent remain cold
transition_distribution=tfd.Categorical(probs=[[0.7,0.3],
                                               [0.2, 0.8]])#cold and hot respectively
observation_distribution=tfd.Normal(loc=[0., 15.], scale=[5., 10.])
#loc is for SD and mean

model = tfd.HiddenMarkovModel(
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=7)

mean = model.mean()
with tf.compat.v1.Session() as sess:
  print(mean.numpy())