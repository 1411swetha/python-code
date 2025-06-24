ec2_list = ["abc", "xyz", "asd", "abc"]
print(ec2_list)
print(type(ec2_list))
##print particular value from list
print(ec2_list[1])
print(ec2_list[2])
##print lenth of list
print(len(ec2_list))
##inbuilt function append(adding one more sting to list)
ec2_list.append("qwe")
print(ec2_list)
print(ec2_list[3])
print(len(ec2_list))
##inbuilt function (removing specified sting from list)
ec2_list.remove("qwe")
print(ec2_list)
print(len(ec2_list))
#print count of particular sting in list
print(ec2_list.count("abc"))
