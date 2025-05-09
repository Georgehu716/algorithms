"""
- https://leetcode.cn/problems/smallest-palindromic-rearrangement-ii/description/

3518. 最小回文排列II

给你一个回文字符串 s 和一个整数 k。
返回 s 的按字典序排列的第 k 小回文排列。如果不存在 k 个不同的回文排列，则返回空字符串。

注意：产生相同回文字符串的不同重排视为相同，仅计为一次。
如果一个字符串从前往后和从后往前读都相同，那么这个字符串是一个回文字符串。
排列是字符串中所有字符的重排。
如果字符串 a 按字典序小于字符串 b，则表示在第一个不同的位置，a 中的字符比 b 中的对应字符在字母表中更靠前。
如果在前 min(a.length, b.length) 个字符中没有区别，则较短的字符串按字典序更小。

示例1：
输入: s = "abba", k = 2
输出: "baab"
解释:
- "abba" 的两个不同的回文排列是 "abba" 和 "baab"。
- 按字典序，"abba" 位于 "baab" 之前。由于 k = 2，输出为 "baab"。

示例2：
输入: s = "aa", k = 2
输出: ""
解释:
- 仅有一个回文排列: "aa".
- 由于 k = 2 超过了可能的排列数，输出为空字符串。
"""
