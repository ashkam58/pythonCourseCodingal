# M8L3A4: Parrot Bird - II
# Coding Grandmaster (Grades 9-12) - Module 8 Lesson 3 Activity 4

class Parrot:
    species = "Bird"

    def __init__(self, name, age, vocabulary):
        self.name = name
        self.age = age
        self.vocabulary = vocabulary

    def speak(self, word):
        if word.lower() in [w.lower() for w in self.vocabulary]:
            return f"{self.name} says: '{word}!'"
        else:
            return f"{self.name} squawks curiously: '{self.name} doesn\'t know that word yet!'"

    def learn_word(self, new_word):
        self.vocabulary.append(new_word)
        print(f"{self.name} has learned a new word: '{new_word}'!")

parrot = Parrot("Rio", 4, ["Hello", "Good Morning", "Codingal"])
print(parrot.speak("Hello"))
print(parrot.speak("Python"))
parrot.learn_word("Python")
print(parrot.speak("Python"))
