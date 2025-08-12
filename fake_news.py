import random

subjects_list = [
    "A rickshaw driver in Mumbai",
    "A pani puri wala",
    "An aunty in Big Bazaar",
    "A chaiwala with WiFi",
    "A goat wearing a saree",
    "A cricket fan painted tricolour",
    "A bollywood hero lookalike",
    "A vada pav seller",
    "A wedding photographer",
    "A groom on a horse",
    "A traffic police without whistle",
    "A samosa vendor",
    "A man dressed as Hanuman",
    "A cow blocking the highway",
    "An auto driver blasting DJ music"
]



actions_list = [
    "dancing like crazy",
    "singing with Neha Kakkar",
    "arguing with Alexa",
    "fighting for a samosa",
    "ordering 500 momos",
    "sleeping on the road",
    "teaching yoga to monkeys",
    "eating golgappa competition",
    "shopping for sarees",
    "doing stand-up comedy",
    "selling chai at India Gate",
    "playing PUBG on stage",
    "arguing with Google Maps",
    "learning TikTok dance",
    "hiding from paparazzi"
]

places_list = [
    "at Dubai Mall",
    "inside a washing machine",
    "on top of Taj Mahal",
    "in a crowded metro",
    "on a moving truck",
    "inside a samosa shop",
    "in Antarctica wearing shorts",
    "at India Gate",
    "on sea beach in rain",
    "in front of a tea stall",
    "inside a haunted house",
    "at roadside dhaba",
    "in jungle with pandas",
    "on moon (breaking news from ISRO)",
    "in a swimming pool full of lassi"
]



while True:
    subject= random.choice(subjects_list)
    action= random.choice(actions_list)
    place=random.choice(places_list)

    headline= f"BRAKING NEWS !: {subject} {action} {place}"

    print("\n"+ headline)


    user_input=input("\nDo you want anathor Headine ? (Yes/no)").lower()
    if user_input == "no":
        break


print("\nThanks for using funny News Headline Generator...")
