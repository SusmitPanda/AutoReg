from distutils.core import setup
setup(
  name = 'AutoReg',         # How you named your package folder (MyLib)
  packages = ['AutoReg'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '''This project is created to get regex of a string in python.
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
                    5.Specialchar_Sensitive :(default= True) It is True means we consider the count of special characters present in the string else it will provide the generic one.
                    ''',   # Give a short description about your library
  author = 'SSP',                   # Type in your name
  author_email = 'susmit.vssut@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['REGEX', 'PYTHON REGEX'],   # Keywords that define your package best
  install_requires=['re'],          # I get to this in a second          
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
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