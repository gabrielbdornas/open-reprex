# Question 1

- **while Loop:** This is an **entry-controlled loop**, meaning it checks a condition before executing the loop body. The loop continues as long as the condition remains true. Ideal for situations where the number of iterations is unknown beforehand (Eck, Chapter 3, page 91)[^1]. Example (Printing numbers from 1 to 5):

```java
int i = 1;
while (i <= 5) {
  System.out.println(i);
  i++;
}
```

**Advantages:** Flexible for unknown iterations. Easy to understand and implement.

**Disadvantages:** Requires manual initialization and update of loop variable. Can be prone to infinite loops if the condition is never met.

- **do-while Loop:** This is an **exit-controlled loop**, guaranteeing execution of the loop body at least once. It evaluates the condition after the code block has run. Useful when you need to perform an action at least once, even if the condition is initially false (Eck, Chapter 3, page 93)[^1]. Example (Reading user input until a valid number is entered):

```java
int number;
do {
  System.out.print("Enter a number: ");
  number = scanner.nextInt();
} while (number <= 0);
```

**Advantages:** Ensures at least one iteration. Suitable for situations where initial execution is crucial.

**Disadvantages:** Can be less intuitive than while loops due to the post-check nature.

- **for Loop:** This is a concise way to manage initialization, condition checking, and increment/decrement in a single line. Often used for iterating over arrays or collections with a known number of elements (Eck, Chapter 3, page 97)[^1].Example (Printing elements of an array):

```java
int[] numbers = {1, 2, 3, 4, 5};
for (int i = 0; i < numbers.length; i++) {
  System.out.println(numbers[i]);
}
```

**Advantages:** Compact syntax for known iterations. Improves code readability.

**Disadvantages:** Less flexible compared to while loops for unknown iterations.

- In Summary, While, do-while, and for loops offer powerful tools for controlling repetition in Java programs. Understanding their nuances and choosing the right one based on your specific needs will lead to efficient and well-structured code.

# Question 2

- **if-else Statements:**(Eck, Chapter 3, page 115)[^1]

* **Strengths:**
    * **Flexibility:** Can handle any type of condition, including comparisons, boolean expressions, and complex logic.
    * **Readability for simple conditions:** Easy to understand for basic checks.
* **Weaknesses:**
    * **Readability for complex logic:** Nested if-else statements can become convoluted and error-prone.
    * **Maintainability:** Modifications require revisiting all conditions.
    * **Performance (rare):** In some cases, with many nested conditions, performance might be slightly slower than switch.

- **switch Statements:**

* **Strengths:**
    * **Readability for multiple choices:** Clear structure for handling various options based on a single value.
    * **Maintainability:** Adding/removing cases is easier without affecting other logic.
    * **Performance (potential):** Can be faster for many equally likely cases due to efficient lookup mechanisms.
* **Weaknesses:**
    * **Limited expression type:** Only works with integer, character, or String expressions for value comparison.
    * **Fall-through behavior:** Requires explicit `break` statements to prevent unintended execution of subsequent cases.


**Real-world examples:**

* **if-else is better for:**
    * Checking user input validity: `if (age >= 18) { ... } else { ... }`
    * Complex calculations with multiple conditions: Verifying complex data for processing.
* **switch is better for:**
    * Handling menu options: `switch (choice) { case 1: ...; break; case 2: ...; break; default: ... }`
    * Day of the week processing: Selecting actions based on an integer representing the day (1-7).

**Combining if-else and switch:**

Sometimes, both approaches can be used together. Imagine a program processing a grade character (A, B, C, etc.). You can use a `switch` to handle each letter grade case, but within a case, you might need an `if-else` to differentiate between plus/minus grades (e.g., `A+`, `B-`).

**Personal Experience:**

During a project, I used a `switch` to handle different file extensions for processing. Each case contained logic specific to the file type. This kept the code clean and easy to understand, especially when adding support for new extensions. However, when validating user input with complex rules, `if-else` statements were necessary to ensure all conditions were met.

**Choosing the Right Approach:**

The best choice depends on the specific situation. Consider:

* **Condition type:** Can you use a simple comparison for a `switch`?
* **Readability:** Will the code be easier to understand with one approach over the other?
* **Maintainability:** How easy will it be to modify the logic in the future?

# References

[^1]: Eck, David J. (2022). Introduction to Programming Using Java. https://math.hws.edu/
javanotes/index.html
