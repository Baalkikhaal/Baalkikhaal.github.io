---
layout: post
author: fubar
title: "What are Python classes?"
tag: programming, architecture
tool: python
excerpt: "The organization of python program is discussed with class as an entity."
date: 12th April, 2022
---

## Abstract

Class is a high level unit of program organization. 
They facilitate a new kind of programming style called the **object oriented programming (OOP)** style.
In contrast to the procedural programming style that constitutes functions,
the OOP style constitutes classes where data is given precedence over flow of logic.
This trade-off leads to new ways implementing behaviour and turns out to be more natural for certain use cases,
for which procedural programming either has no solution or the solution it offers is cumbersome.

As it is a modern approach to progamming, it is pedagogical to compare and contrast classes with other structural units that Python offers like [functions]({% post_url 2022-04-12-What-are-Python-functions %}),
 [modules]({% post_url 2019-09-14-What-are-Python-modules %}). 
Analogies are also drawn with corresponding structures in natural language.

## Introduction

We write programs to model reality. There are two complementary interpretations of reality;
the reductionistic view that the whole is a sum (or composition) of its parts and the hierarchial view 
that the whole **emerges** from its part [Anderson1972](#references).

Therefore, the program architecture is based upon decomposition, i.e.,
 the process of identifying  the parts of the program and stitching them together.
Any architecture is based on making design decisions, that invariably introduce constraints [Brown2011](#references).
Moreover with program architecture, depending upon how the decomposition is performed, introduce certain constraints.

The traditional programming languages like Fortran, C, 
are procedural where a program is **decomposed** into events (or operations or actions). 
These events are then coded into constructs like subprograms, subroutines or functions. 
These constructs are essentially logic driven and supplemented by data. 
Hence procedural can also be called **event-oriented programming** paradigm.

In the 1980's,  with the advent of the Ada programming language,
radically new structural elements or constructs called packages and tasks were introduced wherein the data is given prominence over logic [Booch1986](#references). 
Following Ada, the modern programming languages like C++, Java, Python refurbish these constructs to describe what are called objects. The programs are decomposed into objects. 
The objects are essentially data driven and supplemented by logic
 resulting in what is called object-oriented programming paradigm.
 
In comparison with the natural language, if the data and logic are related to nouns and verbs respectively, 
then modern programming languages weigh up the nouns over the verbs. To illustrate this comparison, 
let us model the canonical Ramayana epic. From a procedural perspective, 
the poem can be famously summarized into just three words-

> Ramayana summary: "కట్టే, కొట్టే, తెచ్చే". which translates in English to "built, beat, brought"

So the summary has essentially three events-- Rama built the bridge, Rama beat Ravana, Rama brought Sita home.
If we model the epic from the object oriented perspective, then we could as well summarize it into three names-

> Ramayana summary: "Rama, Ravana, Sita"

The former summary is very relatable while the latter appears abstract. 
While the procedural decomposition might be more natural for composing poems like Ramayana,
the object-oriented decomposition, as we will soon see later, is ideal for systems that exhibit hierarchial structure.
 
The class construct greatly facilitates object-oriented design. 
It is least to say that to understand OOP is to understand what a class is.
However, due to our natural tendency to think procedurally, 
the complementary programming paragdigm dealing with objects may not be grasped easily.
To exemplify this behaviour, 

As a result, we gradually motivate the transition from procedural to object oriented paradigm 
by describing the class from the perspective of 

- construct
- object
- generator
- namespace

As a construct, class acts as a placeholder of data and logic. 
As an object, class provides an interface to interact with other objects.
As a generator, class provides a template to create objects that share the same quality.
Finally as a namespace, class provides a flexible interface to alter its namespace 
using the property of inheritance. This is the most important feature of class that greatly
improves code reusability and code customization.

Let us explore these features of class below.

## Class as a construct


Data and logic can be respectively compared to names and
 their meanings in the dictionary of a natural language.

Moreover, a class itself is a name with underlying names termed as its **attributes**.
So a class consists of data and method attributes.

As a structural element, a classes encapsulate data and logic using the **class construct** 
(construct, in English, means to form by combining(con) parts or elements(struct).
 
Syntactically, the class construct is a `class` statement. 
A `class` statement is a block statement 
similar to the `def` statement that defines a function.

```python
class MyClass:
	data_attributes
	method_attributes(self, ):
		...
		...	
```

The class acts as a placeholder of its constituent names. 
Since it is also an object it can be assigned to a variable as

```python
my_variable = MyClass()
```

Also it can be passed as an argument to a function like other built-in objects.

```python
my_function(MyClass)
```

> Style Tip: As per the [PEP 8 style guide](https://peps.python.org/pep-0008/), 
it is recommended to use `CapitalizedWords` naming style for class names. 





### Data attributes

### Method attributes

In the general sense, a function interface allows flow of external data.
However, the method attribute, which itself is a function, needs to acccess data
 that is internal to the object interface.
To allow for this, the function interface in the special case of a method attribute is **extended** 
by allowing a **special** argument called **self** that references the object
 of which the method is part of. This is called **self-referencing** and graphically visualized below.
 
![extension-of-function-interface-in-class](/assets/images/Python/self_as_special_argument.svg)

## Class as an object

Since we posited earlier that class is itself a name, 
a natural question arises; whether a class is of type data or logic?.
To answer this question, let us transcend from the above categorization of names 
and introduce the concept of an **object**.

An object is an **abstraction** that encapsulates names.

Names of type data denote the **state** of the object, 
while names of type logic determine its **behaviour** by performing **operations** upon the data.

The verb encapsulate, in English means, to contain something; 
it also means to hide something like a black box. 
Accordingly, objects serve two purposes-

- As a placeholder, the object **defines** its names.
- As an interface, the object provides **access** to its names and if needed
 **hides** them from other objects.

While the first connotation enables name encapsulation, 
the second connotation facilitates **interaction** between objects.

### Name encapsulation


As a programming paradigm, this name encapsulation within a single structure is termed
**object-oriented programming (OOP)** and classes are a natural .

In contrast, functions encapsulate logic, whereas modules hold both data and logic.
So from the above definition of an object, functions and modules are also objects. 
Even the built-ins that constitute functions and modules are objects.


#### Illustration: Joker class

![joker-dc-comics-image](https://upload.wikimedia.org/wikipedia/en/5/5f/Batman_Three_Jokers.jpg)


<div class="post">
	<p>
		Joker of DC comics. Image taken from <a href="https://en.wikipedia.org/wiki/Joker_(character)">Wikipedia</a>.
	</p>
</div>


To illustrate the class construct, 
let us consider the example of the Joker character from DC comics. 
While many actors have played the role fo Joker, as a character, 
there is one-and-only-one Joker. Let us model **the** Joker as a **class of his own**.
As his attributes, the first thing that comes to the mind are his name and his quotes. 
While he delivers a context-dependent dialogue,
for pedagogical purposes, let us model the behaviour that delivers a random quote.

```python
class Joker:
    name = 'The Joker'
    quotes = ['Why so serious?',
              'I just doooo things.',
              'Do I look like I am man with a plan?'
             ]
    def tell_random_quote(self):
        n_quotes = len(self.quotes)
        from random import randint
        quote = self.quotes[randint(0, n_quotes-1)]
        return quote
```

While the data attributes are self-explanatory,
 the method attribute, which are essentially functions,
 contains an additional special argument **self** that has been encountered for the first time.
Before we explain the [self argument](#self-argument),
 let us first see how to access the encapsulated attributes across the object's interface.
 
### Object-to-object interaction

From above, it is clear that `name` and `quotes` are data attributes, 
whereas `random_quote()` is a method attribute.

One way of looking at attributes is to think of them as properties. 
However, an equally valid way of looking at them is to think of them defining the object.

Both these ways are expressions of the object-attribute relation.
In essence, we are dealing with relations. In the former way, the object takes precedence, 
wherease in the later, the attributes take precedence. 
If we work with the later way, then the data attributes define the **state** of the object, 
whereas the method attributes **action** performed by the object and on the object.
The sum total of the state and actions define the **behaviour** of the oject.


In any case, unless there is access to the attributes of the object, 
other objects cannot interact with it, 
thereby an object is of no use in implementing a model of reality.
Python encourages object-to-object interaction using the `object.attribute` expression 
that provides an interface to access and modify the behaviour of the object.

#### Illustration: Access Joker's behaviour

To access Joker's name, we use `Joker.name` expression 
that gets the `name` attribute of `Joker` class.

```python
print(Joker.name)
```

prints

```python
The Joker
```

If we additionally want to listen to a random Joker quote, 
we use `Joker.tell_random_quote(Joker)` expression.

```python
print(Joker.tell_random_quote(Joker))
```

prints

```python
I just doooo things.
```

The above expression in natural language means
"call the `tell_random_quote()` method attribute of `Joker` class object
that takes as an argument the object itself and
 return one of his random quotes to print to the standard output."

There are two features in this expression

- to access the method, we use the `object.attribute` expression, and
- structurally the method is a function that needs to access the class object's data attributes;
 as a result the class object itself is passed as argument.

To summarize 

>  Python is a collection of interacting objects, each of whose attributes can be accessed
by the `object.attribute` expression.
 
## Class as a generator

We posited earlier that Joker is in a league of his own.
 As an abstraction, this is a true statement. 
 However, there have been more than one attempt by Hollywood directors
 to portray this character. 
 Naturally, the definition of the Joker is limited by the imagination
 of the director, the ability of the actor and 
 probably the era during which the movie was released.
 
There are atleast three famous portrayals of The Joker:

- Tim Burton's Joker played by Jack Nicholson,
- Christopher Nolan's Joker played by Heath Ledger, and
- Todd Phillips's Joker played by Joachim Phoenix, 

respectively during the golden, silver and modern era. 
Therefore, in reality, there are more than one Jokers that share the same "Jokerness", 
but are only different as far as "degree of Jokerness" is concerned [Vivekananda](#References). 


> In OOP parlance, objects that share the same 'ness' but are only different as far as the 
"degree of 'ness'" is concerned are called **instances**.

To capture the shared "Jokerness", 
while at the same time delineate the differences in the "degree of Jokerness", 
the [class construct](#class-as-an-object) defined earlier is not sufficient.
Instead, we extend the class construct with the addition of the `__init__()` method attribute.

```python
class my_class:
	__init__(self):
		...
		...
	data_attributes
	method_attributes(self, ):
		...
		...
```

With the use of the `__init__()` method, we define a new `Reel_Joker` class 
that has the `version` attribute,
 in addition to the attributes already defined in the `Joker` class. 
 The `version` denotes the era the movie was released in, the director and 
 the actor that played the role of The Joker. 
 Let us assign these three features as a dictionary to the `version` attribute.
 
```python
class Reel_Joker:
    name = 'The Joker'
    quotes = ['Why so serious?',
              'I doooo things.',
              'Do I look like I am man with a plan?'
             ]
    def __init__(self, age, director, actor):
        self.version = dict(	age=age,
					director=director,
					actor=actor
				)
    def tell_random_quote(self):
        n_quotes = len(self.quotes)
        from random import randint
        quote = self.quotes[randint(0, n_quotes-1)]
        return quote
```

Before we explain the [__init__()](#init-method),
 let us first define the different instances of Joker class.

### Instance of a class

The process of defining a new instance is called **instantiation**.

We can assign an instance to a name using the assignment statement.

```python
joker_golden = Reel_Joker("golden", "Tim Burton", "Jack Nicholson")
joker_silver = Reel_Joker("silver", "Christopher Nolan", "Heath Ledger")
joker_modern = Reel_Joker("modern", "Todd Phillips", "Joachim Phoenix")
```

### __init()__ method

Instantiation needs external data.
For each of the above three unique instances, 
we pass the age, director and actor as external data.
These data are passed to the special method `__init__()` 
that performs the role of instantiation.
In addition to `self`, `__init__` takes the arguments age, director and actor and
respectively assigns to `'director'`, `'actor'` and `'age'` keys of `version` attribute.
To define `version` as an attribute of the class, `self.version` expression is used.

If the `Reel_Joker` class is abstracted graphically as a `Circle` class, 
then the above three instances can be considered to be circles of differing degrees and
center coordinates as shown below.

![class-instance-relationship](/assets/images/Python/class_instance_relationship.svg)

To summarize,

> In the OOP parlance, we say that a class **generates** new **instances** of objects.

An additional feature in the above figure is the directed connectors to denote 
that the instance objects **inherits** attributes of the corresponding class object 
as discussed below in the [section on class inheritance](#class-inheritance). 
But first, let us discuss the instance interface.

#### Instance interface

Since instances are also objects, their attributes can be fetched using the usual `object.attribute` expression.

```python
golden_age_actor = joker_golden.version.get('actor')
silver_age_director = joker_silver.version.get('director')

print(f'{joker_golden.name} of the golden age was played by {golden_age_actor}.')
print(f'{joker_silver.name} of the silver age was directed by {silver_age_director}.')
```

gives the result

```python
The Joker of the golden age was played by Jack Nicholson.
The silver age Joker was director by Christopher Nolan.
```

While the instance and the corresponding class are **different** objects, 
as discussed below in the [section on class inheritance](#class-inheritance), 
they share the same interface because an instance inherits the attributes of the corresponding class.

## Class as a namespace

In the most general sense, a class is a **namespace**, a space of names.

Names in a programming language are broadly categorized into two types

- data
- logic

### Namespace extension by inheritance

In the section on [self argument](#self-argument), 
we have seen how `self` argument allows a class to self-reference its own attributes, 
and in the section on [__init__ construct](#init-method), 
we have seen how `__init__()` method spawns new instances of a class. 
Now let us explore another inheritance, another powerful feature of the class construct.

As discussed earlier, the attributes of a class define it.
If another class's definition has the same attributes as the former
 in addition to a new set of attributes, 
 then it is possible to define the later by **inheriting** the former's attributes
 and only defining the new set of attributes. 
 The process of sourcing one class's attributes to the other is called inheritance.
 The class that sources its attributes is called **superclass**, 
 and the class that inherits the attributes is called **subclass**.
 
To capture the inheritance, 
 [the class-as-a-generator construct](#class-as-a-generator) defined earlier is not sufficient.
Instead, we extend the class-as-a-generator construct to also accept `superclasses` as arguments.

```python
class my_subclass(my_superclass):
	__init__(self):
		...
		...
	data_attributes
	method_attributes(self, ):
		...
		...
```

With the passing of superclass as an argument,
 we can inherit the attributes of the superclass into the sub-class

```python
class Inherited_Joker(Joker):
    def __init__(self, age, director, actor):
        self.version = dict(	age=age,
					director=director,
					actor=actor
				)
``` 

Notice that we have passed the `Joker` class as an argument to the `Inherited_Joker` class.

The above class statement in natural language means
"the `Inherited_Joker` class inherits the attributes of `Joker` class.
 In addition, it has an `__init__` method attribute."
 
Since the `__init__` defines the `version` attribute, the complete list of attributes of `Inherited_Joker` class is

- name
- quotes
- tell_random_quote()
- version

Similarly, another class may source its attributes from the `Inherited_Joker` class.
From this  it is evident that there is a hierarchy

> In OOP parlance, a class inherits attributes from its superclasses and sources attributes to its subclasses. 

### Inheritance interface

We can immediately see two-fold utility in the inheritance interface of class.

- Code resuability
- Namespace 

#### For classes

> Inheritance adds depth to the abstraction.
Inheritance allows efficient reuse of code.

In contrast, functions lack such an inheritance interface. 
As a result functions are useful when namespace extension is not needed.
On the other hand, `import` statements can extend namespaces of modules and packages.
For example, to incorporate the names of a `random` module into the top level script file, 
we use either of the following statements

```python
import random
import random as rd
```
The `randint()` method can then be accessed by the usual `object.attribute` expression as

```python
random.randint()
rd.randint()
```
While this is convenient, 
the namespace extension needs explicit execution of the `import` statement.
However, in the case of classes, it is implicit as the `object.attribute` expression 
initiates an automatic tree search for the attribute across the inheritance hierarchy tree.

#### For instances

In the Python object model, an instance and its corresponding class are two different objects.
However, an instance inherits the attributes of the class. 
For example, the `name` attribute of both the `Reel_Joker` class and any of its instance, 
say `joker_golden` instance object are one and the same.

```python
print(Reel_Joker.name == joker_golden.name)
```
prints

```python
True
```

To summarize,

> In OOP parlance, an instance **inherits** the attributes of the class that generates it.

#### For mutated subclasses

It also allows mutations of the attributes leading  

To summarize,

> Inheritance is the flaship property of object-oriented programming 
that offers efficient code reuse, extension of namespaces, spawning multiple instances and code customization.

### Namespace alteration 


## References

- Lutz2013 - Mark Lutz, "Chapter "OOP: The Big Picture" of "Learning Python", O Reilly 2013.

- Vivekananda - Here we take inspiration from a quote from Swami Vivekananda that summarizes अद्वैत वेदान्त.

> All differences are not that of a kind but only of a degree -- Swami Vivekananda.

- Booch1986 - G. Booch, "Object oriented development", IEEE Transactions on Software Engineering, 1986.

- Anderson1972 - P. W. Anderson, "More Is Different: Broken symmetry and the nature of the hierarchical structure of science.", Science 1972.

- Brown2011 - A. Brown and G. Wilson, "The Architecture of Open Source Applications", Lulu, 2011

## Assets

- [Joker-class](/assets/documents/Python/joker.py)


