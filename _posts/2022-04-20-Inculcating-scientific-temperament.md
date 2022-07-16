---
layout: post
author: fubar
title: "Resources for scientific temperament"
tag: physics
tool: phd
excerpt: "Scientific temperament is not a state. It is a continuous process for aligning one's behaviour to inculcate the spirit of the scientific method. There are many aspects to this process each addressing one or more of the pillars of the scientific method. Here are some guidelines that help nurture these aspects."
date: 20th April, 2022
---

## Scientific method

The scientific method consists of four pillars

- Observation
- Experiment
- Theory
- Dissemination

While the first three pillars are confined to the researcher, 
dissemination enables interaction between them. 
Dissemination has duly gained prominence in modern science. 

The ability to communicate the research is paramount in a fast-paced, attention-deprived world.

The current standard of dissemination is through research papers. Consequently, 
it is imperative to inculcate rigour in our writing. 
Further, academic talks also complement the former mode of dissemination. The following references
act as guidelines for writing research papers and giving academic talks.

## Academic Writing

- [Elements of Style](https://www.google.co.in/books/edition/The_Elements_of_Style/34hCCe9wmq4C?hl=en&gbpv=1&dq=elements+of+style&printsec=frontcover) is a classic style guide for academic writing.
- [Ten simple rules for structuring papers](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619)

## Data Visualization

- [Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)
- [The Visual Display of Quantitative Information](https://www.google.co.in/books/edition/The_Visual_Display_of_Quantitative_Infor/qmjNngEACAAJ?hl=en) is a canonical reference
on composing data visualizations. Its philosophy is summarized by

> the measure of graphical excellence is by how many thoughts a figure provides the reader in as short time as possible by using as little ink as possible.

- [Data Visualization](http://blogs.nature.com/methagora/2013/07/data-visualization-points-of-view.html) is a string of points of view on data visualization published in Nature Methods.
- [Elements of Visual Style](https://www.nature.com/articles/nmeth.2444) is a complementary style guide to Prof. Tufte's "Elements of Style" for data visualization.
- Colormaps are frequently used in literature; it is imperative to use the right kind of colormap to represent the data to avoid artifacts associated with visualization as well as for being colorblind friendly. [Matplotlib's colormap guide](https://matplotlib.org/stable/tutorials/colors/colormaps.html) is a useful starting point that helps choose the right kind of colormap for a given map. It also provides detailed references to the related academic research. To summarize, the human vision is predominantly perceptive to the lightness of color (instead of hue as believed previously). Based on the trends in lightness of colors across each colormap, these are divided into four categories -
	- **Sequential** maps with perceptual uniformity. Perceptual uniformity coloquially means that the human brain is able to satisfactorily map the color trend with the trend in the data. Such maps are useful for representing data that have inherent ordering. Some of the maps are **viridis**, plasma, **inferno**, cividis, magma.
	- **Diverging** colormaps where the Lightness peaks in the middle and is same at the ends. Such maps are useful for representing data that have 'zero crossings' that is predominant central value in the ordered data. Some of the maps are **coolwarm**, Spectral, seismic.
	- **Cyclic** colormaps with equal lightness at the ends. Such maps are useful for representing data with cyclic ordering like phase angle, wind direction, time of day. Some of the maps are **twilight**, hsv.
	- **Qualitative** (also called categorical) colormaps to represent data that has **no** inherent ordering, but can be classified into categories. The lightness of the colors has no particular ordering. Some of the maps are **tab10** (from [Tableau](https://www.tableau.com/)), Accent, Paired.

## Data accessibility

- On [colour-blind](https://www.nature.com/articles/d41586-021-02696-z)-[friendly](https://www.ascb.org/science-news/how-to-make-scientific-figures-accessible-to-readers-with-color-blindness/) figures. 
If the use of categorial colormap like rainbow or jet is unavoidable or desirable, then use the improved [Turbo](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html).

## Talks

- [How to give a good talk](https://www.cell.com/molecular-cell/fulltext/S1097-2765(09)00742-4)

## Esoteric resources

- [Matplotlib tutorial](https://github.com/rougier/matplotlib-tutorial) by Nicolas Rougier
- [Materials for nurturing scientists](https://www.weizmann.ac.il/mcb/UriAlon/materials-nurturing-scientists) by Prof. Uri Alon of Weizmann Institute of Science, Israel.