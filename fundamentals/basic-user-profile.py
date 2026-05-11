# %%
# Print
name = "Ali"
print (name)

age = 25
print (age)

city = "Paris"
print (city)

# %%
# f-strings
print (f"My name is {name}. I am {age} years old and I live in {city}.")

# %%
# Type Casting
age_text = "25"
age_number = int(age_text)

# %%
# Casted Value
next_year_age = age_number + 1
print (f"Next year, {name} will be {next_year_age} years old.")

# %%
# String Methods
print (name.upper())
print (name.lower())
print (name.title())
print (name.replace("Ali", "Amir"))
print(len(name))

# %%
# Lists
skills = ["python", "git", "linux"]
skills.append("docker")
print(skills)
print(skills[0])

# %%
# Tuples
birth_date = (1999, 5, 12)
print(birth_date)
print(birth_date[0])

# %%
# Sets
raw_skills  = ["python", "git", "python", "linux", "git"]
unique_skills = set(raw_skills)
print (unique_skills)

# %%
# User Input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_age_number = int(user_age)

print (f"Hello {user_name}, next year you will be {user_age_number + 1} years old.")

input ("Where do you live? ")
print ("Cool!")
# %%
