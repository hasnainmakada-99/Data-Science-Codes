/* ============================================================
   LESSON 4: FUNCTIONS - def, parameters, return types, recursion
   ============================================================
   A function is a reusable block of code.
   Syntax:
       def functionName(param1: Type1, param2: Type2): ReturnType = {
           // body
           returnValue   // last line = what function returns
       }

   NO return keyword needed - Scala returns the LAST expression!
   ============================================================ */

object Functions {
    def main(args: Array[String]): Unit = {

        // ---------- 1. Function with NO parameters, NO return ----------
        def sayHello(): Unit = {
            println("Hello, World!")
        }

        // ---------- 2. Function with PARAMETERS and NO return ----------
        def greet(name: String): Unit = {
            println(s"Hello, $name!")
        }

        // ---------- 3. Function with parameters and RETURN value ----------
        def add(a: Int, b: Int): Int = {
            a + b            // last expression is returned
        }

        // Better: write functions in ONE LINE (common style)
        def addOneLine(a: Int, b: Int): Int = a + b

        // ---------- 4. Example functions for your lab ----------
        def factorial(n: Int): Int = {
            var f = 1
            for (i <- 1 to n)
                f *= i
            f
        }

        def isEven(n: Int): Boolean = n % 2 == 0

        def maxOf(a: Int, b: Int): Int = {
            if (a > b) a else b
        }

        // ---------- 5. Calling functions ----------
        sayHello()
        greet("Ravi")
        println(s"5 + 3 = ${add(5, 3)}")
        println(s"Factorial of 5 = ${factorial(5)}")
        println(s"Is 10 even? ${isEven(10)}")
        println(s"Max of 10 and 20 = ${maxOf(10, 20)}")

        // Call function INSIDE another function call
        println(s"Factorial of 3 + Factorial of 4 = ${factorial(3) + factorial(4)}")

        // ---------- 6. DEFAULT PARAMETER VALUES ----------
        def power(base: Int, exp: Int = 2): Int = {
            math.pow(base, exp).toInt
        }
        println(s"5^2 = ${power(5)}")        // exp defaults to 2
        println(s"5^3 = ${power(5, 3)}")     // exp = 3

        // ---------- 7. NAMED ARGUMENTS (order doesn't matter) ----------
        println(s"Named args: ${power(exp = 3, base = 2)}")

        // ---------- 8. RECURSION (function calling itself) ----------
        // VERY IMPORTANT - faculty loves recursion!

        def factorialRec(n: Int): Int = {
            if (n <= 1) 1
            else n * factorialRec(n - 1)
        }

        def fibonacciRec(n: Int): Int = {
            if (n <= 1) n
            else fibonacciRec(n - 1) + fibonacciRec(n - 2)
        }

        def sumOfDigits(n: Int): Int = {
            if (n == 0) 0
            else n % 10 + sumOfDigits(n / 10)
        }

        println(s"factorialRec(6) = ${factorialRec(6)}")
        println(s"fibonacciRec(7) = ${fibonacciRec(7)}")
        println(s"sumOfDigits(12345) = ${sumOfDigits(12345)}")

        // ---------- 9. FUNCTION AS AN EXPRESSION ----------
        // can be stored in val
        val triple = (x: Int) => x * 3     // lambda / anonymous function
        println(s"triple(7) = ${triple(7)}")

        // ---------- 10. CALLING A FUNCTION ON EVERY ELEMENT ----------
        // (Preview: Higher Order Functions - covered in Lesson 10)
        val list = List(1, 2, 3, 4, 5)
        println(s"Doubled: ${list.map(x => x * 2)}")     // List(2,4,6,8,10)
        println(s"Evens:   ${list.filter(x => x % 2 == 0)}") // List(2,4)
        println(s"Sum:     ${list.reduce((x, y) => x + y)}") // 15

        // ============ MENU-DRIVEN FUNCTION PROGRAM ============
        println("\n=========== FUNCTION CALCULATOR MENU ===========")
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // Define all operations as functions
        def addFunc(a: Int, b: Int): Int = a + b
        def subFunc(a: Int, b: Int): Int = a - b
        def mulFunc(a: Int, b: Int): Int = a * b
        def divFunc(a: Int, b: Int): Double = a.toDouble / b
        def factFunc(n: Int): Int = {
            if (n <= 1) 1 else n * factFunc(n - 1)
        }

        var choice = 0
        while (choice != 6) {
            println("1. Add")
            println("2. Subtract")
            println("3. Multiply")
            println("4. Divide")
            println("5. Factorial")
            println("6. Exit")
            print("Enter choice: ")
            choice = sc.nextInt()

            choice match {
                case 1 =>
                    print("Enter a, b: ")
                    val (x, y) = (sc.nextInt(), sc.nextInt())  // tuple trick!
                    println(s"$x + $y = ${addFunc(x, y)}")
                case 2 =>
                    print("Enter a, b: ")
                    val x = sc.nextInt(); val y = sc.nextInt()
                    println(s"$x - $y = ${subFunc(x, y)}")
                case 3 =>
                    print("Enter a, b: ")
                    val x = sc.nextInt(); val y = sc.nextInt()
                    println(s"$x * $y = ${mulFunc(x, y)}")
                case 4 =>
                    print("Enter a, b: ")
                    val x = sc.nextInt(); val y = sc.nextInt()
                    if (y != 0) println(s"$x / $y = ${divFunc(x, y)}")
                    else println("Cannot divide by 0!")
                case 5 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    println(s"$n! = ${factFunc(n)}")
                case 6 =>
                    println("Bye!")
                case _ =>
                    println("Invalid choice")
            }
        }

        // ---------- 11. IMPORTANT: Parameter types & return types ----------
        // Rule 1: Every parameter MUST have a type:  (a: Int, b: Int)
        // Rule 2: Return type is optional but good practice: : Int
        // Rule 3: Unit = returns nothing (like void in Java/C)
        // Rule 4: varargs (...): accept any number of args

        def sumAll(nums: Int*): Int = {    // Int* = any number of Ints
            var s = 0
            for (n <- nums) s += n
            s
        }
        println(s"sumAll(1,2,3) = ${sumAll(1, 2, 3)}")
        println(s"sumAll(1,2,3,4,5,6) = ${sumAll(1, 2, 3, 4, 5, 6)}")
    }
}