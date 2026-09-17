/* ============================================================
   LESSON 1: SCALA BASICS - Hello, Variables, Types, Input
   ============================================================

   HOW TO RUN SCALA PROGRAMS
   --------------------------
   Option 1 (Online - EASIEST for practice):
       Go to https://scastie.scala-lang.org  <- paste code, click RUN

   Option 2 (If installed on your PC):
       scala 01_basics.scala          OR
       scalac 01_basics.scala  then  scala HelloBasics

   Remember: Every Scala program needs an "object" with "main" method.
   That's the starting point of your program.
   ============================================================ */

// The object name must match the filename for compiling.
// "def main(args: Array[String]): Unit" is the entry point.
object HelloBasics {
    def main(args: Array[String]): Unit = {

        // ---------- 1. PRINTING OUTPUT ----------
        // println = print + new line (goes to next line after printing)
        println("Hello, World!")
        println("Welcome to Scala!")

        // print = prints WITHOUT moving to next line
        print("Hello ")
        print("World")
        print(" (no new line here)")

        // Prints a blank line
        println()
        println() // another blank line

        // ---------- 2. VARIABLES: val vs var ----------
        // val  = VALUE (immutable / constant, CANNOT change)
        // var  = VARIABLE (mutable / CAN change)

        val age = 21            // val, integer
        println("Age is: " + age)  // + joins strings (concatenation)

        // age = 22  <-- ERROR! val cannot be reassigned

        var score = 50
        println("Score before: " + score)
        score = 75              // var CAN be changed
        println("Score after:  " + score)

        // ---------- 3. DATA TYPES ----------
        // Byte, Short, Int, Long     -> whole numbers
        // Float, Double              -> decimal numbers
        // Char                       -> single character
        // Boolean                    -> true / false
        // String                     -> text (sequence of chars)

        val b: Byte    = 100
        val s: Short   = 30000
        val i: Int     = 100000
        val l: Long    = 10000000000L     // add L for Long
        val f: Float   = 3.14f            // add f for Float
        val d: Double  = 3.14159265
        val c: Char    = 'A'
        val flag: Boolean = true
        val name: String = "Ravi"

        println("Byte: " + b + ", Int: " + i + ", Double: " + d)
        println("Char: " + c + ", Boolean: " + flag + ", String: " + name)

        // ---------- 4. TYPE INFERENCE ----------
        // Scala is smart - it guesses the type for you!
        val x = 10        // Scala knows x is Int
        val y = 3.5       // Scala knows y is Double
        val z = "Hello"   // Scala knows z is String

        // ---------- 5. STRING CONCATENATION (2 ways) ----------
        // Way 1: using +
        println("Value of x is " + x)

        // Way 2: String Interpolation using s"..."  (BEST way!)
        println(s"Value of x is $x")
        println(s"Value of x + y = ${x + y}")   // {} for expressions

        // ---------- 6. INPUT FROM USER (SCANNER) ----------
        // import allows us to use Scanner
        import java.util.Scanner
        val sc = new Scanner(System.in)

        print("Enter your name: ")
        val userName = sc.nextLine()      // reads a whole line (String)

        print("Enter your age: ")
        val userAge = sc.nextInt()        // reads an Int
        sc.nextLine()                     // IMPORTANT: consume leftover newline

        print("Enter your marks (decimal allowed): ")
        val marks = sc.nextDouble()       // reads a Double

        println(s"Hi $userName, you are $userAge years old with $marks marks!")

        // ---------- 7. READING MULTIPLE NUMBERS (for practice questions) ----------
        print("How many numbers? ")
        val n = sc.nextInt()

        var sum = 0
        for (i <- 1 to n) {
            print(s"Enter number $i: ")
            val num = sc.nextInt()
            sum = sum + num     // OR sum += num
        }
        println(s"Sum of $n numbers = $sum")

        // ---------- 8. KEYWORDS / RANGES you'll see everywhere ----------
        // 1 to 10      -> 1,2,3,...,10   (INCLUDES 10)
        // 1 until 10   -> 1,2,3,...,9    (EXCLUDES 10)
        // 1 to 10 by 2 -> 1,3,5,7,9
        // 10 to 1 by -1-> 10,9,8,...,1

        // ---------- 9. QUICK OPERATORS REVIEW ----------
        // Arithmetic:  +  -  *  /  %   (modulus = remainder)
        val a1 = 17
        val a2 = 5
        println(s"17 / 5 = ${a1 / a2}")      // 3 (integer division)
        println(s"17 % 5 = ${a1 % a2}")      // 2 (remainder)
        println(s"17.0 / 5 = ${17.0 / 5}")   // 3.4 (with decimal)
        println(s"2 ^ 5 (pow) = ${math.pow(2, 5)}") // 32.0

        // Comparison:  ==  !=  <  >  <=  >=   -> gives true/false
        // Logical:     &&  ||  !
        // Assignment:  +=  -=  *=  /=  %=

        println("Program ended successfully!")
    }
}