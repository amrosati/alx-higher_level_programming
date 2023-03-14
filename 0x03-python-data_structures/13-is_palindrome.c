#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 0 if it is not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *front, *back;
	int len, i, j;

	if (*head == NULL)
		return (1);

	len = get_len(*head);

	for (i = 0, front = *head; front; i++, front = front->next)
	{
		for (j = 0, back = *head; j < len - i - 1; j++)
			back = back->next;

		if (front->n != back->n)
			return (0);
	}

	return (1);
}

/**
 * get_len - counts length of a list
 * @head: head of list
 *
 * Return: len
 */
int get_len(listint_t *head)
{
	int len = 0;
	listint_t *cursor = head;

	while (cursor)
	{
		len++;
		cursor = cursor->next;
	}

	return (len);
}
