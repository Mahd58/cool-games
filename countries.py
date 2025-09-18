# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class Pakistan():
    def capital(self):
        print("Islamabad is the capital")
    def language(self):
        print("punjabi is the local laguage")
class India():
    def capital(self):
        print("New Delhi is the capital")
    def language(self):
        print("Hindi is the local laguage")
p1=Pakistan()
I1=India()
for counntrie in (p1,I1):
    counntrie.capital()
    counntrie.language()