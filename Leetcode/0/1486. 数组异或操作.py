# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:33:58 2021

@author: 11200
"""


def xorOperation(n, start):
    a = b = start
    for i in range(n - 1):
        a = a + 2
        b = b ^ a
    return b


def mathf(n, start):
    def sumXor(x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0

    e = n & start & 1
    s = start // 2
    ret = sumXor(s - 1) ^ sumXor(s + n - 1)
    return ret << 1 | e


print(mathf(999, 990))
print(xorOperation(999, 990))

'''
看了好久才明白[狗头]，写一下自己的理解, 不会写公式，将就看吧。

**首先需要计算的式子是**：

start⊕(start+2)⊕(start+4)⊕⋯⊕(start+2(n−1))

### 1. 为什么当且仅当 start 为奇数，且 n 也为奇数时，结果的二进制位的最低位才为 1？

如果start是偶数，偶数加偶数还是偶数，n个偶数做异或，最后一位一定是0；如果start是奇数，奇数加偶数是奇数，偶数个奇数做异或，最后一位还是0，只有奇数个奇数做异或，最后一位才是1。根据start和n的奇偶性就可以求出最后一位的值e，值为0或1。

### 2. 转换为带s公式的推导过程

考虑将所有参与异或的数都删除最后一位再进行运算：

start/2⊕(start/2+2/2)⊕(start/2+4/2)⊕⋯⊕(start/2+2(n−1)/2)

为什么除以2就是删除最后一位，就和11/10就是删除十进制的最后一位一样。这里注意除法需要使用向下取整，移位操作就不需要考虑。然后用得到的结果乘于2（既向左移位），再加上最后一位值e：

(start/2⊕(start/2+2/2)⊕(start/2+4/2)⊕⋯⊕(start/2+2(n−1)/2)) * 2 + e

令s=start/2, 得最后的公式：

(s⊕(s+1)⊕(s+2)⊕⋯⊕(s+(n−1))) * 2 + e

### 3.sumXor函数的定义推导

根据sumXor函数的定义：

0⊕1⊕2⊕⋯⊕x

又根据异或运算性质5：

4i⊕(4i+1)⊕(4i+2)⊕(4i+3)=0

既从0开始做异或运算，每四个数字运算的结果都是0，而0异或任何数的结果还是任何数，所以：

当x=4k时，0到x的长度为x+1，既4k+1，每四位运算为0，所以只剩下一位x，既0⊕x=x；

当x=4k+1时，剩下两位，(x−1)⊕x，既4k⊕(4k+1)，两个数仅仅最后一位不同，所以计算结果为1；

当x=4k+2时，剩下三位，(x-2)⊕(x-1)⊕x，既4k⊕(4k+1)⊕(4k+2) => 1⊕(4k+2) => 4k+2+1 => x+1；

当x=4k+3时，剩下0位，既0⊕0=0；

### 4.最后一步怎么理解

(sumXor(s−1)⊕sumXor(s+n−1))×2+e

根据异或运算的相反性：x⊕y⊕y=x

令y表示sumXor(s-1)，既0到s-1的异或结果

令x是我们需要的结果，既s到s+n-1的异或结果

显然x⊕y=sumXor(s+n-1)，所以sumXor(s+n-1)⊕sumXor(s-1)=x成立。
'''

'''
1486. 数组异或操作
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xor-operation-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
