# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:13:46 2021

@author: 11200
"""
from collections import defaultdict


def fun1(words, k):
    # 统计每个单词出现的次数
    count_dict = defaultdict(int)
    for w in words:
        count_dict[w] += 1

    # 以次数为键，单词组成的列表为值的字典
    dic = defaultdict(list)
    for word, count in count_dict.items():
        dic[count].append(word)
    # 按次序排列
    dic = sorted(dic.items(), key=lambda i: -i[0])
    # print(dic)

    ret = []
    for c, w_li in dic:
        w_li.sort()
        ret.extend(w_li)
        if len(ret) > k:
            break
    # print(ret)
    return ret[:k]


if __name__ == '__main__':
    topKFrequent = [fun1]

    for f in topKFrequent:
        print(f(["i", "love", "leetcode", "i", "love", "coding"], k=2) == ["i", "love"])
        print(f(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4) == ["the", "is", "sunny",
                                                                                                  "day"])

"""
692. 前K个高频单词

给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
 

示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
