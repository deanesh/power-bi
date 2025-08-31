import pandas as pd

# Create Employee table
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [101, 102, 101, 103]
})

# Create Department table
departments = pd.DataFrame({
    'dept_id': [101, 102, 103],
    'dept_name': ['HR', 'Finance', 'IT']
})

# Perform inner join
joined_data = pd.merge(employees, departments, on='dept_id', how='inner')

# Return joined data for Power BI
# Power BI will use the final variable in the script
# as the output table
print(joined_data)
joined_data
