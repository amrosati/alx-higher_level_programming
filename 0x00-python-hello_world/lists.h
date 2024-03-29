#ifndef __LISTS_H__
#define __LISTS_H__

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *);
listint_t *add_nodeint(listint_t **, const int);
void free_listint(listint_t *);
int check_cycle(listint_t *);

#endif /* LISTS_H */
