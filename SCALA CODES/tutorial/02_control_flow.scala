/* ============================================================
   LESSON 2: CONTROL FLOW - if/else, match (switch), when
   ============================================================
   MENU-DRIVEN PROGRAMS 101 (MOST IMPORTANT FOR YOUR ASSESSMENT!)

   The pattern for EVERY menu-driven program:
   1. Loop forever (while(true) or do-while) so menu keeps showing
   2. Show menu options
   3. Read user's choice
   4. match/if on the choice and do the work
   5. Option to EXIT breaks the loop
   ============================================================ */

object ControlFlow {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ---------- PART 1: if / else if / else ----------
        print("Enter your percentage: ")
        val p = sc.nextDouble()

        if (p >= 90) {
            println("Grade: A+")
        } else if (p >= 80) {
            println("Grade: A")
        } else if (p >= 70) {
            println("Grade: B")
        } else if (p >= 60) {
            println("Grade: C")
        } else if (p >= 40) {
            println("Grade: D")
        } else {
            println("Grade: F (Fail)")
        }

        // Short form: if..else as an EXPRESSION (stores a value!)
        val result = if (p >= 40) "PASS" else "FAIL"
        println(s"Result: $result")

        // ---------- PART 2: MATCH = Scala's SWITCH ----------
        // This is THE most important thing for menu-driven programs!
        println("\n--- Simple match ---")
        val day = 3

        val dayName = day match {
            case 1 => "Monday"
            case 2 => "Tuesday"
            case 3 => "Wednesday"
            case 4 => "Thursday"
            case 5 => "Friday"
            case 6 => "Saturday"
            case 7 => "Sunday"
            case _ => "Invalid day"     // _ = default (else case)
        }
        println(s"Day $day is $dayName")

        // match with STRINGS
        val fruit = "apple"
        fruit match {
            case "apple"  => println("It's an apple")
            case "mango"  => println("It's a mango")
            case "banana" => println("It's a banana")
            case _        => println("Unknown fruit")
        }

        // match with RANGES and CONDITIONS (using if guards)
        print("\nEnter marks: ")
        val m = sc.nextInt()
        m match {
            case x if x >= 90 => println("Outstanding!")
            case x if x >= 75 => println("Very Good!")
            case x if x >= 60 => println("Good")
            case x if x >= 40 => println("Needs Improvement")
            case _            => println("FAIL")
        }

        // ---------- PART 3: THE CLASSIC MENU-DRIVEN PROGRAM ----------
        // THE PATTERN YOU MUST MEMORIZE!
        var choice = 0
        while (choice != 5) {
            println("\n=========== CALCULATOR MENU ===========")
            println("1. Addition")
            println("2. Subtraction")
            println("3. Multiplication")
            println("4. Division")
            println("5. Exit")
            println("========================================")
            print("Enter your choice (1-5): ")
            choice = sc.nextInt()

            choice match {
                case 1 =>
                    print("Enter two numbers: ")
                    val a = sc.nextInt()
                    val b = sc.nextInt()
                    println(s"$a + $b = ${a + b}")

                case 2 =>
                    print("Enter two numbers: ")
                    val a = sc.nextInt()
                    val b = sc.nextInt()
                    println(s"$a - $b = ${a - b}")

                case 3 =>
                    print("Enter two numbers: ")
                    val a = sc.nextInt()
                    val b = sc.nextInt()
                    println(s"$a * $b = ${a * b}")

                case 4 =>
                    print("Enter two numbers: ")
                    val a = sc.nextInt()
                    val b = sc.nextInt()
                    if (b != 0)
                        println(s"$a / $b = ${a / b.toDouble}")
                    else
                        println("Cannot divide by zero!")

                case 5 =>
                    println("Thank you! Goodbye!")

                case _ =>
                    println("Invalid choice! Please try again.")
            }
        }

        // ---------- PART 4: NESTED if ----------
        print("\nEnter age: ")
        val age = sc.nextInt()

        if (age >= 18) {
            if (age >= 60)
                println("Senior Citizen")
            else
                println("Adult")
        } else {
            println("Minor")
        }

        // ---------- PART 5: Logical operators in conditions ----------
        print("\nEnter marks and attendance: ")
        val marks = sc.nextInt()
        val attendance = sc.nextInt()

        if (marks >= 40 && attendance >= 75)
            println("Eligible for exam")
        else if (marks >= 40 || attendance >= 75)
            println("Partially eligible - check with dept")
        else
            println("Not eligible!")

        println("\nProgram finished!")
    }
}