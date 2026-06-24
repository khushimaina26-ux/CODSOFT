import random

print("=" * 50)
print("SMARTFLIX RECOMMENDATION")
print("=" * 50)

movies = {
    "action": [
        "John Wick",
        "Mad Max: Fury Road",
        "The Dark Knight"
    ],

    "comedy": [
        "3 Idiots",
        "Hera Pheri",
        "jumanji:Welocome to the jungle"
    ],

    "science fiction": [
        "Interstellar",
        "Avatar",
        "The Martian"
    ],

    "horror": [
        "The Conjuring",
        "It",
        "Annabelle"
    ],

    "romantic": [
        "Titanic",
        "La La Land",
        "Me before you"
    ]
}


while True:

    print("\nAvailable genres:")
    print("1. Action")
    print("2. Comedy")
    print("3. Science Fiction")
    print("4. Horror")
    print("5. Romantic")

    genre = input("\nEnter your favorite genre: ").lower()

    if genre in movies:

        print("\nAnalyzing your preferences...")
        print("\nRecommended movies for you:")

        recommendations = random.sample(
            movies[genre],
            min(3, len(movies[genre]))
        )

        for i, movie in enumerate(recommendations, start=1):
            print(f"{i}. {movie}")

    else:
        print("\nGenre not found. Please try again.")

    choice = input("\nDo you want another recommendation? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using Movie Recommendation System!")
        break
