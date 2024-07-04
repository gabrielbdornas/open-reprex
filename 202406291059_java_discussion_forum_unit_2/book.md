
<!-- https://www.pdfforge.org/online/en/markdown-to-pdf -->

# Basic library system in Java

This program simulates a basic library system. It allows users to manage books through a menu-driven interface. Users can choose to add new books, specifying title, author, and quantity. If the book already exists, the program updates the total quantity.

For borrowing and returning books, users need to provide the title and the number of books. The program checks the library's stock and only allows borrowing if enough copies are available. It then updates the quantity accordingly and provides success or error messages. The program also handles situations where users enter invalid choices or try to borrow/return books not found in the library.

```java
// java.util.HashMap is for to
// store book titles as keys and
// their available quantities as values
// Eck, Chapter 10, page 523
import java.util.HashMap;
// java.util.Scanner is for user input
// Eck, Chapter 10, page 551
import java.util.Scanner;

public class LibrarySystem {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, Integer> library = new HashMap<>();

        int choice;

        // Eck, Chapter 3, page 93
        do {
            System.out.
            println("\nWelcome to your Library Management System");
            System.out.println("1. Add Books");
            System.out.println("2. Borrow Books");
            System.out.println("3. Return Books");
            System.out.println("4. Exit");
            System.out.print("What do you want to do? Select one number choice: ");

            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            // Eck, Chapter 3, page 113
            switch (choice) {
                case 1:
                    addBook(library, scanner);
                    break;
                case 2:
                    borrowBook(library, scanner);
                    break;
                case 3:
                    returnBook(library, scanner);
                    break;
                case 4:
                    System.out.println("Exiting Library System. Bye...");
                    break;
                default:
                    System.
                    out.println("Invalid choice!Select one number choice:");
            }
        } while (choice != 4);

        scanner.close();
    }

    private static void
        addBook(HashMap<String, Integer> library, Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();
        System.out.print("Enter author: ");
        String author = scanner.nextLine();
        System.out.print("Enter quantity: ");
        int quantity = scanner.nextInt();

        if (library.containsKey(title)) {
            library.put(title, library.get(title) + quantity);
            System.
            out.println(quantity + " copies of " + title + " added successfully!");
        } else {
            library.put(title, quantity);
            System.out.println(title + " by " + author + " added to library!");
        }
    }

    private static void borrowBook(HashMap<String, Integer> library, Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();
        System.out.print("Enter number of books to borrow: ");
        int borrowQuantity = scanner.nextInt();

        if (library.containsKey(title)) {
            int availableQuantity = library.get(title);
            if (availableQuantity >= borrowQuantity) {
                library.put(title, availableQuantity - borrowQuantity);
                System.
                out.println(borrowQuantity + " copies of " + title + " borrowed successfully!");
            } else {
                System.out.println("Sorry, only " + availableQuantity + " copies of " + title + " are available!");
            }
        } else {
            System.
            out.println("Book not found in the library!");
        }
    }

    private static void returnBook(HashMap<String, Integer> library, Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();
        System.out.print("Enter number of books to return: ");
        int returnQuantity = scanner.nextInt();

        if (library.containsKey(title)) {
            library.put(title, library.get(title) + returnQuantity);
            System.
            out.println(returnQuantity + " copies of " + title + " returned successfully!");
        } else {
            System.out.println("Book not found in the library!");
        }
    }
}
```

Here's a breakdown of the program's flow:

* **Menu System:**
    * Presents a menu with options for adding, borrowing, returning books, and exiting.
    * Uses a loop to keep displaying the menu until the user chooses to exit.
* **Adding Books:**
    * Prompts the user for book title, author, and quantity.
    * Checks if the book already exists in the library (using a HashMap).
        * If it exists, updates the existing quantity with the new quantity.
        * If it's a new book, adds a new entry to the library with the provided title, author, and quantity.
* **Borrowing Books:**
    * Prompts the user for the book title and the number of books to borrow.
    * Checks if the library has enough copies available (compares requested quantity with existing quantity).
        * If enough copies are available, decreases the library's quantity by the borrowed amount and displays a success message.
        * If not enough copies are available, displays an error message indicating how many copies are actually available.
* **Returning Books:**
    * Prompts the user for the book title and the number of books to return.
    * Checks if the book exists in the library.
        * If it exists, increases the library's quantity by the returned amount and displays a success message.
        * If not found, displays an error message.
* **Error Handling:**
    * Handles invalid user input for menu choices and book quantities.
    * Provides informative error messages for situations like trying to borrow/return books not found in the library.

# References

Eck, David J. (2022). Introduction to Programming Using Java. https://math.hws.edu/
javanotes/index.html
