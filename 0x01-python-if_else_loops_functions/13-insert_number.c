#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node at position [number]
 * @head: head of the singly linked list
 * @number: number to insert
 *
 * Return: Address of new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner, *curr, *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	curr = runner = *head;
	if (!*head || curr->n > number)
	{
		new->next = curr;
		*head = new;
		return (*head);
	}
	runner = runner->next;
	for (; runner->n < number && runner; runner = runner->next)
		curr = curr->next;
	new->next = runner;
	curr->next = new;
	return (new);
}
