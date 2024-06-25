<!-- https://math.hws.edu/javanotes/c2/s1.html -->

- Here is a Java program to display the message "Hello World!". Don't expect to understand what's going on here just yet; some of it you won't really understand until a few chapters from now:

```java
/** A program to display the message
 *  "Hello World!" on standard output.
 */
public class HelloWorld {

   public static void main(String[] args) {
      System.out.println("Hello World!");
   }

}   // end of class HelloWorld
```
- The command that actually displays the message is `System.out.println("Hello World!");`.
- This command is an example of a subroutine call statement. It uses a "built-in subroutine" named `System.out.println` to do the actual work.
- Recall that a subroutine consists of the instructions for performing some task, chunked together and given a name.
- A built-in subroutine is one that is already defined as part of the language and therefore automatically available for use in any program.
- The first type begins with `//` and extends to the end of a line. There is a comment of this form on the last line of the above program. The computer ignores the `//` and everything that follows it on the same line.
- The second type of comment starts with `/*` and ends with `*/`, and it can extend over more than one line. The first three lines of the program are an example of this second type of comment.
- A comment that actually begins with `/**`, like this one does, has special meaning; it is a "Javadoc" comment that can be used to produce documentation for the program.
- All programming in Java is done inside "classes." The first line in the above program (not counting the comment) says that this is a class named `HelloWorld`. "HelloWorld," the name of the class, also serves as the name of the program. Not every class is a program. In order to define a program, a class must include a subroutine named `main`, with a definition that takes the form:

```java
public static void main(String[] args) {
      statements
}
```

- When you tell the Java interpreter to run the program, the interpreter calls this `main()` subroutine, and the statements that it contains are executed. Those statements make up the script that tells the computer exactly what to do when the program is executed.
- The `main()` routine can call other subroutines that are defined in the same class or even in other classes, but it is the `main()` routine that determines how and in what order the other subroutines are used.
- The word "public" in the first line of `main()` means that this routine can be called from outside the program. This is essential because the `main()` routine is called by the Java interpreter, which is something external to the program itself.
- As noted above, a subroutine can't exist by itself. It has to be part of a "class".
- Remember that `program-name` is a placeholder for the actual name! If the name of the class is `HelloWorld`, then the class must be saved in a file called `HelloWorld.java`.
- The layout of the program on the page, such as the use of blank lines and indentation, is not part of the syntax or semantics of the language.
- The computer doesn't care about layout—you could run the entire program together on one line as far as it is concerned. However, layout is important to human readers, and there are certain style guidelines for layout that are followed by most programmers.
