# PeP et al. Toolbox-Workshop

Dieses Repository enthält Materialien zum PeP et al. Toolbox-Workshop.

Folgende Themen sind Teil des Workshops:

 - Erste Woche
   - Python-Grundlagen
   - numpy
   - scipy
   - matplotlib
   - uncertainties
   - git
   - Unix-Kommandozeile
 - Zweite Woche
   - Umgang mit LaTeX


# Build Requirements

- up-to-date TeXLive 2018 (pretest at the moment)
- up-to-date anaconda3 (using python 3.6.4)
- poppler (for pdfseparate)
- wget 
- Python notebook extensions `pip install jupyter_contrib_nbextensions`

## Installation

For TeXLive and anaconda, follow the installtion instruction on
http://toolbox.pep-dortmund.org/install

### MacOS 

- `brew install poppler wget`

### Ubuntu

- `sudo apt install poppler-utils`

### Arch

- `sudo pacman -S poppler`


## Working with git

We use the github workflow in this repository, see <https://guides.github.com/introduction/flow/>.

In short, to contribute:

1. Create a new branch using `git branch <name>`
1. Switch to it using `git checkout <name>`
1. Make changes and commit
1. Push the Branch using `git push -u origin <name>`
1. Open a Pull Request on github.
