#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed = NULL, *front = *head, *back = NULL;
	int flag = 1;

	if (*head == NULL)
		return (1);

	reversed = reverse_list(*head);

	while (front)
	{
		back = pop(&reversed);
		if (front->n != back->n)
		{
			flag = 0;
			break;
		}

		front = front->next;
		free(back);
	}

	return (flag);
}

/**
 * reverse_list - reverses a linked list
 * @head: head of list
 *
 * Return: new head of list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *reversed = NULL, *cursor = head;

	while (cursor)
	{
		push(&reversed, cursor->n);
		cursor = cursor->next;
	}

	return (reversed);
}

/**
 * push - inserts a node at the beginning of a list
 * @head: head of list
 * @n: number to insert in node
 *
 * Return: new node (on success)
 */
listint_t *push(listint_t **head, const int n)
{
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = n;
	node->next = *head;
	*head = node;

	return (node);
}

/**
 * pop - pops a node from linked list
 * @head: head of list
 *
 * Return: node
 */
listint_t *pop(listint_t **head)
{
	listint_t *node;

	if (*head == NULL)
		return (NULL);

	node = *head;
	*head = node->next;

	return (node);
}
