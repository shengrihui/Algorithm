#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

bool checkRecord(char* s) {
	int absent = 0, late = 0;
	while (*s != '\0')
	{
		if (*s == 'A')
		{
			absent++;
			late = 0;
			if (absent == 2)return false;
		}
		else if (*s == 'L')
		{
			late++;
			if (late == 3)return false;
		}
		else
		{
			late = 0;
		}
		s++;
	}
	return true;
}

int main()
{
	char s[] = "PLALLAP";
	if (checkRecord(s) == true)
		printf("true");
	else if (checkRecord(s) == false)
		printf("false");

}
