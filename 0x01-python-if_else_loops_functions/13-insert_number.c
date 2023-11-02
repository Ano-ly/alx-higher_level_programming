#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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
