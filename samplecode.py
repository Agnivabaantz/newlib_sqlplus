import subprocess
import string
import matplotlib.pyplot as plt
def run_sqlplus(sqlplus_script):

    p = subprocess.Popen(['sqlplus','/nolog'],stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr) = p.communicate(sqlplus_script.encode('utf-8'))
    stdout_lines = stdout.decode('utf-8').split("\n")

    return stdout_lines
sqlplus_script="""
    connect sys/Colossus as sysdba
    select temp from forecast;
    exit;
    """
sqlplus_output = run_sqlplus(sqlplus_script)
t = sqlplus_output[9:-4]
temp=[]
try:
    for i in t:
        temp.append(float(i.strip()))
except :
    print()
print(temp)
'''for line in sqlplus_output:
    print(line)'''