
#include <stdio.h>
#include <stdlib.h>

int* decode(int* encoded, int encodedSize, int* returnSize) {
	int total = 0; //total前n个正整数异或的结果，
	int odd = 0;  //原数组perm除第一个数后异或的结果，也就是encoded全部数的结果
	int n = encodedSize + 1;  //perm长度
	int* perm = (int*)malloc(sizeof(int) * n);  //分配n个int的存储空间，返回第一个的地址
	int i;

	for (i = 1; i <= n; i++)
		total ^= i;
	for (i = 1; i < encodedSize; i+=2)
		odd ^= encoded[i];

	perm[0] = total ^ odd;
	//printf("%d \n", perm[0]);
	for (i = 0; i < encodedSize ; i++)
	{
		perm[i + 1] = perm[i] ^ encoded[i];
		//printf("%d ", perm[i + 1]);
	}
	*returnSize = n;
	return perm;
}

int main()
{
	int a[] = { 3,1 };
	int b[] = { 6,5,4,6 };
	int sza = sizeof(a) / 4;
	int szb = sizeof(b) / 4;
	int i;
	int* perm;
	int sz = 0;
	perm = decode(a, sza, &sz);
	for (i = 0; i < sz; i++)
	{
		printf("%d ", *(perm + i));
	}
	printf("\n\n");
	perm = decode(b, szb, &sz);
	for (i = 0; i < sz; i++)
	{
		printf("%d ", *(perm + i));
	}return 0;
}


/*
1734. 解码异或后的排列
给你一个整数数组?perm?，它是前?n?个正整数的排列，且?n?是个 奇数?。

它被加密成另一个长度为 n - 1?的整数数组?encoded?，满足?encoded[i] = perm[i] XOR perm[i + 1]?。比方说，如果?perm = [1,3,2]?，那么?encoded = [2,1]?。

给你?encoded?数组，请你返回原始数组?perm?。题目保证答案存在且唯一。

?

示例 1：

输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
示例 2：

输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]
?

提示：

3 <= n <?105
n?是奇数。
encoded.length == n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/