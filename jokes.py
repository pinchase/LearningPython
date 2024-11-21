import random  # Importing random for selecting a random joke

def random_joke_generator():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why can't your nose be 12 inches long? Because then it would be a foot!",
        "What do you call a belt made of watches? A waist of time!",
        "How do you organize a space party? You planet!"
    ]
    
    # Pick a random joke from the list
    joke = random.choice(jokes)
    return joke

# Run the joke generator
if __name__ == "__main__":
    print("Here's a random joke for you:")
    print(random_joke_generator())
