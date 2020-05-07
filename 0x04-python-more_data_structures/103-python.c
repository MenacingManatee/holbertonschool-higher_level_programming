#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject to print info from
 *
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	int sz, i;

	if (!PyList_Check(p))
		return;
	sz = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sz; i++)
	{
		printf("Element %d: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);/*Need to rm*/
		Py_INCREF(p);
	}
}
