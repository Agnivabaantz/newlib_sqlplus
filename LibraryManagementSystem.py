import subprocess

print("1.Displaying databases::")
print("2.Custtomers who have issued books")
print("3.Display authors of books:")
print("4.Exit")
ch = int(input("Enter a choice::"))
def run_sqlplus(sqlplus_script):

    p = subprocess.Popen(['sqlplus','/nolog'],stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr) = p.communicate(sqlplus_script.encode('utf-8'))
    stdout_lines = stdout.decode('utf-8').split("\n")

    return stdout_lines
outfile = open("test.txt","w")
if(ch==1):
    sqlplus_script="""
    connect sys/Colossus as sysdba
    select * from books;
    select * from branch;
    select * from employee;
    select * from issuestatus;
    select * from returnstatus;
    exit;
    """
    sqlplus_output = run_sqlplus(sqlplus_script)
    for line in sqlplus_output:
        sline = line+"\n"
        outfile.write(sline)
        print(line)
elif(ch==2):
    sqlplus_script = """
        connect sys/Colossus as sysdba
        select cusid,cusname from customer,issuestatus where issuestatus.issued_cust = customer.cusid;
        exit;
        """
    sqlplus_output = run_sqlplus(sqlplus_script)
    for line in sqlplus_output:
        print(line)
elif(ch==3):
    sqlplus_script = """
        connect sys/Colossus as sysdba
        select author from books;
        exit;
        """
    sqlplus_output = run_sqlplus(sqlplus_script)
    for line in sqlplus_output:
        print(line)
else:
    print("Exiting database")

