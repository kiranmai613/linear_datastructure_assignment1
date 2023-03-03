def is_rotation(str1,str2):

    if len(str1)!= len(str2):
        return False
    
    str_add=str1+str1

    return  str2 in str_add



str1="hello"
str2="lohel"
print(is_rotation(str1,str2))