import math
# Loan - Amount borrowed by person
#Tenure - Period of loan taken
#Interest - Interest charged on loan
#Frequency - Loan repayment schedule

class EMI:
    # loan_ammount = Loan borrowed by a borrower
    # Interest = Interest charged by a lender
    # Tenure = tenure of loan repayment
    # frequency = frequency of loan reapyment, it is done on monthly, yearly, half yearly, quarterly.

    # PVAR = (loan_amount / interest) * (e/a)
    # e = effective interest rate = (1+i)^n - 1
    # a = (1+i)^n
    # interest = interest / conversion


    def emi(self, loan_amount, interest, tenure, frequency):
        conversion = 0.0
        if frequency == 'MONTHLY':
            conversion = 12.0
        elif frequency == 'QUARTERLY':
            conversion = 4.0
        elif frequency == 'HALF YEARLY':
            conversion =  2.0
        elif frequency == 'YEARLY':
            conversion = 1.0
    
        interest = (interest / (conversion * 100) )
        
        # Tenure Calculation
        if tenure > 12 and conversion == 1.0:
            tenure = tenure /12 
        elif conversion == 2.0:
            tenure = tenure / 6
        elif conversion == 4.0:
            tenure = tenure / 3
    

        a = float(math.pow((1+interest), tenure))
        e = float(a - 1)

        installment = loan_amount*interest*(a/e)

        return installment

object1 = EMI()

loan_amount = float(input("Enter the Loan amount: "))
interest = float(input("Enter the interest: "))
tenure = int(input("Enter the tenure of payment: "))
frequency = input("Enter the frequency of payment from these option Monthly/Quarterly/Half Yearly/Yearly: ")
frequency = frequency.upper()
print("Your EMI will be: ",object1.emi(loan_amount, interest, tenure, frequency))

