# OpenMP

---


```cpp
#include <omp.h>

```

Compiler flags:
`-fopenmp`

## Pragma

```cpp
#pragma omp parallel <params>
{...}
```

- _if(bool)_ - if true -> threads=1
- _num_threads()_
- _default(shared | none)_
- _private(list)_
- _firstprivate(list)_
- _shared(list)_
- _copyin(list)_
- _reduction(op:list)_

## Work Construct

1. **FOR**
```cpp
#pragma omp for <params>
{...}
```
  * _schedule(type,chunk)_
    - static
    - dynamic
    - auto
    - guided
    - runtime
  * private
  * ...
  * _nowait_
  

2. **SECTIONS**

```cpp
#pragma omp sections <params>
{...}
```

3. **single**

```cpp
#pragma omp single <params>
{...}
```

## Other

- `omp_set_num_threads()`
- `omp_get_thread_num()`
- `omp_get_num_threads()`
