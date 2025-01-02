# 2439. 最小化数组中的最大值

给你一个下标从 0 开始的数组 nums, 它含有 n 个非负整数。

每一步操作中，你需要:
- 选择一个满足 1 <= i < n 的整数 i, 且 nums[i] > 0.
- 将 nums[i] 减 1.
- 将 nums[i - 1] 加 1.

你可以对数组执行任意次上述操作，请你返回可以得到的 nums 数组中最大值最小为多少.


示例1:
输入: nums = [3, 7, 1, 6]
输出: 5
解释:

一串最优操作是:
1. 选择 i = 1, nums 变为 [4, 6, 1, 6].
2. 选择 i = 3, nums 变为 [4, 6, 2, 5].
3. 选择 i = 1, nums 变为 [5, 5, 2, 5].

nums 中最大值为 5. 无法得到比 5 更小的最大值.

所以我们返回 5.


