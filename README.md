# cliifs
**Command Line Interface Iterated Function Systems**

Render and view fractals, using the chaos game, from iterated functions systems right on your terminal.

### Screenshot
<img width="1280" alt="cliifs" src="https://user-images.githubusercontent.com/47536723/55172096-ba77ad80-5136-11e9-8c2d-49b412cd3711.png">
<img width="1280" alt="cliifs" src="https://user-images.githubusercontent.com/47536723/55172172-db400300-5136-11e9-9503-1a729f366811.gif">

# Installation
###
Install via pip with `pip install cliifs` or download the appropriate binary from [releases](https://github.com/raphaelreyna/cliifs/releases/tag/v0.4)


# How To Use
cliifs reads in a plaintext file that contains the univariate linear functions you wish to use for your IFS.

The first line must begin with either `1D` or `2D`. 

The following lines each represent the coefficients of linear equations, and you may add as many as you like.

See below for specifics on how to write these files.

See the included examples for more details.

### Invocation example
To render, with animation and color, the IFS stored in a file called `exampleFile`, move into the directory containing exampleFile and run the command:

`cliifs exampleFile -c -a`

#### Flags 
cliifs accepts the following flags
* `-h` for help.
* `-c` to render in random colors.
* `-i N` to render using N iterations.
* `-a` to animate.
* `-d D` to delay each frame by D milliseconds if animating.
* `-m M` to set the collection of markers to be used at random.

## 1 Dimensional Systems
One dimensional systems are given as a test file whose first line reads simply `1D`.

Each subsequent line has the form `a b` which represents the function `f(x) = ax+b`.


## 2 Dimensional Systems
Two dimensional Systems are given as a test file whose first line reads simply `2D`.

Each subsequent line has the form `a1 b1 a2 b2 c1 c2` which represents the vector function `f(v) = Av+b`.

In this function, `A` is the matrix with rows `{a1, b1}` and `{a2, b2}`, `b` is the vector `{c1, c2}` and `v` is the position vector `{x,y}`.

