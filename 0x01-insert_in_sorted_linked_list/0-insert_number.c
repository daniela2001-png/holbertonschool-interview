#include "lists.h"

/**
 * insert_node - inserta un nodo de manera ordenada
 * @head: es un puntero a un puntero a un objeto de nodo
 * @number: numero a insertar
 * Return: la direccion del nuevo nodo o NULL en caso de fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	/* Special case for the head end */
	new_node->n = number;
	if (*head == NULL || (*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		/* Locate the node before the point of insertion */
		current = *head;
		while (current->next != NULL &&
		       current->next->n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
