---
layout: post
author: fubar
title: "Basics of Origin LabTalk scripting language"
tag: programming
tool: originlab
excerpt: "Origin is a graphing and analysis tool used predominantly by experimentalists. In addition to providing convenient UI based routines to plot aesthetic 2D and 3D plots, Origin provides robust analysis tools like linear regression, nonlinear regression, curve fitting routines. *In-situ* LabTalk scripting language allows handling the various columns of data to allow convenient mathematical transformations. In this post, we will consider the structural elements of this scripting language."
date: 11th March, 2021
---

# Features

From [OriginLab][1]

- Origin graphs and analysis results can automatically update on data or parameter change, allowing you to create templates for repetitive tasks or to perform batch operations from the user interface, without the need for programming.
- Extend the capabilities in Origin by installing free Apps available from our website. Connect with other applications such as MATLAB™, LabVIEW™ or Microsoft© Excel, or create custom routines within Origin using our scripting and C languages, embedded Python, or the R console.


[1]: http://cloud.originlab.com/index.aspx?go=Products/Origin

# fitLR X-function

```
range r1 = col(C);
fitLR iy:=(1,2) fixint:=1 intercept:=r1[1] oy:=col(D);
```

>You can add two lines of code to put R value in a User Defined column label row.

```
wks.userparam(++Rvalue);
col(D)[D1]$ = $(fitLR.r);
```

# LabTalk Resources

[Range Notation in LabTalk][2]

[fitLR X-function][3]

[Substitution notation][4]

[2]: https://www.originlab.com/doc/LabTalk/Tutorials/Tutorial-Range-Notation#Worksheet_Cell_Range

[3]: https://www.originlab.com/doc/X-Function/ref/fitLR

[4]: https://www.originlab.com/doc/LabTalk/guide/Substitution-Notation
