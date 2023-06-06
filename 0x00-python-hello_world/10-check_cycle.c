#include "lists.h"

/**
 * check_cycle - function
 *
 * @list: list
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *end = list;

	if (!list)
		return (0);
	while (first && end && end->next)
	{
		first = first->next;
		end = end->next->next;
		if (first == end)
			return (1);
	}
	return (0);
}
