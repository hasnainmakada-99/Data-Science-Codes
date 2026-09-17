/* ============================================================
   LESSON 3: LOOPS - for loop, while, do-while
   ============================================================
   Three ways to repeat:
   1. for    -> used when you KNOW how many times (most common)
   2. while  -> used when you DON'T know how many times (condition first)
   3. do-while -> runs at least once (condition last)
   ============================================================ */

object Loops {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ============ PART 1: FOR LOOP ============

        // Pattern 1: "to" includes the last number
        println("1 to 5:")
        for (i <- 1 to 5)
            println(s"i = $i")          // prints 1,2,3,4,5

        // Pattern 2: "until" excludes the last number
        println("\n1 until 5:")
        for (i <- 1 until 5)
            println(s"i = $i")          // prints 1,2,3,4

        // Pattern 3: with step
        println("\n1 to 10 by 2 (even/odd stepping):")
        for (i <- 1 to 10 by 2)
            print(s"$i ")               // prints 1 3 5 7 9

        println("\n10 to 1 by -1 (reverse):")
        for (i <- 10 to 1 by -1)
            print(s"$i ")               // prints 10 9 8 ... 1

        // Pattern 4: with braces { } and multiple statements
        println("\n\nSum of 1 to 100:")
        var sum = 0
        for (i <- 1 to 100) {
            sum += i
        }
        println(s"Sum = $sum")          // 5050

        // Pattern 5: loop over a collection
        val names = Array("Alice", "Bob", "Charlie")
        println("\nNames:")
        for (name <- names)
            println(name)

        // Pattern 6: loop with INDEX (until + length)
        println("\nNames with index:")
        for (i <- 0 until names.length)
            println(s"names($i) = ${names(i)}")

        // Pattern 7: loop over a STRING (each character)
        println("\nCharacters of 'Scala':")
        for (ch <- "Scala")
            print(ch + " ")

        // Pattern 8: if CONDITION inside loop (like a filter)
        println("\n\nOnly even numbers from 1 to 20:")
        for (i <- 1 to 20 if i % 2 == 0)
            print(s"$i ")

        // Pattern 9: NESTED for loops (multiplication table!)
        println("\n\n--- Multiplication Table (2 to 5) ---")
        for (i <- 2 to 5) {
            for (j <- 1 to 10) {
                println(s"$i x $j = ${i * j}")
            }
            println() // blank line between tables
        }

        // ============ PART 2: WHILE LOOP ============
        // Check condition FIRST, then run.
        // If condition is false from start, loop runs ZERO times.

        println("\n--- while loop: sum user numbers until 0 ---")
        var total = 0
        var num = -1
        while (num != 0) {
            print("Enter a number (0 to stop): ")
            num = sc.nextInt()
            total += num
        }
        println(s"Total = $total")

        // ============ PART 3: DO-WHILE LOOP ============
        // Runs FIRST, then checks. Always runs at least once.
        // BEST for menu-driven programs!

        println("\n--- do-while: simple menu ---")
        var option = 0
        do {
            println("\n1. Say Hello")
            println("2. Say Goodbye")
            println("3. Exit")
            print("Choose: ")
            option = sc.nextInt()

            if (option == 1) println("Hello there!")
            else if (option == 2) println("Goodbye!")
            else if (option == 3) println("Exiting...")
            else println("Invalid!")

        } while (option != 3)

        // ============ PART 4: break and continue ============
        // Scala doesn't have "break" or "continue" like Java/C.
        // Use a boolean flag - this pattern appears in exams!

        println("\n--- break simulation using flag ---")
        var found = false
        for (i <- 1 to 100 if !found) {
            println(s"Checking $i...")
            if (i == 5) found = true     // "break" after 5
        }

        // ============ CLASSIC LAB PROGRAMS ============

        // 1) Factorial using for loop
        print("\nEnter a number for factorial: ")
        val n = sc.nextInt()
        var fact = 1
        for (i <- 1 to n)
            fact *= i
        println(s"Factorial of $n = $fact")

        // 2) Prime number check
        print("Enter a number to check prime: ")
        val p = sc.nextInt()
        var isPrime = true
        if (p <= 1) isPrime = false
        for (i <- 2 to math.sqrt(p).toInt if isPrime) {
            if (p % i == 0) isPrime = false
        }
        if (isPrime) println(s"$p is PRIME")
        else println(s"$p is NOT prime")

        // 3) Fibonacci series
        print("How many Fibonacci terms? ")
        val terms = sc.nextInt()
        var a = 0
        var b = 1
        print(s"Fibonacci series ($terms terms): $a $b")
        for (_ <- 3 to terms) {
            val next = a + b
            print(s" $next")
            a = b
            b = next
        }
        println()

        // 4) Palindrome number
        print("Enter a number: ")
        val orig = sc.nextInt()
        var rev = 0
        var temp = orig
        while (temp > 0) {
            rev = rev * 10 + temp % 10    // extract last digit
            temp = temp / 10              // remove last digit
        }
        if (rev == orig) println(s"$orig is a PALINDROME")
        else println(s"$orig is NOT a palindrome")

        println("\nAll loop concepts covered!")
    }
}