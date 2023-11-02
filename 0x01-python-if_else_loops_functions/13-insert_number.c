#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node at a point in a linked list
 * @head: pointer to head
 * @number: number to be inserted
 * Definition - inserts a node at a point
 * Return: pointer to inserted node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *store_iter;
	listint_t *iter;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	iter = *head;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	if ((iter->n > number) || (iter == NULL))
	{
		store_iter = iter;
		*head = new;
		new->next = store_iter;
		return (iter);
	}

	while (iter != NULL)
	{
		store_iter = iter;
		iter = iter->next;
		if (iter == NULL)
		{
			store_iter->next = new;
			return (store_iter->next);
		}
		if (iter->n > number)
		{
			store_iter->next = new;
			new->next = iter;
			iter = new;
			return (iter);
		}
	}
	return (NULL);
}
