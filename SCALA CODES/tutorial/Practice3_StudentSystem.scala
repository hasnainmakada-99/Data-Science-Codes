/* ============================================================
   PRACTICE 3: MOCK ASSESSMENT - Student Management System
   (Uses classes + collections + menu = full marks program!)
   ============================================================ */

// The main program object
object Practice3 {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        import scala.collection.mutable.ArrayBuffer

        val sc = new Scanner(System.in)
        val students = ArrayBuffer[StudentRecord]()

        var choice = 0
        while (choice != 9) {
            println("\n======= STUDENT MANAGEMENT SYSTEM =======")
            println("1. Add student")
            println("2. Display all students")
            println("3. Search student by roll number")
            println("4. Update marks")
            println("5. Delete student")
            println("6. Highest marks (topper)")
            println("7. Count passed / failed")
            println("8. Average marks of class")
            println("9. Exit")
            println("=========================================")
            print("Enter choice: ")
            choice = sc.nextInt()

            choice match {
                case 1 =>
                    print("Roll number: ")
                    val roll = sc.nextInt()
                    print("Name: ")
                    val name = sc.next()
                    print("Marks: ")
                    val marks = sc.nextInt()
                    students += StudentRecord(roll, name, marks)
                    println("Student added successfully!")

                case 2 =>
                    if (students.isEmpty)
                        println("No students in the list!")
                    else {
                        println("--- All Students ---")
                        for (s <- students) println(s)
                    }

                case 3 =>
                    print("Enter roll number to search: ")
                    val key = sc.nextInt()
                    val found = students.filter(_.roll == key)
                    if (found.isEmpty) println(s"No student with roll $key")
                    else println(found.head)

                case 4 =>
                    print("Enter roll number: ")
                    val roll = sc.nextInt()
                    val idx = students.indexWhere(_.roll == roll)
                    if (idx == -1)
                        println("Student not found!")
                    else {
                        print("New marks: ")
                        val newMarks = sc.nextInt()
                        students(idx) = students(idx).copy(marks = newMarks)
                        println("Marks updated!")
                    }

                case 5 =>
                    print("Enter roll number to delete: ")
                    val roll = sc.nextInt()
                    val idx = students.indexWhere(_.roll == roll)
                    if (idx != -1) {
                        students.remove(idx)
                        println("Student deleted!")
                    } else {
                        println("Student not found!")
                    }

                case 6 =>
                    if (students.isEmpty)
                        println("No students!")
                    else {
                        val topper = students.maxBy(_.marks)
                        println(s"Topper: $topper")
                    }

                case 7 =>
                    val passed = students.count(_.marks >= 40)
                    println(s"Passed = $passed, Failed = ${students.length - passed}")

                case 8 =>
                    if (students.isEmpty)
                        println("No students!")
                    else
                        println(s"Average = ${students.map(_.marks).sum.toDouble / students.length}")

                case 9 => println("Thank you! Goodbye!")
                case _ => println("Invalid choice!")
            }
        }
    }
}

// Case class = automatic toString, equals, copy, pattern matching
case class StudentRecord(roll: Int, name: String, marks: Int)