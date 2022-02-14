#include "GA.h"
const X_Range Range[De_Variable] = { X_Range(-3.0,12.1) ,X_Range(4.1,5.8) };//�Ա��������߻���x1,x2��ȡֵ��Χ
//vector<Individual> nowpopulation;//P(t)��Ⱥ
//vector<Individual> midpopulation;//�м���Ⱥ���������ѡ�����������
//vector<Individual> nextpopulation;//P(t+1)��Ⱥ
Population nowpopulation;
Population midpopulation;
Population nextpopulation;

//X_Rangeʵ��
X_Range::X_Range(double Lower, double Upper) :m_Lower(Lower), m_Upper(Upper)//���캯��
{}
double X_Range::GetUpper()const//��ȡ��������
{
	return m_Upper;
}
double X_Range::GetLower()const//��ȡ��������
{
	return m_Lower;
}
bool X_Range::inRange(double x)const//�ж�x�Ƿ��ڷ�Χ��
{
	if (x >= m_Lower && x <= m_Upper)
		return true;
	else
		return false;
}

//Individualʵ��
Individual::Individual(double* Variable)//���캯��
{
	for (int i = 0; i < De_Variable; i++)
	{
		if(Range[i].inRange( Variable[i]))
		{
			m_Variable[i] = Variable[i];
		}
		else
		{
			cerr << "�Ա���ȡֵ�д���" << endl;
			exit(1);
		}
	}
	nowpopulation.CalculaFitness(this);
	m_ReFitness = 0;
	m_SumFitness = 0;
	next = NULL;

}
double* Individual::GetVariable()//��ȡ����ֵ
{
	return m_Variable;
}
double Individual::GetFitness()const//��ȡ��Ӧֵ
{
	return m_Fitness;
}
double Individual::GetReFitness()const//��ȡ��Ӧֵ����
{
	return m_ReFitness;
}
double Individual::GetSumFitness()const//��ȡ�ۼӸ���
{
	return m_SumFitness;
}
void Individual::ChaFitness(const double fitness)//�޸���Ӧֵ
{
	m_Fitness = fitness;
}
void Individual::ChaReFitness(const double ReFitness)//�޸���Ӧֵ����
{
	m_ReFitness = ReFitness;
}
void Individual::ChaSumFitness(const double SumFitness)//�޸��ۼӸ���
{
	m_SumFitness = SumFitness;
}
void Individual::Copy_Foom(Individual* individual)//�������޸�Ϊindividualһ��
{
	m_Fitness = individual->GetFitness();
	m_ReFitness = individual->GetReFitness();
	m_SumFitness = individual->GetSumFitness();
	for (int i = 0; i < De_Variable; i++)
		m_Variable[i] = individual->GetVariable()[i];
}

