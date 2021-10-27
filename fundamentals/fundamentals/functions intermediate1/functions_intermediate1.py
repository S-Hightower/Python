# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def change_x(some_list):
#     some_list[1][0] = 15
# change_x(x)

# def change_name(some_list):
#     some_list[0]['last_name'] = 'Bryant'
# change_name(students)

# def change_sports(some_dict):
#     some_dict['soccer'][0] = 'Andres'
# change_sports(sports_directory)

# def change_z(some_list):
#     some_list[0]['y'] = 30
# change_z(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# # iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

def iterateDictionary(students):
    for dict in students:
        for key, value in dict.items():
            print( key, value)

iterateDictionary(students)

# def iterateDictionary2(key_name, some_list):
#     for index in range(len(some_list)):
#         print(some_list[index][key_name])

# iterateDictionary2('first_name', students)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# def print_info(dict):
#     for key,list in dict.items():
#         print("-----------")
#         print(f"{len(list)} {key.upper()}")
#         for item in list:
#             print(item)

# print_info(dojo)