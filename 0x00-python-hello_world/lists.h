#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>

 /**
  * n - An integer variable that holds a value.
  * next -  A pointer to another listint_s structure, which represents
  * the next node in a linked list.
  *
  *  listint_t - consists of two members: n, next.
  */

/* struct listint_s - Represents a node in a singly linked list of integers..*/
typedef struct listint_s
{
int n;
struct listint_s *next;

} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif /* LISTS_H */
