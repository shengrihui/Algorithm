////https://www.cnblogs.com/suchang/p/10550181.html
////求多元函数 f(x1,x2)=21.5+x1*sin(4pi*x1)+x2sin(20pi*x2)
//#include<random>
//#include<vector>
//#include<iostream>
//#include<cmath>
//#include<ctime>
//#include<cstdlib>
//#include<bitset>
//#include<iomanip>
//using namespace std;
//const double PI = 3.141592653589793;//定义一个不可改变的常量值PI
//const int Po_Size = 50;//种群规模 population
//const int Ev_Algebra = 500;//进化代数 evolution algebra
//const double Ov_Probability = 0.850;//交叉概率，交叉概率用于判断两辆个体是否需要交叉 overlapping
//const double Va_Probability = 0.050;//变异概率，变异概率用于判断任一个体是否需要变异 variation
//const int De_Variable = 2;//函数自变量的个数
//const int length1 = 24;//精确到6位小数，用24位二进制编码
//const int length2 = 23;//精确到6位小数，用23位二进制编码
////2的24次方=16777216，2的23次方=8388608
////精确到6位小数，整数部分一位或二位
//
//class X_Range//自变量取值范围类，适用于多个变量
//{
//private:
//	double m_Upper;//自变量上界取值
//	double m_Lower;//自变量下界取值
//public:
//	X_Range(double Lower, double Upper);
//	double GetUpper()const;
//	double GetLower()const;
//};
//class Individual//定义个体类
//{
//private:
//	double m_Variable[De_Variable];//存放变量x1,x2,x3......(这道题就是x1,x2)
//	double m_Fitness;//适应值
//	double m_ReFitness;//适应值概率
//	double m_SumFitness;//累加概率，为轮盘转做准备
//public:
//	Individual() {};//默认构造函数
//	Individual(double* Variable);//构造函数
//	double* GetVariable();//获取变量值
//	double GetFitness()const;//获取适应值
//	double GetReFitness()const;//获取适应值概率
//	double GetSumFitness()const;//获取累加概率
//	void ChaFitness(const double Fitness);//修改适应值
//	void ChaReFitness(const double ReFitness);//修改适应值概率
//	void ChaSumFitness(const double SumFitness);//修改累加概率
//};
//
//void Initialize();//初始化种群，得到第一代个体
//void CaculaFitness();//计算个体适应值
//void CaculaReFitness();//计算个体适应值概率
//void CalculaSumFitness();//计算个体累加概率
//void seclect();//选择
//void crossing();//杂交
//void variating();//变异
//double Scand();//产生0到1的小数
//void genetic_algorithm();//遗传算法
//
////自变量取值范围向量和种群向量
//const X_Range Range[De_Variable] = { X_Range(-3.0,12.1) ,X_Range(4.1,5.8) };//自变量（基因）x1,x2的取值范围
//vector<Individual> nowpopulation;//P(t)种群
//vector<Individual> midpopulation;//中间种群，存放轮盘转后选择的优秀个体
//vector<Individual> nextpopulation;//P(t+1)种群
//
////X_Range类实现
//X_Range::X_Range(double Lower, double Upper) :m_Lower(Lower), m_Upper(Upper)
//{}
//double X_Range::GetUpper()const
//{
//	return m_Upper;
//}
//double X_Range::GetLower()const
//{
//	return m_Lower;
//}
//
////Individual类实现
//Individual::Individual(double* Variable)//构造函数
//{
//	for (int i = 0; i < De_Variable; i++)//循环自变量逐个赋值
//	{
//		if (Variable[i] >= Range[i].GetLower() && Variable[i] <= Range[i].GetUpper())//对自变量的取值进行进行判断
//			m_Variable[i] = Variable[i];
//		else//如果不符合要求，则发出出错警告，并返回
//		{
//			cerr << "自变量取值出错" << endl;
//			exit(1);
//		}
//	}
//	//将适应值等初始化为0
//	m_Fitness = 0;
//	m_ReFitness = 0;
//	m_SumFitness = 0;
//}
//double* Individual::GetVariable()//获取变量值
//{
//	return m_Variable;
//}
//double Individual::GetFitness()const//获取适应值
//{
//	return m_Fitness;
//}
//double Individual::GetReFitness()const//获取适应值概率
//{
//	return m_ReFitness;
//}
//double Individual::GetSumFitness()const//获取累加概率
//{
//	return m_SumFitness;
//}
//void Individual::ChaFitness(const double Fitness)//修改适应值
//{
//	m_Fitness = Fitness;
//}
//void Individual::ChaReFitness(const double ReFitness)//修改适应值概率
//{
//	m_ReFitness = ReFitness;
//}
//void Individual::ChaSumFitness(const double SumFitness)//修改累加概率
//{
//	m_SumFitness = SumFitness;
//}
//
//
//void Initialize()//初始化种群，得到第一代个体
//{
//	double X[Po_Size][De_Variable];//
//	for (int j = 0; j < De_Variable; j++)
//	{
//		//循环结束后，所有随机值就保存在了X矩阵中
//		//因为x1,x2...的范围(Range[j])不同，所以，j循环在外边
//		default_random_engine e(time(0));//引擎，生成随机序列
//		uniform_real_distribution<double> u(Range[j].GetLower(), Range[j].GetUpper());//分布
//		for (int i = 0; i < Po_Size; i++)
//		{
//			X[i][j] = u(e);
//		}
//	}
//
//	//生成对象（染色体），并加入到初始种群中
//	for (int i = 0; i < Po_Size; i++)
//	{
//		double variable[De_Variable];
//		for (int j = 0; j < De_Variable; j++)
//		{
//			variable[j] = X[i][j];
//		}
//		Individual individual(variable);//生成对象（染色体）
//		nowpopulation.push_back(individual);//加入到初始种群中
//	}
//}
//void CaculaFitness()//计算个体适应值
//{
//	double fitness;//临时变量
//	double X[De_Variable];//临时变量
//	//f(x1,x2)=21.5+x1*sin(4pi*x1)+x2sin(20pi*x2)
//	for (int i = 0; i < Po_Size; i++)
//	{
//		for (int j = 0; j < De_Variable; j++)
//			X[j] = nowpopulation.at(i).GetVariable()[j];
//		fitness = 21.5 + X[0] * sin(4 * PI * X[0]) + X[2] * sin(20 * PI * X[1]);//计算适应值
//		nowpopulation.at(i).ChaFitness(fitness);//修改该对象（染色体）的适应值
//	}
//}
//void CaculaReFitness()//计算个体适应值概率
//{
//	double sum = 0;
//	double temp = 0;
//	for (int i = 0; i < Po_Size; i++)
//		sum += nowpopulation.at(i).GetFitness();
//	for (int i = 0; i < Po_Size; i++)
//	{
//		temp = nowpopulation.at(i).GetFitness() / sum;
//		nowpopulation.at(i).ChaReFitness(temp);
//	}
//}
//void CalculaSumFitness()//计算个体累加概率
//{
//	double summation = 0;
//	for (int i = 0; i < Po_Size; i++)
//	{
//		summation += nowpopulation.at(i).GetReFitness();
//		nowpopulation.at(i).ChaSumFitness(summation);
//	}
//}
//void seclect()//选择
//{
//	default_random_engine e(time(0));//引擎
//	uniform_real_distribution<double> u(0.0, 1.0);//分布
//	double array[Po_Size];
//	for (int i = 0; i < Po_Size; i++)
//		array[i] = u(e);
//	for (int j = 0; j < Po_Size; j++)
//	{
//		for (int i = 1; i < Po_Size; i++)
//		{
//			//这个有问题
//			if (array[j] < nowpopulation[i - 1].GetSumFitness())//我怀疑这个主要就是处理第0个的情况，就是累加概率在0到nowpupulation[0].GetSumFitness()
//			{
//				midpopulation.push_back(nowpopulation.at(i - 1));
//				//cout << "i-1:" << i - 1 << endl;
//			}
//			if (array[j] >= nowpopulation[i - 1].GetSumFitness() && array[j] <= nowpopulation[i].GetSumFitness())
//			{
//				midpopulation.push_back(nowpopulation.at(i));
//				//cout <<"i"<< i << endl;
//			}
//		}
//	}
//	nowpopulation.clear();
//}
//void crossing()//杂交
//{
//	int num = 0;//记录次数
//	double corss = 0.0;//保存随机产生的概率值
//	srand((unsigned)time(NULL));//根据系统时间设置随机数种子,设置一次随机种子就行
//	double array1[De_Variable], array2[De_Variable];//临时存储父亲和母亲的变量值
//	{
//		//判断双亲是否需要杂交，随机生成一个0到1的小数，如果这个数大于杂交概率，则放弃杂交，直接遗传给下一代，否则，对父母体进行杂交
//		corss = Scand();
//		if (corss <= Ov_Probability)//如果corss小于等于杂交概率Ov_Probability就进行单点杂交
//		{
//			//首先寻找对应下标的个体并且保存
//			for (int i = 0; i < De_Variable; i++)
//			{
//				array1[i] = midpopulation.at(num).GetVariable()[i];//父亲的自变量
//				array2[i] = midpopulation.at(num + 1).GetVariable()[i];//母亲自变量
//			}
//			int localx1, localx2;//记录基因交叉点的位置
//			int corssx1[length1], corssx2[length2];//作为交换基因的数组
//			double newx1[2], newx2[2];//分别用来保存基因交换后所对应自变量值
//			bool p1 = true, p2 = true;
//			//然后对双亲变量进行编码并且进行单点杂交
//			for (int j = 0; j < De_Variable; j++)//array1的x1编码之后和array2的x1编码后进行单点杂交，以此类推
//			{
//				if (j == 0)//x1进行编码并且杂交
//				{
//					bitset<length1> array1b1((array1[j] + 3.0) * pow(10, 6));//加上3.0形成一个unsigaed数之后在进行母体1的x1编码
//					bitset<length1> array2b1((array2[j] + 3.0) * pow(10, 6));//加上3.0形成一个unsigaed数之后在进行母体2的x1编码        
//					//现在随机生成0到length1-1的数，确定交叉点的位置
//					localx1 = rand() % length1;
//					//现在进行单点交叉，交换双亲localx1后面的基因
//					for (int i = 0; i < localx1; i++)
//						corssx1[i] = array1b1[i];
//					for (int k = 0; k < localx1; k++)
//						array1b1[k] = array2b1[k];
//					for (int s = 0; s < localx1; s++)
//						array2b1[s] = corssx1[s];
//					//新值保存在newx1数组中，x1基因完成单点杂交操作
//					newx1[0] = double(array1b1.to_ullong()) / pow(10, 6) - 3.0;
//					newx2[0] = double(array2b1.to_ullong()) / pow(10, 6) - 3.0;
//					//对新产生的值进行判断，判断是否超出范围，如果超出范围则不杂交
//					if (newx1[0]< Range[0].GetLower() || newx1[0]>Range[0].GetUpper() || newx2[0]<Range[0].GetLower() || newx2[0]>Range[0].GetUpper())
//					{
//						p1 = false;
//						break;
//					}
//				}
//				if (j == 1)//x2进行编码并且杂交
//				{
//					bitset<length2> array1b2((array1[j]) * pow(10, 6));//母体1的x2编码
//					bitset<length2> array2b2((array2[j]) * pow(10, 6));//母体2的x2编码
//								//现在随机生成0到length2-1的数，确定交叉点的位置
//					localx2 = rand() % length2;
//					//现在进行单点交叉，交换双亲localx2后面的基因
//					for (int i = 0; i < localx2; i++)
//						corssx2[i] = array1b2[i];
//					for (int k = 0; k < localx2; k++)
//						array1b2[k] = array2b2[k];
//					for (int s = 0; s < localx2; s++)
//						array2b2[s] = corssx2[s];
//					//新值保存在newx2数组中，x2基因完成单点杂交操作
//					newx1[1] = double(array1b2.to_ullong()) / pow(10, 6);
//					newx2[1] = double(array2b2.to_ullong()) / pow(10, 6);
//					//对新产生的值进行判断，判断是否超出范围，如果超出范围则不杂交
//					if (newx1[1]< Range[1].GetLower() || newx1[1]>Range[1].GetUpper() || newx2[1]<Range[1].GetLower() || newx2[1]>Range[1].GetUpper())
//					{
//						p2 = false;
//						break;
//					}
//				}
//			}
//			if (p1 == true && p2 == true)
//			{
//				Individual newchiled1(newx1);
//				Individual newchiled2(newx2);
//				nextpopulation.push_back(newchiled1);
//				nextpopulation.push_back(newchiled2);
//			}
//			else//将原来的个体遗传给下一代
//			{
//				nextpopulation.push_back(midpopulation.at(num));
//				nextpopulation.push_back(midpopulation.at(num + 1));
//			}
//		}
//		else//否则直接遗传给下一代nextpopulation
//		{
//			nextpopulation.push_back(midpopulation.at(num));//生成一个新的个体并且加入到nextpopulation中
//			nextpopulation.push_back(midpopulation.at(num + 1));
//		}
//		num += 2;
//	}
//	midpopulation.clear();//清空midpopulation
//}
//void variating()//变异
//{
//	int num = 0;
//	cout << nextpopulation.size();
//	while (num < Po_Size)
//	{
//		double variation = Scand();//随机产生一个0到1的小数，用于判断是否进行变异
//		if (variation <= Va_Probability)//如果variation小于变异系数，则需要进行变异
//		{
//			double x[2];
//			bool p = true;
//			int x1local, x2local;
//			x[0] = nextpopulation.at(num).GetVariable()[0];
//			x[1] = nextpopulation.at(num).GetVariable()[1];
//			bitset<length1> array1((x[0] + 3.0) * pow(10, 6));//x1编码
//			bitset<length2> array2(x[1] * pow(10, 6));//x2编码
//			x1local = rand() % length1;//array1该位取反
//			x2local = rand() % length2;//array2该位取反
//			array1.flip(x1local);//改变array1 x1local位的状态
//			array2.flip(x2local);//改变array2 x2local位的状态
//			x[0] = double(array1.to_ullong()) / pow(10, 6) - 3.0;
//			x[1] = double(array2.to_ullong()) / pow(10, 6);
//			//判断是否符合条件
//			if (x[0]< Range[0].GetLower() || x[0]>Range[0].GetUpper() || x[1]<Range[1].GetLower() || x[1]>Range[1].GetUpper())
//				p = false;
//			if (!p)
//				nowpopulation.push_back(nextpopulation.at(num));
//			if (p)
//			{
//				Individual newchiled(x);
//				nowpopulation.push_back(newchiled);
//			}
//		}
//		else
//		{
//			nowpopulation.push_back(nextpopulation.at(num));
//			cout << num << endl;
//		}
//		num++;
//	}
//	nextpopulation.clear();//清空nextpopulation
//}
//double Scand()//产生0到1的小数
//{
//	int N = rand() % 999;
//	return (double)N / 1000.0;
//}
//void genetic_algorithm()
//{
//	Initialize();//初始化种群,随机生成第一代个体
//	 //进化500代
//	for (int i = 0; i < Ev_Algebra; i++)
//	{
//		CaculaFitness();//适应度计算
//		CaculaReFitness();//适应度概率计算
//		CalculaSumFitness();//计算累加个体概率
//		seclect();//选择
//		crossing();//杂交
//		variating();//变异
//	}
//	CaculaFitness();//适应度计算
//	double maxfitness = nowpopulation.at(0).GetFitness();
//	int maxid = 0;
//	int k;
//	for (k = 0; k < Po_Size; k++)
//	{
//		if (maxfitness < nowpopulation.at(k).GetFitness())
//		{
//			maxfitness = nowpopulation.at(k).GetFitness();
//			maxid = k;
//		}
//	}
//	//进化500代之后输出
//	cout << "x1" << setw(10) << "x2" << setw(15) << "Fitness" << endl;
//	for (int j = 0; j < Po_Size; j++)
//		cout << nowpopulation.at(j).GetVariable()[0] << setw(10) << nowpopulation.at(j).GetVariable()[1] << setw(10) << nowpopulation.at(j).GetFitness() << endl;
//	cout << "x1=" << nowpopulation.at(maxid).GetVariable()[0] << " ，" << "x2=" << nowpopulation.at(maxid).GetVariable()[1] << "时取得最大值：" << maxfitness << endl;
//}
//
//
////int main()
////{
////	genetic_algorithm();
////
////	/*for (Individual i : midpopulation)
////		cout << i.GetVariable()[0] << "  "
////		<< i.GetVariable()[1] << "  "
////		<< i.GetFitness() << "  "
////		<< i.GetReFitness() << "  "
////		<< i.GetSumFitness() << endl;*/
////	return 0;
////}