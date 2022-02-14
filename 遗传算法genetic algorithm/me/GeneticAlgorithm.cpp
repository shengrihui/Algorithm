#include "GA.h"
const X_Range Range[De_Variable] = { X_Range(-3.0,12.1) ,X_Range(4.1,5.8) };//自变量（或者基因）x1,x2的取值范围
//vector<Individual> nowpopulation;//P(t)种群
//vector<Individual> midpopulation;//中间种群，存放轮盘选择后的优秀个体
//vector<Individual> nextpopulation;//P(t+1)种群
Population nowpopulation;
Population midpopulation;
Population nextpopulation;

//X_Range实现
X_Range::X_Range(double Lower, double Upper) :m_Lower(Lower), m_Upper(Upper)//构造函数
{}
double X_Range::GetUpper()const//获取变量上限
{
	return m_Upper;
}
double X_Range::GetLower()const//获取变量下限
{
	return m_Lower;
}
bool X_Range::inRange(double x)const//判断x是否在范围内
{
	if (x >= m_Lower && x <= m_Upper)
		return true;
	else
		return false;
}

//Individual实现
Individual::Individual(double* Variable)//构造函数
{
	for (int i = 0; i < De_Variable; i++)
	{
		if(Range[i].inRange( Variable[i]))
		{
			m_Variable[i] = Variable[i];
		}
		else
		{
			cerr << "自变量取值有错误" << endl;
			exit(1);
		}
	}
	nowpopulation.CalculaFitness(this);
	m_ReFitness = 0;
	m_SumFitness = 0;
	next = NULL;

}
double* Individual::GetVariable()//获取变量值
{
	return m_Variable;
}
double Individual::GetFitness()const//获取适应值
{
	return m_Fitness;
}
double Individual::GetReFitness()const//获取适应值概率
{
	return m_ReFitness;
}
double Individual::GetSumFitness()const//获取累加概率
{
	return m_SumFitness;
}
void Individual::ChaFitness(const double fitness)//修改适应值
{
	m_Fitness = fitness;
}
void Individual::ChaReFitness(const double ReFitness)//修改适应值概率
{
	m_ReFitness = ReFitness;
}
void Individual::ChaSumFitness(const double SumFitness)//修改累加概率
{
	m_SumFitness = SumFitness;
}
void Individual::Copy_Foom(Individual* individual)//将内容修改为individual一样
{
	m_Fitness = individual->GetFitness();
	m_ReFitness = individual->GetReFitness();
	m_SumFitness = individual->GetSumFitness();
	for (int i = 0; i < De_Variable; i++)
		m_Variable[i] = individual->GetVariable()[i];
}

//Population实现
Population::Population()
{
	head = new Individual;
	tail = new Individual;
	head->next = NULL;
	tail = head;
	m_size = 0;
}
void Population::push_back(Individual* indiviual)//加到最后
{
	indiviual->next = tail->next;
	tail->next = indiviual;
	tail = indiviual;
	m_size++;
}
void Population::push_sort(Individual* indiviual)//有序地加入
{
	Individual* p = head;
	while (p != NULL && p->next!=NULL)
	{
		if (indiviual->GetFitness() > p->next->GetFitness())
		{
			indiviual->next = p->next;
			p->next = indiviual;
			m_size++;
			return;
		}
		p = p->next;
	}
	if (p == NULL || p->next == NULL)
		Population::push_back(indiviual);
}
Individual* Population::at(int i)//按位取
{
	if (i < 0 || i >= m_size)
	{
		cerr << "下标越界！" << endl;
		exit(1);
	}
	int count = 0;
	Individual* q = head->next;
	while (count < i)
	{
		q = q->next;
		count++;
	}
	return q;
}
Individual* Population::operator [](int i)//同at()
{
	return Population::at(i);
}
void Population::clear()//清空
{
	Individual* q;
	tail = head->next;
	while (tail != NULL)
	{
		q = tail;
		tail = q->next;
		delete q;
		if (q != NULL)
			q = NULL;
	}
	tail = head;
	head->next = NULL;
	m_size = 0;
}
void Population::print()//打印种群信息
{
	Individual* p = head -> next;
	int num = 0;
	int w = 12;
	while (p != NULL)
	{
		cout << ++num << setw(w)
			<< p->GetVariable()[0] << setw(w)
			<< p->GetVariable()[1] << setw(w)
			<< p->GetFitness() << setw(w)
			<< p->GetReFitness() << setw(w)
			<< p->GetSumFitness() << endl;
		p = p->next;
	}
	cout << "size=" << m_size << endl;
}
int Population::size()//种群现在大小
{
	return m_size;
}
void Population::CalculaFitness(Individual*individual)//计算个体的适应值
{
	double x1 = individual->GetVariable()[0];
	double x2 = individual->GetVariable()[1];
	double fitness = 21.5 + x1 * sin(4 * PI * x1) + x2 * sin(20 * PI * x2);
	individual->ChaFitness(fitness);
}
void Population::CalculaReFitness()//计算个体的适应值概率
{
	double sum = 0;
	Individual* p = head->next;
	while (p != NULL)
	{
		sum += p->GetFitness();
		p = p->next;
	}
	p = head->next;
	while (p != NULL)
	{
		double refitness = p->GetFitness() / sum;
		p->ChaReFitness(refitness);
		p = p->next;
	}

}
void Population::CalculaSumFitness()//计算累加个体概率
{
	double sum = 0.0;
	Individual* p = head->next;
	while (p != NULL)
	{
		sum += p->GetReFitness();
		p->ChaSumFitness(sum);
		p = p->next;
	}
}
void Population::shuffle()//打乱
{
	Individual* temp = new Individual;
	for (int i = 0; i < 1000; i++)
	{
		int a = rand() % Po_Size;
		int b = rand() % Po_Size;
		if (a == b)continue;
		temp->Copy_Foom(this->at(a));
		this->at(a)->Copy_Foom(this->at(b));
		this->at(b)->Copy_Foom(temp);
	}
}
Individual* Population::Head()//获得头指针
{
	return head;
}

