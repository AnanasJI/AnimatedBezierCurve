from setuptools import setup

setup(
    name="animate_bezier",
    version="0.5",
    description="Produces an interactive altair chart of a bezier curve saved as a html",
    author="Anna",
    packages=["animate_bezier"],
    install_requires=["numpy", "pandas", "seaborn", "altair", "typing", "altair_saver"],
)
