# FEE CALCULATOR

# Step 1: Take student name
print("Enter the details of Student")
print("----------------------------------")
name = input("Enter the student name: ")

# Step 2: Take fee details
print("\nENTER THE FEE DETAILS")
admission_fees = int(input("Enter the Admission Fees: "))
tuition_fees = float(input("Enter the Tuition Fees: "))
hostel_fees = float(input("Enter the Hostel Fees: "))

# Step 3: Calculate total fees
total_fees = admission_fees + tuition_fees + hostel_fees

# Step 4: Display output
print("\n----------------------------------")
print("STUDENT DETAILS")
print("----------------------------------")
print("Student name is:", name)
print("Admission Fees is:", admission_fees)
print("Tuition Fees is:", tuition_fees)
print("Hostel Fees is:", hostel_fees)
print("Total Fees is:", total_fees)
print("----------------------------------")
