from pygments.styles.solarized import SolarizedLightStyle
from pygments.token import Comment

styles = SolarizedLightStyle.styles.copy()
# remove *italic* in the default
styles[Comment] = '#93a1a1'



class Toolbox(SolarizedLightStyle):
    styles = styles
