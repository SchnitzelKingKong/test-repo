course="  python ProGramming"
print(len(course))
print(course)

#   ---------------------------------------------   #
####            SELECTTING CHARACTERS           #####
#   ---------------------------------------------   #

# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])

#   ---------------------------------------------   #
####            ESCAPE SEQUENCES                #####
#   ---------------------------------------------   #

# \"
# \'
# \\
# \n
# \"

##   ---------------------------------------------   #
####            ???????                         #####
##   ---------------------------------------------   #
#
first = "Albert"
last = "Einstein"
full0 = first + ", " + last
## Formatted Strings
full1 = f"{last} {first}"
full2 = f"{(1+2+3+4+5+6+9.87654321)/7}"
print(full1)

##   ---------------------------------------------   #
####            ???????                         #####
##   ---------------------------------------------   #
#
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip().title())
print(course.find("Pro")) # case sensitv!!
print(course.replace("p", "j"))
print("Pro" in course)
print("swift" not in course)

