#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *tardy, *quick;

	if (!list)
	{
		return (0);
	}
	tardy = list;
	quick = list->next;
	while (quick && tardy && quick->next)
	{
		if (tardy == quick)
		{
			return (1);
		}
		tardy = tardy->next;
		quick = quick->next->next;
	}
	return (0);
}
