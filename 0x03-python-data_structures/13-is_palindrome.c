#include "lists.h"
/**
 *is_palindorome - palindrome checker
 *@head: head of list
 *Return: 1 if palindrome  otherwise 
 */
int is_palindrome(listint_t **head)
{
int len = 0, i = 0;
listint_t *hold1 , *tail ,*temp, *hold2;
if (*head == NULL || (*head)->next == NULL)
return (1);
hold1 = *head;
temp = *head;
tail = NULL;
while (temp)
{
first(&tail, temp->n);
temp = temp->next;
len++;
}
hold2 = tail;
while (hold1)
{
if ( i == len / 2)
break;
if (hold1->n != hold2->n)
return (0);
hold1 = hold1->next;
hold2 = hold2->next;
i++;
}
free_listint(tail);
return (1);
}
/**
 *first - add node at the head
 *@head: head of linked list
 *@n: number
 *Return: address of new list
 */
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
