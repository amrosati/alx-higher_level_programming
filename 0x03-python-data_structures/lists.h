#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>

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
listint_t *add_nodeint_end(listint_t **, const int);
void free_listint(listint_t *);
int is_palindrome(listint_t **);
listint_t *reverse(listint_t **);
int compare(listint_t *, listint_t *);

#endif /* LISTS_H */
