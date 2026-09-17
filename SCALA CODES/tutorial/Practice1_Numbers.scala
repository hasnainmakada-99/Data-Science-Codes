/* ============================================================
   PRACTICE 1: MOCK ASSESSMENT - Number & Math Operations
   (Everything a menu-driven program might ask)
   ============================================================ */

object Practice1 {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        var choice = 0
        while (choice != 11) {
            println("\n=========== NUMBER PROGRAMS MENU ===========")
            println(" 1. Factorial of a number")
            println(" 2. Check prime")
            println(" 3. Fibonacci series")
            println(" 4. Palindrome number")
            println(" 5. Reverse a number")
            println(" 6. Count digits")
            println(" 7. Armstrong number")
            println(" 8. Sum of digits")
            println(" 9. GCD of two numbers")
            println("10. LCM of two numbers")
            println("11. Exit")
            println("=============================================")
            print("Enter your choice: ")
            choice = sc.nextInt()

            // Helper functions (defined inside match for clarity)
            choice match {
                case 1 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var f = 1
                    for (i <- 1 to n) f *= i
                    println(s"$n! = $f")

                case 2 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var prime = n > 1
                    for (i <- 2 to math.sqrt(n).toInt if prime)
                        if (n % i == 0) prime = false
                    println(if (prime) s"$n is PRIME" else s"$n is NOT prime")

                case 3 =>
                    print("Enter number of terms: ")
                    val t = sc.nextInt()
                    var a = 0; var b = 1
                    print(s"Series: $a $b")
                    for (_ <- 3 to t) {
                        val c = a + b
                        print(s" $c")
                        a = b
                        b = c
                    }
                    println()

                case 4 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var rev = 0; var temp = n
                    while (temp > 0) {
                        rev = rev * 10 + temp % 10
                        temp /= 10
                    }
                    println(if (rev == n) s"$n is a PALINDROME" else s"$n is NOT")

                case 5 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var rev = 0; var temp = n
                    while (temp > 0) {
                        rev = rev * 10 + temp % 10
                        temp /= 10
                    }
                    println(s"Reverse of $n = $rev")

                case 6 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var temp = n; var count = 0
                    while (temp > 0) {
                        count += 1
                        temp /= 10
                    }
                    println(s"$n has $count digits")
                    // or: println(s"Digits = ${n.toString.length}")

                case 7 =>
                    // Armstrong: 153 = 1^3 + 5^3 + 3^3 = 153
                    print("Enter n: ")
                    val n = sc.nextInt()
                    val digits = n.toString.length
                    var sum = 0; var temp = n
                    while (temp > 0) {
                        sum += math.pow(temp % 10, digits).toInt
                        temp /= 10
                    }
                    println(if (sum == n) s"$n is an ARMSTRONG number"
                            else s"$n is NOT an Armstrong number")

                case 8 =>
                    print("Enter n: ")
                    val n = sc.nextInt()
                    var temp = n; var s = 0
                    while (temp > 0) {
                        s += temp % 10
                        temp /= 10
                    }
                    println(s"Sum of digits of $n = $s")

                case 9 =>
                    print("Enter two numbers: ")
                    val x = sc.nextInt(); val y = sc.nextInt()
                    var a = x; var b = y
                    while (b != 0) {
                        val r = a % b
                        a = b
                        b = r
                    }
                    println(s"GCD($x, $y) = $a")

                case 10 =>
                    print("Enter two numbers: ")
                    val x = sc.nextInt(); val y = sc.nextInt()
                    var a = x; var b = y
                    while (b != 0) {
                        val r = a % b
                        a = b
                        b = r
                    }
                    val gcd = a
                    val lcm = (x * y) / gcd
                    println(s"LCM($x, $y) = $lcm")

                case 11 =>
                    println("Thank you! Goodbye!")

                case _ =>
                    println("Invalid choice! Enter 1-11.")
            }
        }
    }
}