/* ============================================================
   LESSON 7: COLLECTIONS - List, Map, Set, (and quick Vector/Buffer)
   ============================================================
   Collections hold many values together.

   COLLECTION      | MUTABLE?  | ORDER?  | DUPLICATES?
   --------------- | --------- | ------- | -----------
   List            | No        | Yes     | Yes
   Array           | Yes       | Yes     | Yes
   Set             | No        | No      | NO!
   Map             | No        | No      | Keys unique
   ArrayBuffer     | Yes       | Yes     | Yes
   ============================================================ */

object CollectionsLesson {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ==================== 1. LIST ====================
        // Immutable - cannot change once created.
        // BUT you can create new lists FROM it.

        val fruits = List("apple", "mango", "banana", "grapes")
        val numbers = List(10, 20, 30, 40, 50)

        println(s"Fruits: $fruits")
        println(s"Length = ${fruits.length}")
        println(s"Is empty? ${fruits.isEmpty}")
        println(s"Head (first) = ${fruits.head}")
        println(s"Tail (rest) = ${fruits.tail}")
        println(s"Last = ${fruits.last}")
        println(s"Element at index 1 = ${fruits(1)}")

        // Adding elements (returns NEW list)
        val more = 5 :: fruits          // prepend with ::
        println(s"5 :: fruits = $more")

        val more2 = fruits :+ "kiwi"    // append
        println(s"fruits :+ kiwi = $more2")

        val combined = numbers ::: List(60, 70)   // concat lists (:::)
        println(s"Combined = $combined")

        // Operations
        println(s"Sum = ${numbers.sum}")
        println(s"Max = ${numbers.max}, Min = ${numbers.min}")
        println(s"Product = ${numbers.product}")
        println(s"Contains 30? ${numbers.contains(30)}")
        println(s"Sorted = ${List(5,3,1,4,2).sorted}")
        println(s"Reversed = ${numbers.reverse}")
        println(s"Distinct = ${List(1,1,2,2,3).distinct}")

        // Looping
        println("\nLooping:")
        for (f <- fruits) println(f)
        fruits.foreach(f => println(s"Fruit: $f"))

        // PRINT LIST WITH COMMAS (VERY common exam question!)
        println("\n--- List printing with commas ---")
        println(numbers.mkString(", "))             // 10, 20, 30, 40, 50
        println(numbers.mkString(" | "))            // any separator
        println(numbers.mkString("[", ", ", "]"))  // [10, 20, 30, 40, 50]
        // manual loop version (no trailing comma):
        for (i <- 0 until numbers.length) {
            print(numbers(i))
            if (i != numbers.length - 1) print(", ")
        }
        println()
        // foreach version:
        var firstEl = true
        numbers.foreach { x =>
            if (!firstEl) print(", ")
            print(x)
            firstEl = false
        }
        println()

        // ==================== 2. SET ====================
        // Only unique values! Duplicates dropped automatically.
        // No order guaranteed.

        val s = Set(1, 2, 3, 3, 2, 1, 4)
        println(s"\nSet(1,2,3,3,2,1,4) = $s")   // Set(1,2,3,4) - duplicates removed

        val s2 = s + 10            // add
        val s3 = s - 2             // remove
        println(s"After +10: $s2")
        println(s"After -2: $s3")
        println(s"Contains 3? ${s.contains(3)}")
        println(s"Union = ${Set(1,2,3) union Set(3,4,5)}")          // 1,2,3,4,5
        println(s"Intersection = ${Set(1,2,3) intersect Set(3,4,5)}") // 3
        println(s"Difference = ${Set(1,2,3) diff Set(3,4,5)}")       // 1,2
        println(s"Size = ${s.size}")

        // PRINT SET WITH COMMAS
        println(s"Set with commas: ${s.mkString(", ")}")

        // ==================== 3. MAP ====================
        // key -> value pairs. Like a dictionary.

