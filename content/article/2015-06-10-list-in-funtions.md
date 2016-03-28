Title: List behaviar in function as default parameter
Date: 2015-06-10 12:00:58.000000000 +05:30
Modified: 
Category: git
Tags: python,  
Slug: list-behaviar-in-function-as-default-parameter
Authors: mukesh
Summary: 
Status: draft

def listTest(a, list=[]):
    list.append(a)
    return list

x = listTest(10)
y = listTest(123,[])
z = listTest('a')

print "list1 = %s" % x
print "list2 = %s" % y
print "list3 = %s" % x

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3



The output of the above code will be:

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']

Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

With this revised implementation, the output would be:

list1 = [10]
list2 = [123]
list3 = ['a']

