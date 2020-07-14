---
layout: post
author: fubar
tag: programming
title: "References for learning C++"
excerpt: "C++ references of websites, books, code and APIs for learning C/C++."
date: 24th May, 2020
---

<div class="box">
<img src="/assets/images/C++/C++Logo.png"
alt="C++-logo"
width = 150px >
</div>

## Abstract

Programming is a science as well as an art. Developing the required skills takes time and effort and an enthusiasm to learn. The learning draws parallels with that of learning a natural language such as English.
Just as the required skills to learn a natural language are reading, listening, writing and speaking, so the skills for learning a programming language are reading code, writing code. Also just as we need to know the proper language constructs like grammar (syntax), contextual use of language (semantics), we need to learn the syntax as well as

### Sites
- [Learncpp](https://www.learncpp.com/)
- [CS fundamentals](https://www.cs-fundamentals.com/)

### Books

- [SO Book Guide](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)
- [C++ Program Design by Cohoon and Davidson](https://www.mhhe.com/engcs/proglang/cohoon/) I refered to this book for my CS101 course in 2005
- [C++ Notes for Professionals](https://goalkicker.com/CPlusPlusBook/)
- [C++ How to Program by Deitel and Deitel](https://www.pearson.com/us/higher-education/program/Deitel-C-How-to-Program-Plus-My-Lab-Programming-with-Pearson-e-Text-Access-Card-Package-10th-Edition/PGM1100513.html)

### Code

Like learning natural language involves listening as a major component, programming language skills are developed by reading lots of good code. It exposes the learner to good programming practices.

- [Code with C/C++](https://www.codewithc.com/c-projects-with-source-code/)
- [Curated list of programming projects](https://github.com/Baalkikhaal/project-based-learning#cc) Language agnostic projects to improve the programming skills using project based learning
- [Project Euler](https://projecteuler.net/about) Weekly addition of a new problem that demands skills in mathematics and programming. A fun way to start learning programming and mathematics in a hand-in-glove manner.

### Libraries

Some famous libraries that help in learning how APIs are written. By reading their source code, one can learn how good programmers structure their code and also how to abstract functionality so that code has increased reusability quotient.

- [OpenGLM](https://glm.g-truc.net/0.9.9/index.html) OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics software.
- [SDL2](https://www.libsdl.org/index.php) Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D.
- [BLAS](https://www.netlib.org/blas/) Basic Linear Algebra Subroutines are **Fortran** routines that provide basic building blocks for basic vector and matrix operations. There is a C/C++ interface.
    - Level-1 BLAS performs scalar, vector and vector-vector operations,
    - Level-2 BLAS performs matrix-vector operations,
    - Level-3 BLAS performs matrix-matrix operations.


- [LAPACK](https://www.netlib.org/lapack/) Linear Algebra PACKage utilizes BLAS subroutines to provide routines for solving systems of simultaneous linear equations, least-squares solutions of linear systems of equations, eigenvalue problems, and singular value problems. The associated matrix factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are also provided. There is a C/C++ interface.
- [OpenGL](https://www.opengl.org/) The Industry's Foundation for High Performance Graphics
- [OpenCV](https://opencv.org/) (Open Source Computer Vision library)
is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

---

## Hands on Tutorials
Following are hands on tutorials for various aspects of program development. As a typical cycle of program development involves

- writing source code
- compiling the code
- debugging the code

### Writing C/C++ program (#TODO)

Tutorials explaining good programming practices while writing code are given here. Some esoteric aspects of writing good code, which I cannot at the current moment categorize them due to my own lack of understanding, are

- avoiding hard coding
- practing a convention for writing code. Though there is no C++ standard for writing the code, in order for the code to be readable, we need to adopt one convention and stick. There is no universal convention. Some adopt the Hungarian convention for the brackets, what is the other one I dont have idea. A [LazyFoo article on writing readable code](https://lazyfoo.net/articles/article02/index.php) and an [article on coding style for Inkscape project](https://inkscape.org/develop/coding-style/) are starters.
    - properly indent code
    - give descriptive names to the variables
    - Develop a naming standard
    - Properly comment your code
- refactoring (not sure what that means... however most of the Inkscape legacy code is undergoing refactoring)
- any good references for writing code?

### Compiling a C/C++ program
Compiling can be as simple as executing the command

    g++ helloWorld.cpp -o helloWorld

or as difficult as compiling  various source files, linking various static and dynamic libraries. It is one of the important component of program development. These tutorials provide hands on experience with compiling C++ programs.

- Learn the basics of compilation from a [Medium post titled Learn How to Compile a C++ program](https://medium.com/better-programming/learn-how-to-compile-a-c-program-382c4c690bdc)
- Individual steps of compilation of a C program are beautifully explained
in a [CS fundamentals blog post](https://www.cs-fundamentals.com/c-programming/how-to-compile-c-program-using-gcc)

### Static vs Dynamic Linking

- A simple explanation of static and dynamic libraries in a [Learncpp tutorial](https://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/)

- A further discussion is done in a [CS fundamentals post](https://cs-fundamentals.com/tech-interview/c/difference-between-static-and-dynamic-linking)

- (Optional) A nuanced comparison of performance issues with static and dynamic linking in a [SO post](https://stackoverflow.com/questions/1993390/static-linking-vs-dynamic-linking)

### How to use library for Application development

- We need to configure the compiler of our IDE and a [LearnCPP post] explains it using the case of VisualStudio and Codeblocks

- As a simple concrete example a [Medium post titled Navigating the world of distributed code](https://medium.com/better-programming/navigating-the-world-of-distributed-c-code-e439406f3e42) explains how to work with uncompiled library/ header only libary and use `make` tool to configure the compiler

- As a concrete example, I was successful in configuring the MingW compiler of Codeblocks IDE to use [SDL2 library](https://www.libsdl.org/index.php) by following the [GRHMedia blog post] listed in the [SDL's Tutorial Wiki](https://wiki.libsdl.org/Tutorials) as a video tutorial.

### (Advanced)How to create a library?

This is an advanced topic. I have not explored it but can refer to [Create Static and Dynamic Link Libraries in C on Linux](https://www.cs-fundamentals.com/c-programming/static-and-dynamic-linking-in-c#static-libraries) from CS-fundamentals blog.

## Debugging code

Tutorials explaining good programming practices while debugging code are given here.(#TODO)
