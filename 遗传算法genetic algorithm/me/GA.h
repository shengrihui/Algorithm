#pragma once
#include <random>
#include <vector>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <bitset>
#include <iomanip>
using namespace std;
const double PI = 3.141592653589793;//定义一个不可改变的常量值PI
const int Po_Size = 50;//种群规模
const int Ev_Algebra = 500;//进化代数
const double Ov_Probability = 0.850; //交叉概率,交叉概率用于判断两两个体是否需要交叉
const double Va_Probability = 0.250;//变异概率,变异概率用于判断任一个体是否需要变异
const int De_Variable = 2;//函数自变量的个数,如果要进行多元函数的最值求解，直接修改自变量数个De_Variable即可
const int pow_xp = 7;//精确到几位小数
const int length = 28;
//const int length1 = 24;//精确到6位小数，用24位二进制编码
//const int length2 = 22;//精确到6位小数，用23位二进制编码
//第一个数的范围是X_Range(-3.0,12.1) ,第二个数的范围是X_Range(4.1,5.8)
//最大跨度是15.1，为了精确到6位小数，15.1*pow(10,6)
//pow(2,24)=16777216 > 15.1*pow(10,6
//因此直接选用大的24，包括下所有范围
//但自变量2只需要23位，在取随机杂交点的是偶，还是要有两种不同的值
const int Length[De_Variable] = { 28,25 };
const double Better_Proportion = 0.08;//种群中多少比例较好的直接选择到下一轮
const double Worse_Proportion = 0.08;//种群中多少比例较差的直接淘汰

class X_Range //自变量取值范围类，适用于多个变量
{
private:
    double m_Upper;//变量的上界取值
    double m_Lower;//变量的下界取值
public:
    X_Range(double Lower, double Upper);//构造函数
    double GetUpper()const;//获取变量上限
    double GetLower()const;//获取变量下限
    bool inRange(double x)const;//判断x是否在范围内
};
class Individual //定义个体类
{
private:
    double m_Variable[De_Variable];//存放变量x1,x2,x3........
    double m_Fitness;//适应值
    double m_ReFitness;//适应值概率
    double m_SumFitness;//累加概率，为轮盘转做准备
public:
    Individual* next;//种群单链表指针
    Individual() {}//默认构造函数
    Individual(double* Variable);//构造函数
    double* GetVariable();//获取变量值
    double GetFitness()const;//获取适应值
    double GetReFitness()const;//获取适应值概率
    double GetSumFitness()const;//获取累加概率
    void ChaFitness(const double fitness);//修改适应值
    void ChaReFitness(const double ReFitness);//修改适应值概率
    void ChaSumFitness(const double SumFitness);//修改累加概率
    void Copy_Foom(Individual* individual);//将内容修改为individual一样
};
class Population
{
private:
    Individual* head;
    Individual* tail;
    int m_size;
public:
    Population();
    void push_back(Individual* indiviual);//加到最后
    void push_sort(Individual* indiviual);//有序地加入
    Individual* at(int i);//按位取
    Individual* operator [](int i);//同at()
    void clear();//清空
    void print();//打印种群信息
    int size();//种群现在大小
    void CalculaFitness(Individual* indiviual);//计算个体的适应值
    void CalculaReFitness();//计算个体的适应值概率
    void CalculaSumFitness();//计算累加个体概率
    void shuffle();//打乱
    Individual* Head();//获得头指针
};

void Initialize();//随机初始化种群，得到第一代个体
void seclect();//种群选择
void crossing();//杂交
void variating();//变异
double Srand();//随机产生0到1的随机小数
void genetic_algorithm();//遗传算法
