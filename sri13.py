#single inheritance
class A:

    def displayA(self):
        print("Inheritance A class")
class B(A):

            def displayB(self):
                 print("Inheritance B class")

class C(B):

            def displayB(self):
                 print("Inheritance C class")


obj=C()
obj.displayA()
obj.displayB()
obj.displayC()


                
