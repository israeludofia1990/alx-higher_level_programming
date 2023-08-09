#include "lists.h"
/**
 * check_cycle - checks for cycle in singly linked list
 * @list: list
 * Return: integer
 */
int check_cycle(listint_t *list)
{
	listint_t *prev, *cur;

	cur = list;
	prev = list;

	while (cur && prev && cur->next)
	{
		prev = prev->next;
		cur = cur->next->next;
		if (cur == prev)
			return (1);
	}
	return (0);
}
