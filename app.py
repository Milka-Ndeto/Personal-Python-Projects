#Pilau Recipe

def make_pilau():
    """Prints the recipe and steps to make delicious Pilau."""
    print("🌟🍛 Welcome to the Ultimate Pilau Recipe! 🍛🌟")
    print("Serves: 4 | Prep Time: 🕒 15 mins | Cook Time: 🕒 45 mins\n")
    print("✨ Let's get started! ✨\n")

    # Ingredients
    print("🛒 **Ingredients:**")
    ingredients = {
        "🍚 Rice": "2 cups",
        "🥩 Beef (or chicken)": "500g, cubed",
        "🧅 Onions": "2 large, sliced",
        "🧄 Garlic": "4 cloves, minced",
        "🌱 Ginger": "1 inch, grated",
        "🌶️ Pilau Masala": "2 tbsp",
        "🌿 Cumin Seeds": "1 tsp",
        "🍂 Cinnamon Stick": "1 piece",
        "🍃 Cloves": "4-6 pieces",
        "⚫ Black Pepper": "1 tsp",
        "🍃 Bay Leaves": "2",
        "🍅 Tomatoes": "2 large, chopped",
        "🥔 Potatoes (optional)": "2 medium, cubed",
        "🛢️ Vegetable Oil": "4 tbsp",
        "🧂 Salt": "to taste",
        "💧 Water": "4 cups",
        "🌿 Coriander": "Fresh, chopped (for garnish)"
    }

    for ingredient, amount in ingredients.items():
        print(f"  - {ingredient}: {amount}")
    print("\n")

    # Cooking Instructions
    print("🧑‍🍳 **Instructions:**\n")
    steps = [
        "1️⃣ Heat the oil in a large pot over medium heat. 🍳",
        "2️⃣ Add the sliced onions and sauté until golden brown. 🧅✨",
        "3️⃣ Stir in garlic, ginger, cumin seeds, cinnamon, cloves, black pepper, and bay leaves. Cook for 1-2 minutes. 🌿🌶️",
        "4️⃣ Add the meat and cook until browned. 🥩🍖",
        "5️⃣ Mix in the tomatoes and optional potatoes, then cook until the tomatoes are soft. 🍅🥔",
        "6️⃣ Add pilau masala and salt, stirring well to coat everything. 🌶️🧂",
        "7️⃣ Pour in water and bring to a boil. 💧🔥",
        "8️⃣ Add the rice, lower the heat, cover, and simmer until the rice is fully cooked and water is absorbed (about 20 minutes). 🍚⏳",
        "9️⃣ Remove from heat and let it rest for 5 minutes before fluffing with a fork. 🪄🍴",
        "🔟 Garnish with fresh coriander and serve hot! 🌿🍽️"
    ]

    for step in steps:
        print(step)
    print("\n🌟 Enjoy your homemade pilau! 🍛🎉")

# Call the function to display the recipe
make_pilau()
