#This project is created to get regex of a string in python.

# Example:
```
from AutoReg import AutoReg
ar=AutoReg()
print(ar.getRegex('ahjas'))
```

#Below are few parameters we have to provide according to our requirements.
#1.Case_Sensitive :(default=True)It is True means we consider the case of alphabets. It means we consider the upper/lower case of alphabet. If it is False it 		  means we do not consider the lower or upper case of alphabets. 
#2.Char_Sensitive :(default=True) It is True means we consider the count of alphabets present in the string else it will provide the generic one.
#3.Digit_Sensitive :(default=True) It is True means we consider the count of digits present in the string else it will provide the generic one.
#4.Space_Sensitive :(default= True) It is true means we consider the count of space present in the string else it will provide the generic one.
#5.Specialchar_Sensitive :(default= True) It is True means we consider the count of special characters present in the string else it will provide the generic one.




