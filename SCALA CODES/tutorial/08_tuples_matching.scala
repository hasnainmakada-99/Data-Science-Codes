/* ============================================================
   LESSON 8: TUPLES & PATTERN MATCHING (deep dive)
   ============================================================
   Tuple = group of different values together, like a row in a table.
   Pattern matching = the switch-case on steroids.

   Tuple syntax:   (value1, value2, value3, ...)
   ============================================================ */

object TuplesMatching {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ==================== 1. TUPLES ====================

        // Creating tuples - can hold ANY mix of types
        val t1 = (101, "Ravi", 50000)              // Int, String, Int
        val t2 = (1, 2, 3, 4, 5)                   // 5 elements
        val t3 = ("apple", 3.14, true)             // mixed types

        println(s"t1 = $t1")

        // Accessing elements
        println(s"t1._1 = ${t1._1}")               // 101
        println(s"t1._2 = ${t1._2}")               // Ravi
        println(s"t1._3 = ${t1._3}")               // 50000

        // NOTE: use _1, _2, _3 ... (starting from 1, NOT 0!)

        // DESTRUCTURING (very common!)
        val (id, empName, salary) = t1
        println(s"id=$id, name=$empName, salary=$salary")

        // Swapping a pair
        val pair = (10, 20)
        println(s"Original: $pair")
        println(s"Swapped: ${pair.swap}")

        // Tuple in a function - return multiple things at once!
        def minMax(nums: List[Int]): (Int, Int) = {
            (nums.min, nums.max)      // returns a tuple
        }
        val (mn, mx) = minMax(List(5, 2, 9, 1, 7))
        println(s"Min = $mn, Max = $mx")

        // List of tuples (like a table!)
        val students = List(
            (1, "Ravi", 85),
            (2, "Sita", 92),
            (3, "Ram", 78)
        )
        println("\nStudents table:")
        for ((sid, sname, smarks) <- students)
            println(s"ID: $sid, Name: $sname, Marks: $smarks")

        // ==================== 2. PATTERN MATCHING - THE POWERS ====================

        println("\n=========== PATTERN MATCHING POWERS ===========")

        // Power 1: match on EXACT value
        val x = 2
        val msg = x match {
            case 1 => "One"
            case 2 => "Two"
            case _ => "Other"
        }
        println(s"x=$x -> $msg")

        // Power 2: match on TYPE
        def typeOf(v: Any): String = v match {
            case i: Int    => s"Integer: $i"
            case d: Double => s"Double: $d"
            case s: String => s"String: $s"
            case b: Boolean => s"Boolean: $b"
            case _          => "Unknown type"
        }
        println(typeOf(42))
        println(typeOf(3.14))
        println(typeOf("hi"))
        println(typeOf(true))

        // Power 3: match with CONDITIONS (if guards)
        val score = 85
        score match {
            case s if s >= 90 => println("A+")
            case s if s >= 80 => println("A")
            case s if s >= 70 => println("B")
            case s if s >= 60 => println("C")
            case _            => println("F")
        }

        // Power 4: match on collection patterns
        println("\nCollection matching:")
        val list1 = List(1, 2, 3)
        list1 match {
            case List(a, b, c)        => println(s"3 elements: $a, $b, $c")
            case List(a, b, _*)       => println(s"At least 2 elements")
            case List()               => println("Empty list")
            case _                    => println("Something else")
        }

        // Power 5: match on Tuple pattern
        val point = (5, -3)
        point match {
            case (0, 0) => println("Origin")
            case (x, 0) => println(s"On X axis at $x")
            case (0, y) => println(s"On Y axis at $y")
            case (x, y) if x > 0 && y > 0 => println("Quadrant I")
            case (x, y) if x < 0 && y > 0 => println("Quadrant II")
            case (x, y) if x < 0 && y < 0 => println("Quadrant III")
            case (x, y) if x > 0 && y < 0 => println("Quadrant IV")
            case _ => println("Unknown point")
        }

        // Power 6: match EVERYTHING (_ = wildcard)
        val anything: Any = "whatever"
        anything match {
            case 5         => println("It's 5")
            case "hello"   => println("It's hello")
            case _         => println("None of the above")   // default
        }

        // Power 7: match with Option (Some/None - important!)
        // Option = a box that either has a value (Some) or is empty (None)
        def safeDivide(a: Int, b: Int): Option[Int] = {
            if (b == 0) None
            else Some(a / b)
        }

        val result1 = safeDivide(10, 2)
        val result2 = safeDivide(10, 0)

        println(s"\nsafeDivide(10,2): $result1")
        println(s"safeDivide(10,0): $result2")

        result1 match {
            case Some(value) => println(s"Division result = $value")
            case None        => println("Cannot divide by zero!")
        }

        result2 match {
            case Some(value) => println(s"Division result = $value")
            case None        => println("Cannot divide by zero!")
        }

        // ==================== CLASSIC MATCH EXAMPLES FOR LAB ====================

        // Example 1: Day of week calculator
        print("\nEnter day number (1-7): ")
        val day = sc.nextInt()
        val dayName = day match {
            case 1 => "Monday"
            case 2 => "Tuesday"
            case 3 => "Wednesday"
            case 4 => "Thursday"
            case 5 => "Friday"
            case 6 => "Saturday"
            case 7 => "Sunday"
            case _ => "Invalid day number!"
        }
        println(dayName)

        // Example 2: Month days
        print("Enter month number (1-12): ")
        val month = sc.nextInt()
        val daysInMonth = month match {
            case 1 | 3 | 5 | 7 | 8 | 10 | 12 => 31
            case 4 | 6 | 9 | 11              => 30
            case 2                           => 28
            case _                           => 0
        }
        println(s"Days = $daysInMonth")

        // Example 3: Number of days calculator (is a leap year?)
        print("Enter a year: ")
        val year = sc.nextInt()
        val isLeap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
        if (isLeap) println(s"$year is a LEAP year") else println(s"$year is NOT a leap year")

        // ==================== MENU: PERSON DATABASE ====================
        println("\n=========== SIMPLE PERSON DATABASE ===========")
        // We'll store each person as a (name, age, marks) tuple

        var people = List[(String, Int, Int)]()   // empty list of tuples

        var pchoice = 0
        while (pchoice != 4) {
            println("\n1. Add person")
            println("2. Show all")
            println("3. Show toppers (marks >= 90)")
            println("4. Exit")
            print("Choice: ")
            pchoice = sc.nextInt()

            pchoice match {
                case 1 =>
                    print("Name: ")
                    val pname = sc.next()
                    print("Age: ")
                    val page = sc.nextInt()
                    print("Marks: ")
                    val pmarks = sc.nextInt()
                    people = people :+ (pname, page, pmarks)   // append tuple
                    println("Person added!")

                case 2 =>
                    if (people.isEmpty)
                        println("No records yet!")
                    else {
                        println("All people:")
                        for ((n, a, m) <- people)
                            println(s"  $n, age $a, marks $m")
                    }

                case 3 =>
                    val toppers = people.filter(_._3 >= 90)
                    if (toppers.isEmpty)
                        println("No toppers found!")
                    else
                        for ((n, a, m) <- toppers)
                            println(s"  $n $m")

                case 4 => println("Bye!")
                case _ => println("Invalid!")
            }
        }

        println("\nTuples & pattern matching complete!")
    }
}