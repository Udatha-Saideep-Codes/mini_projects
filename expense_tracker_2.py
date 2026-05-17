month={'12/12/13':([('biscuits',120),('chocolates',240)],360)}
category_total=0
# categories_and_total={'category':([{expense:(cost_of_expense,date)}],category_total)}
categories_and_total={}
category_ranking={}
# these functions add keys and their values. values are of list types or list+other combined types, which may not actually easy to do in the same program  
def add_category(category):
    if category not in categories_and_total:
        categories_and_total[category]=([],category_total)
    else:
        pass

def add_date(date):
    if date not in month:
        month[date]=([],0)

def int_error(var):
    while True:
        try:
            value=int(input(f'Enter {var}:'))
        except ValueError:
            print('Enter a valid value!')
        else:
            return value

def add_expense():
    print('date format is day/month/year')
    date=input('Enter date:')
    no_of_expenses=int_error('Number of expenses')
    for spent in range(no_of_expenses):
        expense=input('    Enter expense:')
        category=input('    Enter category:').lower().capitalize()        
        add_category(category)
        cost_of_expense=int(input('    Enter cost of Expense:'))
        # categories and total dict insertion
        categories_and_total[category][0].append({expense:(cost_of_expense,date)})
        category_expense=categories_and_total[category][1]+cost_of_expense
        categories_and_total[category]=list(categories_and_total[category])
        categories_and_total[category][1]=category_expense
        categories_and_total[category]=tuple(categories_and_total[category])
        tuple(categories_and_total[category])
        # category-ranking insertion. category total will be over written for every new expense in that category
        category_ranking[category]=category_expense
        # month insertion
        add_date(date)
        month[date]=list(month[date])
        date_expense=month[date][1]+cost_of_expense
        month[date][0].append(((expense,cost_of_expense)))
        month[date]=tuple(month[date])

def search_category():
    category=input('Enter category:').lower().capitalize()    
    if category not in categories_and_total:
        print(f'There is no category named {category}')
    else:
        print('The expenses in the category are:')#food
        category_expense=categories_and_total[category]#([{expense:(cost_of_expense,date)}],category_total)
        for expense in category_expense[0]:
            for item,cost_and_date in expense.items():
                print(f'    {item} costed {cost_and_date[0]} and was purchased on {cost_and_date[1]}')
        print(f'the cost of all expenses in this category {category_expense[1]}')
        
def daily_expense_summary():
    date=input('Enter date:')
    if date not in month:
        print('There are no expenses on that date')
    else:
        print(f'Expenses on {date} are:')
        for date_and_expense in month[date][0]:
            print(f'    {date_and_expense[0]} costed {date_and_expense[1]}')
        print(f'The total expense on {date} is {month[date][1]}')

def category_totals():
    print('The category totals are:')
    for category,category_total in categories_and_total.items():
        print(f"    {category}'s total is {category_total[1]}")

def highest_spending_category():
    for category,category_total in category_ranking.items():
        if category_total == max(category_ranking.values()):
            print(f'The highest spending category is {category} which has a total of {category_total}')

def monthly_report():
    category_total_list=sorted((category_ranking.values()))
    for rank in range(len(category_total_list)):
        for category,total in category_ranking.items():
            if category_total_list[rank]==total:
                print(f'''Category:{category} 
    category total is {total}''')

while True:
    print('''Your expense tracker
    1. Add expense 
    2. Know Your expenses in a category
    3. Know your expense on a day
    4. Know category wise total expense cost 
    5. Know category on which you have spent the most 
    6. Get your monthly category wise expense cost
    7. Quit''')
    choice=int_error('your choice:')
    match choice:
        case 1:
            add_expense()
        case 2:
            search_category()
        case 3:
            daily_expense_summary()
        case 4:
            category_totals()
        case 5:
            highest_spending_category()
        case 6:
            monthly_report()
        case 7:
            break