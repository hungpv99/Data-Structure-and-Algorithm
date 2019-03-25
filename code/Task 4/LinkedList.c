#include<stdio.h>
#include<stdlib.h>

struct NODE
{
    int data;
    struct NODE *next;
};

struct SNODE
{
    struct NODE *head, *last;
    int size;
};

void init(struct SNODE *s);
int add(struct SNODE *s, int data, int pos);
int removeAt(struct SNODE *s, int pos);
struct NODE* find(struct SNODE s, int data);
struct SNODE clone(struct SNODE *target, struct SNODE s);
void append(struct SNODE *target, struct SNODE s);
void delete(struct SNODE *s);
int size(struct SNODE s);
void reverse(struct SNODE *s);
void sort(struct SNODE *target, int type);
void print(struct SNODE s);


int main()
{
    struct SNODE s;
    init(&s);
    add(&s, 10, 0);
    add(&s, 23, 0);
    add(&s, 28, 0);
    add(&s, 34, 0);
    add(&s, 35, 0);
    struct SNODE x;
    init(&x);
    clone(&x, s);
    print(x);
    return 0;
}

void init(struct  SNODE *s)
{   
    s->head = NULL;
    s->last = NULL;
    s->size = 0;
}
int add(struct SNODE *s, int data, int pos)
{
    struct NODE *node = (struct NODE*) malloc(sizeof(struct NODE));
    node->data = data;
    node->next = NULL;
    
    //add head
    if(pos == 0)
    {
        if(s->head == NULL)
        {
            s->head = node;
            s->last = node;
            s->size ++;
            return 1;
        }
        else
        {
            node->next = s->head;
            s->head = node;
            s->size ++;
            return 1;
        }
    }
    
    //add tail            
    if(pos == -1)
    {
        if(s->head == NULL)
        {
            s->head = node;
            s->last = node;
            s->size ++;
            return 1;
        }
        else
        {   
            s->last->next = node;
            s->last = node;
            s->size ++;
            return 1;
        }
    }        

    //add at pos
    if(pos > 0 && pos < s->size)
    {
        if(pos > 0 && pos < s->size)
        {
            struct NODE *p = s->head;
            for(int i=1; i<pos; i++)
            {
                p = p->next;
            }
            node->next = p->next;
            p->next = node;
            return 1;
        }
    }

    
    free(node);
    printf("ERROR: the index is out of bounds!");
    return 0;
}

int removeAt(struct SNODE *s, int pos)
{
    if(pos == 0)
    {
        struct NODE *p = s->head;
        s->head = p->next;
        free(p);
        s->size --;
        return 1;
    }

    if(pos == -1)
    {
        struct NODE *p = s->head;
        for(int i=1; i<s->size; i++)
        {
            p = p->next;
        }
        struct NODE *temp = p->next;
        s->last = p;
        s->last->next = NULL;
        free(temp);
        s->size --;
        return -1;
    }

    if(pos > 0 && pos < s->size)
    {
        struct NODE *p = s->head;
        for(int i=1; i<pos; i++)
        {
            p = p->next;
        }
        struct NODE *temp = p->next;
        p->next = temp->next;
        free(temp);
        s->size --; 
        return 1;
    }
    
    printf("ERROR: the index is out of bounds!");
    return 0;
}

struct NODE* find(struct SNODE s, int data)
{
    struct NODE *p;
    for(p=s.head; p != NULL; p = p->next)
    {
        if(p->data == data)
            return p;
    }
    return NULL;
}

struct SNODE clone(struct SNODE *target, struct SNODE s)
{
    
    for(int i=0; i < target->size; i++)
        removeAt(target,-1);

    struct NODE *p;
    for(p = s.head; p != NULL; p = p->next)
    {
        add(target,p->data,-1);
    }
}

void append(struct SNODE *target, struct SNODE s)
{
    struct NODE *p;
    for(p = s.head; p != NULL; p = p->next)
    {
        add(target, p->data, -1);
    }
}

void delete(struct SNODE *s)
{
    
    while(s->head != NULL)
    {
        struct NODE *p = s->head;
        s->head = p->next;
        free(p);
    }
}

int size(struct SNODE s)
{
    return s.size;
}

void reverse(struct SNODE *s)
{
    struct NODE *p = s->head->next;
    for(p ; p != NULL; p = p->next)
    {
        add(s,p->data,0);
    }
    for(int i = 0; i < s->size; i++)
        removeAt(s,-1);
}

void sort(struct SNODE *target, int type)
{
    //Selection sort
    for(struct NODE *p = target->head; p->next != NULL; p = p->next)
    {
        struct NODE *iTemp = p;
        for(struct NODE *q = p->next; q != NULL; q = q->next)
        {
            if(type == 0)
            {
                if(q->data < iTemp->data)
                {
                    iTemp = q;
                }
            }
            else{
                if(type == 1)
                {
                    if(q->data > iTemp->data)
                    {
                        iTemp = q;
                    }
                }
            }
            
        }
        if(p->data != iTemp->data)
        {
            int temp = p->data;
            p->data = iTemp->data;
            iTemp->data = temp;
        }
    }
}

void print(struct SNODE s)
{
    printf("\n[");
    while(s.head->next != NULL)
    {
        printf("%d, ", s.head->data);
        s.head = s.head->next;
    }
    printf("%d]\n", s.head->data);
}
