import re

class AutoReg:
    def __init__(self):
        self.regex_special_char='''$&+,:;=?@#|'{<>.-^}*()%![]'''
    def find_char_regex(self,chr):
        if chr.isalpha()==True:
            if self.Case_Sensitive==True and self.Char_Sensitive==True:
                if chr.isupper()==True:
                    return '[A-Z]'
                else:
                    return '[a-z]'
            elif self.Case_Sensitive==False and self.Char_Sensitive==True:
                return '\D'
            elif self.Case_Sensitive==True and self.Char_Sensitive==False:
                if chr.isupper()==True:
                    return '[A-Z]+' 
                else:
                    return '[a-z]+'
            elif self.Case_Sensitive==False and self.Char_Sensitive==False:
                return '\D+'
        elif chr.isnumeric()==True:
            if self.Digit_Sensitive==True:
                return '\d'
            else:
                return '\d+'
        elif chr==' ':
            if self.Space_Sensitive==True:
                return '\s'
            else:
                return '\s+'
        elif chr in self.regex_special_char:
            if self.Specialchar_Sensitive==True:
                return '\\'+chr
            else:
                return '\W+'

    def getRegex(self,chr,Case_Sensitive=True,Char_Sensitive=True,Digit_Sensitive=True,Space_Sensitive=True,Specialchar_Sensitive=True):
        self.Case_Sensitive = Case_Sensitive
        self.Char_Sensitive = Char_Sensitive
        self.Digit_Sensitive = Digit_Sensitive
        self.Space_Sensitive = Space_Sensitive
        self.Specialchar_Sensitive = Specialchar_Sensitive        
        regex=[self.find_char_regex(i) for i in chr]
        final_str_ls=[]
        inter_ls=[regex[0]]
        regex.append('A1S@')
        for i in range(1,len(regex)):
            if regex[i] != 'A1S@':
                #print(i)
                if regex[i]==inter_ls[-1]:
                    #print('Y')
                    inter_ls.append(regex[i])
                else:
                    #print('N')
                    final_str_ls.append(inter_ls)
                    inter_ls=[]
                    inter_ls.append(regex[i])
            else:
                final_str_ls.append(inter_ls)
        final_Str=''
        for i in range(len(final_str_ls)):
            if '+' not in final_str_ls[i][0]:
                cnt=len(final_str_ls[i])
                if cnt!=1:
                    reg_str=final_str_ls[i][0]+'{'+str(cnt)+'}'
                    # final_Str += reg_str
                else:
                    reg_str=final_str_ls[i][0]
                final_Str += reg_str
            else:
                reg_str = final_str_ls[i][0]
                final_Str += reg_str
        return final_Str

if __name__ == '__main__':
    chr='ABC123'
    Case_Sensitive=True
    Char_Sensitive=False
    Digit_Sensitive=True
    Space_Sensitive=False
    Specialchar_Sensitive=True

    ar = AutoReg()
    print(ar.getRegex(chr))