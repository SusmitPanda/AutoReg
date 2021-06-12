from distutils.core import setup
setup(
  name = 'AutoReg',         
  packages = ['AutoReg'],  
  version = '0.2',      
  license='MIT',        
  description = '''Python package to get regex of string.
                Example:
                String =’ABC123’
                from AutoReg import getRegex
                output = getRegex("ABC123")
                print(output)
                [A-Z]{3}\d{3}

                Below are few parameters we have to provide according to our requirements.
                1.Case_Sensitive :(default=True)It is True means we consider the case of alphabets. It means we consider the upper/lower case of alphabet. If it is False it 		  means we do not consider the lower or upper case of alphabets. 
                2.Char_Sensitive :(default=True) It is True means we consider the count of alphabets present in the string else it will provide the generic one.
                3.Digit_Sensitive :(default=True) It is True means we consider the count of digits present in the string else it will provide the generic one.
                4.Space_Sensitive :(default= True) It is true means we consider the count of space present in the string else it will provide the generic one.
                5.Specialchar_Sensitive :(default= True) It is True means we consider the count of special characters present in the string else it will provide the generic one.''',

  author = 'SusmitPanda',                   
  author_email = 'susmit.vssut@gmail.com',     
  url = 'https://github.com/SusmitPanda/AutoReg',   
  keywords = ['REGEX', 'PYTHON REGEX','AUTO REGEX'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],)