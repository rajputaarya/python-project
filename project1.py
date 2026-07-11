expenses=[]
members=[]
def welcome():

    print("*"*70)
    print(" "*15," WELCOME TO SMART EXPENSE SPLITTER ")
    print("*"*70)

def show_menu():

    print(".....MAIN MENU.....")
    print("1. Create new group")
    print("2. Add expense")
    print("3. View expense")
    print("4. Calculate split")
    print("5. Exit")

def create_group():

    global group_name
    global members
    global expense

    choice=int(input("enter the choice 1 or 2  "))
    if choice==1:
        print("New group is created ")
    elif choice==2:
        print("Thank you for using smart expense splitter ")
    else :
        print("Please enter valid choice ")

    group_name=input("enter the group name : ")

    members_no=int(input("Enter the total number of members :"))

    if members_no<=0:
        print("members should be greater than 0 ")
    else :
        for i in range (members_no):
            name=input("Enter the name of member : ")
            members.append(name)
            i+=1
        print("Group name is ", group_name)
        print("Total numbers of member : ",members_no )
        print("Names of the members are ")
        for i in range (members_no):
            print("Member ",(i+1),":",members[i])
        print("....Group created succesfully.... ") 

def add_expenses():

    global expenses

    if members==0:
        print("First create the group first")
        return
    

    while True:
        categories = ["Food","Travel","Hotel","Shopping","Fuel","Movie","Others"]
        print(".....ADD EXPENSE.....")
        print("Expense categories")

        for i in range(len(categories)):
            print(f"{i+1}.{categories[i]}")
        choice=int(input("category choice : "))

        if 1<=choice<=len(categories):
            category=categories[choice-1]
        else:
            print("Invalid category choice")

        description=input("Expense description : ")
        amount=float(input("Amount: "))

        if amount==0:
            print("Amount must be greater than zero ")

        print("Who paid??")

        for i in range (len(members)):
            print(f"{i+1}.{members[i]}")
        who_pay= int(input("choose member "))

        if 1<=who_pay<=len(members):
            paid_by=members[who_pay-1]
        else:
            print("Invalid choice")

        expense={"category":category,"description":description,"amount":amount,"paid_by":paid_by}
        expenses.append(expense)

        print(".......Expense added successfully!.........")

        again = input("Do you want to add another expense? (Yes/No): ")

        if again.lower() != "yes":
            break


def view_expenses():
    
    if len(expenses)==0:
        print("Expense not found") 
    
    print(".....TOTAL EXPENSE.....")

    total=0
    for i in range(len(expenses)):
        print(f"expenses {i+1}")
        print(f"category : {expenses[i]['category']}")
        print(f"description :{expenses[i]['description']}")
        print(f"amount: {expenses[i]['amount']}")
        print(f"paid by : {expenses[i]['paid_by']}")
        total+=expenses[i]['amount']

    print(".................................................")
    print(f"total eaxpense : { total}")
def calculate_split():

    global expense
    global members

    if len(expenses)==0:
        print("No expense found")
    
    total_expense=0
    for expense in expenses:
        total_expense+=expense["amount"]
    
    total_members=len(members)

    equal_share= total_expense/total_members

    paid={}

    for member in members :
        paid[member]=0

    for expense in expenses:
        paid[expense["paid_by"]]+=expense["amount"]

    print("-"*50)
    print("                      EXPENSE SUMMARY")
    print("-"*50)

    print(f"Total_expense : {total_expense }")
    print(f"Total_members : {total_members}")
    print(f"Equal_share : {equal_share  }")

    print("-"*50)
    print("{:<15}{:15}{:<15}{:15}".format("Member","Paid","Should pay","Balance"))
    print("-"*50)

    balances={}

    for member in members :
        balance= paid[member]-equal_share
        balances[member]=balance

        print("{:<15}{:<15.2f}{:<15.2f}{:<15.2f}".format(member,paid[member],equal_share,balance))

    print("-"*50)
    print("              BALANCE MEANING")

    print("Positive (+) -> Person should receive money")
    print("Negative (-) -> Person should pay money")

    return balances 

def settlement(balances):

    payers=[]
    receivers=[]

    for member,balance in balances.items():
        if balance > 0:
            receivers.append([member,round(balance,2)])
        elif balance < 0:
            payers.append([member,round(-balance,2)])

    print("*"*50)
    print("                SMART SETTLEMENT")
    print("*"*50)

    if len(receivers)==0 and len(payers)==0:
        print("Everyone is already settled ")
    
    i=0
    j=0

    while i<len(payers) and j< len(receivers):
        payers_name=payers[i][0]
        payers_amount= payers[i][1]

        receivers_name= receivers[j][0]
        receivers_amount= receivers[j][1]
        amount = min(payers_amount, receivers_amount)

        print(f"{payers_name} pays ₹{amount:.2f} to {receivers_name}")

        payers[i][1] -= amount
        receivers[j][1] -= amount

        if payers[i][1] == 0:
            i += 1

        if receivers[j][1] == 0:
            j += 1




welcome()
show_menu()
create_group()
add_expenses()
view_expenses()
balances=calculate_split()
settlement(balances)




    