//Populationʵ��
Population::Population()
{
	head = new Individual;
	tail = new Individual;
	head->next = NULL;
	tail = head;
	m_size = 0;
}
void Population::push_back(Individual* indiviual)//�ӵ����
{
	indiviual->next = tail->next;
	tail->next = indiviual;
	tail = indiviual;
	m_size++;
}
void Population::push_sort(Individual* indiviual)//����ؼ���
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
Individual* Population::at(int i)//��λȡ
{
	if (i < 0 || i >= m_size)
	{
		cerr << "�±�Խ�磡" << endl;
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
Individual* Population::operator [](int i)//ͬat()
{
	return Population::at(i);
}
void Population::clear()//���
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
void Population::print()//��ӡ��Ⱥ��Ϣ
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
int Population::size()//��Ⱥ���ڴ�С
{
	return m_size;
}
void Population::CalculaFitness(Individual*individual)//����������Ӧֵ
{
	double x1 = individual->GetVariable()[0];
	double x2 = individual->GetVariable()[1];
	double fitness = 21.5 + x1 * sin(4 * PI * x1) + x2 * sin(20 * PI * x2);
	individual->ChaFitness(fitness);
}
void Population::CalculaReFitness()//����������Ӧֵ����
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
void Population::CalculaSumFitness()//�����ۼӸ������
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
void Population::shuffle()//����
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
Individual* Population::Head()//���ͷָ��
{
	return head;
}

void Initialize()//�����ʼ����Ⱥ���õ���һ������
{
	double X[Po_Size][De_Variable];
	for (int j = 0; j < De_Variable; j++)
	{
		default_random_engine e(time(0));//���棬�����������
		uniform_real_distribution<double> u(Range[j].GetLower(), Range[j].GetUpper());//�ֲ�
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
void seclect()//��Ⱥѡ��
{
	//ֱ����̭�ϲ�ļ���
	int worse_index = Po_Size * (1 - Worse_Proportion);
	for (int i = worse_index; i < Po_Size; i++)
	{
		nowpopulation[i]->ChaFitness(0.0);
	}
	nowpopulation.CalculaReFitness();
	nowpopulation.CalculaSumFitness();

	//���Ϻõ�ֱ��Ū�����ӽ���Ⱥ��
	for (int i = 0; i < Po_Size * Better_Proportion; i++)
	{
		Individual* individual = new Individual;
		individual->Copy_Foom(nowpopulation[i]);
		midpopulation.push_sort(individual);
	}

	//����ת
	default_random_engine e(time(0));//���棬�����������
	uniform_real_distribution<double> u(0.0,1.0);//�ֲ�
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
void crossing()//�ӽ�
{
	midpopulation.shuffle();
	double cross = 0.0;
	int num = 0;
	while (num < Po_Size)
	{
		cross = Srand();
		//ȡ��midpopulation��ǰ����
		Individual* father = midpopulation[0];
		Individual* mother = midpopulation[1];
		midpopulation.Head()->next = midpopulation[2];
		if (cross < Ov_Probability)//���ӽ������ڽ����ӽ�
		{
			//�ӽ�ǰ�Ļ���
			double* father_variable = father->GetVariable();
			double* mother_variable = mother->GetVariable();
			//�ӽ���Ľ��
			double father_new[De_Variable] = { 0 };
			double mother_new[De_Variable] = { 0 };
			bool flag = false;//�Ƿ��ӽ��ɹ�
			for (int i = 0; i < De_Variable; i++)//ѭ�����õı���������
			{
				//ȡ����i�������Ա���x)��ֵ
				double f_v_x = father_variable[i];
				double m_v_x = mother_variable[i];
				//���� 
				// x->y �ȶ�x����ת��
				// y=(x+3.0)*pow(10,6)
				// y=(x-Range[i].GetLower())*pow(10,6)
				bitset<length> f_v_b((f_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				bitset<length> m_v_b((m_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				//�����ӽ���
				int local = rand() % Length[i];
				//�ӽ�
				bool temp;
				for (int k = length - 1; k > local; k--)
				{
					temp = f_v_b[k];
					f_v_b[k] = m_v_b[k];
					m_v_b[k] = temp;
				}
				//����
				double f_new = double(f_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				double m_new = double(m_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				//���ӽ����ֵ�����ж�
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
			//����ӽ��ɹ�
			if (flag)
			{
				for (int i = 0; i < De_Variable; i++)
				{
					father_variable[i] = father_new[i];
					mother_variable[i] = mother_new[i];
				}
				//�����޸���Ӧֵ
				nextpopulation.CalculaFitness(father);
				nextpopulation.CalculaFitness(mother);
			}
		}
		//�����ӽ������ڣ�ֱ�Ӽӵ�nextpopulation
		//�ӽ����ɹ��������ı�ӵ�nextpopulation
		//�ӽ��ɹ����ı��˻���ӵ�nextpopulation
		nextpopulation.push_sort(father);
		nextpopulation.push_sort(mother);

		num += 2;
	}
	midpopulation.clear();
}
void variating()//����
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
		va = k < better_num ?1.0: Srand();//ǰ�����ϺõĲ�����
		if (va < Va_Probability)//����
		{
			for (int i = 0; i < De_Variable; i++)
			{
				//����
				double p_v_x = parent_variable[i];
				bitset<length> p_v_b((p_v_x - Range[i].GetLower()) * pow(10, pow_xp));
				//����
				int local = rand() % Length[i];
				p_v_b.flip(local);
				//����
				double p_new=(double)(p_v_b.to_ullong()) / pow(10, pow_xp) + Range[i].GetLower();
				//�޸�child_variable
				if ((Range[i]).inRange(p_new))
					child_variable[i] = p_new;
			}
		}
		//�½����壬����nowpopulation
		Individual* individual = new Individual(child_variable);
		nowpopulation.CalculaFitness(individual);
		nowpopulation.push_sort(individual);
	}
	nextpopulation.clear();
}
double Srand()//�������0��1�����С��
{
	int N = rand() % 999;
	return (double)N / 1000.0;
}
void genetic_algorithm()//�Ŵ��㷨
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
		//if (num >= 10)//�����Ӧֵ10��û�б仯������
		{
			variating();
			/*cout << "��" << i << "�֣����죬" << setw(10)
				<< "���ţ�" << nowpopulation[0]->GetFitness()
				<< "��" << nowpopulation[Po_Size - 1]->GetFitness() << endl;*/
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

			cout << "��" << i << "�֣��ӽ���" << setw(10)
				<< "���ţ�" << nowpopulation[0]->GetFitness()
				<< "��" << nowpopulation[Po_Size - 1]->GetFitness() << endl;
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