def main():
    """
    Calculates and displays the monthly payment for a loan based on user input.

    This function acts as a monthly payment loan calculator. It prompts the user
    to enter the principal amount of the loan, the annual interest rate, and the
    duration of the loan in years. It then calculates the monthly payment based
    on these inputs using the formula for a fixed-rate loan. The calculated
    monthly payment is displayed to two decimal places.

    Parameters:
    None

    Returns:
    None: The function outputs the calculated monthly payment to the console
    and does not return a value.
    """
    
    print("")
    print("Monthly payment loan calculator ")
    print("")

    while True:
        principal = float(input("Input the loan amount: "))
        apr = float(input("Input the annual interest rate: "))
        years = int(input("Input amount of years: "))

        monthly_interest_rate = apr / 1200
        amount_months = years * 12
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_months))

        print("The monthly payment for this loan is : %.2f " % monthly_payment)
        print("")

main()