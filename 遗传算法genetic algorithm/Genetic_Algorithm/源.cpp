////https://www.cnblogs.com/suchang/p/10550181.html
////���Ԫ���� f(x1,x2)=21.5+x1*sin(4pi*x1)+x2sin(20pi*x2)
//#include<random>
//#include<vector>
//#include<iostream>
//#include<cmath>
//#include<ctime>
//#include<cstdlib>
//#include<bitset>
//#include<iomanip>
//using namespace std;
//const double PI = 3.141592653589793;//����һ�����ɸı�ĳ���ֵPI
//const int Po_Size = 50;//��Ⱥ��ģ population
//const int Ev_Algebra = 500;//�������� evolution algebra
//const double Ov_Probability = 0.850;//������ʣ�������������ж����������Ƿ���Ҫ���� overlapping
//const double Va_Probability = 0.050;//������ʣ�������������ж���һ�����Ƿ���Ҫ���� variation
//const int De_Variable = 2;//�����Ա����ĸ���
//const int length1 = 24;//��ȷ��6λС������24λ�����Ʊ���
//const int length2 = 23;//��ȷ��6λС������23λ�����Ʊ���
////2��24�η�=16777216��2��23�η�=8388608
////��ȷ��6λС������������һλ���λ
//
//class X_Range//�Ա���ȡֵ��Χ�࣬�����ڶ������
//{
//private:
//	double m_Upper;//�Ա����Ͻ�ȡֵ
//	double m_Lower;//�Ա����½�ȡֵ
//public:
//	X_Range(double Lower, double Upper);
//	double GetUpper()const;
//	double GetLower()const;
//};
//class Individual//���������
//{
//private:
//	double m_Variable[De_Variable];//��ű���x1,x2,x3......(��������x1,x2)
//	double m_Fitness;//��Ӧֵ
//	double m_ReFitness;//��Ӧֵ����
//	double m_SumFitness;//�ۼӸ��ʣ�Ϊ����ת��׼��
//public:
//	Individual() {};//Ĭ�Ϲ��캯��
//	Individual(double* Variable);//���캯��
//	double* GetVariable();//��ȡ����ֵ
//	double GetFitness()const;//��ȡ��Ӧֵ
//	double GetReFitness()const;//��ȡ��Ӧֵ����
//	double GetSumFitness()const;//��ȡ�ۼӸ���
//	void ChaFitness(const double Fitness);//�޸���Ӧֵ
//	void ChaReFitness(const double ReFitness);//�޸���Ӧֵ����
//	void ChaSumFitness(const double SumFitness);//�޸��ۼӸ���
//};
//
//void Initialize();//��ʼ����Ⱥ���õ���һ������
//void CaculaFitness();//���������Ӧֵ
//void CaculaReFitness();//���������Ӧֵ����
//void CalculaSumFitness();//��������ۼӸ���
//void seclect();//ѡ��
//void crossing();//�ӽ�
//void variating();//����
//double Scand();//����0��1��С��
//void genetic_algorithm();//�Ŵ��㷨
//
////�Ա���ȡֵ��Χ��������Ⱥ����
//const X_Range Range[De_Variable] = { X_Range(-3.0,12.1) ,X_Range(4.1,5.8) };//�Ա���������x1,x2��ȡֵ��Χ
//vector<Individual> nowpopulation;//P(t)��Ⱥ
//vector<Individual> midpopulation;//�м���Ⱥ���������ת��ѡ����������
//vector<Individual> nextpopulation;//P(t+1)��Ⱥ
//
////X_Range��ʵ��
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
////Individual��ʵ��
//Individual::Individual(double* Variable)//���캯��
//{
//	for (int i = 0; i < De_Variable; i++)//ѭ���Ա��������ֵ
//	{
//		if (Variable[i] >= Range[i].GetLower() && Variable[i] <= Range[i].GetUpper())//���Ա�����ȡֵ���н����ж�
//			m_Variable[i] = Variable[i];
//		else//���������Ҫ���򷢳������棬������
//		{
//			cerr << "�Ա���ȡֵ����" << endl;
//			exit(1);
//		}
//	}
//	//����Ӧֵ�ȳ�ʼ��Ϊ0
//	m_Fitness = 0;
//	m_ReFitness = 0;
//	m_SumFitness = 0;
//}
//double* Individual::GetVariable()//��ȡ����ֵ
//{
//	return m_Variable;
//}
//double Individual::GetFitness()const//��ȡ��Ӧֵ
//{
//	return m_Fitness;
//}
//double Individual::GetReFitness()const//��ȡ��Ӧֵ����
//{
//	return m_ReFitness;
//}
//double Individual::GetSumFitness()const//��ȡ�ۼӸ���
//{
//	return m_SumFitness;
//}
//void Individual::ChaFitness(const double Fitness)//�޸���Ӧֵ
//{
//	m_Fitness = Fitness;
//}
//void Individual::ChaReFitness(const double ReFitness)//�޸���Ӧֵ����
//{
//	m_ReFitness = ReFitness;
//}
//void Individual::ChaSumFitness(const double SumFitness)//�޸��ۼӸ���
//{
//	m_SumFitness = SumFitness;
//}
//
//
//void Initialize()//��ʼ����Ⱥ���õ���һ������
//{
//	double X[Po_Size][De_Variable];//
//	for (int j = 0; j < De_Variable; j++)
//	{
//		//ѭ���������������ֵ�ͱ�������X������
//		//��Ϊx1,x2...�ķ�Χ(Range[j])��ͬ�����ԣ�jѭ�������
//		default_random_engine e(time(0));//���棬�����������
//		uniform_real_distribution<double> u(Range[j].GetLower(), Range[j].GetUpper());//�ֲ�
//		for (int i = 0; i < Po_Size; i++)
//		{
//			X[i][j] = u(e);
//		}
//	}
//
//	//���ɶ���Ⱦɫ�壩�������뵽��ʼ��Ⱥ��
//	for (int i = 0; i < Po_Size; i++)
//	{
//		double variable[De_Variable];
//		for (int j = 0; j < De_Variable; j++)
//		{
//			variable[j] = X[i][j];
//		}
//		Individual individual(variable);//���ɶ���Ⱦɫ�壩
//		nowpopulation.push_back(individual);//���뵽��ʼ��Ⱥ��
//	}
//}
//void CaculaFitness()//���������Ӧֵ
//{
//	double fitness;//��ʱ����
//	double X[De_Variable];//��ʱ����
//	//f(x1,x2)=21.5+x1*sin(4pi*x1)+x2sin(20pi*x2)
//	for (int i = 0; i < Po_Size; i++)
//	{
//		for (int j = 0; j < De_Variable; j++)
//			X[j] = nowpopulation.at(i).GetVariable()[j];
//		fitness = 21.5 + X[0] * sin(4 * PI * X[0]) + X[2] * sin(20 * PI * X[1]);//������Ӧֵ
//		nowpopulation.at(i).ChaFitness(fitness);//�޸ĸö���Ⱦɫ�壩����Ӧֵ
//	}
//}
//void CaculaReFitness()//���������Ӧֵ����
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
//void CalculaSumFitness()//��������ۼӸ���
//{
//	double summation = 0;
//	for (int i = 0; i < Po_Size; i++)
//	{
//		summation += nowpopulation.at(i).GetReFitness();
//		nowpopulation.at(i).ChaSumFitness(summation);
//	}
//}
//void seclect()//ѡ��
//{
//	default_random_engine e(time(0));//����
//	uniform_real_distribution<double> u(0.0, 1.0);//�ֲ�
//	double array[Po_Size];
//	for (int i = 0; i < Po_Size; i++)
//		array[i] = u(e);
//	for (int j = 0; j < Po_Size; j++)
//	{
//		for (int i = 1; i < Po_Size; i++)
//		{
//			//���������
//			if (array[j] < nowpopulation[i - 1].GetSumFitness())//�һ��������Ҫ���Ǵ����0��������������ۼӸ�����0��nowpupulation[0].GetSumFitness()
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
//void crossing()//�ӽ�
//{
//	int num = 0;//��¼����
//	double corss = 0.0;//������������ĸ���ֵ
//	srand((unsigned)time(NULL));//����ϵͳʱ���������������,����һ��������Ӿ���
//	double array1[De_Variable], array2[De_Variable];//��ʱ�洢���׺�ĸ�׵ı���ֵ
//	{
//		//�ж�˫���Ƿ���Ҫ�ӽ����������һ��0��1��С�����������������ӽ����ʣ�������ӽ���ֱ���Ŵ�����һ�������򣬶Ը�ĸ������ӽ�
//		corss = Scand();
//		if (corss <= Ov_Probability)//���corssС�ڵ����ӽ�����Ov_Probability�ͽ��е����ӽ�
//		{
//			//����Ѱ�Ҷ�Ӧ�±�ĸ��岢�ұ���
//			for (int i = 0; i < De_Variable; i++)
//			{
//				array1[i] = midpopulation.at(num).GetVariable()[i];//���׵��Ա���
//				array2[i] = midpopulation.at(num + 1).GetVariable()[i];//ĸ���Ա���
//			}
//			int localx1, localx2;//��¼���򽻲���λ��
//			int corssx1[length1], corssx2[length2];//��Ϊ�������������
//			double newx1[2], newx2[2];//�ֱ�����������򽻻�������Ӧ�Ա���ֵ
//			bool p1 = true, p2 = true;
//			//Ȼ���˫�ױ������б��벢�ҽ��е����ӽ�
//			for (int j = 0; j < De_Variable; j++)//array1��x1����֮���array2��x1�������е����ӽ����Դ�����
//			{
//				if (j == 0)//x1���б��벢���ӽ�
//				{
//					bitset<length1> array1b1((array1[j] + 3.0) * pow(10, 6));//����3.0�γ�һ��unsigaed��֮���ڽ���ĸ��1��x1����
//					bitset<length1> array2b1((array2[j] + 3.0) * pow(10, 6));//����3.0�γ�һ��unsigaed��֮���ڽ���ĸ��2��x1����        
//					//�����������0��length1-1������ȷ��������λ��
//					localx1 = rand() % length1;
//					//���ڽ��е��㽻�棬����˫��localx1����Ļ���
//					for (int i = 0; i < localx1; i++)
//						corssx1[i] = array1b1[i];
//					for (int k = 0; k < localx1; k++)
//						array1b1[k] = array2b1[k];
//					for (int s = 0; s < localx1; s++)
//						array2b1[s] = corssx1[s];
//					//��ֵ������newx1�����У�x1������ɵ����ӽ�����
//					newx1[0] = double(array1b1.to_ullong()) / pow(10, 6) - 3.0;
//					newx2[0] = double(array2b1.to_ullong()) / pow(10, 6) - 3.0;
//					//���²�����ֵ�����жϣ��ж��Ƿ񳬳���Χ�����������Χ���ӽ�
//					if (newx1[0]< Range[0].GetLower() || newx1[0]>Range[0].GetUpper() || newx2[0]<Range[0].GetLower() || newx2[0]>Range[0].GetUpper())
//					{
//						p1 = false;
//						break;
//					}
//				}
//				if (j == 1)//x2���б��벢���ӽ�
//				{
//					bitset<length2> array1b2((array1[j]) * pow(10, 6));//ĸ��1��x2����
//					bitset<length2> array2b2((array2[j]) * pow(10, 6));//ĸ��2��x2����
//								//�����������0��length2-1������ȷ��������λ��
//					localx2 = rand() % length2;
//					//���ڽ��е��㽻�棬����˫��localx2����Ļ���
//					for (int i = 0; i < localx2; i++)
//						corssx2[i] = array1b2[i];
//					for (int k = 0; k < localx2; k++)
//						array1b2[k] = array2b2[k];
//					for (int s = 0; s < localx2; s++)
//						array2b2[s] = corssx2[s];
//					//��ֵ������newx2�����У�x2������ɵ����ӽ�����
//					newx1[1] = double(array1b2.to_ullong()) / pow(10, 6);
//					newx2[1] = double(array2b2.to_ullong()) / pow(10, 6);
//					//���²�����ֵ�����жϣ��ж��Ƿ񳬳���Χ�����������Χ���ӽ�
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
//			else//��ԭ���ĸ����Ŵ�����һ��
//			{
//				nextpopulation.push_back(midpopulation.at(num));
//				nextpopulation.push_back(midpopulation.at(num + 1));
//			}
//		}
//		else//����ֱ���Ŵ�����һ��nextpopulation
//		{
//			nextpopulation.push_back(midpopulation.at(num));//����һ���µĸ��岢�Ҽ��뵽nextpopulation��
//			nextpopulation.push_back(midpopulation.at(num + 1));
//		}
//		num += 2;
//	}
//	midpopulation.clear();//���midpopulation
//}
//void variating()//����
//{
//	int num = 0;
//	cout << nextpopulation.size();
//	while (num < Po_Size)
//	{
//		double variation = Scand();//�������һ��0��1��С���������ж��Ƿ���б���
//		if (variation <= Va_Probability)//���variationС�ڱ���ϵ��������Ҫ���б���
//		{
//			double x[2];
//			bool p = true;
//			int x1local, x2local;
//			x[0] = nextpopulation.at(num).GetVariable()[0];
//			x[1] = nextpopulation.at(num).GetVariable()[1];
//			bitset<length1> array1((x[0] + 3.0) * pow(10, 6));//x1����
//			bitset<length2> array2(x[1] * pow(10, 6));//x2����
//			x1local = rand() % length1;//array1��λȡ��
//			x2local = rand() % length2;//array2��λȡ��
//			array1.flip(x1local);//�ı�array1 x1localλ��״̬
//			array2.flip(x2local);//�ı�array2 x2localλ��״̬
//			x[0] = double(array1.to_ullong()) / pow(10, 6) - 3.0;
//			x[1] = double(array2.to_ullong()) / pow(10, 6);
//			//�ж��Ƿ��������
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
//	nextpopulation.clear();//���nextpopulation
//}
//double Scand()//����0��1��С��
//{
//	int N = rand() % 999;
//	return (double)N / 1000.0;
//}
//void genetic_algorithm()
//{
//	Initialize();//��ʼ����Ⱥ,������ɵ�һ������
//	 //����500��
//	for (int i = 0; i < Ev_Algebra; i++)
//	{
//		CaculaFitness();//��Ӧ�ȼ���
//		CaculaReFitness();//��Ӧ�ȸ��ʼ���
//		CalculaSumFitness();//�����ۼӸ������
//		seclect();//ѡ��
//		crossing();//�ӽ�
//		variating();//����
//	}
//	CaculaFitness();//��Ӧ�ȼ���
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
//	//����500��֮�����
//	cout << "x1" << setw(10) << "x2" << setw(15) << "Fitness" << endl;
//	for (int j = 0; j < Po_Size; j++)
//		cout << nowpopulation.at(j).GetVariable()[0] << setw(10) << nowpopulation.at(j).GetVariable()[1] << setw(10) << nowpopulation.at(j).GetFitness() << endl;
//	cout << "x1=" << nowpopulation.at(maxid).GetVariable()[0] << " ��" << "x2=" << nowpopulation.at(maxid).GetVariable()[1] << "ʱȡ�����ֵ��" << maxfitness << endl;
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