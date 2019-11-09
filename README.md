# hermetrics
Python library for distance and similarity metrics

## Install (Comming soon...)

From pypi:

```bash
pip install hermetrics
```

## Overview
Hermetrics is a library designed for use in experimentation with string metrics. The library features a base class *Metric* which is highly configurable and can be used to implement custom metrics.

Based on *Metric* are some common string metrics already implemented to compute the *distance* between two strings. Some common edit distance metrics as *Levenshtein* can be parametrized with different costs for each edit operation, althought have been only thorougly tested with unitary costs.

A metric has three main methods *distance*, *normalized_distance* and *similarity*. In general the *distance* method computes the absolute distance between two strings, whereas *normalized_distance* can be used to scale the distance to a particular range, usually (0,1), and the *similarity* method is being normally defined as (1-*normalized_distance*).

The normalization of the distance can be customized overriding the auxiliary methods for its computation. Those methods are *max_distance*, *min_distance* and *normalize*.

## Metrics

For the time being the following metrics have been implemented:

### Hamming

### Levenshtein

Levenshtein distance is usually known as "the" edit distance. It is defined as the minimum number of edit operations (*deletion*, *insertion* and *substitution*) to transform the source string into the target string. The algorithm for distance computation is implemented using the dynamic programming approach with the full matrix construction, althought there are optimizations for time and space complexity those are not implemented here.

```python
from hermetrics.levenshtein import Levenshtein

lev = Levenshtein()

lev.distance('ace', 'abcde') # 2
lev.normalized_distance('ace', 'abcde') # 0.4
lev.similarity('ace', 'abcde') # 0.6
```  
### OSA (Optimal String Alignment)


### Damerau-Levenshtein


### Jaccard


### Dice (Sorenson-Dice)


### Jaro


### Jaro-Winkler


## To Do

* Use \**kwargs instead of cost tuples
* Weighted Levenshtein
* More metrics
* Allow variable maximun prefix length in Jaro-Winkler
* Backtracking operations
