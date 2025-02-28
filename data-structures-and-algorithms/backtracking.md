# Backtracking

- https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf


recursive strategy


## N Queens

The prototypical backtracking problem is the classical n Queens Problem, the problem is to place n queens to an n * n chessboard, so that no two queens are attacking each other.

For readers not familiar with the rules of chess, this means that no two queens are in the same row, the same column, or the same diagonal.

Trial and errors

We place queens on the board one row at a time, starting with the top row. To place rth queen, we methodically try all n squares in row r from left to right in a simple for loop. If a particular square is attacked by an earlier queen, we ignore that square; otherwise, we tentatively place a queen on that square and recursively grope for consistent placements of the queens in later rows.

```
place_queens(Q[1..n], r):
    if r = n + 1
        print Q[1..n]
    else
        for j <- 1 to n
            legal = True
            for i <- 1 to r - 1
                if (Q[i] = j) or (Q[i] = j + r - i) or (Q[i] = j - r + i)
                    legal = False
            if legal
                Q[r] = j
                place_queens(Q[1..n], r + 1) # Recursion!
```

The execution of place_queens can be illustrated using a recursion tree. The backtracking search for complete solutions is equivalent to a depth-first search of this tree.
