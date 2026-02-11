
student = {
    "Name": "Azifa",
    "Age": 21,
    "Branch": "AI & ML"
}

# Add new key-value
student["College"] = "SDMCET"
print("After Adding College:", student)

# Update existing key
student["Age"] = 22
print("After Updating Age:", student)

# Delete a key
del student["Branch"]
print("After Deleting Branch:", student)