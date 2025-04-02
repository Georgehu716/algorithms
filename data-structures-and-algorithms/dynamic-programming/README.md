# Dynamic Programming

- SkienaTheAlgorithmDesignManual


The most challenging algorithmic problems involve optimization, where we seek to find a solution that maximizes or minimizes some function.

Traveling salesman problem (TSP).

Greedy algorithms that make the best local decision at each step are typically efficient but usually do not guarantee global optimality. Exhaustive search algorithms that try all possibilities and select the best always produce the optimum result, but usually at a prohibitive cost in terms of time complexity.

Dynamic programming combines the best of both worlds. It gives us a way to design custom algorithms that systematically search all possibilities (thus guaranteeing correctness) while storing results to avoid recomputing (thus providing efficiency). By storing the consequences of all possible decisions and using this information in a systematic way, the total amount of work is minimized.

Dynamic programming is a technique for efficiently implementing a recursive algorithm by storing partial results. The trick is seeing whether the naive recursive algorithm computes the same subproblems over and over again. If so, storing the answer for each subproblems in a table to look up instead of recompute can lead to an efficient algorithm. Speed a correct recursive algorithm up by using a results matrix.

Dynamic programming is generally the right method for optimization problems on combinatorial objects that have an inherent left to right order among components. What is left to right order?
