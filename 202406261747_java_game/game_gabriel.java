// java.util.Scanner is for user input
// and java.util.Random to choose random words.
// Eck, Chapter 2, page 48
import java.util.Scanner;
// Eck, Chapter 5, page 226
import java.util.Random;

public class RhymeRider {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();

    // Define a list of words. Could be improved
    String[] wordList = {
      "glove",
      "love",
      "cat",
      "hat",
      "tree",
      "sea",
      "fun",
      "sun",
      "age",
      "wage",
    };

    int score = 0;
    int totalQuestions = 0;
    boolean keepPlaying = true;

    System.out.println("Let's play a rhyme game!");
    // The game loop keeps running
    // until the user decides to stop (keepPlaying = false).
    while (keepPlaying) {
      // In each loop, a random word is chosen,
      // and the user is prompted to guess a rhyming word.
      // A basic isRhyme function checks if the last
      // two characters of the words match (a more sophisticated
      // rhyming check can be implemented).
      int randomIndex = random.nextInt(wordList.length);
      String word = wordList[randomIndex];

      System.out.println("What rhymes with " + word + "?");
      String guess = scanner.nextLine();

      // Check if the guess rhymes
      // Eck, Chapter 3, page 79
      if (isRhyme(word, guess)) {
        System.out.println("Great rhyme!");
        // The score is kept track of,
        // and the game displays messages based on the guess.
        score++;
        totalQuestions++;
      } else {
        System.out.println("Hmm, not quite. Try again!");
        totalQuestions++;
      }

      System.out.println("Continue riding? (y/n)");
      String choice = scanner.nextLine().toLowerCase();
      keepPlaying = choice.equals("y");
    }

     double percentage = (double) score / totalQuestions * 100;
    System.out.println("Thanks for playing Rhyme Game! Your've made "
    + score + " out of "
    + totalQuestions +
    " (" + percentage + "%)");
  }

  /**
   * Checks if two words rhyme (basic implementation)
   *
   * @param word1 First word
   * @param word2 Second word
   * @return True if the words rhyme, false otherwise
   */
  public static boolean isRhyme(String word1, String word2) {
    // Simple check based on the last two characters (can be improved)
    // Eck, Chapter 2, page 34
    return word1.toLowerCase().
           endsWith(word2.
           toLowerCase().
           substring(word2.length() - 2));
  }
}
