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
**Master thread** - thread 0
- _if(bool)_ - if true -> threads=1
- _num_threads()_
- _copyin(list)_
- _reduction(op:list)_

## Work Sharing Construction

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
  * _private_
  * ...
  * _nowait_ - without barrier


2. **SECTIONS**

```cpp
#pragma omp sections <params>
{
...
  #pragma omp section
  {
    ...
  }

}//BARIERA
```

3. **single**

```cpp
#pragma omp single <params>
{...}
```
## Data Scope Attribute Clauses

- _default(shared | none)_
- _private(list)_
- _firstprivate(list)_
- _shared(list)_
- _threadprivate_

## Sync Constructructions

- *master*
- *critical*
- *ordered*
- *atomic*
- *flush*
- *barrier*

## Other

- `omp_set_num_threads()`
- `omp_get_thread_num()`
- `omp_get_num_threads()`
