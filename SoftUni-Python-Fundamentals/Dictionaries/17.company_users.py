current_line = input()
company_dict = {}
while current_line != "End":
    company_name, comp_id = current_line.split(" -> ")
    if company_name not in company_dict:
        company_dict[company_name] = []
        company_dict[company_name].append(comp_id)
    else:
        if comp_id not in company_dict[company_name]:
            company_dict[company_name].append(comp_id)
    current_line = input()
for company, comp_id in company_dict.items():
    print(company)
    for id in comp_id:
        print(f"-- {id}")






