# 1. Two Sum

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/two-sum/)
[![Tags](https://img.shields.io/badge/Array-4B8BBE?style=for-the-badge)](https://leetcode.com/problems/two-sum/)
[![Tags](https://img.shields.io/badge/Hash_Table-FF6F61?style=for-the-badge)](https://leetcode.com/problems/two-sum/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/two-sum/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-1716_ms-9B59B6?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-19.8_MB-3498DB?style=for-the-badge)

</div>

## Problem

You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than `O(n^2)` time complexity?

## Approach

Brute force: for each index `i`, check every later index `j` and test whether `nums[i] + nums[j] == target`. Returns as soon as a matching pair is found.

## Complexity

- **Time:** O(n^2)
- **Space:** O(1)

## Notes

This is the brute-force approach. The follow-up asks for better than O(n^2) — a single-pass hash map (storing each number's index as you go and checking for its complement) gets this down to O(n) time / O(n) space.