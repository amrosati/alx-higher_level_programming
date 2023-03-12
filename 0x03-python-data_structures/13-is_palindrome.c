#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of list
 *
 * Return: 1 if it is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed = NULL, *cursor = *head, *rcursor = NULL;
	int flag = 1;

	if (*head == NULL)
		return (1);

	reversed = reverse_list(*head);
	rcursor = reversed;

	while (cursor)
	{
		if (cursor->n != rcursor->n)
		{
			flag = 0;
			break;
		}

		cursor = cursor->next;
		rcursor = rcursor->next;
	}

	free_listint(reversed);
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
	listint_t *nhead = NULL, *cursor = head;

	while (cursor)
	{
		add_nodeint(&nhead, cursor->n);
		cursor = cursor->next;
	}

	return (nhead);
}

/**
 * add_nodeint - inserts a node at the beginning of a list
 * @head: head of list
 * @n: number to insert in node
 *
 * Return: new node (on success)
 */
listint_t *add_nodeint(listint_t **head, const int n)
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
 * free_listint - frees a linked list
 * @head: head of list
 *
 * Return: nothing
 */
void free_listint(listint_t *head)
{
	if (head == NULL)
		return;

	free_listint(head->next);
	free(head);
}
