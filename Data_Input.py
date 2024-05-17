projct_name="MultiFamilyProma"
project_num=0
addigned_dev=" "
market = ""
prop_size_acres=0.00
prop_size_sf= 0.00
total_units=1
density_acre=1
num_building=1

# Create a dictionary with the provided data
data = {
    'Project Name': 'Multifamily Pro Forma',
    'Project #': '----',
    'Assigned Developer': '_______ _______',
    'Address': '1660 S HWY 100',
    'Latitude & Longitude': '',
    'Market': 'MN',
    'Property Size (Acres)': 5.00,
    'Property Size (sf)': 217800,
    'Total Units': 200,
    'Density, Per Acre': 40.0,
    'Number of Buildings': 1,
    'Number of Elevators': 2,
    'Development Type': 'Multi-Family',
    '# of Draws/ Months of Const.': 24,
    'Construction Start (Month #)': 1,
    'Closing Date/ Start of Const. (use 1st of mo.)': '1/1/2025'
}



class EscalationAssumptions:
    def __init__(self):
        self.data = {
            'Base Rent': {'Yr 1': 0.03, 'Yr 2': 0.03, 'Yr 3': 0.03, 'Yr 4': 0.03, 'Yr 5': 0.03, 'Yr 6': 0.025, 'Yr 7+': 0.025, '15 Year Average': 0.0263},
            'Other Income': {'Yr 1': 0.005, 'Yr 2': 0.005, 'Yr 3': 0.005, 'Yr 4': 0.005, 'Yr 5': 0.005, 'Yr 6': 0.005, 'Yr 7+': 0.005, '15 Year Average': 0.005},
            'Taxes': {'Yr 1': 0.03, 'Yr 2': 0.03, 'Yr 3': 0.03, 'Yr 4': 0.03, 'Yr 5': 0.03, 'Yr 6': 0.0225, 'Yr 7+': 0.0225, '15 Year Average': 0.0245},
            'Expenses': {'Yr 1': 0.03, 'Yr 2': 0.03, 'Yr 3': 0.03, 'Yr 4': 0.03, 'Yr 5': 0.03, 'Yr 6': 0.025, 'Yr 7+': 0.025, '15 Year Average': 0.0263}
        }

    def add_item(self, item_name, values):
        self.data[item_name] = values

    def display_assumptions(self):
        print("\tEscalation Assumptions:")
        print("\t\tYr 1\tYr 2\tYr 3\tYr 4\tYr 5\tYr 6\tYr 7+\t15 Year Average")
        for item, values in self.data.items():
            print(f"\t\t{item}\t", end="")
            for value in values.values():
                print(f"{value}\t", end="")
            print()

# Test the class
escalation = EscalationAssumptions()
escalation.display_assumptions()

