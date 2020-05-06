#include "lists.h"
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject to print info from
 *
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	int sz;

	if (!PyList_Check(p))
	{
		printf("Not a list\n");
		return;
	}
	sz = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", sz);
}
