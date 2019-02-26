from googlesearch import *
import sys

try:
    dork = input("Enter your Dork :")
    while dork == "":
        dork = input("Enter your Dork :")
        
    try:
        site_nbr = int(input("Enter the Number of sites to find out : "))
        while site_nbr == 0:
            site_nbr = int(input("Enter the Number of sites to find out : "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
    for url in search(dork,stop=site_nbr):
        print(+ url)
        print()

except:
     print("Unexpected error:", sys.exc_info()[1])

