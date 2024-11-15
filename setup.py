import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools

setuptools.setup(
    name="gspan_mining",
    version="0.2.3",
    packages=['gspan_mining'],
)

# python -m subgraph_extraction -s 2 -l 3 -u 4 ./graphdata/test_graph.txt