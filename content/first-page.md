title: Pelican Supports Syntax Highlighting
date: 2019-05-14  
category: Programming

## JavaScript

Does code highlighting work here?

```javascript
// ES5
function foo() {
  console.log("bar baz");
}

// ES6+
const blah = () => {
  let a = [1,2,3];
  return = a.map(x => x + 1);
}

```

## Haskell

Function application with the `<*>` operator and a `Maybe` context:

```haskell
Just (*2) <*> Just 10
Just 20
```

Why might you want to do that?

```haskell
Just (*2) <*> Just "asdf"
-- ERROR....!!!
```

Things blow up if incompatible types are used. Whoa!

Here's some more functional fun.

```haskell
(*) <$> [1,2] <*> [3]
[3,6]
```

The code above maps the multiplication operator to the first list [1,2] to produce 
the functions something like this `[(\x -> x * 1), (\x -> x * 2)]`. These functions
are in turn each applied to to `[3]` giving `[3,6]`.

## Python

Input

```python
import numpy as np
a = np.arange(9),reshape(3,3)
a
```

Output:

```python
array([[0, 1, 2],
       [3, 4, 5],
	   [6, 7, 8]])
```

Multiplying `a` by a scalar quantity

```python
a * 2
```

Gives:

```python
array([[ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
```
