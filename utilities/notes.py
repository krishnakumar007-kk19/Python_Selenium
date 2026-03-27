"""
xdist = used to connect & run multiple tests at same time

flaky test cases = non stable/irregular output getting as trying

cross browser testing =
multiple browsers one after another execution is happening
one after another

multi browser testing =
parallel multiple browsers one after another execution is happening
all browsers open at same time & runs parallelly

*****************************************************************

waits :
the pause giving in test, so to load the applications files

TYPES :
implicit waits :
if taking time for loading of url/general commands
there we can mention this

explicit waits :


fluent waits :
advanced version of explicit waits
explicit wait apply only once
if we want to wait until a specific element
is loaded
to give additional

***************************************************************
chaining :
process doing at end of the process.

2 types : pages & class chaining

there are rules :
A )*Web element interactions should be present in the respective page classes according to its UI visibility
eg : link of admin page is in admin_page.py, not in home_page.py

B )*if an interaction with the element doesn't make any change in the resultant page, then return self.
eg : when doing an input at a time of "enter user name", we are not accessing no other pages.
    we need to give return self at end of the function.

C )*if an interaction with the element makes any change in the resultant page,
    then return the object of respective page
Eg: when "sign in" is clicked - home page should be loaded.

*****************************************************************

circular import error :
back to back direct of code within .py files

"""