class ApartmentRentAssumptions:
    def __init__(self):
        self.data = {
            'Market Rate': {
                'Studio': {'%': 15.0, 'Count Input': 30, 'Count Totals': 30.0, 'Gross SF': '535 SF', 'All Units': 16050, 'Rent, Mo': '$1,450', 'Rent, PSF Gross': '$2.71', 'Rent, All Units': '$43,500', 'Rent, Annual': '$522,000'},
                '1 Bed': {'%': 45.0, 'Count Input': 90, 'Count Totals': 90.0, 'Gross SF': '715 SF', 'All Units': 64350, 'Rent, Mo': '$1,750', 'Rent, PSF Gross': '$2.45', 'Rent, All Units': '$157,500', 'Rent, Annual': '$1,890,000'},
                '2 Bed': {'%': 35.0, 'Count Input': 70, 'Count Totals': 70.0, 'Gross SF': '1,150 SF', 'All Units': 80500, 'Rent, Mo': '$2,350', 'Rent, PSF Gross': '$2.04', 'Rent, All Units': '$164,500', 'Rent, Annual': '$1,974,000'},
                '3 Bed': {'%': 5.0, 'Count Input': 10, 'Count Totals': 10.0, 'Gross SF': '1,300 SF', 'All Units': 13000, 'Rent, Mo': '$3,000', 'Rent, PSF Gross': '$2.31', 'Rent, All Units': '$30,000', 'Rent, Annual': '$360,000'},
                'Other': {'%': 0.0, 'Count Input': 0, 'Count Totals': 0.0, 'Gross SF': '0', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'}
            },
            'Affordable': {
                'Studio - Affordable': {'%': 0.0, 'Count Input': 'N/A', 'Count Totals': 0.0, 'Gross SF': '535 SF', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'},
                '1 Bed - Affordable': {'%': 0.0, 'Count Input': 'N/A', 'Count Totals': 0.0, 'Gross SF': '715 SF', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'},
                '2 Bed - Affordable': {'%': 0.0, 'Count Input': 'N/A', 'Count Totals': 0.0, 'Gross SF': '1,150 SF', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'},
                '3 Bed - Affordable': {'%': 0.0, 'Count Input': 'N/A', 'Count Totals': 0.0, 'Gross SF': '1,300 SF', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'},
                'Other - Affordable': {'%': 0.0, 'Count Input': 'N/A', 'Count Totals': 0.0, 'Gross SF': '0', 'All Units': 0, 'Rent, Mo': '$0', 'Rent, PSF Gross': '$0', 'Rent, All Units': '$0', 'Rent, Annual': '$0'}
            },
            'Consolidated Apartment Rent Summary': {
                'Gross Potential Rent - Apartments': {'Total Unit Count': 200, 'Avg Gross SF': '870 SF', 'All Units SF': '173,900 SF', 'Avg. Rent/Mo': '$1,978', 'Avg Rent PSF': '$2.27', 'Total Monthly Rent': '$395,500', 'Total Annual Rent': '$4,746,000'}
            }
        }

    def add_item(self, item_name, values):
        self.data[item_name] = values

    def display_assumptions(self):
        print("\tApartment Rent Assumptions:")
        for category, items in self.data.items():
            print(f"\t{category}:")
            for unit_type, values in items.items():
                print(f"\t\t{unit_type}:")
                for key, value in values.items():
                    print(f"\t\t\t{key}: {value}")

# Test the class
apartment_rent = ApartmentRentAssumptions()
apartment_rent.display_assumptions()


# Define apartment rent assumptions
apartment_rent_assumptions = {
    "Studio": {"percent": 15.0, "count_input": 30, "gross_sf": 535, "rent_mo": 1450},
    "1 Bed": {"percent": 45.0, "count_input": 90, "gross_sf": 715, "rent_mo": 1750},
    "2 Bed": {"percent": 35.0, "count_input": 70, "gross_sf": 1150, "rent_mo": 2350},
    "3 Bed": {"percent": 5.0, "count_input": 10, "gross_sf": 1300, "rent_mo": 3000},
}

# Calculate total units and other metrics
total_units = sum(val["count_input"] for val in apartment_rent_assumptions.values())
gross_sf = sum(val["count_input"] * val["gross_sf"] for val in apartment_rent_assumptions.values())
total_monthly_rent = sum(val["count_input"] * val["rent_mo"] for val in apartment_rent_assumptions.values())
total_annual_rent = total_monthly_rent * 12

# Print results
print("Total Units:", total_units)
print("Gross SF:", gross_sf)
print("Total Monthly Rent:", total_monthly_rent)
print("Total Annual Rent:", total_annual_rent)



# Define miscellaneous income assumptions
miscellaneous_income_assumptions = {
    "Surface Parking Stalls": {"num_stalls": 0, "rate_per_month": 30, "occupancy": 0.95},
    "Garage Parking Stalls": {"num_stalls": 200, "rate_per_month": 150, "occupancy": 0.95},
    "Storage Units": {"num_units": 12, "rate_per_month": 50, "occupancy": 0.8},
    "Work-From-Home Offices": {"num_units": 0, "rate_per_month": 100, "occupancy": 1.0},
    "Pet Rent/Month": {"num_pet_owners": 60, "rate_per_month": 40, "pet_owner_percent": 0.3},
    "Bad Debt": {"percent_of_gpr": -0.003, "total": -71},
    "Rental Incentives": {"percent_of_gpr": -0.01, "total": -237},
    "Short Term/MTM Rent": {"percent_of_gpr": 0.003, "total": 71}
}

# Calculate total miscellaneous income
total_miscellaneous_income = sum(val["num_stalls"] * val["rate_per_month"] * val["occupancy"] if "num_stalls" in val else
                                 val["num_units"] * val["rate_per_month"] * val["occupancy"] if "num_units" in val else
                                 val["num_pet_owners"] * val["rate_per_month"] * val["pet_owner_percent"] if "num_pet_owners" in val else
                                 val["total"] for val in miscellaneous_income_assumptions.values())

# Print total miscellaneous income
print("Total Miscellaneous Income:", total_miscellaneous_income)

# Define other income assumptions
other_income_assumptions = {
    "Late/NSF Fees": {"percent_of_gpr": 0.003, "total": 71},
    "Pet Fee": {"annual_amount": 400, "total": 60},
    "Application Fee": {"amount_per_unit": 50, "total": 38},
    "Move-In Admin Fee": {"amount_per_unit": 200, "total": 100},
    "Administration Fee": {"percent_of_gpr": 0.001, "total": 81},
    "Re-Rental Charges": {"percent_of_gpr": 0.0025, "total": 59},
    "Rub Recovery": {"total": 464},
    "Tech Fee/Month": {"amount_per_month": 50, "total": 570},
    "Premium Views/Rents": {"annual_premium": 0, "total": 0},
    "Solar": {"annual_income": 0, "total": 0},
    "Misc (Guest Rm, Club Rm, Cable Inc)": {"annual_income": 10000, "total": 50}
}

# Calculate total other income
total_other_income = sum(val["percent_of_gpr"] * 100 * val["total"] if "percent_of_gpr" in val else
                         val["annual_amount"] * 100 if "annual_amount" in val else
                         val["amount_per_unit"] * 200 if "amount_per_unit" in val else
                         val["amount_per_month"] * 12 * 200 if "amount_per_month" in val else
                         val["total"] for val in other_income_assumptions.values())

# Print total other income
print("Total Other Income:", total_other_income)

# Retail income assumptions
retail_income_assumptions = {
    "Retail Rental Rate (NNN)": 30.00,
    "Leasable Retail Space (SqFt.)": 0,
    "Annual Rent Escalation": 0.02,
    "Retail Lease-up Start Month": 37,
    "Retail Lease Term": 120,
    "RETAIL STABILIZED VACANCY FACTOR": 0.05,
    "RETAIL VACANCY FACTOR START MONTH": 37,
    "Retail Tenant Improvement Allowance": 150.00,
    "Retail Leasing Commissions (%)": 0.06,
    "Retail Leasing Capital Fund Month": 37,
    "Total Retail Revenue": 0,
    "GPR - Retail": 0,
    "Vacancy - Retail": 0,
    "Retail Income PSF": 0,
    "Annual Retail Income": 0
}

# Total retail income
total_retail_income = retail_income_assumptions["Total Retail Revenue"]

# Total operating income
total_operating_income = 25675  # From previous calculations

# Retail expenses assumptions
retail_expenses = {
    "Maintenance": 142900,
    "Admin., Legal, Marketing": 89540,
    "Wages & Payroll": 266400,
    "Management Fees": 154050,
    "Utilities": 229200,
    "Property Taxes": 630000,
    "Insurance & Misc.": 103500,
    "Reserves": 30000
}

# Total operating expenses
total_operating_expenses = sum(retail_expenses.values())

# Print total retail income, total operating income, and total operating expenses
print("Total Retail Income:", total_retail_income)
print("Total Operating Income:", total_operating_income)
print("Total Operating Expenses:", total_operating_expenses)


# Operating expense load assumptions
opex_load = {
    "Maintenance": {"Year 1 PUPY": 715, "Year 1 Total": 142900},
    "Admin., Legal, Marketing": {"Year 1 PUPY": 448, "Year 1 Total": 89540},
    "Wages & Payroll": {"Year 1 PUPY": 1332, "Year 1 Total": 266400},
    "Management Fees": {"Year 1 PUPY": 770, "Year 1 Total": 154050},
    "Utilities": {"Year 1 PUPY": 1146, "Year 1 Total": 229200},
    "Property Taxes": {"Year 1 PUPY": 3150, "Year 1 Total": 630000},
    "Insurance & Misc.": {"Year 1 PUPY": 518, "Year 1 Total": 103500},
    "Reserves": {"Year 1 PUPY": 150, "Year 1 Total": 30000}
}

# Calculate load percentages
for expense, values in opex_load.items():
    year_1_total = values["Year 1 Total"]
    opex_load[expense]["Year 1 Load"] = year_1_total / opex_load["OPEX LOAD TOTALS"]["Year 1 Total"] * 100
    for year in range(2, 8):
        opex_load[expense][f"Year {year} Load"] = 100.00

# Print opex_load
print("Operating Expense Load:")
for expense, values in opex_load.items():
    print(expense)
    for year in range(1, 8):
        print(f"Year {year} Load: {values[f'Year {year} Load']:.2f}%")

# Construction loan details
construction_loan = {
    "Interest Rate": 6.75,
    "Total Funding": 37375000,
    "Ending Balance": 36550619,
    "Term (Mos)": 60,
    "Amortization (mos)": 360,
    "IO Period (mos)": 36
}

# Loan refinance details
refinance_loan = {
    "Interest Rate": 6.00,
    "Total Funding": 45344372,
    "Refi Period (month #)": 61,
    "Term": 300,
    "Amortization (mos)": 360,
    "IO Period (mos)": 0,
    "P&I Period (mos)": 61
}

# Function to calculate debt service
def calculate_debt_service(loan):
    interest_rate = loan["Interest Rate"] / 100
    total_funding = loan["Total Funding"]
    term = loan["Term"]
    amortization = loan["Amortization (mos)"]
    io_period = loan["IO Period (mos)"]
    p_i_period = loan.get("P&I Period (mos)", term)  # Default to term if not provided

    monthly_interest_rate = interest_rate / 12
    loan_balance = total_funding
    monthly_payment = (monthly_interest_rate * loan_balance) / (1 - (1 + monthly_interest_rate) ** -amortization)
    total_debt_service = 0

    for month in range(1, term + 1):
        if month <= io_period:
            total_debt_service += monthly_interest_rate * loan_balance
        elif io_period < month <= p_i_period:
            total_debt_service += monthly_payment
            loan_balance -= monthly_payment - monthly_interest_rate * loan_balance
        else:
            monthly_interest = monthly_interest_rate * loan_balance
            total_debt_service += monthly_interest
            monthly_principal = monthly_payment - monthly_interest
            loan_balance -= monthly_principal

    return total_debt_service

# Calculate debt service for construction loan and refinance loan
construction_debt_service = calculate_debt_service(construction_loan)
refinance_debt_service = calculate_debt_service(refinance_loan)

# Print results
print("Debt Service for Construction Loan:", construction_debt_service)
print("Debt Service for Refinance Loan:", refinance_debt_service)


