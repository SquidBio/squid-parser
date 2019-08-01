from setuptools import setup

setup(
    name='squid-parser',
    version='0.1',
    description='Convert squid files to gcode',
    url='http://github.com/SquidBio/squid-parser',
    author='Isaac Ellmen',
    author_email='isaac@squidbio.com',
    packages=['squidparse'],
    entry_points={
        'console_scripts': ['squidparse=squidparse.command_line:main'],
    }
)