void Initialize()//随机初始化种群，得到第一代个体
{
	double X[Po_Size][De_Variable];
	for (int j = 0; j < De_Variable; j++)
	{
		default_random_engine e(time(0));//引擎，生成随机序列
		uniform_real_distribution<double> u(Range[j].GetLower(), Range[j].GetUpper());//分布
		for (int i = 0; i < Po_Size; i++)
			X[i][j] = u(e);
	}
	for (int i = 0; i < Po_Size; i++)
	{
		Individual* individual = new Individual(X[i]);
		nowpopulation.push_sort(individual);
	}
	nowpopulation.CalculaReFitness();
	nowpopulation.CalculaSumFitness();
}
void seclect()//种群选择
{
	//直接淘汰较差的几个
	int worse_index = Po_Size * (1 - Worse_Proportion);
	for (int i = worse_index; i < Po_Size; i++)
	{
		nowpopulation[i]->ChaFitness(0.0);
	}
	nowpopulation.CalculaReFitness();
	nowpopulation.CalculaSumFitness();

	//将较好的直接弄到待杂交种群中
	for (int i = 0; i < Po_Size * Better_Proportion; i++)
	{
		Individual* individual = new Individual;
		individual->Copy_Foom(nowpopulation[i]);
		midpopulation.push_sort(individual);
	}

	//轮盘转
	default_random_engine e(time(0));//引擎，生成随机序列
	uniform_real_distribution<double> u(0.0,1.0);//分布
	Individual* p;
	for (int i = 0; i < Po_Size * (1 - Better_Proportion); i++)
	{
		double temp = u(e);
		p = nowpopulation[0];
		while (temp > p->GetSumFitness())
		{
			p = p->next;
		}
		Individual* individual = new Individual;
		individual->Copy_Foom(p);
		midpopulation.push_sort(individual);
	}
	nowpopulation.clear();
}
void crossing()//杂交
{
	midpopulation.shuffle();
	double cross = 0.0;
	int num = 0;
	while (num < Po_Size)
	{
		cross = Srand();
		//取出midpopulation的前两个
		Individual* father = midpopulation[0];
		Individual* mother = midpopulation[1];
		midpopulation.Head()->next = midpopulation[2];
		if (cross < Ov_Probability)//在杂交概率内进行杂交
		{
			//杂交前的基因
			double* father_variable = father->GetVariable();
			double* mother_variable = mother->GetVariable();
			//杂交后的结果
			double father_new[De_Variable] = { 0 };
			double mother_new[De_Variable] = { 0 };
			bool flag = false;//是否杂交成功
			for (int i = 0; i < De_Variable; i++)//循环不用的变量（基因）
			{
				//取出第i个基因（自变量x)的值
				double f_v_x = father_variable[i];
				double m_v_x = mother_variable[i];
				//编码 
				// x->y 先对x进行转换
				// y=(x+3.0)*pow(10,6)
				// y=(x-Range[i].GetLower())*pow(10,6)
				bitset<length> f_v_b((f_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				bitset<length> m_v_b((m_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				//产生杂交点
				int local = rand() % Length[i];
				//杂交
				bool temp;
				for (int k = length - 1; k > local; k--)
				{
					temp = f_v_b[k];
					f_v_b[k] = m_v_b[k];
					m_v_b[k] = temp;
				}
				//解码
				double f_new = double(f_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				double m_new = double(m_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				//对杂交后的值进行判断
				if ((Range[i]).inRange(f_new) && (Range[i]).inRange(m_new))
				{
					father_new[i] = f_new;
					mother_new[i] = m_new;
					flag = true;
				}
				else
				{
					flag = false;
					break;
				}
			}
			//如果杂交成功
			if (flag)
			{
				for (int i = 0; i < De_Variable; i++)
				{
					father_variable[i] = father_new[i];
					mother_variable[i] = mother_new[i];
				}
				//计算修改适应值
				nextpopulation.CalculaFitness(father);
				nextpopulation.CalculaFitness(mother);
			}
		}
		//不在杂交概率内，直接加到nextpopulation
		//杂交不成功，不做改变加到nextpopulation
		//杂交成功，改变了基因加到nextpopulation
		nextpopulation.push_sort(father);
		nextpopulation.push_sort(mother);

		num += 2;
	}
	midpopulation.clear();
}
void variating()//变异
{  
	int better_num = Po_Size * Better_Proportion;
	double va = 0.0;
	for (int k = 0; k < Po_Size; k++)
	{
		Individual* parent = nextpopulation[k];
		Individual* child = new Individual;
		double* parent_variable = parent->GetVariable();
		double child_variable[De_Variable] = { 0 };
		for (int i = 0; i < De_Variable; i++)
			child_variable[i] = parent_variable[i];
		va = k < better_num ?1.0: Srand();//前几个较好的不变异
		if (va < Va_Probability)//变异
		{
			for (int i = 0; i < De_Variable; i++)
			{
				//编码
				double p_v_x = parent_variable[i];
				bitset<length> p_v_b((p_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				//变异
				int local = rand() % Length[i];
				p_v_b.flip(local);
				//解码
				double p_new=(double)(p_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				//修改child_variable
				if ((Range[i]).inRange(p_new))
					child_variable[i] = p_new;
			}
		}
		//新建个体，加入nowpopulation
		Individual* individual = new Individual(child_variable);
		nowpopulation.CalculaFitness(individual);
		nowpopulation.push_sort(individual);
	}
	nextpopulation.clear();
}
double Srand()//随机产生0到1的随机小数
{
	int N = rand() % 999;
	return (double)N / 1000.0;
}
void genetic_algorithm()//遗传算法
{
	double best = 0.0;
	double now_best = 0.0;
	int num = 0;
	srand((unsigned)time(NULL));
	Initialize();
	cout << ".......init......" << endl;
	nowpopulation.print();
	for (int i = 0; i < Ev_Algebra; i++)
	{
		seclect();
		crossing();
		now_best = nextpopulation[0]->GetFitness();
		if (best >= now_best)
			num++;
		else
		{
			num = 0;
			best = now_best;
		}
		//if (num >= 10)//最大适应值10轮没有变化，变异
		{
			variating();
			/*cout << "第" << i << "轮，变异，" << setw(10)
				<< "最优：" << nowpopulation[0]->GetFitness()
				<< "最差：" << nowpopulation[Po_Size - 1]->GetFitness() << endl;*/
		}
		/*else
		{
			for (int k = 0; k < Po_Size; k++)
			{
				Individual* individual = new Individual;
				individual->Copy_Foom(nextpopulation[k]);
				nowpopulation.push_sort(individual);
			}
			nextpopulation.clear();

			cout << "第" << i << "轮，杂交，" << setw(10)
				<< "最优：" << nowpopulation[0]->GetFitness()
				<< "最差：" << nowpopulation[Po_Size - 1]->GetFitness() << endl;
		}*/

		/*cout << "\n##############################################################\n" << i << endl;
		nowpopulation.CalculaReFitness();
		nowpopulation.CalculaSumFitness();
		nowpopulation.print();*/
		cout.precision(13);
		cout << i << setw(20)
			<< nowpopulation[0]->GetFitness() << endl;
	}
}