/* ============================================================
   PRACTICE 2: MOCK ASSESSMENT - Array & String Programs
   ============================================================ */

object Practice2 {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        var choice = 0
        while (choice != 7) {
            println("\n==== ARRAY & STRING PROGRAMS MENU ====")
            println("1. Array - largest, smallest, sum, average")
            println("2. Array - linear search")
            println("3. Array - count even/odd, reverse, sort")
            println("4. String - palindrome, reverse, vowels")
            println("5. String - count words & character frequency")
            println("6. 2D Array - matrix add & display")
            println("7. Exit")
            println("======================================")
            print("Choice: ")
            choice = sc.nextInt()

            choice match {
                case 1 =>
                    print("How many elements? ")
                    val n = sc.nextInt()
                    val arr = new Array[Int](n)
                    for (i <- 0 until n) {
                        print(s"Element ${i + 1}: ")
                        arr(i) = sc.nextInt()
                    }
                    println(s"Array: ${arr.mkString(", ")}")
                    println(s"Largest = ${arr.max}")
                    println(s"Smallest = ${arr.min}")
                    println(s"Sum = ${arr.sum}")
                    println(s"Average = ${arr.sum.toDouble / n}")

                case 2 =>
                    print("How many elements? ")
                    val n = sc.nextInt()
                    val arr = new Array[Int](n)
                    for (i <- 0 until n) {
                        print(s"Element ${i + 1}: ")
                        arr(i) = sc.nextInt()
                    }
                    print("Search for: ")
                    val key = sc.nextInt()
                    var pos = -1
                    for (i <- 0 until n if pos == -1)
                        if (arr(i) == key) pos = i
                    if (pos != -1) println(s"Found at index $pos")
                    else println("Not found!")

                case 3 =>
                    print("How many elements? ")
                    val n = sc.nextInt()
                    val arr = new Array[Int](n)
                    for (i <- 0 until n) {
                        print(s"Element ${i + 1}: ")
                        arr(i) = sc.nextInt()
                    }
                    println(s"Original: ${arr.mkString(", ")}")
                    println(s"Reversed: ${arr.reverse.mkString(", ")}")
                    println(s"Ascending: ${arr.sorted.mkString(", ")}")
                    println(s"Descending: ${arr.sorted.reverse.mkString(", ")}")
                    println(s"Evens = ${arr.filter(_ % 2 == 0).mkString(", ")}")
                    println(s"Odds = ${arr.filter(_ % 2 != 0).mkString(", ")}")

                case 4 =>
                    println("Enter a string: ")
                    sc.nextLine()   // consume leftover newline
                    val s = sc.nextLine()

                    if (s == s.reverse) println(s"'$s' is a PALINDROME")
                    else println(s"'$s' is NOT a palindrome")

                    println(s"Reversed: ${s.reverse}")

                    var v = 0
                    for (c <- s.toLowerCase if "aeiou".contains(c)) v += 1
                    println(s"Vowels = $v, Consonants = ${s.count(_.isLetter) - v}")

                case 5 =>
                    println("Enter a sentence: ")
                    sc.nextLine()
                    val sen = sc.nextLine()
                    val words = sen.trim.split("\\s+")
                    println(s"Word count = ${words.length}")

                    println("Enter a character: ")
                    val ch = sc.next().charAt(0)
                    var count = 0
                    for (c <- sen if c == ch) count += 1
                    println(s"Frequency of '$ch' = $count")

                case 6 =>
                    print("Rows and columns (r c): ")
                    val r = sc.nextInt(); val c = sc.nextInt()
                    val m1 = Array.ofDim[Int](r, c)
                    val m2 = Array.ofDim[Int](r, c)

                    println("Matrix 1:")
                    for (i <- 0 until r; j <- 0 until c) {
                        print(s"m1($i,$j): ")
                        m1(i)(j) = sc.nextInt()
                    }
                    println("Matrix 2:")
                    for (i <- 0 until r; j <- 0 until c) {
                        print(s"m2($i,$j): ")
                        m2(i)(j) = sc.nextInt()
                    }

                    println("\nMatrix 1:")
                    for (i <- 0 until r) {
                        for (j <- 0 until c) print(s"${m1(i)(j)} ")
                        println()
                    }
                    println("Matrix 2:")
                    for (i <- 0 until r) {
                        for (j <- 0 until c) print(s"${m2(i)(j)} ")
                        println()
                    }
                    println("Sum:")
                    for (i <- 0 until r) {
                        for (j <- 0 until c) print(s"${m1(i)(j) + m2(i)(j)} ")
                        println()
                    }

                case 7 => println("Bye!")
                case _ => println("Invalid choice!")
            }
        }
    }
}