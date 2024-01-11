#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int num;

	while(h != NULL)
	{
		printf("%d\n", h->n);
		num += 1;
		h = h->next;
	}
	return num;
}
