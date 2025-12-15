# PROJECT : FAKE NEWS HEADLINE GENERATOR

import random

subjects = [
    "Salman Khan",
    "Hrithik Roshan",
    "Group of Monkeys",
    "Hardhik Pandya",
    "Rohit Sharma",
    "Rahul Gandhi",
    "Mr. Bean",
    "Dhruvn"
]

actions = [
    "eating",
    "swimming in",
    "launches a war on",
    "becomes a",
    "gets chased by",
    "stealing",
    "robbering",
    "begging for",
    "living on"
]

places_or_things = [
    "Great Wall of China",
    "a river",
    "Machhu Pichhu",
    "Italy",
    "Mariana Trench",
    "Amazon Forest",
    "pig mud",
    "a volcano",
    "Antarctica"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"\n🚨 BREAKING NEWS 🚨 : {subject} {action} {place_or_thing}"
    print(headline)

    user_input = input("\nDo you want to generate more FAKE NEWS? (yes/no): ").strip().lower()

    if user_input == "no":
        print("\nTHANKS FOR USING FAKE NEWS GENERATOR! Have a FUN day 😄")
        break