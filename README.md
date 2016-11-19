# PyMake <img align="right" src="res/images/pymake-logo.png">

**PyMake** is a tool for automating build tasks. It comes with ready-made
templates for several different compilers, allowing you to quickly set up
portable build tasks. **With PyMake, it becomes trivial to set up complex build
tasks, doing everything from library and executable compilation to asset
building and even deployment.**

### -> [Download now!](https://github.com/philiparvidsson/pymake/releases/) <-

## Getting Started

1. Download and install [Python 2.7.x](https://www.python.org/downloads/).
2. Start with one of the [example](examples) or [template](templates) files,
picking one relevant to your project.
3. If needed, modify the file. See the guide for instructions on how to do so.
3. Build your project by running your make script. You can either type `python
your_make_file.py` or `./your_make_file.py` (only on Linux).

### Prerequisities

* [Python 2.7.x](https://wiki.python.org/moin/BeginnersGuide/Download)

### Installing

#### Begin by downloading and installing [Python 2.7.x](https://www.python.org/downloads/).
On Linux, depending on your distribution, Python comes pre-installed. This means that you do not need to install anything for mshl to work. If you don't have Python (you can check by typing python in a terminal), you might be able to install it by typing `sudo apt-get install python`.

On Windows, you need to install Python manually. See [this link](https://wiki.python.org/moin/BeginnersGuide/Download) for more information.

#### Download the latest mshl release.
The latest pymake scripts are always available [here](https://github.com/philiparvidsson/pymake/releases/). Download and save `pymake.py` along with any make script you need for your project.

### Building

#### Begin by creating a simple make script.
To familiarize yourself with pymake, you can begin by writing a simple make script. You could also use one of the [example programs](examples), or the one below if you just want to try out pymake quickly:

```python
#!/usr/bin/env python

# This simple make script builds a C# project, compiling all files in the src
# directory and outputting the program in the bin directory.

import os, sys
sys.path.insert(0, os.path.join('build', 'pymake'))
from pymake import *

import csc

pymake(csc.defaultConf(), {
    'name': 'Program.exe',

    'flags': ['/target:exe',
              '/o',
              '/platform:x64'],

    'libs': ['System.dll'],
})
```

Since pymake scripts are written in Python, there is no limit to their complexity. This allows you to create very complex and secure build and deployment scripts for your projects.

#### Build your project.
Save your script in a file named `make.py` in your project directory. Make sure you have installed pymake into the `build/pymake` directory (this is the standard directory, but can always be changed if needed). Invoke your make script by running it with the following command: `python make.py`

Make sure you are in your project directory, where your `make.py` file is.

## Running the Tests

n/a

## Deployment

### Deploying make scripts

Along with your `make.py` file, you need to store the `pymake.py` file in your project, along with any template files you may have used.

## Built With

* **emacs** - The best text editor out there! ;-)
* **Python** - A widely used high-level, general-purpose, interpreted, dynamic programming language.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/philiparvidsson/pymake/tags).

## Authors

* **Philip Arvidsson** - *Initial work* - [philiparvidsson](https://github.com/philiparvidsson)

See also the list of [contributors](https://github.com/philiparvidsson/pymake/contributors) who participated in this project.

## License

This project is licensed under the MIT License—see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

n/a
