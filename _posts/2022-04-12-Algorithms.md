---
layout: post
author: fubar
title: "Algorithms"
tag: programming
tool: python
excerpt: "Some of the routinely encountered algorithms."
date: 12th April, 2022
---

## Abstract

Algorithms are the hotspots of any program.
They are the abstraction of logic that is coded into a program.
Any program almost always an algorithm under the hood.

## Algorithms

In the thesis, we have worked with hardware interfacing and image processing.
For each set of measurement or analysis, there is an algorithm that is doing the heavy-lifting.
Following are these algorithms.

### Canny edge detection

In [KerrPy]() we have used the Canny Edge detection algorithm to detect domain wall from a Kerr micrograph.

The algorithm was given by John F. Canny in 1986.

It is a multistage algorithm involving

- Noise reduction,
- Finding intensity gradient,
- Non-maximum suppression, and
- Hysteresis thresholding.

### PID loop

PID loops are used in various engineering systems with closed feedback.
In our Kerr microscopy system, we use PID loop to set in-plane field.
The in-plane field component are configured in a closed feedback mechanism,
where the field is set by voltage controlled current source and 
the resultant field is sensed by a Hall sensor.

### Genetic algorithm for XRR profile fitting

X-ray reflectivity profiles for ultra-thin multilayer films exhibit variety of features
like

- Keissing fringes
- superlattice oscillations
- decreasing amplitude of oscillations
- logarithmic decay of reflectivity signal

These features can be modelled within the Paratt formalism using the following parameters
for each of the layers

- thickness
- roughness
- $\delta$, $\beta$ coefficients of the refractive index

For a multilayer with 4 layers, this can lead to atleast 16 parameters,
 in addition to other parameters like the intensity scaling factor, initial $q_z$, substrate roughness,
 substrate refractive index. 
 
Unless, we know the nominal values of the parameters,
it is difficult to converge to the global minimum
using conventional gradient based algorithms like simplex or gradient.

Even if we know the nominal values,
it is highly likely for the trajectory of minimization to settle in a deep **local** minimum.

To avoid such inaccuracies, we have used genetic-algorithm based minimization.

