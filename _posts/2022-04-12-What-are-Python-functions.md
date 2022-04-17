---
layout: post
author: fubar
title: "What are Python functions?"
tag: programming, architecture
tool: python
excerpt: "The organization of python program is discussed with function as an entity."
date: 12th April, 2022
---

## Abstract

Functions are the most basic unit of program organization.
They enhance code reusability, equivalently reduce redundancy.
Functions enable procedural decomposition of logic and data
 thereby allowing procedural style of programming.
In certain use cases, when mutation of data is not allowed or needs to be enforced,
so that data transformation is the only logic that is allowed,
a specific set of functions can be used to enforce such constraints.
This style of programming is called functional programming.
Function  scoping of logic that promotes reuse of names.

## What is a funtion?

In the most basic sense, a function is a self-contained block of statements and expressions.
Since statements and expressions represent logical operations, 
a more concrete definition of a function is that it is an interface that **encapsulates** logic.

However logic has no meaning by itself. It has to act upon data.
 So data are **passed** to this interface as arguments.
 From symmetry arguments, if data are passed, conversely,
 we can expect the interface to **return** data.
 
The above interface is syntactically defined as

```python
def my_function(data):
	logic
	return new_data
```

The qualifier self-contained in the above definition can be understood from the perspective of scope.
A function scopes the data within its definition to restrict its range of visibility. 

> In the advanced case, functions can have attributes.
> In the special case of [lambda functions](% 2021-02-27-What-are-lambda-functions %), function can act as expressions.

## Encapsulation of logic 

Since function encapsulates logic,
it can be called upon whenever the corresponding block of logic needs to be executed.
For a recurring need for execution,
 calling a function is more efficient than copying-pasting the corresponding blockin two ways -

- Code reusability
- Code redundancy

### Code reusability

 Instead of copy-pasting the procedure at every requirement,
 we can call the procedure. So the block of code is replaced by a single call statement.
 This leads to lean code. Technically, the process of replacing recurring blocks of code
 with calls to the corresponding function is called factoring. 
 Since program development is like writing a research article, they both need continuous refinement.
 The cyclical process of this replacement is called **refactoring** the code.
 
To illustrate this feature,
 let us find the area of rectange with a diagonal delimited by a point and the origin.
 If $(x, y)$ are the coordinates of the point, then the area is given by
 
$$
A = xy.
$$

To implement this logic, we have

```python
x, y = 2, 3
area = x * y
print(area)
```

Now for two rectangles defined by the points $(2, 3)$ and $(3, 4)$ the areas are given by

```python
x1, y1 = 2, 3
area1 = x1 * y1
print(area1)
x2, y2 = 3, 4
area2 = x2 * y2
print(area2)
```

### Code redundancy

Debugging is an important step in the development cycle.
 If there is need to refine the procedure, it is easier in the case of function than 
correcting at every location of the explicit code.

![Python-program-architecture-functions](/assets/images/Python/program_architecture_with_functions.svg)


## Flow of data

Since a function encapsulates logic, when function interfaces interact with each other,
 only data flows across their interfaces.

![two-point-formula-for-line](/assets/images/Python/two_point_formula_for_line.svg)

To illustrate this let us define the equation for a line in two dimensions given two points it passes through.
The general form of the line is given by

$$
y  = mx + c
$$

Let us define the function that takes independent variable x and returns dependent variable y.

```python
def line(x, m, c):
	y = m*x + c
	return y
```

To find the two point formula, we need to first translate the axes to the first point,
i.e. $(0, 0) \rightarrow (x_1, y_1)$.
This leads to the transformations $x \rightarrow x', y\rightarrow y'$ with the rules of transformation

$$
x' = x - x_1, \quad y' = y - y_1.
$$

In the new $x'-y'$ coordinate system,
our line now passes through the origin with the familiar equation

$$
y' = m x',
$$
 
where the slope of the line is
 
$$
m = \frac{y_2 - y_1}{x_2 - x_1}.
$$
 
Let us define a function that takes the two points as arguments and returns the slope
 
