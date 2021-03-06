---
layout: post
author: fubar
tag: programming
title: "What are python modules?"
excerpt: "The organization of python program is discussed with module as an entity."
date: 14th September, 2019
---

## Abstract

<img
    src="/assets/images/Python/pythonLogo.svg"
    alt="python-logo"
    align = left
/>

In this chapter, the author introduces modules. Modules form the highest organization structure in a Python program. The *rationale* behind modules lies in code reusability, a primary feature that Python *wants* you to do. Using module as an example for *namespace*, the author tries to drive home the point that a program is about managing namespaces, i.e. the space of names. This concept is revisted in other topics like [functions](chapter-on-functions) and [classes](chapter-on-classes). This is followed by explaining the internal process when modules are imported, how existing modules are searched, and the freedom of type of module imported.

---

## Module

### What is a module?

- Modules serve as the **highest organizational structure** in the architecture of a Python program. Essentially, a Python program is a system of modules.
- Modules are glorified namespaces.
- In concrete terms, a module typically corresponds to a Python file.

### Why use a module?

Code reuse
- Modules lets you save code in files permanently. So, code is *persistent* unlike the code run in Python interactive prompt

Namespace partitioning
- As a self contained system of variables/names known as **namespace**, module minimizes variable name clashes across the program.

Implementing shared services or metadata
- A shared resources usually entails a single copy across the system. A module can serve to contain such shared resources like global variables.

### How to access the module namespace?

The names of a module *namespace* can be accessed/imported by two statements and and one important function
- `import` statement fetches a whole module.
- `from` statement fetches particular names from a module.
- `imp.reload` function reloads a module without stopping Python.
All names defined at the top level of module file become attributes of the imported module object. In OOP jargon,

> the module file's global scope *morphs* into the module object's attribute namespace when it is imported.

---

### Python Program architecture

- A program is a system of modules, with one main top-level file and zero or more supplemental files called *modules*.
- The top-level file (a.k.a script) contains the main flow of control of the program.
- Modules are collections/libraries of tools to be used by the script.
- Script uses the tools defined in module files, and modules use tools defined in other modules.
- Module don't do anything when run directly; they define the tools intended for use in other files.
- [TODO](#TODO)

![Image: PythonProgramArchitecture](/path/to/architecture-image.png)

<script>
//Run script right away
  window.onload = function () {
//We'll be appending the icon to this DIV later
          var s = Snap("#iconDiv");
//Have Snap load the SVG file
    Snap.load("/assets/images/icon.svg", function(f) {
//Assign the white rectangle
                whiteRect = f.select("#whiteRect");
//Assign the whole icon group
                icon = f.select("#icon");
//When the icon is hovered over, have the white rectangle move up slightly with elastic properties
                icon.hover(function() {
        whiteRect.animate({y:270.0}, 500, mina.elastic);
                },
//And return to original position when not hovered over
                           function() {
        whiteRect.animate({y:276.82181}, 500, mina.elastic);
      }
                );
//Finally append the icon to iconDiv in the body
    s.append(f);
    });
  };
</script>

<!--Here's the DIV that will hold the animated SVG icon-->
<div id="iconDiv"></div>

---

### Standard Library modules

- A Python installation comes with a set of standard library modules (around 200 modules) for various programming tasks like operating system interfaces (`os`, `sys`), object persistence, text pattern matching (`re`), network (`requests`) and Internet scripting, GUI construction (`tkinter`)
- They are not part of the Python language, but come installed with a standard Python installation.
- Due to the standard nature, they are expected to wok portably on most platforms.

---

### How imports work

- In contrast to C/C++ `#include`, which are textual insertions of file into another, Python's `import` are runtime operations involving
  - Find the module's files.
  - Compile it to byte code (if needed).
  - Run the module code to build the objects it defines.

- Finding the module involves searching the *module search path*
- On first import, the code is compiled to generate a byte code `.pyc` file. Unless the source code is modified, subsequent imports simply reuses the byte code.
  - `.pyc` speed future imports.
  - Compilation happens when file is imported. So the top-level script file is usually not compiled. To have the script file both executed as well as imported, `__name__` and `__main__` are used.
- Running/executing the bytecode **assigns** names in the importee namespace to the attributes of the imported module object.

---

### Module search path

Imports mention only the filename without extension, which is searched in a path formed by concatenation of following directories and the left most search result is taken as the file path.

- home directory of the importee files.
- `PYTHONPATH` directories.
- Standard library Modules.
- .pth path file listing custom directories.
- `site-packages` subdirectory in the Python installation for listing the third-party extensions.

- The module search path is assigned to `path` attribute of the `sys` standard modules

```python
import sys
print sys.path
```

Since only the filename without extension is searched, an `import mod` can resolve to any of the following files:
- *mod.py* source code file.
- *mod.pyc* byte code file.
- *mod.pyo* optimized byte code file (Generated when the script is executed using `-O` flag).
- *mod.so* or *mod.dll* compiled extension module which is dynamically linked when imported.
- *mod* directory for package imports.

---

## Summary

The idea of structuring program is the *rationale* behind modules. Modules act as namespaces so that names in one module cannot be seen by another module, unless the former is imported. This Python Program architecture helps in dividing the logic into self-contained components. In addition to the home directory and standard library modules, custom modules can be searched via the module search path setting the `PYTHONPATH` environment variable or .pth files in top-level. While importing a module, Pythons allows freedom to choose from a variety of file extensions like .py, .pyc, .pyo, .so or a directory also (as we will see in the [next chapter](chapter-on-packages)).

This is a [link]({% link _posts/2019-08-30-bananas.md %})  that refers to past post.

The permalink to this page is {{ page.path }}

This is an internal link in Jekyll [Module Search-Path](#Module-search-path)
