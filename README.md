# 🧑‍🎓 12th Grade CS Final Project

My 12th grade CS final project, where I showcased the basics of programming learnt in my 11th and 12th grade.

---

### My Motivation

My final year project revolved around the obsession of creating a clone of
the `Wordle` game by `NYTimes`. The game fascinated me enough to make me think how it was really made.

Since the final project was meant to showcase our skills that we learnt, I thought of making a program which only uses those as the building blocks for this program.

I did'nt have a coding background back then, but this project itself taught me more than I ever did in my CS classes. Because of thisproject itself, I got ideas on how to implement a seemingly simple project, `I sill have lots to learn :^)`.

---

### About the Project

This project is simple:

1. You enter a 5 letter english word
2. The program takes that word and then does the following:
   - Count the length of the word, if more than one then invalid
   - Checks if any character of the word is digit, space or special character, if yes then invalid
   - If the above conditions are false, then it capitalize the letters and puts it as the user's guess
3. Then the program extracts the words from the processed user's guess, and stylizes it (I was thinking way too much 😅).
4. The program also stylizes the answer to be found too.
5. Finally, the program extracts the letters from the two stylized words: guess and answer, and compares them. It says if the letter in guess is in answer, and if in correct position.
6. The user is given 6 tries to guess the answer.

---

### Remarks

As you can see, there are many flaws in this project, such as:

- You can type any word as long as it was all in english letters. Example: `ABCDE`.
- The invalid inputs are considered as a guess by the user. It is a waste as it doesn't give any further information about the answer itself.
- Redundant logic applied in many sections.

And yes, the entire code is not very readable.

---

### License

This progrm is licensed under the [MIT License](/LICENSE).

You can do whatever you want to do with this code.