#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */

int check_cycle(listint_t *list)
{
listint_t *human, *car;

	if (list == NULL || list->next == NULL)
		return (0);

	human = list->next;
	car = list->next->next;

	while (human && car && car->next)
	{
		if (human == car)
			return (1);

		human = human->next;
		car = car->next->next;
	}

	return (0);
}


