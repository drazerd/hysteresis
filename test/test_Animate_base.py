# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:49:09 2021

@author: Christian
"""


import numpy as np
import hysteresis.plotSpecial.animate as ani
import hysteresis as hys
import scipy

np.random.seed(101)
x = np.linspace(0, 1, 101)*10
y = np.sin(x)
trianglexy = np.column_stack((x, y))

test = hys.Hysteresis(trianglexy)
testBase = ani.AnimationBase()


def test_Play():
    assert testBase.play == True
    
def test_Toggle():
    testBase.togglePlay()
    assert testBase.play == False

# test_Play()
# test_Toggle()


# xyAni = ani.getAnixy(trianglexy, 2)

# frames  =ani.getAniFrames(trianglexy[:,0], 0.1)

# myAnimation = ani.Animation(test,None,1,5)
# out = myAnimation.Animate()