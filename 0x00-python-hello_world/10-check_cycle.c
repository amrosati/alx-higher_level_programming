#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cursor = NULL;

	if (list == NULL)
		return (0);

	cursor = list->next;
	while (cursor != list && cursor != NULL)
		cursor = cursor->next;

	if (cursor == list)
		return (1);
	return (0);
}
