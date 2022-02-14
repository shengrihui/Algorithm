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
const double PI = 3.141592653589793;//����һ�����ɸı�ĳ���ֵPI
const int Po_Size = 50;//��Ⱥ��ģ
const int Ev_Algebra = 500;//��������
const double Ov_Probability = 0.850; //�������,������������ж����������Ƿ���Ҫ����
const double Va_Probability = 0.250;//�������,������������ж���һ�����Ƿ���Ҫ����
const int De_Variable = 2;//�����Ա����ĸ���,���Ҫ���ж�Ԫ��������ֵ��⣬ֱ���޸��Ա�������De_Variable����
const int pow_xp = 7;//��ȷ����λС��
const int length = 28;
//const int length1 = 24;//��ȷ��6λС������24λ�����Ʊ���
//const int length2 = 22;//��ȷ��6λС������23λ�����Ʊ���
//��һ�����ķ�Χ��X_Range(-3.0,12.1) ,�ڶ������ķ�Χ��X_Range(4.1,5.8)
//�������15.1��Ϊ�˾�ȷ��6λС����15.1*pow(10,6)
//pow(2,24)=16777216 > 15.1*pow(10,6
//���ֱ��ѡ�ô��24�����������з�Χ
//���Ա���2ֻ��Ҫ23λ����ȡ����ӽ������ż������Ҫ�����ֲ�ͬ��ֵ
const int Length[De_Variable] = { 28,25 };
const double Better_Proportion = 0.08;//��Ⱥ�ж��ٱ����Ϻõ�ֱ��ѡ����һ��
const double Worse_Proportion = 0.08;//��Ⱥ�ж��ٱ����ϲ��ֱ����̭

class X_Range //�Ա���ȡֵ��Χ�࣬�����ڶ������
{
private:
    double m_Upper;//�������Ͻ�ȡֵ
    double m_Lower;//�������½�ȡֵ
public:
    X_Range(double Lower, double Upper);//���캯��
    double GetUpper()const;//��ȡ��������
    double GetLower()const;//��ȡ��������
    bool inRange(double x)const;//�ж�x�Ƿ��ڷ�Χ��
};
class Individual //���������
{
private:
    double m_Variable[De_Variable];//��ű���x1,x2,x3........
    double m_Fitness;//��Ӧֵ
    double m_ReFitness;//��Ӧֵ����
    double m_SumFitness;//�ۼӸ��ʣ�Ϊ����ת��׼��
public:
    Individual* next;//��Ⱥ������ָ��
    Individual() {}//Ĭ�Ϲ��캯��
    Individual(double* Variable);//���캯��
    double* GetVariable();//��ȡ����ֵ
    double GetFitness()const;//��ȡ��Ӧֵ
    double GetReFitness()const;//��ȡ��Ӧֵ����
    double GetSumFitness()const;//��ȡ�ۼӸ���
    void ChaFitness(const double fitness);//�޸���Ӧֵ
    void ChaReFitness(const double ReFitness);//�޸���Ӧֵ����
    void ChaSumFitness(const double SumFitness);//�޸��ۼӸ���
    void Copy_Foom(Individual* individual);//�������޸�Ϊindividualһ��
};
class Population
{
private:
    Individual* head;
    Individual* tail;
    int m_size;
public:
    Population();
    void push_back(Individual* indiviual);//�ӵ����
    void push_sort(Individual* indiviual);//����ؼ���
    Individual* at(int i);//��λȡ
    Individual* operator [](int i);//ͬat()
    void clear();//���
    void print();//��ӡ��Ⱥ��Ϣ
    int size();//��Ⱥ���ڴ�С
    void CalculaFitness(Individual* indiviual);//����������Ӧֵ
    void CalculaReFitness();//����������Ӧֵ����
    void CalculaSumFitness();//�����ۼӸ������
    void shuffle();//����
    Individual* Head();//���ͷָ��
};

void Initialize();//�����ʼ����Ⱥ���õ���һ������
void seclect();//��Ⱥѡ��
void crossing();//�ӽ�
void variating();//����
double Srand();//�������0��1�����С��
void genetic_algorithm();//�Ŵ��㷨
