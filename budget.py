########################################################## defining variables
self_employed = 0
hourly_wage = 0
working_hours = 0
second_hourly_wage = 0
second_working_hours = 0
income_tax = 0
health_insurance = 0
life_insurance = 0
car_insurance = 0
home_insurance = 0
pet_expenses = 0
car_payment = 0
home_payment = 0
rent = 0
card_payment = 0
groceries = 0
utilities = 0
internet_service = 0
phone_bill = 0
miscellaneous_expenses = 0
monthly_goal = 0
yearly_goal = 0
number_of_incomes= 0
all_incomes=[]
extra_income = 0
dividend = 0
extra_expenses = 0
user_wage = 0
second_job_self_employed = 0
first_month_two = 0
second_month_two = 0
third_month_two = 0
########################################################## defining function
def get_float(prompt_txt):
    while True:
        try:
            cleaned_input= input(prompt_txt).strip().replace("$","").replace(",","")
            if cleaned_input in ["admin"]:
                exit()
            return float(cleaned_input)
        except ValueError:
            print("Invalid response, please only use number (e.g., $15.34, 1200), no letter.")
def get_integer(prompt_txt):
    while True:
        try:
            clean_input= input(prompt_txt).strip().replace("$","").replace(",","")
            return int(clean_input)
            if cleaned_input in ["admin"]:
                exit()
        except ValueError:
            print("Invalid response, please only use number (e.g., 5, 2), no letter.")
def get_percent(prompt_txt):
    while True:
        try:
            cleaned_input= input(prompt_txt).strip().replace("%","").replace(",","")
            if cleaned_input in ["amind"]:
                exit()
            return float(cleaned_input)

        except ValueError:
            print("Invalid response, please only use number (e.g., 15.34, 1200), no letter.")
