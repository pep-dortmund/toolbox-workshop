# PeP et al. Toolbox Workshop <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a> [![CI](https://github.com/pep-dortmund/toolbox-workshop/actions/workflows/ci.yml/badge.svg)](https://github.com/pep-dortmund/toolbox-workshop/actions/workflows/ci.yml)

Dieses Repository enthält Materialien zum PeP et al. Toolbox Workshop.

Folgende Themen sind Teil des Workshops:

 - Erste Woche
   - Python-Grundlagen
   - numpy
   - matplotlib
   - scipy
   - uncertainties
   - Unix-Kommandozeile
   - make
   - git
 - Zweite Woche
   - Umgang mit LaTeX

## License

The programming code examples in this material are shared under the GnuGPLv3 license.
The lecture material (e.g. jupyter notebooks) are shared under the Creative Commons Attribution-NonCommercial License: https://creativecommons.org/licenses/by-nc/4.0/legalcode.txt, so they cannot be used for commercial training / tutorials / lectures.


# Build Requirements

- up-to-date TeXLive 2023
- up-to-date anaconda3 (using python 3.11) or miniconda with packages in `environment.yml`
- poppler (for pdfseparate)
- wget

## Installation

For TeXLive and mamba, follow the installation instruction on
http://toolbox.pep-dortmund.org/install

Create the environment with the required packages using

```
mamba env create -f environment.yml
```

and activate it each time you are working in this project using

```
mamba activate toolbox
```

### MacOS

- `brew install poppler wget`

### Ubuntu

- `sudo apt install poppler-utils`

### Arch

- `sudo pacman -S poppler`


## Working with git

Before your first commit, make sure to run ``pre-commit install`` to set up our ``pre-commit hooks`` run
every time you commit. This ensures code quality before pushing.

We use the github workflow in this repository, see <https://guides.github.com/introduction/flow/>.
In short, to contribute:

1. Create a new branch and switch to it using `git switch -c <name>`
1. Make changes and commit
1. Push the Branch using `git push -u origin <name>`
1. Open a Pull Request on github.
