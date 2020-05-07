#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

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
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sz; i++)
	{
		printf("Element %d: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);/*Need to rm*/
		Py_INCREF(p);
	}
}

/**
 * print_python_bytes - prints the size, contents, and addresses of python bytes
 * @p: PyObject to print info from
 *
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz;
	char *s;
	int i, max;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &s, &sz);
	printf("[.] bytes object info\n");
	printf("  size: %d\n", (int)sz);
	printf("  trying string: %s\n", s);
	max = (int)sz + 1 > 10 ? 10 : (int)sz + 1;
	printf("first %d bytes: ", max);
	for (i = 0; i < max; i++)
	{
		printf("%02x ", s[i] & 0xFF);
	}
	putchar('\n');
	return;
}
