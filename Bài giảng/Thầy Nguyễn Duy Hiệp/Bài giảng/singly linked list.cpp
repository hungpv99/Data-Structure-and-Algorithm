#include <stdlib.h>
#include <stdio.h>

typedef int DATA_TYPE; //dat DATA_TYPE la kieu int

typedef struct list {
	DATA_TYPE  item;      /* data item */
	struct list *pNext;   /* point to successor */
} LIST;

void insert_list(LIST  *&l,   DATA_TYPE  x)
{
    LIST *p;    		/* temporary pointer */
    p = (LIST*)malloc( sizeof(LIST) );
    p->item = x;
    p->pNext = l;
    l = p;
}

//ham chen phan tu moi vao cuoi danh sach
void insert_last(LIST  *&l,   DATA_TYPE  x)
{
    LIST *p,*ptr;    		/* temporary pointer */
    p = (LIST*)malloc( sizeof(LIST) );
    p->item = x;
    
    //Tim phan tu cuoi danh sach
    ptr=l;
    //neu danh sach rong
    if(ptr==NULL)
    {
        p->pNext=NULL;
        l=p;         
    }
    else //tim phan tu cuoi cung (co con tro pNext la NULL)
    {
        while(ptr->pNext !=NULL) ptr=ptr->pNext;
        
        ptr->pNext=p;
        p->pNext=NULL;
    }
}

LIST *search_list(LIST *l, DATA_TYPE  x)
{
	if (l == NULL) return(NULL);
	if (l->item == x)
		return(l);
	else
		return( search_list(l->pNext, x) );
}

//tra ve phan tu truoc phan tu can xoa
LIST *predecessor_list(LIST *l, DATA_TYPE x)
{
    if ((l == NULL) || (l->pNext == NULL)) {
    printf("Error: Danh sach rong hoac co 1 phan tu.\n");
    return(NULL);
    }
    if ((l->pNext)->item == x)
    	return(l);
    else
    	return( predecessor_list(l->pNext, x) );
}

void  delete_list(LIST  *&l, DATA_TYPE  x)
{
    LIST *p; 	/* item pointer */
    LIST *pred; 	/* predecessor pointer */
    p = search_list(l, x);
    if (p != NULL) {
        pred = predecessor_list(l, x);
        
        if (pred == NULL) 	/* splice out out list */
           l = p->pNext;
        else
            pred->pNext = p->pNext;
        free(p); 		/* free memory used by node */
    }
}

//Ham dung de in danh sach
void display(LIST *Head)
{
     while(Head!=NULL)
     {
         printf("%i-->",Head->item);
         Head = Head->pNext;             
     }              
     printf("X\n");   
}

//Ham dung de them cac phan tu vao cuoi day
void input_list(LIST *&Head)
{
    DATA_TYPE  x;
    printf("Nhap gia tri can them : ");
    scanf("%d",&x);
    insert_last(Head,x); 
}


int main()
{
    LIST *Head=NULL;
    display(Head);
    
    //them mot so phan tu vao dau danh sach
    insert_list(Head,5);
    insert_list(Head,3);
    insert_list(Head,7);
    
    insert_last(Head,12);
    insert_last(Head,19);
    insert_last(Head,14);
    
    input_list(Head);
    input_list(Head);
    
    display(Head);
    system("pause");
    return 0;
}
