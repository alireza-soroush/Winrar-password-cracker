import itertools
from subprocess import check_output
import string

passfound = False

#uppercase letters + lowercase letters + digits and symbols
passlist = string.ascii_letters+string.digits+'!'+'@'+'#'+'$'+'%'+'+'+'/'+'_'+'*'

#range(minimum digits,maximum digits)
#Example: range(2,5) ---> (minimum digits|-> aa,ab,ac) ... aaa,aab,aac ... (aaaa,aaab,aaac |<-maximum digits)
for i in range(1,17):
    generator = itertools.product(passlist,repeat=i)
    for password in generator:

        try:            #Give the unrar.exe path with x in the middle and filename -p at the end
                        #Example: '"C://Program Files/WinRAR/unrar.exe" x myfile.rar -p'
            check_output(r'"unrar.exe path" x filename.rar -p' + "".join(password),shell=True) 
            print("\npassword found ! --> " + "".join(password),"\n")
            passfound = True
            break
        except:
            print("  --> "+"".join(password))
            continue
    if passfound == True:
        break
