import random
import pandas as pd

# Configurable parameters
crafts = [
    "Story_Writing", "Direction", "Production", "Cinematography", "Editing", "Art_Direction",
    "Sound_Design", "Music", "Costume_Design", "Makeup", "Choreography", "Acting", "Stunts",
    "VFX", "Animation", "Graphics_Titles", "Lighting", "Set_Properties", "Still_Photography",
    "Publicity_Promotion", "Production_Management", "Subtitling_Dubbing", "Color_Grading", "Distribution"
]
members_per_craft = 10  # You can change this to any number

# Random name generators
first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Jamie", "Riley", "Sam", "Casey", "Avery", "Robin"]
last_names = ["Smith", "Johnson", "Lee", "Clark", "Evans", "Wright", "Turner", "Reed", "Morgan", "Campbell"]

# Generate dummy members
data = []
for craft_id, craft in enumerate(crafts, start=1):
    for i in range(members_per_craft):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = full_name.lower().replace(" ", ".") + f"{random.randint(1,99)}@filmcrafters.com"
        experience = random.randint(1, 20)
        data.append({
            "craft_id": craft_id,
            "craft_name": craft,
            "member_name": full_name,
            "email": email,
            "years_experience": experience
        })

# Create and export as CSV
df = pd.DataFrame(data)
df.to_csv("dummy_film_craft_members.csv", index=False)

print("CSV file 'dummy_film_craft_members.csv' created with", len(df), "rows.")
