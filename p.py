print("hellow world")
a=10
b=10
if a>b:
    print(a,"is greater");
elif a==b:
    print(b,"is greater")
else:
    print(b,"is greater")

a=1234;
x=a;
sum=0;
while(x>0):
    sum = sum + (x%10)
    x = x//10;

print("sum of ", a, "=", sum)

y="aa";
print(y)

a,b,c="Mongo", "apple", "banana"
fruits=a,b,c;
print(fruits);

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
x=1j
y=12j
print(x + y)

x= range(1,100,2);

print(tuple(x))


#searching if a character exist in a string

x = " Hello this is a python searching string question"
def search(s) -> bool:
    # i=0
    # while(i<len(x)):
    #     if(x[i]==s):
    #         return i
    #     i= i+1
    # return -1
    if s in x:
        return True
    else:
        return False

print(search("string"))

def splitText(text):
    i = 0
    st=""
    ls=[]
    while(i<len(text)):
        if(text[i]==" "):
            i+=1
            if(len(st) > 0):
                ls.append(st)
            st=""
            continue

        st+=text[i]
        
        if( i == len(text)-1):
            ls.append(st)
        i+=1
    return ls

print(splitText(x))

name = "Rohan"
greet = lambda name : print("Hello",name);

greet(name)


class Animal:
    name =""

    def eat(self):
        print("I can eat");

class Dog(Animal):
    def display(self):
        print("My name is", self.name);

labrador = Dog()
labrador.name="Libra"

labrador.eat()

labrador.display()