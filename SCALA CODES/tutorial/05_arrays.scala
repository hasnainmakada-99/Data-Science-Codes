/* ============================================================
   LESSON 5: ARRAYS - the MOST asked topic in lab assessments!
   ============================================================
   An array = collection of elements of the SAME type in order.
   Index starts at 0.  Array(50) -> element at position 5.

   Two ways to create:
   1. With values:  Array(10, 20, 30)
   2. Empty with size: new Array[Int](5)
   ============================================================ */

object ArraysLesson {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ---------- 1. CREATING ARRAYS ----------
        val arr1 = Array(10, 20, 30, 40, 50)        // values given
        val arr2 = new Array[Int](5)                // size 5, all zeros
        val arr3 = Array.ofDim[Int](5)              // same as above
        val names = Array("Ravi", "Sita", "Ram")    // String array
        val marks = Array(85.5, 90.0, 78.25)        // Double array

        // ---------- 2. ACCESSING & CHANGING ELEMENTS ----------
        println(s"arr1(0) = ${arr1(0)}")        // 10  (parentheses = index!)
        println(s"arr1(4) = ${arr1(4)}")        // 50

        arr2(0) = 100                           // assigning value
        arr2(1) = 200
        println(s"arr2(0) = ${arr2(0)}, arr2(1) = ${arr2(1)}")

        // ---------- 3. IMPORTANT PROPERTIES ----------
        println(s"Length of arr1 = ${arr1.length}")
        println(s"First element = ${arr1.head}")
        println(s"Last element = ${arr1.last}")
        println(s"Sum = ${arr1.sum}")
        println(s"Max = ${arr1.max}")
        println(s"Min = ${arr1.min}")

        // ---------- 4. PRINTING AN ARRAY (3 ways) ----------
        // Way 1: loop with index
        println("\nPrinting with for-index loop:")
        for (i <- 0 until arr1.length)
            print(s"${arr1(i)} ")
        println()

        // Way 2: foreach (on each element)
        println("Printing with foreach:")
        arr1.foreach(x => print(s"$x "))     // OR: arr1.foreach(println)
        println()

        // Way 3: mkString (join into one string with separator)
        println("Printing with mkString:")
        println(arr1.mkString(", "))
        println(arr1.mkString(" | "))

        // ---------- 5. LOOPING OVER ARRAYS ----------
        println("\nElements with index using zipWithIndex:")
        for ((value, index) <- arr1.zipWithIndex)
            println(s"index $index = $value")

        // ---------- 6. ARRAY OPERATIONS (VERY IMPORTANT) ----------
        val a = Array(5, 3, 8, 1, 9, 2)

        println(s"Sorted ascending:  ${a.sorted.mkString(", ")}")
        println(s"Sorted descending: ${a.sorted.reverse.mkString(", ")}")
        println(s"Reversed:          ${a.reverse.mkString(", ")}")
        println(s"First 3:           ${a.take(3).mkString(", ")}")
        println(s"Last 2:            ${a.takeRight(2).mkString(", ")}")
        println(s"Evens only:        ${a.filter(_ % 2 == 0).mkString(", ")}")
        println(s"Doubled:           ${a.map(_ * 2).mkString(", ")}")

        // ---------- 7. TAKING INPUT INTO AN ARRAY ----------
        print("\nHow many elements in your array? ")
        val n = sc.nextInt()

        val userArr = new Array[Int](n)
        for (i <- 0 until n) {
            print(s"Enter element ${i + 1}: ")
            userArr(i) = sc.nextInt()
        }
        println(s"Your array: ${userArr.mkString(", ")}")

        // ---------- 8. COMMON LAB PROGRAMS ON ARRAYS ----------
        val nums = Array(12, 45, 7, 89, 23, 56, 34)

        // a) Find largest & smallest
        println(s"\nLargest = ${nums.max}, Smallest = ${nums.min}")

        // b) Sum of elements
        println(s"Sum = ${nums.sum}, Average = ${nums.sum.toDouble / nums.length}")

        // c) Count even & odd
        var evens = 0
        for (x <- nums if x % 2 == 0) evens += 1
        println(s"Evens = $evens, Odds = ${nums.length - evens}")

        // d) Linear search
        print("Enter element to search: ")
        val key = sc.nextInt()
        var pos = -1
        for (i <- 0 until nums.length if pos == -1) {
            if (nums(i) == key) pos = i
        }
        if (pos != -1) println(s"Found at index $pos")
        else println("Not found!")

