from math import floor
import pprint
import re

class RoiCalc():
    """
        A program to calculate the cash on cash return of a rental property.
        Takes in inputs for address, value, interest rate, down payment, and other/repairs.
        Calculates taxes, mortgage, rent, property management, and ROI.
        Uses standardized formulas and national number averages.
        Stores property info in a dictionary.
        Can compare properties from the dictionary.
    """

    def __init__(self):
        self.properties = {}      


    def property_info(self):
        # address input
        address = input("\nWhat is the address of the property?\n ")

        pattern = re.compile('[0-9]+[\.]?[0-9]?[0-9]?')
        # value input
        while True:
            orig_value = input("\nWhat does the property cost? (example: 200000)\n ")
            value = orig_value.replace('$', '').replace(',','')
            match_value = pattern.search(value)
            if match_value:
                break
            else:
                print("That is not a valid input...Try again.")

        # interest input
        while True:
            orig_interest = input("\nWhat is the interest rate? (example: 4.5)\n ")
            interest = orig_interest.replace('%', '').replace(',','')
            match_interest = pattern.search(interest)
            if match_interest:
                break
            else:
                print("That is not a valid input...Try again.")

        # down payment input
        while True:
            orig_down_payment = input("\nHow much is the down payment? (example: 40000)\n ")
            down_payment = orig_down_payment.replace('$', '').replace(',','')
            match_down_payment = pattern.search(down_payment)
            if match_down_payment:
                break
            else:
                print("That is not a valid input...Try again.")

        # other/repairs input
        while True:
            orig_repairs = input("\nIf there is other immediate expenses such as repairs, what is the cost? (example: 0)\n ")
            repairs = orig_repairs.replace('$', '').replace(',','')
            match_repairs = pattern.search(repairs)
            if match_repairs:
                break
            else:
                print("That is not a valid input...Try again.")

        value = float(value)
        interest = float(interest)
        down_payment = float(down_payment)
        repairs = float(repairs) 
        price = (value - down_payment)

        # income
        rent = (value / 100.00)
        income_total = rent
        print(f"\nThe monthly income total is: ${income_total}.")

        # expenses
        tax = round(((price * .0107) / 12.00), 2)
        insurance = 150.00
        vacancy = 100.00
        repair_issues = 100.00
        capex = 100.00
        prop_manage = rent * .10
        r = (interest / 100.00)
        mortgage = round(((price * r) / 12.00), 2)
        expense_total = round((tax + insurance + vacancy + repair_issues + capex + prop_manage + mortgage), 2)
        print(f"\nThe monthly expense total is: ${expense_total}.")

        # investment 
        closing_costs = (price * .03)
        investment_total = (down_payment + closing_costs + repairs) 
        print(f"\nThe investment total is: ${floor(investment_total)}.")

        # ROI
        yearly_total = (income_total - expense_total) * 12.00
        yearly_total = round(yearly_total, 2)
        print(f"\nThe yearly earnings are: ${yearly_total}.")
        roi = (yearly_total / investment_total) * 100.00
        roi = round(roi, 2)
        print(f"\nThe cash on cash ROI is: {roi}%.")

        # Creates property dictionary
        self.properties[address] = {}
        self.properties[address]['Value'] = value
        self.properties[address]['Down payment'] = down_payment
        self.properties[address]['Interest rate'] = interest
        self.properties[address]['Monthly taxes'] = tax        
        self.properties[address]['Monthly mortgage'] = mortgage
        self.properties[address]['Monthly rent'] = rent
        self.properties[address]['Total monthly income'] = income_total
        self.properties[address]['Total monthly expense'] = expense_total
        self.properties[address]['Total investment'] = investment_total
        self.properties[address]['Yearly earnings'] = yearly_total
        self.properties[address]['ROI'] = roi


    def compare_dict(self):
        while True:
            dict_one = input("\nWhat is the address of the first property you want to compare?\n ")
            if dict_one not in self.properties:
                print("There is no record of that property. Try again.")
            else:
                break

        while True:
            dict_two = input("\nWhat is the address of the second property you want to compare?\n ")
            if dict_two not in self.properties:
                print("There is no record of that property. Try again.")
            else:
                print(f"\n{dict_one}: \n{self.properties[dict_one]}")
                print("")
                print(f"\n{dict_two}: \n{self.properties[dict_two]}")
                break


    def view_dict(self):
        pprint.pprint(self.properties)


doms_calc = RoiCalc()


def run():
    print("\nWelcome to the ROI calculator.")
    home = "\nPlease choose one: \n\n(1) Calculate   (2) Compare   (3) View All   (4) Quit\n "
    while True:
        response = input(home)
        if response.strip() == '1':
            doms_calc.property_info()

        elif response.strip() == '2':
            doms_calc.compare_dict()

        elif response.strip() == '3':
            doms_calc.view_dict()

        elif response.strip() == '4':
            break

        else:
            print("Invalid Response...Try Again.")  

run()