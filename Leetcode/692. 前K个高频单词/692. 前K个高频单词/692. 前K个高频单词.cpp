#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pprint(char** st, int* sz_w, int sz);
//int mylen(char ch[]);
int company2words(char* w1, char* w2, int k);
void print_word(char* w);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {
    int i, j, l;    //临时变量
    char** ret = (char**)calloc(k, 4);//返回的结果
    int* word_index = (int*)calloc(wordsSize, sizeof(int));//相当于每个单词的的index
    char** word_set = NULL;//单词集合
    int* word_count = NULL;//不同的单词出现的次数
    //set,count的下标就是单词的index
    int m = 0, temp;
    char* p = NULL;
    int left, right;


    //****************************************
    //建立单词的index，
    //i循环所有单词，如果第i个单词已经设了index则continue
        // j从i+1开始循环，如果第j个和第i个两个单词一样，就把第j个单词的index设为和第i个一样为l
    //结束后可以说明一共有l个单词
    l = 0;
    for (i = 0; i < wordsSize; i++)
    {
        if (word_index[i] != 0)
            continue;
        l++;
        word_index[i] = l;
        for (j = i + 1; j < wordsSize; j++)
        {
            if (word_index[j] != 0)
                continue;
            if (strlen(words[i]) == strlen(words[j]))
            {
                //printf("%d %d ", i, j);
                //print_word(words[i]);
                //print_word(words[j]);
                word_index[j] = company2words(words[i], words[j], l);
            }
        }
    }

    //*******************************************
    //单词index技术，并加入到set里
    word_count = (int*)calloc(l, 4);
    word_set = (char**)calloc(l, 4);
    for (i = 0; i < wordsSize; i++)
    {
        word_count[word_index[i] - 1] += 1;
        word_set[word_index[i] - 1] = words[i];
    }

    //*******************************************
    //对count进行选择排序
    //同时对相下标的set进行排序
    //得到按次数排好的set
    for (i = 0; i < l - 1; i++)
    {
        //int m = i, temp;
        m = i;
        //char* p = NULL;
        for (j = i + 1; j < l; j++)
        {
            if (word_count[j] > word_count[m])
                m = j;
        }
        if (m != i)
        {
            temp = word_count[i]; word_count[i] = word_count[m]; word_count[m] = temp;
            p = word_set[i]; word_set[i] = word_set[m]; word_set[m] = p;
        }
    }

    //***************************************
    //用left和right划出相同次数的区间，并对区间内的单词按字母顺序排序
    //int left, right;
    for (left = 0, right = 1; ;)
    {
        //right和left一样，right++然后continue，直到不一样为止
        //同时保证right不越界
        if (word_count[right] == word_count[left])
        {
            printf("%d %d %d\n", left, right, l);
            right++;
            if (right == l)
                right--;
            else
                continue;
        }
        for (i = left; i < right - 1; i++)
        {
            for (j = right - 1; j > i; j--)
            {
                printf("\t%d %d %d\n", i, j, l);
                if (company2words(word_set[j], word_set[j - 1], -2) == -1)
                {
                    char* p = NULL;
                    p = word_set[j]; word_set[j] = word_set[j - 1]; word_set[j - 1] = p;
                }
            }
        }
        left = right;
        right = left + 1;
        if (right == l)break;
    }


    //*************************************
    //生成结果
    m = 0;
    while (m < k)
    {
        ret[m] = word_set[m];
        returnSize[m] = strlen(word_set[m]);
        m++;
    }



    //************************************
   //测试用
   /* for (i = 0; i < wordsSize; i++)
        printf("%d ", word_index[i]);
    printf("\n");
    for (i = 0; i < l; i++)
    {
        printf("%d ", word_count[i]);
        print_word(word_set[i]);
        printf("\n");
    }*/

    return ret;

}


//对两个单词进行比较
//w1大返回0，w2大返回-1
//如果两个相等返回k，在建立单词index的时候，k是index，只是比较大小的时候返回-2
int company2words(char* w1, char* w2, int k)
{
    while (*w1 != '\0')
    {
        if (*w1 > *w2)
            return 0;
        else if (*w1 < *w2)
            return -1;
        w1++; w2++;
    }
    return k;

}


//打印一个单词
void print_word(char* w)
{
    while (*w != '\0')
    {
        printf("%c", *w);
        w++;
    }
}

//打印二级指针指向的所有单词
//sz_w数组里存每个单词的长度，sz一共有多单词（st长度）
void pprint(char** st, int* sz_w, int sz)
{
    int i, j;
    for (i = 0; i < sz; i++)
    {
        for (j = 0; j < sz_w[i]; j++)
            printf("%c", st[i][j]);
        printf(" ");
    }
    printf("\n");

}


//int mylen(char ch[])
//{
//    int sz = 0;
//    char* end = ch;
//    while (*end != '\0')
//    {
//        sz++;
//        end++;
//    }
//    return end - ch;
//
//}


int main()
{
    int i;
    char w1[] = "i", w2[] = "love", w3[] = "leetcode", w4[] = "i", w5[] = "love", w6[] = "coding";
    char* ex1p[] = { w1,w2,w3,w4,w5,w6 };
    int sz_ex1[] = { 1,4,8,1,4,7 };
    char** ex1pp = ex1p;
    int  k1 = 2;
    int* retsz1 = (int*)calloc(k1, 4);
    char** ret1 = NULL;


    char ww1[] = "the", ww2[] = "day", ww3[] = "is", ww4[] = "sunny", ww5[] = "the";
    char ww6[] = "the", ww7[] = "the", ww8[] = "sunny", ww9[] = "is", ww10[] = "is";
    char ww11[] = "sunny", ww12[] = "day", ww13[] = "day";
    //char* ex2p[] = { ww1,ww2,ww3,ww4,ww5,ww6,ww7,ww8,ww9,ww10 };
    char* ex2p[] = { ww1,ww2,ww3,ww4,ww5,ww6,ww7,ww8,ww9,ww10,ww11,ww12,ww13 };
    char** ex2pp = ex2p;
    int sz_ex2[13] = { 0 };
    for (i = 0; i < 13; i++)
    {
        sz_ex2[i] = strlen(ex2p[i]);;
    }
    int  k2 = 4;
    int* retsz2 = (int*)calloc(k2, 4);

    pprint(ex1pp, sz_ex1, 6);
    ret1 = topKFrequent(ex1pp, 6, k1, retsz1);

    pprint(ret1, retsz1, k1);
    printf("\n\n\n\n");


    pprint(ex2pp, sz_ex2, 13);
    char** ret2 = topKFrequent(ex2pp, 13, k2, retsz2);
    pprint(ret2, retsz2, k2);

    return  0;
}




/*
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
 

扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

*/