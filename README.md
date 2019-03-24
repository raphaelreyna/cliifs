# cliifs
**Command Line Interface Iterated Function Systems**

Render and view fractals from iterated functions systems right on your terminal.

# How To Use
cliifs reads in a plaintext file that contains the univariate linear functions you wish to use for your IFS.

The first line must begin with either `1D` or `2D`. 

The following lines each represent the coefficients of linear equations, and you may add as many as you like.

See below for specifics on how to write these files.

See the included examples for more details.


## 1 Dimensional Systems
One dimensional systems are given as a test file whose first line reads simply `1D`.

Each subsequent line has the form `a b` which represents the function `f(x) = ax+b`.


## 2 Dimensional Systems
Two dimensional Systems are given as a test file whose first line reads simply `2D`.

Each subsequent line has the form `a1 b1 a2 b2 c1 c2` which represents the vector function `f(v) = Av+b`.

In this function, `A` is the matrix with rows `{a1, b1}` and `{a2, b2}`, `b` is the vector `{c1, c2}` and `v` is the position vector `{x,y}`.
