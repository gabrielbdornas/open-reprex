import java.util.Scanner;

public class QuizGame {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = 0;
        int totalQuestions = 5;

        // Define questions and answers (modify these with your own content)
        String[] questions = {
                "What is the capital of France? \nA) London \nB) Paris \nC) Berlin \nD) Rome",
                "What is the largest planet in our solar system? \nA) Earth \nB) Mars \nC) Jupiter \nD) Venus",
                "What year did the first iPhone launch? \nA) 2004 \nB) 2007 \nC) 2010 \nD) 2013",
                "How many sides does a hexagon have? \nA) 4 \nB) 5 \nC) 6 \nD) 8",
                "What is the symbol for the element gold? \nA) Fe \nB) Au \nC) Cu \nD) Ag"
        };

        char[] correctAnswers = {'B', 'C', 'B', 'C', 'B'};

        // Loop through each question
        for (int i = 0; i < totalQuestions; i++) {
            System.out.println(questions[i]);
            char userAnswer = getUserAnswer(scanner);

            // Check user answer and update score
            if (checkAnswer(userAnswer, correctAnswers[i])) {
                score++;
                System.out.println("Correct!\n");
            } else {
                System.out.println("Incorrect. The correct answer is " + correctAnswers[i] + ".\n");
            }
        }

        // Calculate and display final score
        double percentage = (double) score / totalQuestions * 100;
        System.out.println("Your final score is " + score + " out of " + totalQuestions + ".");
        System.out.println("Percentage: " + percentage + "%");
    }

    /**
     * Gets the user's answer (A, B, C, or D)
     *
     * @param scanner Scanner object to read user input
     * @return User's answer as a character (A, B, C, or D)
     */
    public static char getUserAnswer(Scanner scanner) {
        char answer;
        do {
            System.out.print("Enter your answer (A, B, C, or D): ");
            answer = scanner.nextLine().toUpperCase().charAt(0);
        } while (answer != 'A' && answer != 'B' && answer != 'C' && answer != 'D');
        return answer;
    }

    /**
     * Checks if the user's answer matches the correct answer
     *
     * @param userAnswer User's answer as a character (A, B, C, or D)
     * @param correctAnswer Correct answer as a character (A, B, C, or D)
     * @return True if the answer is correct, false otherwise
     */
    public static boolean checkAnswer(char userAnswer, char correctAnswer) {
        return userAnswer == correctAnswer;
    }
}