        // Creating maps (3 ways)
        val m1 = Map("Ravi" -> 85, "Sita" -> 92, "Ram" -> 78)   // -> makes pair
        val m2 = Map(1 -> "One", 2 -> "Two", 3 -> "Three")
        // val m3 = Map(("Ravi", 85), ("Sita", 92))   // alternative syntax

        println(s"\nm1 = $m1")
        println(s"Ravi's marks = ${m1("Ravi")}")       // 85
        println(s"Get with default = ${m1.getOrElse("Krishna", 0)}") // 0, safe way
        println(s"Contains key 'Ram'? ${m1.contains("Ram")}")
        println(s"All keys = ${m1.keys}")
        println(s"All values = ${m1.values}")
        println(s"Size = ${m1.size}")

        // Adding & removing
        val m1b = m1 + ("Krishna" -> 88)
        println(s"After adding Krishna: $m1b")
        val m1c = m1b - "Ram"
        println(s"After removing Ram: $m1c")

        // Looping over a map
        println("\nLooping over map:")
        for ((key, value) <- m1)
            println(s"$key scored $value")

        // Printing map keys/values with commas
        println(s"Keys: ${m1.keys.mkString(", ")}")
        println(s"Values: ${m1.values.mkString(", ")}")

        // ==================== 4. ArrayBuffer (mutable list) ====================
        import scala.collection.mutable.ArrayBuffer

        val buffer = ArrayBuffer[Int]()      // empty buffer
        buffer += 10                          // add
        buffer += 20
        buffer += 30
        buffer -= 20                          // remove value
        buffer(0) = 99                        // change by index
        println(s"\nArrayBuffer = $buffer")

        val buffer2 = ArrayBuffer(1, 2, 3)
        buffer2 ++= List(4, 5, 6)             // add many at once
        println(s"buffer2 = $buffer2")

        // ==================== 5. Mutable collections ====================
        // Scala default collections are IMMUTABLE.
        // To make them changeable, add: scala.collection.mutable.

        val mutableSet = scala.collection.mutable.Set(1, 2, 3)
        mutableSet += 4        // actually changes the set
        println(s"Mutable Set after += 4: $mutableSet")

        val mutableMap = scala.collection.mutable.Map("a" -> 1)
        mutableMap("b") = 2    // actually adds new key
        println(s"Mutable Map: $mutableMap")

        // ==================== MENU PROGRAM: COLLECTION STATS ====================
        println("\n=========== NUMBER STATS MENU ===========")
        print("How many numbers? ")
        val n = sc.nextInt()

        var nums = List[Int]()
        for (i <- 1 to n) {
            print(s"Enter number $i: ")
            nums = nums :+ sc.nextInt()     // build the list
        }
        println(s"Your list: $nums")

        var cchoice = 0
        while (cchoice != 7) {
            println("\n1. Sum")
            println("2. Average")
            println("3. Min / Max")
            println("4. Count evens and odds")
            println("5. Sort (ascending/descending)")
            println("6. Remove duplicates")
            println("7. Exit")
            print("Choice: ")
            cchoice = sc.nextInt()

            cchoice match {
                case 1 => println(s"Sum = ${nums.sum}")
                case 2 => println(s"Average = ${nums.sum.toDouble / nums.length}")
                case 3 => println(s"Min = ${nums.min}, Max = ${nums.max}")
                case 4 =>
                    val evens = nums.count(_ % 2 == 0)
                    println(s"Evens = $evens, Odds = ${nums.length - evens}")
                case 5 =>
                    println(s"Ascending: ${nums.sorted}")
                    println(s"Descending: ${nums.sorted.reverse}")
                case 6 => println(s"Distinct: ${nums.distinct}")
                case 7 => println("Bye!")
                case _ => println("Invalid!")
            }
        }

        // QUICK SUMMARY TABLE (MEMORIZE):
        // List:  immutable, ordered, duplicates allowed
        // Set:   immutable, unordered, NO duplicates
        // Map:   key-value pairs, keys unique
        // ArrayBuffer: mutable, can add/remove freely

        println("\nCollections complete!")
    }
}