"""
Java:
-------
int x = 10;  Initialization
(OR)

int x; # Declaration
x = 10 # Initialization


Python:
--------
x = 10  Initialization

"""


req ="""
Entity: noun form
Operation: CRUD 

    1. STATE     : Datatypes/DataStructures - INPUT OUTPUT
    2. Behavior  : Operators, DM, Loops    : Functions/OOPs

Note:
-----
Without State, we can't get Behavior.
To get Behavior, State is mandatory.
   
REQ: adding two numbers
input    : two int     
outupt   : int
Behavior : +


Entity: Employee / CREATE, RETRIEVE, UPDATE, DELETE (CRUD)
==========================================================
    1. STATE:
    ---------   
variable: Attributes: eid, name,   sal,  location,  mobile,    mailid,          is_perm, department, incentives
value   : Values    : 1, Madhu, 10000.59, Bangalore, 324324234, email@gmail.com,  False,  Admin,      500.50
type    : datatypes:  int,  str,   float,     str,     str,     str,              bool,   string,     float

    2. BEHAVIOR:
    --------------
    CRUD : CREATE / RETRIEVE / UPDATE / DELETE 
        - Create an Employee     : While Onboarding  
        - Retrieve Employee info : By Employee / Organization
        - Update                 : Update Address / Mobile / Salary Hike / Designation
        - Delete Employee        : While resignation / termination
Note:
-----
  numbers
#  long data type is deprecated
phone_nums storing in format of strings

  
Domain:
-----------
1. Banking : 10 entities
2. ECommerce: 
3. HealthCare
4. Telecom
5. Insurance
6. Trading, Financial 
7. Transport 
8. Entertainment 
9. Food 
10. Electricity 

  
  
  
  
  

Entity: Student 
===================
    1. STATE:
    ---------   
                 int rno = 100    
                ================
variable: Attributes: rno, name, marks, gender, class, section, result, school, location, par_contnum, dob
value   : Values    : 100, Madhu, 54, Male, 5th, B, True, "DPS", "Bangalore", 324324, 14-Jun-32
type    : datatypes:  int, str, float, str, str, str, str, bool

    2. BEHAVIOR:
    --------------
    CRUD : CREATE / RETRIEVE / UPDATE / DELETE 
        - Create Student         : While joining school  (School)
        - Retrieve Student info  : By Student / School
        - Update                 : Parentscontactnum, Addr, MailID / Marks, Grade, Class, Section 
        - Delete Student         : While leaving / Termination



"""