def questionnare():
    global extra_income
    global user_wage
    global self_employed
    global hourly_wage
    global working_hours
    global second_hourly_wage
    global second_working_hours
    global income_tax
    global health_insurance
    global life_insurance
    global car_insurance
    global home_insurance
    global pet_expenses
    global car_payment
    global home_payment
    global rent
    global card_payment
    global groceries
    global utilities
    global internet_service
    global phone_bill
    global miscellaneous_expenses
    global monthly_goal
    global yearly_goal
    global extra_expenses
    global all_incomes
    global dividend
    global user_second_job_pay
    global second_job_self_employed
    global first_month_two
    global second_month_two
    global third_month_two
    while True:
        user_wage= input("Are you self-employed? (y/n) ").strip().lower() ####self employed portion of the code
        if user_wage in ["yes","y"]:
            while True:
                average_monthly= input("Do you know your net monthly average? (y/n) ")
                if average_monthly in ["yes","y"]:
                    self_employed= get_float("How much do you make a month net on average? ")
                    break
                elif average_monthly in ["no","n"]:
                    first_month= get_float("How much did you make net last month? ")
                    second_month= get_float("How much did you make net two months ago? ")
                    third_month= get_float("How much did you make net three months ago? ")
                    self_employed= (first_month+second_month+third_month)/3
                    break
                elif average_monthly in ["admin"]:
                    exit()
                else:
                        print("Please enter a valid response.")
            break
        elif user_wage in ["no","n"]:
           hourly_wage= get_float("What is your hourly wage? ")
           working_hours= get_float("How many hours do you work per week? ")
           break
        elif user_wage in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_job= input("Do you have a second job? (y/n): ").strip().lower() ####second job question 
        if user_job in ["yes","y"]:
            while True:
                user_second_job_pay= input("Does your second job pay hourly rate? (y/n): ").strip().lower()
                if user_second_job_pay in ["yes", "y"]:
                    second_hourly_wage= get_float("What is your hourly wage for the second job? ")
                    second_working_hours= get_float("How many hours do you work per week for the second job? ")
                    break
                elif user_second_job_pay in ["no","n"]:
                    while True:
                        average_monthly_two= input("Do you know your net monthly average? (y/n) ")
                        if average_monthly_two in ["yes","y"]:
                            second_job_self_employed= get_float("How much do you make a month net on average? ")
                            break
                        elif average_monthly_two in ["no","n"]:
                            first_month_two= get_float("How much did you make net last month? ")
                            second_month_two= get_float("How much did you make net two months ago? ")
                            third_month_two= get_float("How much did you make net three months ago? ")
                            second_job_self_employed= (first_month+second_month+third_month)/3
                            break
                        elif average_monthly_two in ["admin"]:
                            exit()
                        else:
                            print("Please enter a valid response.")
                elif user_second_job_pay in ["admin"]:
                    exit()
                else:
                    print("Please enter a valid respoonse.")
            break
        elif user_job in ["no","n"]:
            second_hourly_wage= 0
            second_working_hours= 0
            break
        elif user_job in ["admin"]:
            exit()
        else:
            print("Please enter a valid reponse")
    while True:
        user_dividends = input("Do you get any dividends? (y/n): ").lower().strip()
        if user_dividends in ["yes","y"]:
            dividend= get_float("How much do you get in total from dividends? ")
            all_incomes.append(dividend)
            break
        elif user_dividends in ["no", "n"]:
            dividend= 0
            break
        elif user_dividends in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_extra_income= input("Do you have any extra income? (y/n): ")
        if user_extra_income in ["yes","y"]:
            extra_income= get_float("How much do you get from extra income? ")
            all_incomes.append(extra_income)
            break
        elif user_extra_income in ["no","n"]:
            extra_income= 0
            break
        elif user_extra_income in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    income_tax= get_percent("How much is the income tax in your state? ") ###### state tax question
    health_insurance= get_float("How much do you pay in health insurance? ") ##### insurance portion until the next hashtag
    while True:
        user_life_insurance= input("Do you have life insurace? (y/n): ").strip().lower().replace("$", "")
        if user_life_insurance in ["yes","y"]:
            life_insurance= get_float("How much do you pay in life insurance? ")
            break
        elif user_life_insurance in ["no","n"]:
            life_insurance= 0
            break
        elif user_life_insurance in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    car_insurance= get_float("How much do you pay in car insurance? ")
    home_insurance= get_float("How much do you pay in home insurace? ")
    #############################################################################################
    while True:
        user_choice = input("Do you have pets? (y/n): ").strip().lower() ##### pet quesitons 
        if user_choice in ["yes", "y"]:
            pet_insurance= get_float("How much is spent on pet insurance? ")
            pet_food= get_float("How much is spent on pet food? ")
            pet_grooming= get_float("How much is spent on pet grooming? ")
            pet_expenses= pet_insurance+pet_food+pet_grooming
            break
        elif user_choice in ["no", "n"]:
            pet_expenses= 0
            break
        elif user_choice in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_car = input("Do you have debt on a car? (y/n): ").strip().lower() ############## debt on the car
        if user_car in ["yes", "y"]:
            car_payment= get_float("How much do you pay for the car? ")
            break
        elif user_car in ["no", "n"]:
            car_payment = 0
            break
        elif user_car in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_home = input("Do you have debt on a home? (y/n): ").strip().lower() ############## debt on a home 
        if user_home in ["yes", "y"]:
            home_payment= get_float("How much do you pay for the home? ")
            break
        elif user_home in ["no", "n"]:
            home_payment = 0
            while True:
                user_rent=input("Do you rent a home? (y/n) ").lower().strip()
                if user_rent in ["yes","y"]:
                    rent=get_float("How much is your rent? ")
                    break
                elif user_rent in ["no","n"]:
                    rent= get_float("How much do you pay for your living arrangment? ")
                    break
                elif user_rent in ["admin"]:
                    exit()
                else:
                    print("Please enter a valid response.")
            break
        elif user_home in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_credit_card = input("Do you have debt on credit cards? (y/n): ").strip().lower()  ######## debt for credit cards
        if user_credit_card in ["yes", "y"]:
            card_payment= get_float("How much do you pay for the cards? ")
            break
        elif user_credit_card in ["no", "n"]:
            card_payment = 0
            break
        elif user_credit_card in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    groceries= get_float("How much do you spend on groceries in a month? ")####### groceries
    water_bill= get_float("How much do you pay on the water bill? ")####### water bill
    gas_bill= get_float("How much do you pay on the home gas bill? ")########## home gas
    electricity_bill= get_float("How much do you pay on the electricity bill? ")######## electricity
    utilities= water_bill + gas_bill + electricity_bill #########total utilities
    internet_service= get_float("How much do you pay on the internet? ") ########## internet bill
    while True:
        user_connectivity = input("Is the phone bill included with the internet? (y/n): ").strip().lower() ############ is phone seperate
        if user_connectivity in ["yes","y"]:
            phone_bill= 0
            break
        elif user_connectivity in ["no","n"]:
            phone_bill= get_float("How much do you pay for the phone bill? ")
            break
        elif user_connectivity in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    miscellaneous_expenses= get_float("How much do you spend in miscellaneous things? (haircuts, eating out, car gas, etc) ") ###### extra spending 
    while True:
        user_extra_expenses= input("Do you have any other expenses that are not being taken into account? (y/n) ").lower().strip()
        if user_extra_expenses in ["yes","y"]:
            extra_expenses= get_float("How much more should be taken into account for expenses? ")
            break
        elif user_extra_expenses in ["no","n"]:
            extra_expenses= 0
            break
        elif user_extra_expenses in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    while True:
        user_savings= input("Do you plan to start saving? (y/n) ").strip().lower() ####### savings option
        if user_savings in ["yes","y"]:
            while True:
                user_save_style= input("Do you have a monthly or yearly target? (y/m) ").strip().lower()
                if user_save_style in ["yearly", "y"]:
                    yearly_goal= get_float("How much did you want to save a year? ")
                    break
                elif user_save_style in ["m", "monthly"]:
                    monthly_goal = get_float("How much did you want to save a month? ")
                    yearly_goal= 0
                    break
                elif user_save_style in ["admin"]:
                    exit()
                else:
                    print("Please enter a valid response.")
            break
        elif user_savings in ["no","n"]:
            yearly_goal= 0
            monthly_goal=0
            break
        elif user_savings in ["admin"]:
            exit()
        else:
            print("Please enter a valid response.")
    return
