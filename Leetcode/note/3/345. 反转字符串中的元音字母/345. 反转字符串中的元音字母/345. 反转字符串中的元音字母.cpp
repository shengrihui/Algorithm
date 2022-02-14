#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>>
int isVowel(char ch)
{
	char vowels[] = "aeiouAEIOU";
	for (int i = 0; vowels[i]; i++)
	{
		if (ch == vowels[i])return 1;
	}
	return 0;
}

char* reverseVowels(char* s)
{
	int i = 0, j = strlen(s)-1;
	char tmp = s[0];
	int i_step = 1, j_step = -1;
	while (i < j)
	{
		if (1 == isVowel(s[i]))
			i_step = 0;
		if (1 == isVowel(s[j]))
			j_step = 0;
		if (i_step == 0 && j_step == 0)
		{
			printf("%c %c %s\n", s[i], s[j], s);
			tmp = s[i];
			s[i] = s[j];
			s[j] = tmp;
			i_step = 1;
			j_step = -1;
		}
		i += i_step;
		j += j_step;

	}
	return s;

}

int main()
{
	char s[] = "leetcode";
	char ss[] = "hello";
	printf("%s", reverseVowels(s));

	printf("%s", reverseVowels(ss));
	return 0;
}