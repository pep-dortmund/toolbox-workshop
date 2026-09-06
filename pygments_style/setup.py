from setuptools import setup

setup(
    name="toobox_style",
    version="1.0.0",
    py_modules=["toolbox_style"],
    entry_points={"pygments.styles": ["toolbox = toolbox_style:Toolbox"]},
)
