#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cursor = list, *fcursor = list;

	while (cursor && fcursor && fcursor->next)
	{
		cursor = cursor->next;
		fcursor = fcursor->next->next;
		if (cursor == fcursor)
			return (1);
	}

	return (0);
}
