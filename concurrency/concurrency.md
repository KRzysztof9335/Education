# What is concurrency?

Concurrency is a way to make your code work faster by removing impediments slowing down code execution. There are two main cases when one can use concurrency:

  - [IO bound](#io-bound-problems)
  - [CPU bound](#cpu-bound-problems)

> Premature optimization is the root of all evil. Donald Knuth

Before attempting to introduce any parallelism think of Donald's famous sentence. If you still need to introduce it, you have three main tricks:
  - [multiprocessing](#multiprocessing)
  - [multithreading](#multithreading)
  - [async](#asyncio)


Short comparison between them:
| Concurrency trick | Problem type | Process num   | Switch decision|
| :---              |    :----:    |          ---: | ---:           |
| Multiprocessing   | CPU bound    |     many      |    no switch   |
| Multithreading    | IO bound     |      1        |      OS        |
| Asyncio           | IO bound     |      1        |   event loop   |

## IO bound problems

For those problems the main reason that slows the execution is **long waiting time for resources from network or from disk**. Those problems can be solved by using multiprocessing, multithreading and asyncio. However multiprocessing is not recommended for those problems.

## CPU bound problems

For those problems the main reason that slows execution is **your CPU limitation**. Examples of those problems are: mathematical computations, machine learning and so on.  To overcome it you need to execute your code on multiple CPU cores. Here multiprocessing is the solution. Usage of threading or asyncio at best will not have an effect but in many scenarios it will slow down.

## Multiprocessing

Ideal for CPU bounds. Tasks are executed on **many processes**. Do not use more CPUs then your hardware has.


## Multithreading

Good for IO bound. Task are executed **multiple** threads in **1** process. Do not use too many threads, since context switching is expensive. Optimal number is between 5-10 and depends on tasks. Needs experimenting.

View example: [threading.py](examples/threading.py)

Here we need to create ThreadPoolExecutor as context manager which will map function to be executed. This manager may stop any thread at any point of time even during simplest operation like:
```
x = x + 1
```
Threading speeds execution on IO bounds tasks but it is not optimal way.

Moreover, code you write has to be 'Thread safe' to avoid 'Concurrency problems'.


## Asyncio

Ideal for IO bounds. Tasks are executed on **1** thread in **1** process.


## Multiprocessing vs asyncio

Rule of thumb: "Use asyncio when you can, use multithread when you must."

# Concurrency problems

# race conditions

TODO

# dead-locks

TODO