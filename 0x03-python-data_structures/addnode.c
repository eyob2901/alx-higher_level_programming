#include "lists.h"
listint_t *first(listint_t **head, const int n)
{
  listint_t *temp;
  temp = malloc(sizeof(listint_t));
  if (temp == NULL)
    return (NULL);
  temp->n = n;
  temp->next = *head;
  *head = temp;
  return (temp);
}
