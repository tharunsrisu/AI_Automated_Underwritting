# Market Rate Units
market_rate_units = [
    {"unit_type": "Studio", "percentage": 15.0, "count": 30, "gross_sf": 535, "rent_month": 1450, "rent_psf": 2.71, "total_monthly_rent": 43500, "total_annual_rent": 522000},
    {"unit_type": "1 Bed", "percentage": 45.0, "count": 90, "gross_sf": 715, "rent_month": 1750, "rent_psf": 2.45, "total_monthly_rent": 157500, "total_annual_rent": 1890000},
    {"unit_type": "2 Bed", "percentage": 35.0, "count": 70, "gross_sf": 1150, "rent_month": 2350, "rent_psf": 2.04, "total_monthly_rent": 164500, "total_annual_rent": 1974000},
    {"unit_type": "3 Bed", "percentage": 5.0, "count": 10, "gross_sf": 1300, "rent_month": 3000, "rent_psf": 2.31, "total_monthly_rent": 30000, "total_annual_rent": 360000}
]

total_market_rate_units = sum(unit["count"] for unit in market_rate_units)
total_market_rate_gross_sf = sum(unit["gross_sf"] * unit["count"] for unit in market_rate_units)
total_market_rate_monthly_rent = sum(unit["total_monthly_rent"] for unit in market_rate_units)
total_market_rate_annual_rent = sum(unit["total_annual_rent"] for unit in market_rate_units)
avg_market_rate_gross_sf = total_market_rate_gross_sf / total_market_rate_units
avg_market_rate_rent_month = total_market_rate_monthly_rent / total_market_rate_units
avg_market_rate_rent_psf = total_market_rate_monthly_rent / total_market_rate_gross_sf

# Affordable Units
affordable_units = []

# Market Rate & Affordable Combined
total_units = total_market_rate_units
total_gross_sf = total_market_rate_gross_sf
total_monthly_rent = total_market_rate_monthly_rent
total_annual_rent = total_market_rate_annual_rent
avg_gross_sf = avg_market_rate_gross_sf
avg_rent_month = avg_market_rate_rent_month
avg_rent_psf = avg_market_rate_rent_psf

affordable_percentage = 0.0

# Print the data
print("Market Rate Units:")
for unit in market_rate_units:
    print(f"{unit['unit_type']}: {unit['percentage']}%, {unit['count']} units, {unit['gross_sf']} SF, ${unit['rent_month']}/month, ${unit['rent_psf']}/SF, ${unit['total_monthly_rent']} total monthly rent, ${unit['total_annual_rent']} total annual rent")
print(f"Totals: {total_market_rate_units} units, {total_market_rate_gross_sf} SF, ${total_market_rate_monthly_rent} total monthly rent, ${total_market_rate_annual_rent} total annual rent, {avg_market_rate_gross_sf} avg SF, ${avg_market_rate_rent_month:.2f} avg rent/month, ${avg_market_rate_rent_psf:.2f} avg rent/SF")

print("\nAffordable Units:")
print("There are no affordable units listed.")

print("\nMarket Rate & Affordable Combined:")
print(f"Totals: {total_units} units, {total_gross_sf} SF, ${total_monthly_rent} total monthly rent, ${total_annual_rent} total annual rent, {avg_gross_sf} avg SF, ${avg_rent_month:.2f} avg rent/month, ${avg_rent_psf:.2f} avg rent/SF")
print(f"Affordable Percentage: {affordable_percentage}%")