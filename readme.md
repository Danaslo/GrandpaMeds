# Project description:
We all have (or had) that one grumpy grandpa who always tried to dodge taking his medication. He'll come up with any excuse—mixing up the order, skipping doses, or just straight-up "forgetting."

Now, like every Sunday, it's your job to check his pills for the week and make sure they're in the right order for the upcoming days.

This time, though, he’s promised to take it seriously—no cheating, at least for the next week. But he gives you a warning: if you mess up the pill order and something goes wrong, he’ll make sure you hear about it every single day, with that classic angry-grandpa voice, for a whole month.

So, for the sake of your grandpa’s health—and your own peace of mind—you better get this right.

____

# Game explanation: 

This is a simple game about sorting medicines for your grandfather. He will hand to you his doctor's report, and you need to check it up to not miss the medication. Look twice! Medicines can have similar names, but be for totally different purposes!

____

# Code explanation:

I'm just aiming to get used to OOP with Python, so i create little games like these to practise and get some understanding on how the flow of information works in Python classes. As for now i don't see much difference from Java (syntax aside, of course) and i plan on looking up a bit of Django, but i want to deepen my understanding of Python before i do that.

That said, let me explain you the code. In this case is very simple:

# **Classes**

**Medication**: Contains the name and the dosis of the pill the grandfather needs to take.
    - *Attributes*:
        - *name*: Name of the pill
        - *dose*: Dose of the med.

    - *Methods*:
        - *Getters*:
        - *to_String*: Needed to get both the name and the dose of the medicine.

**Game**: Contains all game logic.
    - *Attributes*
        - *med-box*: Contains all the pills in the house. Of course, all of them are mixed up.
        - *pillbox*: Map storing all the daily meds needed. Your job is to fill it up correctly.

**Test**: Test class for playing the game.

*Analysis:* After finishing it i realise i haven't used the dose attribute in the Medication class at all. Since this is just some practise i don't think i'll come back to this, but if i do i'll add it to the doctor's report to add another layer of confusion.
