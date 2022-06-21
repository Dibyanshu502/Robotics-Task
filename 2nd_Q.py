'''
Students(super set) is list of lists(subset)
a) def numbers(Students):{
    return num(dictornary-->"courses: no. of studnets that choose the course")
}
# Expectation:
#{"math": 3, "phy": 2, "chem": 2, "cs": 1, "eco": 1,"history":1}
'''

'''
b)def popular(num):
    Return: popular_course --- a string the name of the course which has been done by the
most number of student
#expectation
math
'''
 

    
    
    
# a)
def numbers(Students):                                                                                                  # def created
    list1 = []
    for i in range(len(Students)) :                                                                                     # Multidimentional list concept
        for j in range(len(Students[i])) : 
            list1.append(Students[i][j])
    
    num = {}
    for elements in list1:
        num[elements] = list1.count(elements)
    
    #  OR
    # num = {elements:list1.count(elements) for elements in list1}                      # Dictionary Compression form
    return num                                                                                                           # num returned

# b)
def popular(num):
    popular_course = max(num,key=num.get)
    # popular_course = max(num,key=num.get)                                                                                 # printing the key having max value
    return popular_course


# n = int(input("Enter the no. of elements"))
# Students = list(map(list, input("Enter the list ").strip()))[:n]
# print("User List: ", Students)

Students = [['math', 'phy', 'chem', 'cs'], ['math', 'phy'], ['math', 'chem'], ['history', 'eco']]
x = numbers(Students)
print(x)
y = popular(x)
print("The most popular course is: ",y)

        
        


# for i in range (n):
#     Students = list(input("Enter courses for each student as list :"))

# print(Students)