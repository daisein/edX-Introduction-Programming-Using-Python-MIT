def payingDebtOffInOneYear(balance, annualInterestRate, monthlyPaymentRate, months=12):
    """
    Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
    """
    def pay_monthly(balance, annualInterestRate, monthlyPaymentRate):
        monthly_interest_rate = annualInterestRate / 12.0
        minimum_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        print(updated_balance_each_month)
        return(updated_balance_each_month)

    if months == 0:
        return(round(balance, 2))
    else:
        return payingDebtOffInOneYear(pay_monthly(balance, annualInterestRate, monthlyPaymentRate), annualInterestRate, monthlyPaymentRate, months-1)

# print(payingDebtOffInOneYear(60000, 0.2, 0.1))
# this following line makes the edX userface work:
# print(payingDebtOffInOneYear(balance, annualInterestRate, monthlyPaymentRate))

def payingDebtOffInOneYear(balance, annualInterestRate):
    """
    Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
    """
    monthly_rate = annualInterestRate / 12
    minimum_monthly_payment = 10
    new_balance = float(balance)


    while balance > 0:
        minimum_monthly_payment += 5
        balance = new_balance
        for month in range(12):
            balance -= minimum_monthly_payment
            balance += balance * monthly_rate

    return('Lowest Payment: ' + str(minimum_monthly_payment))

# print(payingDebtOffInOneYear(3310 , 0.2))

# print(payingDebtOffInOneYear(balance,annualInterestRate))


def payOffwithBisectionSearch(balance, annualInterestRate):
    """
    若要求已知函数 f(x) = 0 的根 (x 的解)，则:
    先找出一个区间 [a, b]，使得f(a)与f(b)异号。根据介值定理，这个区间内一定包含着方程式的根。
    求该区间的中点 m = (a+b) /2，并找出 f(m) 的值。
    若 f(m) 与 f(a) 正负号相同则取 [m, b] 为新的区间, 否则取 [a, m].
    重复第2和第3步至理想精确度为止。
    """
    global new_balance
    new_balance = float(balance)

    start_pay = float(balance/12)
    end_pay = float(balance)

    def pay(minimum_monthly_payment):
        balance = new_balance
        monthly_rate = annualInterestRate / 12
        for month in range(12):
            balance -= minimum_monthly_payment
            balance += balance * monthly_rate
        return(balance)

    def binarySearch(start, end):

        mid = ((start + end)/2)

        if -1 < pay(mid) < 1:
            # print('perf')
            return mid

        elif pay(mid) > 1:
            # print('paying too little')
            # print(mid,end)
            return(binarySearch(mid, end))

        elif pay(mid) < -1:
            # print('paying too much')
            # print(start,mid)
            return(binarySearch(start, mid))

    return(round(binarySearch(start_pay, end_pay), 2))

print(payOffwithBisectionSearch(balance, annualInterestRate))
# print(payOffwithBisectionSearch(999999, 0.18))
