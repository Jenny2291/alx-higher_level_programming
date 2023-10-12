#include "list.h"

/**
* distinct_len - return the number of elements in
* a double linked list
*
* @h: head of the list
* Return: the number of nudes in the list 
*/
size_t distinct_len(const distint_t *h)
{
    int count;

    count = 0;

    if (h == NULL)
        return (count);

    while (h->prev != NULL)
        h = h->prev;

    while (h != NULL)
    {
        count++;
        h = h->next;
    }
    return (count);
}