```python
def slope(x1, y1, x2, y2):
	m = (y2 - y1)/(x2-x1)
	return m
```

With the rules of transformation, the equation in the old coordinate system is

$$
y - y_1 = m (x - x_1),
$$

so that

$$
y  = m x  +  y_1 - m x_1,
$$

where the y-intercept $c = y_1 - m x_1$.

So let us define a function that returns the y-intercept

```python
def y_intercept(x1, y1, x2, y2):
	m = slope(x1, y1, x2, y2)
	c = y1 - m*x1
	return c
```
Using the above functions, the function for a two-point formula for a line is

```python
def line_two_point(x, x1, y1, x2, y2):
	m = slope(x1, y1, x2, y2)
	c = y_intercept(x1, y1, x2, y2)
	y = line(x, m, c)
	return y
```

### Procedural decomposition

From a bird's eye view, with the use of functions we can decompose the procedure
of finding the two-point fromula for a line into components with the data flowing
between them as shown below.

![procedural-decomposition-with-functions](/assets/images/Python/procedural_decomposition_with_functions.svg)

From the above figure, it appears that there is a depth axis in the decomposition,
with the `line_two_point()` being at the top level and the `slope()` at the lowest level.
However, that is merely our bias as there is no particular ordering,
 notwithstanding the fact that `line_two_point()` calls `slope()` and other functions.
 The abstraction can be compared with islands connected by water,
 where the procedural constructs and the data act as islands and water respectively.
 
![procedural-decomposition-is-not-hierarchial](/assets/images/Python/procedural_decomposition_is_not_hierarchial.svg)

This suggests that procedural decomposition is not hierarchial. 
By deduction, all the components therefore occupy the same level of abstraction of logic
so that procedural programming has no depth in the abstraction.

We can as well represent the logic abstraction of procedural programming graphically as below.

![procedural-decomposition-is-flat](/assets/images/Python/procedural_decomposition_is_flat.svg)

> Procedural decomposition is flat.
  
## When to use functions?


Also functions offer customization of code. The arguments that the function requires
can be used to modify the behaviour of the function.

Functions allow for procedural decomposition, so that the behaviour that the code has to emulate
can be categorized into unconnected procedures.
This style of programming the behaviour is called **procedural programming style**.

## When **not** to use functions?  

When the behaviour of a system depends upon its state,
it becomes necessary to keep track of the system state. 
The state of a system can be defined by a set of parameters also called as attributes.

When there is a need to remember the state of the system,
we use functions along with the so-called `global` variables.
From the namespace perspective, global variables are names in the global scope.
As a result, these variables can be accessed anywhere except inside a function,
we need to declare its globalness. This is done by 

	global x

However, this style of designing a stateful system using functions and global variables
is discouraged as it breaks many of the Python idioms

An alternative is to use function attributes.

Another behaviour that cannot be programmed effectively with functions is when it demands composition.
To understand this sentence, let us take the analogy of composing music. 
Music is beautiful to hear when it is harmonious.
When we analyze this harmony, music boils down to a sequence of syllables with a pattern.
So a composer plays the bottom-up role of stringing together the basic elements
to form a harmonious patterns. These patterns can once again be combined to form more complex patterns
finally leading to music.

When the behaviour of a system can be understood as formed due to basic elements, 
it needs a style of programming that encourages composition.
While functions facilitate procedural decomposition,
they are limited by the flatness of such decomposition.
When a recursive composition needs to be programmed it becomes difficult and unnatural to use functions.

Python offers classes that naturally facilitate mimicking such behaviour. 
This style of programming is called the **object oriented programming (OOP) style**.
The [post on classes]({% post_url 2022-04-12-What-are-Python-classes %}) describes OOP in more detail.

## Summary

To summarize, functions prioritize logic over data.

As a basic unit of code organization, functions facilitate code reusability,
 while at the same time minimize code redundancy.
 
The interface of a function allows for decomposition of logic leading to procedural decomposition. 

Procedural decomposition is at the most flat. For hierarchial decomposition, we need classes.

## References

Chapter "Function Basics" of "Learning Python" by Mark Lutz.