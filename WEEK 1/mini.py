expenses=[]
def add_expense():
    desc=input("Enter description: ")
    amount=float(input("Enter the amount: "))
    expenses.append({'Description':desc, 'Amount':amount})

def view_expenses():
    for exp in expenses:
        print(f'{exp['Description']} - ${exp['Amount']}')

def show_total():
    total=0
    for exp in expenses:
        total+=exp['Amount']
    print(f'Total money spent:{total}')

while True:
    print("1.ADD EXPENSE\n 2.VIEW EXPENSES\n 3.TOTAL EXPENSES\n 4.EXIT")
    choice=int(input("Enter your choice: "))

    if choice==1:
        add_expense()
    elif choice==2:
        view_expenses()
    elif choice==3:
        show_total()
    elif choice==4:
        break
    else:
        print('invalid Input')