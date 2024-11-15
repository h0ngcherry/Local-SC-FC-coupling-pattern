# <div align = center>Local SC-FC coupling pattern</div>

**Subgraph extraction** is based on deep coding tree and gSpan algorithm.

### Data availability statement
The data is not publicly available due to permission reasons. The data are available from the corresponding author on reasonable request.

### Counterfactual Explanation
The counterfactual interpretation based on local SC-FC coupling is based on the DiCE framework. We only give the relevant test code here, and the detailed code will be updated after the paper is accepted. For more details, please visit: https://github.com/interpretml/DiCE.

### How to install

This project was implemented on **Python 3.7** and **MATLAB R2018b**.

Install this project using pip:

```sh
pip install gspan-mining
pip install dice-ml
```

### How to run

```sh
python -m subgraph_extraction -s [minsup] -l [vertex_lower_limit] -u [vertex_upper_limit] ./graphdata/test_graph.txt
python -m subgraph_extraction -s 2 -l 3 -u 4 ./graphdata/test_graph.txt
```

### Reference
- [Paper](https://pure.mpg.de/rest/items/item_1790437/component/file_3075625/content)

Tsuda, Koji. "Entire regularization paths for graph data." Proceedings of the 24th international conference on Machine learning. 2007.

- [Paper](http://www.cs.ucsb.edu/~xyan/papers/gSpan-short.pdf)

Yan, Xifeng, and Jiawei Han. "gspan: Graph-based substructure pattern mining." 2002 IEEE International Conference on Data Mining, 2002. Proceedings.. IEEE, 2002.

- [Paper](https://dl.acm.org/doi/pdf/10.1145/3351095.3372850)

Mothilal, Ramaravind K., Amit Sharma, and Chenhao Tan. "Explaining machine learning classifiers through diverse counterfactual explanations." Proceedings of the 2020 conference on fairness, accountability, and transparency. 2020.


### Additional information
Currently, only the prototype code of this study has been uploaded. The corresponding complete code and some details of the experiment will be supplemented after the paper is accepted.


