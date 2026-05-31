name = input("Enter your name: ")
print(f"Hello {name}, let's record your skills.")

skills_input = input("Enter your skills seperated by commas: ")
skills_list = skills_input.split(",")

print(f"Your skills list: {skills_list}")


clean_skills = [skill.strip() for skill in skills_list if skill.strip()]

unique_skills = list(set(clean_skills))

print(f"\n{name}'s skills (unique): {unique_skills}")