        // e) Reverse array
        println(s"Reversed: ${nums.reverse.mkString(", ")}")

        // ---------- 9. 2D ARRAYS (MATRICES) ----------
        println("\n=========== 2D ARRAYS / MATRICES ===========")

        // Create a 2D array with values
        val matrix = Array(
            Array(1, 2, 3),
            Array(4, 5, 6),
            Array(7, 8, 9)
        )

        // Create empty 3x3 (3 rows x 3 cols)
        val empty2D = Array.ofDim[Int](3, 3)

        // Access element: matrix(row)(col)
        println(s"matrix(0)(0) = ${matrix(0)(0)}")   // 1
        println(s"matrix(2)(1) = ${matrix(2)(1)}")   // 8
        println(s"Number of rows = ${matrix.length}")
        println(s"Number of cols in row 0 = ${matrix(0).length}")

        // Print matrix with nested loops
        println("\nMatrix:")
        for (i <- 0 until matrix.length) {          // rows
            for (j <- 0 until matrix(i).length) {   // cols of row i
                print(s"${matrix(i)(j)} ")
            }
            println()   // new line after each row
        }

        // ---------- 10. MATRIX MENU PROGRAM ----------
        println("\n=========== MATRIX OPERATIONS MENU ===========")

        // Taking 2 matrices as input
        val r = 2
        val c = 2
        val m1 = Array.ofDim[Int](r, c)
        val m2 = Array.ofDim[Int](r, c)

        println(s"Enter elements of Matrix 1 ($r x $c):")
        for (i <- 0 until r; j <- 0 until c) {
            print(s"m1($i)($j): ")
            m1(i)(j) = sc.nextInt()
        }

        println(s"Enter elements of Matrix 2 ($r x $c):")
        for (i <- 0 until r; j <- 0 until c) {
            print(s"m2($i)($j): ")
            m2(i)(j) = sc.nextInt()
        }

        var mchoice = 0
        while (mchoice != 5) {
            println("\n1. Add matrices")
            println("2. Subtract matrices")
            println("3. Multiply matrices")
            println("4. Display matrices")
            println("5. Exit")
            print("Choice: ")
            mchoice = sc.nextInt()

            mchoice match {
                case 1 =>
                    val result = Array.ofDim[Int](r, c)
                    for (i <- 0 until r; j <- 0 until c)
                        result(i)(j) = m1(i)(j) + m2(i)(j)
                    println("Result (Addition):")
                    for (i <- 0 until r) {
                        for (j <- 0 until c)
                            print(s"${result(i)(j)} ")
                        println()
                    }

                case 2 =>
                    val result = Array.ofDim[Int](r, c)
                    for (i <- 0 until r; j <- 0 until c)
                        result(i)(j) = m1(i)(j) - m2(i)(j)
                    println("Result (Subtraction):")
                    for (i <- 0 until r) {
                        for (j <- 0 until c)
                            print(s"${result(i)(j)} ")
                        println()
                    }

                case 3 =>
                    // Matrix multiplication: m1(r x c) * m2(c x c)
                    val result = Array.ofDim[Int](r, c)
                    for (i <- 0 until r)
                        for (j <- 0 until c)
                            for (k <- 0 until c)
                                result(i)(j) += m1(i)(k) * m2(k)(j)
                    println("Result (Multiplication):")
                    for (i <- 0 until r) {
                        for (j <- 0 until c)
                            print(s"${result(i)(j)} ")
                        println()
                    }

                case 4 =>
                    println("Matrix 1:")
                    for (i <- 0 until r) {
                        for (j <- 0 until c) print(s"${m1(i)(j)} ")
                        println()
                    }
                    println("Matrix 2:")
                    for (i <- 0 until r) {
                        for (j <- 0 until c) print(s"${m2(i)(j)} ")
                        println()
                    }

                case 5 => println("Bye!")
                case _ => println("Invalid!")
            }
        }

        // ---------- 11. OTHER USEFUL ARRAY METHODS ----------
        val arr = Array(4, 2, 5, 1, 3)
        println(s"\nContains 5? ${arr.contains(5)}")
        println(s"Index of 2: ${arr.indexOf(2)}")
        println(s"Sorted: ${arr.sorted.mkString(",")}")
        println(s"Distinct elements: ${Array(1,1,2,2,3).distinct.mkString(",")}")
        println(s"Sum of even elements: ${arr.filter(_ % 2 == 0).sum}")

        println("\nArray concepts complete!")
    }
}