########################################################## inputs
while True:
    user_finances= input("Is this for household or personal finances? (h/p)").strip().lower()
    if user_finances in ["personal","p","personal finances","personal finance"]:
        questionnare()
        break
    #### this is the rest of the code if it is household finances
    elif user_finances in ["household","h","household finance","household finances"]:
        while True:
            user_sole_provider= input("Are you a sole provider? (y/n) ").strip().lower()
            if user_sole_provider in ["yes","y"]:
                questionnare()
                break
            elif user_sole_provider in ["no","n"]:
                while True:
                    divided_payment= input("Do you divdide the payment with them? (y/n) ")
                    if divided_payment in ["yes","y"]:
                        while True:
                            control_of_finances= input("Do you have control over the finances? (y/n) ")
                            if control_of_finances in ["yes","y"]:                        
                                number_of_incomes= get_integer("How many incomes are there in the household? ")
                                all_incomes=[]
                                print("Enter the income for each person seperately.")
                                while number_of_incomes>0:
                                    single_income=get_float("Enter the income:") 
                                    all_incomes.append(single_income)
                                    number_of_incomes=number_of_incomes-1
                                questionnare()
                                break
                            elif control_of_finances in ["no","n"]:
                                questionnare()
                                break
                            elif control_of_finances in ["admin"]:
                                exit()
                            else:
                                print("Please enter a valid response.")
                        while True:
                            user_extra_expenses= input("Do you have any other expenses that are not being taken into account? (y/n) ").lower().strip()
                            if user_extra_expenses in ["yes","y"]:
                                extra_expenses= get_float("How much more should be taken into account for expenses? ")
                                break
                            elif user_extra_expenses in ["no","n"]:
                                extra_expenses= 0
                                break
                            elif user_extra_expenses in ["admin "]:
                                exit()
                            else:
                                print("Please enter a valid response.")
                        break
                    elif divided_payment in ["no","n"]:
                        questionnare()
                        break
                    elif divided_payment in ["admin"]:
                        exit()
                    else:
                        print("Please enter a valid response")
                break
            elif user_sole_provider in ["admin"]:
                exit()
            else:
                print("Please enter a valid response.")
    elif user_finances in ["admin"]:
        exit()
    else:
        print("Please enter a valid response.")    
########################################################## calculations
if user_wage in ["yes","y"]:
    main_income_monthly = self_employed
else:
    main_income_monthly = (hourly_wage * working_hours) * 4
combined_income = sum(all_incomes)
second_income = (second_hourly_wage * second_working_hours) * 4
gross_income = main_income_monthly + second_income + combined_income
net_income = round(gross_income * (1 - income_tax / 100), 2)
if yearly_goal > 0:
    monthly_goal = round((yearly_goal / 12), 2)

if monthly_goal > 0:
    expenses = health_insurance + life_insurance + car_insurance + home_insurance + pet_expenses + car_payment + home_payment + rent + card_payment + groceries + utilities + internet_service + phone_bill + miscellaneous_expenses + monthly_goal + extra_expenses
else:
    expenses = health_insurance + life_insurance + car_insurance + home_insurance + pet_expenses + car_payment + home_payment + rent + card_payment + groceries + utilities + internet_service + phone_bill + miscellaneous_expenses + extra_expenses
left_over = round((net_income - expenses), 2)
########################################################## output
print("This is your net income", net_income)
print("This is your total expense", expenses)
if monthly_goal >0:
    print("This is your monthly savings goal", monthly_goal)
print("This is what remains after", left_over)
