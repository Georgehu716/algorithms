# Levenshtein distance

- What it is, its implementation and usage.
- Build something useful using it. (Application)

edit distance

- github.com/spf13/cobra, Suggestions
- https://en.wikipedia.org/wiki/Levenshtein_distance
- https://rust-algo.club/levenshtein_distance/
- https://nlp.stanford.edu/IR-book/html/htmledition/edit-distance-1.html
- https://leetcode.com/problems/edit-distance/
- Go implementation to calculate Levenshtein Distance: https://github.com/agnivade/levenshtein
- https://pkg.go.dev/search?q=levenshtein
- https://www.less-bug.com/posts/rounding-out-edit-distance-the-levenshtein-distance-algorithm/
- in real world production: https://vishnubharathi.codes/blog/levenshtein-distance/
- [] using levenshtein distance algorithm to support pdm: https://github.com/pdm-project/pdm/pull/3274
- python SequenceMatcher: https://github.com/pdm-project/pdm/issues/3270


Iterative with full matrix

```
function LevenshteinDistance(char s[1..m], char t[1..n]):
  // for all i and j, d[i,j] will hold the Levenshtein distance between
  // the first i characters of s and the first j characters of t
  declare int d[0..m, 0..n]

  set each element in d to zero

  // source prefixes can be transformed into empty string by
  // dropping all characters
  for i from 1 to m:
    d[i, 0] := i

  // target prefixes can be reached from empty source prefix
  // by inserting every character
  for j from 1 to n:
    d[0, j] := j

  for j from 1 to n:
    for i from 1 to m:
      if s[i] == t[j]:
        substitutionCost := 0
      else:
        substitutionCost := 1
      d[i, j] := min(d[i-1, j] + 1, // deletion
                     d[i, j-1] + 1, // insertion
		     d[i-1, j-1] + substitutionCost) // substitution
  return d[m, n]
```

```go
func minDistance(word1 string, word2 string) int {
	m, n := len(word1), len(word2)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i < m+1; i++ {
		for j := 0; j < n+1; j++ {
			if i == 0 || j == 0 {
				dp[i][j] = i + j
			} else if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
			}
		}
	}
	return dp[m][n]
}
```


## Articles

### Understanding the Levenshtein Distance Equation for Beginners

- [x] https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0


fuzzy string matching

ruby gem levenshtein-ffi

The levenshtein distance is a number that tells you how different two strings are. The higher the number, the more different the two strings are. At a minimum, the number of edits are required to change one into the other. An "edit" is defined by either an insertion of a character, a deletion of a character, or a replacement of a character.

piecewise functions

$$
lev_{a, b}(i, j) =
\begin{cases}
max(i, j) & \text{if } min(i, j) = 0, \\
\\
min
\begin{cases}
lev_{a, b}(i - 1, j) + 1 \\
lev_{a, b}(i, j - 1) + 1 \\
lev_{a, b}(i - 1, j - 1) + 1_{a_i \neq b_j}
\end{cases}
& \text{otherwise}.
\end{cases}
$$


### The Levenshtein distance in production

- [ ] https://vishnubharathi.codes/blog/levenshtein-distance/

edit distance problem: https://leetcode.com/problems/edit-distance/description/

Grokking Algorithms: https://www.manning.com/books/grokking-algorithms

practical applications: git diff, cobra, spell checker.

"The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other."

git levenshtein distance: https://github.com/git/git/blob/53f9a3e157dbbc901a02ac2c73346d375e24978c/levenshtein.h

```c
#ifndef LEVENSHTEIN_H
#define LEVENSHTEIN_H

int levenshtein(const char *string1, const char *string2,
	int swap_penalty, int substitution_penalty,
	int insertion_penalty, int deletion_penalty);

#endif
```

Damerau-Levenshtein algorithm

