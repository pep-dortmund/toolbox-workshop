# PeP et al. Toolbox-Workshop <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>

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

## License

The programming code examples in this material are shared under the GnuGPLv3 license.
The lecture material (e.g. jupyter notebooks) are shared under the Creative Commons Attribution-NonCommercial License: https://creativecommons.org/licenses/by-nc/4.0/legalcode.txt, so they cannot be used for commercial training / tutorials / lectures.


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

### Comic Sans
In den LaTeX-Slides wird _Comic Sans_ verwendet.
Für Ubuntu kann dieser Font mit
`sudo apt install ttf-mscorefonts-installer`
installiert werden.
Für Fedora und weitere `rpm`-basierte Systeme
soll laut
<http://mscorefonts2.sourceforge.net/>
erst
`yum install curl cabextract xorg-x11-font-utils fontconfig`
und dann
`rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm`
ausgegführt werden (nicht getestet).
Für Arch Linux kann
<https://wiki.archlinux.org/index.php/Microsoft_fonts> helfen (nicht getestet).
