import pandas as pd

# Sample data
data = {
    'EMPLOYEE_ID': [102, 101, 101, 201, 114, 122, 200, 176, 176, 200],
    'START_DATE': ['2001-01-13', '1997-09-21', '2001-10-28', '2004-02-17', '2006-03-24', 
                   '2007-01-01', '1995-09-17', '2006-03-24', '2007-01-01', '2002-07-01'],
    'END_DATE': ['2006-07-24', '2001-10-27', '2005-03-15', '2007-12-19', '2007-12-31', 
                 '2007-12-31', '2001-06-17', '2006-12-31', '2007-12-31', '2006-12-31'],
    'JOB_ID': ['IT_PROG', 'AC_ACCOUNT', 'AC_MGR', 'MK_REP', 'ST_CLERK', 'ST_CLERK', 
               'AD_ASST', 'SA_REP', 'SA_MAN', 'AC_ACCOUNT'],
    'DEPARTMENT_ID': [60, 110, 110, 20, 50, 50, 90, 80, 80, 90]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Group by EMPLOYEE_ID and count the occurrences of each JOB_ID
job_count = df.groupby('EMPLOYEE_ID')['JOB_ID'].nunique()

# Get the employee IDs who have done two or more jobs
multiple_jobs = job_count[job_count >= 2].index

# Display the result
print("Employee IDs who did two or more jobs:")
print(multiple_jobs)
