#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

int _strcmp(const char *s1, char *s2);
void print_python_bytes(PyObject *p);
/**
 * print_python_list_info - prints some basic info about python lists
 * @p: PyObject to print info from
 *
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	long int sz, i;
	PyObject *type;

	if (!PyList_Check(p))
		return;
	sz = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < sz; i++)
	{
		type = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, type->ob_type->tp_name);
		if (!_strcmp(type->ob_type->tp_name, "bytes"))
			print_python_bytes(PyList_GET_ITEM(p, i));
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
	printf("  first %d bytes: ", max);
	for (i = 0; i < max; i++)
	{
		printf("%02hhx ", s[i] & 0xFF);
	}
	putchar('\n');
	return;
}

/**
 * _strcmp - compares two strings
 *@s1: string 1 to be compared
 *@s2: string 2 to be compared
 * Return: a positive, negative, or 0 number based on the first different char
 */
int _strcmp(const char *s1, char *s2)
{
	while ((*s1 != '\0' && *s2 != '\0') && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	if (*s1 == *s2)
		return (0);
	else
		return (*s1 - *s2);
}
