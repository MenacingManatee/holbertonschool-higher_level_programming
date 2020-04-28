#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;
	int i, j;

	check = current = list;
	for (i = 0; current; i++)
	{
		check = list;
		current = current->next;
		for (j = 0; check != current && j < i; j++)
			check = check->next;
		if (check == current)
			return (1);
	}
	return (0);
}
