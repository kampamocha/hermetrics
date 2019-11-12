# hermetrics
Python library for distance and similarity metrics

## Install (Comming soon...)

From pypi:

```bash
pip install hermetrics
```

## Overview
Hermetrics is a library designed for use in experimentation with string metrics. The library features a base class *Metric* which is highly configurable and can be used to implement custom metrics.

Based on *Metric* are some common string metrics already implemented to compute the *distance* between two strings. Some common edit distance metrics such as *Levenshtein* can be parametrized with different costs for each edit operation, althought have been only thorougly tested with costs equal to 1. Also, in theory, the implemented metrics can be used to compare any iterable in addition to strings, but more tests are needed.

A metric has three main methods *distance*, *normalized_distance* and *similarity*. In general the *distance* method computes the absolute distance between two strings, whereas *normalized_distance* can be used to scale the distance to a particular range, usually (0,1), and the *similarity* method being normally defined as (1-*normalized_distance*).

The normalization of the distance can be customized overriding the auxiliary methods for its computation. Those methods are *max_distance*, *min_distance* and *normalize*.

## *Metric* class

*Metric* is a base class that can receive as arguments six specific functions to be used as methods for the metric being implemented. The class constructor just assign the functions received as parameters to the class methods. If ypu omit some parameter then a default method is used.

```python
class Metric:
    """Class for metric implementations"""

    def __init__(self, distance=None, max_distance=None, min_distance=None, normalize=None, normalized_distance=None,  similarity=None, name='Generic'):
        """Class constructor - receives a function for distance or similarity evaluation"""
        self.name = name
        self.distance = distance or self.distance
        self.max_distance = max_distance or self.max_distance
        self.min_distance = min_distance or self.min_distance
        self.normalize = normalize or self.normalize        
        self.normalized_distance = normalized_distance or self.normalized_distance
        self.similarity = similarity or self.similarity
```  
### Default methods
Description of default methods for the *Metric* class. In general a method of a metric receives three parameters:
* *source*. The source string or iterable to compare.
* *target*. The target string or iterable to compare.
* *cost=1*. If a number, the unit cost for any edit operations. If a tuple, the cost for edit operations in the following order (deletion, insertion, substitution, transposition).

#### distance
The *distance* method computes the total cost of transforming the *source* string on the *target* string. The default method just return 0 if the strings are equal and 1 otherwise.

#### max_distance
Returns the maximum value of the distance between *source* and *target* given a specific *cost* for edit operations. The default method just return 1 given *source* and *target* don't have both length=0, in that case just return 0.

#### min_distance
Return 0.

##### normalize
This method is used to scale a value between two limits, usually those obtained by *max_distance* and *min_distance*, to the (0,1) range. Unlike the other methods, *normalize* doesn't receive the usual arguments (*source*, *target* and *cost*), instead receive the following:

* *x*. The value to be normalized.
* *low=0*. The minimum value for the normalization, usually obtained with *min_distance* method.
* *high=1*. The maximum value for the normalization, usually obtained with *max_distance* method.

#### normalized distance
Scale the distance between *source* and *target* for specific *cost* to the (0,1) range using *max_distance*, *min_distance* and *normalize*.

#### similarity
Computes how similar are *source* and *target* given a specific *cost*. By default defined as 1 - *normalized_distance* so the result is also in the (0,1) range.

## Metrics

For the time being the following metrics have been implemented:

### Hamming

The Hamming distance count the positions where two strings differ. Normally the Hamming distance is only defined for strings of equal size but in this implementation strings of different size can be compared counting the difference in size as part of the distance.

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

<img src="https://latex.codecogs.com/svg.latex?\Large&space;D=\frac{2J}{1+J}"/>

```python
from hermetrics.dice import Dice

dic = Dice()

dic.distance('abcd', 'abce') # 0.25
dic.similarity('abcd', 'abce') # 0.75
``` 

### Jaro

*Jaro* distance is based on the *matching* characters present on two strings and the number of transpositions between them. A *matching* occurs when a character of a string is present on the other string but in a position no further away that certain threshold based on the lenght of the strings. The *Jaro* distance is normalized.

```python
from hermetrics.jaro import Jaro

jar = Jaro()

jar.distance('abcd', 'abe') # 0.278
jar.similarity('abcd', 'abe') # 0.722
``` 

### Jaro-Winkler

Extension of *Jaro* distance with emphasis on the first characters of the strings, so strings that have *matching* characters on the beginning have more similarity than those that havae *matching* characters at the end.

```python
from hermetrics.jaro_winkler import JaroWinkler

jaw = JaroWinkler()

jaw.distance('abcd', 'abe') # 0.222
jaw.similarity('abcd', 'abe') # 0.778
``` 

## To Do

* Use \**kwargs instead of cost tuples
* Weighted Levenshtein
* Allow variable maximun prefix length in Jaro-Winkler
* Implement backtracking of operations
* More metrics
