/* ============================================================
   LESSON 10: HIGHER ORDER FUNCTIONS - map, filter, reduce, etc.
   ============================================================
   These are FUNCTIONS THAT WORK ON COLLECTIONS.
   They accept a function and apply it to each element.
   VERY common in exams!

   THE BIG FOUR (memorize these):
   - map:      transform EVERY element  -> same count out
   - filter:   keep elements that PASS a condition -> fewer out
   - reduce:   combine all elements into ONE value
   - foreach:  do something with each element, no result

   Shorthand:  x => x * 2    (x goes in, x*2 comes out)
               _ * 2         (underscore = the element)
   ============================================================ */

object HigherOrder {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        val nums = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        // ==================== 1. MAP ====================
        println(s"Original:        $nums")

        // double each number
        println(s"Doubled (map):   ${nums.map(x => x * 2)}")
        // shorthand with _
        println(s"Doubled (_):     ${nums.map(_ * 2)}")
        // square each
        println(s"Squared:         ${nums.map(x => x * x)}")
        // to strings
        println(s"To strings:      ${nums.map(x => s"Num$x")}")
        // map on strings
        println(s"Uppercase names: ${List("ravi", "sita", "ram").map(_.toUpperCase)}")

        // ==================== 2. FILTER ====================
        println(s"\nEvens:           ${nums.filter(_ % 2 == 0)}")
        println(s"Odds:            ${nums.filter(_ % 2 != 0)}")
        println(s"Greater than 5:  ${nums.filter(_ > 5)}")
        println(s"Multiples of 3:  ${nums.filter(_ % 3 == 0)}")

        // ==================== 3. REDUCE ====================
        println(s"\nSum (reduce):    ${nums.reduce((a, b) => a + b)}")
        println(s"Product:         ${nums.reduce((a, b) => a * b)}")
        println(s"Max (reduce):    ${nums.reduce((a, b) => if (a > b) a else b)}")

        // ==================== 4. FOREACH ====================
        println("\nForeach (print each):")
        nums.foreach(x => print(s"$x "))     // or nums.foreach(println)
        println()

        // ==================== 5. COMBINING MAP + FILTER ====================
        println(s"\nEvens doubled:   ${nums.filter(_ % 2 == 0).map(_ * 2)}")
        println(s"Odd squares:     ${nums.filter(_ % 2 != 0).map(x => x * x)}")

        // ==================== 6. OTHER USEFUL ONES ====================
        // count - how many match condition
        println(s"\nCount of evens:  ${nums.count(_ % 2 == 0)}")

        // find - first match (returns Option)
        println(s"First > 5:       ${nums.find(_ > 5)}")   // Some(6)

        // exists / forall - true/false checks
        println(s"Any > 9?         ${nums.exists(_ > 9)}")
        println(s"All > 0?         ${nums.forall(_ > 0)}")

        // sortBy / sorted
        println(s"Sorted desc:     ${nums.sorted.reverse}")
        println(s"Sort by abs:     ${List(-5, 2, -1, 4).sortBy(_.abs)}")

        // take / drop
        println(s"Take 3:          ${nums.take(3)}")
        println(s"Drop 3:          ${nums.drop(3)}")

        // groupBy
        println(s"Group evens/odds: ${nums.groupBy(_ % 2 == 0)}")

        // zip - pair up two lists
        println(s"Zip:             ${List("a", "b").zip(List(1, 2))}")

        // ==================== 7. REAL-WORLD EXAMPLES ====================
        println("\n=== EXAM-STYLE EXAMPLES ===")

        // a) Student marks analysis
        val marks = List(85, 42, 91, 67, 35, 78, 95)
        println(s"Marks:              $marks")
        println(s"Students passed:    ${marks.filter(_ >= 40)}")
        println(s"Pass count:         ${marks.count(_ >= 40)}")
        println(s"Toppers (90+):      ${marks.filter(_ >= 90)}")
        println(s"Failed:             ${marks.filter(_ < 40)}")
        println(s"Average:            ${marks.sum.toDouble / marks.length}")
        println(s"Max marks:          ${marks.max}")
        println(s"Distinction (75+):  ${marks.count(_ >= 75)}")

        // b) Words analysis
        val words = List("scala", "java", "python", "c", "ruby")
        println(s"Words:              $words")
        println(s"Word lengths:       ${words.map(_.length)}")
        println(s"Long words (>4):    ${words.filter(_.length > 4)}")
        println(s"Capitalized:        ${words.map(_.capitalize)}")

        // c) Numbers: even squares sum
        println(s"Sum of even squares: ${nums.filter(_ % 2 == 0).map(x => x * x).sum}")

        // ==================== LAMBDA / ANONYMOUS FUNCTIONS ====================
        println("\n=== ANONYMOUS FUNCTIONS ===")

        // Anonymous function stored in a val
        val addOne: Int => Int = x => x + 1
        val isEven: Int => Boolean = x => x % 2 == 0

        println(s"addOne(5) = ${addOne(5)}")
        println(s"isEven(5) = ${isEven(5)}, isEven(8) = ${isEven(8)}")

        // ==================== MENU-DRIVEN PROGRAM ====================
        println("\n=========== COLLECTION PROCESSOR MENU ===========")
        print("How many numbers? ")
        val n = sc.nextInt()

        var data = List[Int]()
        for (i <- 1 to n) {
            print(s"Enter number $i: ")
            data = data :+ sc.nextInt()
        }
        println(s"Your data: $data")

        var hchoice = 0
        while (hchoice != 8) {
            println("\n1. Double all")
            println("2. Keep evens only")
            println("3. Keep odds only")
            println("4. Sum")
            println("5. Average")
            println("6. Min & Max")
            println("7. Evens doubled, then sum")
            println("8. Exit")
            print("Choice: ")
            hchoice = sc.nextInt()

            hchoice match {
                case 1 => println(s"Doubled: ${data.map(_ * 2)}")
                case 2 => println(s"Evens:   ${data.filter(_ % 2 == 0)}")
                case 3 => println(s"Odds:    ${data.filter(_ % 2 != 0)}")
                case 4 => println(s"Sum:     ${data.sum}")
                case 5 => println(s"Average: ${data.sum.toDouble / data.length}")
                case 6 => println(s"Min: ${data.min}, Max: ${data.max}")
                case 7 =>
                    val result = data.filter(_ % 2 == 0).map(_ * 2).sum
                    println(s"Evens doubled summed = $result")
                case 8 => println("Bye!")
                case _ => println("Invalid!")
            }
        }

        println("\nHigher order functions complete!")
    }
}