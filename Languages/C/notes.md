# what is static in c?
Three different meaning depending on where it is placed.

1. behind a variable inside the function. then it would be initialized once and retains its value.

```
void print (){
  static int y = 0;
  printf("%d",y);
  y++;
}
// output 012345...
```

2. behind a function. then it is only available to the file it is declared in. Same goes for variable declared in the file scope but outside the function.

# array is not a lvalue in c!
```
int a[2];
int c [2] = {1,2};
a = c; //  this is not possible
```
2. how does the memory look like for process?
![](image1.JPG)
![](image2.JPG)

https://www.youtube.com/watch?v=h-HBipu_1P0&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_

when you say int a in c, it assigned a 4 bytes in memory and the value (a,int, address in memory) is stored in a look up table.

3. what are pointer in c?
pointers store address of a certain type of variables.  they have special operations like * to deference them to show the content of the address they are storing.

4. what is an & in c?
It is operation on the variable to get its memory address.

5. Why do we need strong type when declaring pointers. int * to shore int pointer. pointer only store address. so why not use generic  types?
Very good question. It is useful when we are dereferencing it. for example.

```
int a = 5;
int * p = &a;
printf("%d",*p);
```  
Lets assume the that a is stored in memory from 200 to 203 because int is 4 bytes. p only stores 200. when we print \*p  the program has to know that the a is stored in 4 bytes. that information is known becasue \*p is int pointer.
Reference:
https://www.youtube.com/watch?v=JTttg85xsbo&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=3  
6. What is void pointer?
we can do the following
```
int a = 4;
int *p = &a;
void * vp = p;
printf("%d",*vp) // we can not deference a void pointer. we dont know how to read the content of the vp.
printf("%d",vp) // we can only access the address of the vp
```

7. Pointer to pointer?
https://www.youtube.com/watch?v=d3kd5KbGB48&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=4

8. call by value vs call by Reference
https://www.youtube.com/watch?v=LW8Rfh6TzGg&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=5

9. pointers and Array
https://www.youtube.com/watch?v=LW8Rfh6TzGg&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=6

10. Arrays as function arguments
https://www.youtube.com/watch?v=CpjVucvAc3g&index=7&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_

11. char [] vs char *
char * immutable. this is like a constant. allocates the string + pointer in memory
char [] is mutable but the first pointer is constant. allocates memory only for string.
https://overiq.com/c-programming/101/character-array-and-character-pointer-in-c/
