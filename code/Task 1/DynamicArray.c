#include<stdio.h>
#include<stdlib.h>


#define initialCapacity 10

//----------------STRUCT----------------------------------
struct ArrayList
{
	int capacity;
	int used;
	double* array;
};

//----------------INITIAL ARRAY-----------------------------
void initialArray(struct ArrayList* arrayList)
{
	arrayList->capacity = initialCapacity;
	arrayList->used = 0;
	arrayList->array = (double*) malloc(sizeof(double)*arrayList->capacity);
}


//-----------------RESIZE ARRAY------------------------------

void doubleCapacity(struct ArrayList* arrayList)
{
    arrayList->capacity *= 2;
    
    arrayList->array = (double*) realloc(arrayList->array,sizeof(double)*arrayList->capacity);
}

void halfCapacity(struct ArrayList* arrayList)
{
	arrayList->capacity /= 2;
  	
  	arrayList->array = (double*) realloc(arrayList->array,sizeof(double)*arrayList->capacity);
}

void checkResize(struct ArrayList* arrayList)
{
	if(arrayList->used > (arrayList->capacity-1)) 
		doubleCapacity(arrayList);
	
	if(arrayList->used < (arrayList->capacity/3) && arrayList->capacity > initialCapacity) 
		halfCapacity(arrayList);
}


//-----------------ADD ELEMENT--------------------------------

void addTail(struct ArrayList* arrayList,double value)
{
    arrayList->array[arrayList->used] = value;
    
    arrayList->used++;

    checkResize(arrayList);
}

void addHead(struct ArrayList* arrayList, double value)
{
	double temp;
	int i;
	for(i=0; i<arrayList->used; i++)
	{	
		temp = arrayList->array[i];
		arrayList->array[i]=value;
		value = temp;
	}
	arrayList->array[arrayList->used]=value;
	arrayList->used++;

	checkResize(arrayList);
}

void addAt(struct ArrayList* arrayList, int position, double value)
{	
	if(position >= 0 && position <= arrayList->used)
	{
		double temp;
		int i;
		for(i=position; i<arrayList->used; i++)
		{	
			temp = arrayList->array[i];
			arrayList->array[i]=value;
			value = temp;
		}
		arrayList->array[arrayList->used]=value;
		arrayList->used++;

		checkResize(arrayList);
	}
	else
	{
		printf("%s\n", "The element is out of bounds!");
	}
	
}


//-----------------GET ELEMENT--------------------------------

double getAt(struct ArrayList arrayList, int i)
{
	if(i >= 0 && i < arrayList.used)
	{
		return arrayList.array[i];
	}
	else
	{
		printf("%s\n", "The element is out of bounds!");
	}
}

double getFisrt(struct ArrayList arrayList)
{
	return arrayList.array[0];
}

double getEnd(struct ArrayList arrayList)
{
	return arrayList.array[arrayList.used];
}


//-----------------DELETE ELEMENT-----------------------------
void deleteEnd(struct ArrayList* arrayList)
{
	arrayList->used--;

	checkResize(arrayList);
}

void deleteFirst(struct ArrayList* arrayList)
{
	int i;
	for(i=0; i<arrayList->used-1; i++)
	{
		arrayList->array[i]=arrayList->array[i+1];
	}
	arrayList->used--;

	checkResize(arrayList);
}

void deleteAt(struct ArrayList* arrayList, int position)
{
	if(position >= 0 && position < arrayList->used)
	{
		int i;
		for(i=position; i < arrayList->used - 1; i++)
		{
			arrayList->array[i]=arrayList->array[i+1];
		}
		arrayList->used--;

		checkResize(arrayList);
	}
	else
	{
		printf("%s\n", "The element is out of bounds!");
	}
	

}
//------------------MAIN---------------------------------------

void printArray(struct ArrayList arrayList)
{
	int i;
	printf("[");
	for(i=0; i<arrayList.used-1; i++)
	{
		printf("%0.2f, ",arrayList.array[i]);
	}
	printf("%0.2f]\n",arrayList.array[arrayList.used-1]);
}

int main()
{
    //test
    struct ArrayList array;

    initialArray(&array);

    
  
    addTail(&array,1);
    addTail(&array,2);
    addTail(&array,3);
	addTail(&array,4);
	addTail(&array,5);
    addTail(&array,6);
    addTail(&array,7);
	addTail(&array,8);
	addTail(&array,9);
	addTail(&array,10);
	addTail(&array,11);
	addTail(&array,12);
	addTail(&array,13);
	addTail(&array,14);
	addAt(&array,14,6);

	

	printf("%d\n", array.capacity);
	printf("%d\n", array.used);
    printArray(array);
}
