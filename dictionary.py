# info = {
#     "name": "MD GHUFRAN ALAM",
#     "City": "MUZAFFARPUR",
#     "College": "NIELIT SRINAGAR",
#     "age": 25,
#     "is_adult": True,
#     "marks": 95.0,
#     "subjects" : ["python","cpp","c","sql"],
    

# }
# null_dict = {}
# null_dict["name"] = "srinagar"
# print(null_dict)
# print(info["name"])
# print(info["College"])

# info["name"]= "arman"
# info["surname"]= "alam"
# print(info)

# NESTED DICTIONARY 
# student = {
#     "name": "ghufran alam",
#     "subject":{
#         "phy": 90,
#         "chem":80,
#         "math":79
#     }
# }
# print(student["subject"] ["chem"])
# print(len(student))
# print(len(list(student.keys())))
# print(student.values())
# print(list(student.values()))
# print(student.items())
# pairs = list(student.items())
# print(pairs[0])

# print(student["name2"]) # error
# print(student.get("name2")) #none

# student.update({"city": "muzaffarpur"})
# new_dict = {"name":"md alam", "age":21}
# student.update(new_dict)
# print(student)

# collection = {1,2,3,4, 4, "hello","ghufran", "hello"}
# collection = set() #empty set; syntax
# print(collection)
# print(len(collection))
# print(type(collection))

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("ghufran alam")
# collection.add((1,2,3))
# # collection.remove(1)
# collection.clear()
# print(len(collection))


# collection = {"hello","python","world", "ghufran"}
# print(collection.pop())


#SET METHODS
# set1 = {1,2,3,}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))

#LETS PRACTICE QUESTION
# dictionary ={
#     "cat": "a small animal",
#     "table": ["a piece of furniture","list of facts & figures"]
# }
# print(dictionary)

# subjects ={
#     "python","java","c++","python","javascript","java","python","java","c++","c"

# }
# print(subjects)
# print(len(subjects))


# marks = {}
# x = int(input("Enter phy: "))
# marks.update({"phy": x})

# x = int(input("Enter math: "))
# marks.update({"math": x})

# x = int(input("Enter chem: "))
# marks.update({"chem": x})

# print(marks)

# values = {9,"9.0"}
# print(values)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)
