def calculate_income_tax(gross_salary):
    tax = 0.0
    if gross_salary <= 2500:
        tax = 0.0
    elif gross_salary <= 5000:
        tax = (gross_salary - 2500) * 0.05
    elif gross_salary <= 10000:
        tax = 125.0 + (gross_salary - 5000) * 0.10
    else:
        tax = 625.0 + (gross_salary - 10000) * 0.20
    return tax

def generate_payroll():
    emp_id = input()
    emp_name = input()
    basic_pay = float(input())
    hra = float(input())
    da = float(input())
    conveyance = float(input())
    medical = float(input())
    ot_hours = float(input())
    ot_rate = float(input())
    incentives = float(input())

    ot_pay = ot_hours * ot_rate
    total_allowances = hra + da + conveyance + medical
    gross_salary = basic_pay + total_allowances + ot_pay + incentives

    pf = basic_pay * 0.12
    pt = 200.00
    income_tax = calculate_income_tax(gross_salary)
    total_deductions = pf + pt + income_tax

    net_salary = gross_salary - total_deductions

    print("=" * 60)
    print(f"{'EMPLOYEE SALARY STATEMENT':^60}")
    print("=" * 60)
    print(f"Employee ID   : {emp_id:<20} Employee Name : {emp_name}")
    print("-" * 60)
    print(f"{'EARNINGS':<30}{'AMOUNT':>10} | {'DEDUCTIONS':<20}{'AMOUNT':>8}")
    print("-" * 60)
    print(f"{'Basic Pay':<30}{basic_pay:>10.2f} | {'Provident Fund':<20}{pf:>8.2f}")
    print(f"{'HRA':<30}{hra:>10.2f} | {'Prof. Tax':<20}{pt:>8.2f}")
    print(f"{'DA':<30}{da:>10.2f} | {'Income Tax':<20}{income_tax:>8.2f}")
    print(f"{'Conveyance Allowance':<30}{conveyance:>10.2f} | {'':<20}{'':>8}")
    print(f"{'Medical Allowance':<30}{medical:>10.2f} | {'':<20}{'':>8}")
    print(f"{'Overtime Pay':<30}{ot_pay:>10.2f} | {'':<20}{'':>8}")
    print(f"{'Performance Incentives':<30}{incentives:>10.2f} | {'':<20}{'':>8}")
    print("-" * 60)
    print(f"{'Gross Earnings':<30}{gross_salary:>10.2f} | {'Total Deductions':<20}{total_deductions:>8.2f}")
    print("=" * 60)
    print(f"{'NET PAYABLE':<42} : ${net_salary:>14.2f}")
    print("=" * 60)

if __name__ == "__main__":
    generate_payroll()
