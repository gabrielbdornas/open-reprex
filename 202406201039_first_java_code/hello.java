// https://www.youtube.com/watch?v=RLi1rOgTRbA

public class hello {
  public static void main (String[] args) {
    // it must be on doble quotes
    System.out.println("Hello World!");

    // Variables
    int num = 5;
    double numDouble = 4.6;
    // it must be on single quotes
    char firstInitial = 'k';
    String name = "Gabriel";
    boolean isHome = true;

    System.out.println(num);
    System.out.println(numDouble);
    System.out.println(firstInitial);
    System.out.println(name);
    System.out.println(isHome);

    if (name.equals("Gabriel")) {
      System.out.println("Print your name: Great!");
    } else {
      System.out.println("Print your name: Tel me your name.");
    }

    // not iqual !=
    // And &&
    // Or ||
    if (num < 18) {
      System.out.println("You are not an adult.");
    }

    System.out.println("While loop example");
    while(num < 18) {
      System.out.println("While test: You're not an adult");
      // num + 1
      num ++;
    }

    System.out.println("For loop example");
    for (int i = 0; i < 20; i++){
      System.out.println(i);
    }

    System.out.println("Do loop example");
    int x = 0;
    do {
      System.out.println("Print this 10 times");
      x ++;
    } while(x < 10);


  }

}
