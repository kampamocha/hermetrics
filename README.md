# hermetrics
Python library for distance and similarity metrics

## Install (Comming soon...)

From pypi:

```bash
pip install hermetrics
```

## Overview
Hermetrics is a library designed for use in experimentation with string metrics. The library features a base class *Metric* which is highly configurable and can be used to implement custom metrics.

Based on *Metric* are some common string metrics already implemented to compute the *distance* between two strings. Some common edit distance metrics such as *Levenshtein* can be parametrized with different costs for each edit operation, althought have been only thorougly tested with unitary costs. Also, in theory, the implemented metrics can be used to compare any iterable in addition to strings, but more tests are needed.

A metric has three main methods *distance*, *normalized_distance* and *similarity*. In general the *distance* method computes the absolute distance between two strings, whereas *normalized_distance* can be used to scale the distance to a particular range, usually (0,1), and the *similarity* method is being normally defined as (1-*normalized_distance*).

The normalization of the distance can be customized overriding the auxiliary methods for its computation. Those methods are *max_distance*, *min_distance* and *normalize*.


## Metrics

For the time being the following metrics have been implemented:

### Hamming

The Hamming distance count the positions where two strings differ. Normally the Hamming distance is only defined for strings of equal size but in this implementation strings of different size can be compared.

```python
from hermetrics.hamming import Hamming

ham = Hamming()

ham.distance('abcd', 'abce') # 1
ham.normalized_distance('abcd', 'abce') # 0.25
ham.similarity('abcd', 'abce') # 0.75
```  

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

The *OSA* distance is based on the *Levenshtein* distance but counting the *transposition* as a valid edit operation with the restriction that no substring can be transposed more than once.

```python
from hermetrics.osa import Osa

osa = Osa()

osa.distance('abcd', 'abdc') # 1
osa.normalized_distance('abcd', 'abdc') # 0.25
osa.similarity('abcd', 'abdc') # 0.75
``` 

### Damerau-Levenshtein

The *Damerau-Levenshtein* distance is like *OSA* but without the restriction on the number of transpositions for the same substring.

```python
from hermetrics.damerau_levenshtein import DamerauLevenshtein

dam = DamerauLevenshtein()

dam.distance('abcd', 'cbad') # 2
dam.normalized_distance('abcd', 'cbad') # 0.5
dam.similarity('abcd', 'cbad') # 0.5
``` 

### Jaccard

The *Jaccard* index considers the strings as a *bag-of-characters* set and computes the cardinality of the intersection over the cardinality of the union. The distance function for *Jaccard* index is already normalized.

```python
from hermetrics.jaccard import Jaccard

jac = Jaccard()

jac.distance('abcd', 'abce') # 0.4 
jac.similarity('abcd', 'abce') # 0.6
``` 

### Dice (Sorenson-Dice)

Is related to *Jaccard* index in the following manner:

$D = 2J / (1+J)$

### Jaro


### Jaro-Winkler


## To Do

* Use \**kwargs instead of cost tuples
* Weighted Levenshtein
* Allow variable maximun prefix length in Jaro-Winkler
* Implement backtracking of operations
* More metrics
