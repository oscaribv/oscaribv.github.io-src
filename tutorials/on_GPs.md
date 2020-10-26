Title: Test
Date: 2017-12-02 
Modified: 2019-06-30
Slug: test
Lang: en
Category: tutorials
Tags: tutorials, GPs
Authors: Oscar Barragán


# On Gaussian-Process


All starts with *Data*. A collection of observations/measurement of some observable that we want to describe with some model in order to infer physics. 
In my case as an astronomer, I want to see if a given model predicts the observations that deny the inmutability of the sky. 

## Basics of data analysis

A typical (and well funded) approach is to assume that our data are *Gaussian distributed*.
But what does this really mean? Here you can see an example of *Data*, some measurements _y_ taken at different times _t_. Each datum _yi_ has an asociated error bar _sigmai_. 


FIG

When we say that our data is *Gaussian distributed*, we literally mean that each datum i is a *Gaussian distribution* (in the y-axis) with mean yi and standard deviation sigmai. Something like this

FIG

If I try to create a plot with a Gaussian for each datum that would be a mess. So I prefer to add an extra dimension to my plot. If we keep in our assumption that data are Gaussian distributed, or data set would look like something like this

FIG

Look again to the previous two plots. They look different, but they are exactly the same. We have time in one axis, our observable y in the other, and the Guassian behavior of our data expressed in two different ways: in the common approach where the Guassiasinity is implicitly represented by an error bar and this fancy 3D plot where Guassianity explicitly is a thing. 


We want to use these data to infer some physical properties, so what I do is to use some parametric model (i.e., some function that maps some parameters _x_ at different times _t_ into the quantites that I measured) and construct a model that describes better my data (more about this below).  

In order to see if our model describes well our data, we need to learn how to compare them. 
We cannot symply take the difference (fi -yi) between 


Look well that equation. Since the identity of our datum is not a point, but instead a Guassian, we need to compare with which probability or model explains the datum i. i
And because the intrinsic property of the probabilities, we can compute the probability that our model explains the whole data setby multiplying each individual probability.   
This probabilistic entity has the name of *Gaussian Likelihood*. And it tells you how well your model explains your (Gaussian distributed) data.

The Guassian likelihood is well know in data analysis aproaches. You can find the best set of parameters that describe your model by maximasing it, or you can put it together to a set of Priors and make Bayesian inference, etc. The Gaussian likelihood is really fun. 

Now let us analyse with more detail the Gaussian likelihood behavior between two points yi and yj. 


But, what happens if there are correlations? Gaussian likelihood and bivariate Gaussian distribution.

 
