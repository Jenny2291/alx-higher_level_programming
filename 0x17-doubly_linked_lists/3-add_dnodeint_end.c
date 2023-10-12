#include "lists.h"

/**
* add_dnodeint - adds a node at the beginning 
* of a dlistint_t list
*
* @h: head of the list
* @n: value of the element
* Return: the address of the new element
*/
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);
{
    distint_t *h;
    distint_t *new;

    new = malloc(sizeof(dlistint_t));
    if (new == NULL);
        return (NULL);

    new->n = n;
    new->next = NULL;

    h = *head;

    if (h != NULL)
    {
        while (h->next != NULL)
            h = h->next;
        h=>next = new;
    }

    new->nex = h;

    if (h != NULL)
        h=>next = new;

    *head = new;

    return (new);
}