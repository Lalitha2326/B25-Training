'''

'''
'''
Basic Operations:  

I. Arithmetics : Addition, Subtraction, Multiplication, and Division
                 Modulus, Floor Division, Exponential, Power
                 2**3       3 % 2 = 1 
                 2*3        7 // 2 = 3
                            7/2 = 3.5


REQ: Add given numbers :
=============================

2+5  6+2  4+6 : 10  12+43 123+432   1234+43 -5+4 4322+432.4+4/5
2+5+6
     Scenarios:
         - Is it only integers or float is allowed ?
         - Only positive or only negative or both positive/negative ?
         - Is there any limit of input data ?
         - Similar or Diff data  12 + 14  12 + 134
         - 0 is allowed or not 
         
         : 2 + 3 
         : 2 + 0.5 
         : 23 + 45 
         : 1.4 + 2.5
         : 4556 + 66553
         : -103 + 56
         : -104.22 + 567.32
         : 2/3 - 5/6 + 78/9
         : 12 + 45 + 76

Addition ? YES
    4 + 3   : 7
    39 + 54 : 93
    43 + 65 + 34     
    39
    54


Addition        :   Usecase: 2 + 3 = 5   
                                Scenarios :  2 + 3 + 6 = 11 
                                             -2 + 5    = 3

Requirement: Adding numbers(Perform addition).
             Consider only positive numbers and 0
                UseCases(Scenarios):    I. Positive,Negative
                                         - Addition of both positive
                                         - Addition of neg, positive
                                         - Adidtion of both negative
                                         - Addition of pos, 0
                                         - Addition of neg, 0
                                     II.Rational,Irrational,Imaginary,Real    
                                    III. Based on no of input values
                                          - 2 input  values
                                          - 3 input values 
                                          ..... n 
Subtraction     :   2 - 3 = -1
                   -2 - 5 = -7
             
Multiplication  :   2 X 3 = 6
                   -5 X 3 = -15
                   
Division        :   21 / 4 = quotient 5,remainder 1
                   -20 / 3 = quotient -6, remainder -2

BODMAS Principle:  operators precedence 
-------------------
Brackets      :  ()  
Of            :  power of 
              :  percent of 
              :  fraction of  
Division      :  %
Multiplication:  X
Addition      :  +
Subtraction   :  - 


II. Comparison :
-----------------

 =,  ==
Symbol     Words            Example Use
-------------------------------------------------
==          equals           1 + 1 == 2  ==> True
≠ !=          not equal to     1 + 1 ≠ 1  ==> True
>          greater than     5 > 7      ==> False
<          less than        7 < 9      ==> True
≥          greater than or 
           equal to         money ≥ 1
≤          less than or 
           equal to         bill ≤ 3
           
Combining:
----------
Example: Ramesh is having rupees 10. Then, he buys something and mentions that 
         he also got some change. How much did she spend?
Answer:  
   We know he did spend some money because he mentioned he bought something. 
   So, whatever he spent must be more than rupees 1.
      - Ramesh's spending is greater than rupees 1.

   We know he didn't spend all of his rupees 10 because he mentioned getting change. 
   So, whatever he spent must be less than rupees 10.
      - Ramesh's spending is less than rupees 10.
      
Putting these together, we express it as:

   - rupees 1 < "What Ramesh Spends" < rupees 10
   
- If we say "Ramesh Spends > rupees 0" (Ramesh spends greater than rupees 0), 
  it's the same as saying "rupees 0 < Ramesh Spends" (which means rupees 0 is less than what Ramesh spends).
We just need to make our symbols (> or <) point towards the smaller value, keeping things consistent.

'''