#include "lists.h"
#include <stdio.h>

/**
 * main - test code
 *
 * Return: 0 (on success)
 */
int main(void)
{
	listint_t *head = NULL;

	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 1);
        add_nodeint_end(&head, 2);
        add_nodeint_end(&head, 4);
        add_nodeint_end(&head, 275);
        add_nodeint_end(&head, 388);
        add_nodeint_end(&head, 445);
        add_nodeint_end(&head, 604);
        add_nodeint_end(&head, 1024);
	print_listint(head);
	
	printf("\n------------------------------\n");

	insert_node(&head, 27);
	insert_node(&head, 1000);
	insert_node(&head, 3);
	insert_node(&head, -9);
	insert_node(&head, -3);
	insert_node(&head, 0);

	print_listint(head);

	free_listint(head);

	return (0);
}
