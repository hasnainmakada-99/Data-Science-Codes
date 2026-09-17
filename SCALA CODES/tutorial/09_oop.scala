/* ============================================================
   LESSON 9: OOP - Classes, Objects, Constructors, Inheritance
   ============================================================
   KEY IDEA:
   - class  = blueprint/template  (like a cookie cutter)
   - object = a single instance   (the cookie)

   IMPORTANT FOR EXAM: object HelloWorld { def main... }
   - "object" with main = program starting point
   - object is a SINGLETON (only one of it)
   ============================================================ */

// ---------- 0. Object = entry point (like you've been doing) ----------
object OOPLesson {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ==================== 1. CLASSES ====================
        // A class needs to be created ("instantiated") before use

        println("=========== CLASSES ===========")

        // Creating objects (instances) from a class
        val stu1 = new Student(1, "Ravi", 85)   // new = create instance
        val stu2 = new Student(2, "Sita", 92)

        // Accessing fields (attrs) and calling methods
        println(s"Student 1: ID=${stu1.id}, Name=${stu1.name}, Marks=${stu1.marks}")
        println(s"Student 2: ID=${stu2.id}, Name=${stu2.name}, Marks=${stu2.marks}")
        stu1.display()
        stu2.display()

        println(s"Ravi passed? ${stu1.isPassed}")   // calling method without ()
        println()

        // ==================== 2. VAR / VAL IN CONSTRUCTOR ====================
        val c1 = new Circle(5)
        println(s"Circle radius = ${c1.radius}")
        println(s"Area = ${c1.area}")
        println(s"Circumference = ${c1.circumference}")
        println()

        // ==================== 3. CASE CLASSES (rocket fuel) ====================
        // A case class gives you for FREE:
        //   - automatic constructor that works without "new"
        //   - equals, hashCode, toString
        //   - pattern matching support (perfect with match!!)
        //   - copy method

        val book1 = Book("Scala Basics", "Martin", 500)
        val book2 = Book("Data Science", "Andrew", 850)

        println(s"Automatic toString: $book1")
        println(s"Author of book2: ${book2.author}")

        // copy (with modifications)
        val book1b = book1.copy(price = 450)
        println(s"Copied with new price: $book1b")

        // == compares VALUE with case classes (not reference!)
        val book3 = Book("Scala Basics", "Martin", 500)
        println(s"book1 == book3 : ${book1 == book3}")   // true!

        // Pattern match a case class
        def describe(b: Book): String = b match {
            case Book(t, a, p) if p > 800 => s"$t by $a - EXPENSIVE"
            case Book(t, a, p)            => s"$t by $a costs $p"
        }
        println(describe(book1))
        println(describe(book2))
        println()

        // ==================== 4. INHERITANCE ====================
        println("=========== INHERITANCE ===========")

        val dog = new Dog("Tommy")
        val cat = new Cat("Kitty")

        dog.sound()     // inherited from Animal + override
        cat.sound()
        dog.eat()       // method from Animal (base class)
        println(s"${dog.name} is a ${dog.species}")

        // Using polymorphism - treat all as Animal
        val animals: List[Animal] = List(dog, cat)
        for (a <- animals) {
            print(s"${a.name}: ")
            a.sound()
        }
        println()

        // ==================== 5. TRAITS (interface in Scala) ====================
        println("=========== TRAITS ===========")

        val car = new Car("Tesla")
        val bike = new Bike("Honda")

        car.start()
        car.stop()
        bike.start()
        bike.stop()
        println()

        // ==================== 6. EVERYTHING COMES TOGETHER ====================
        // Menu-driven Student Management System using classes!

        println("=========== STUDENT MANAGER MENU (using classes) ===========")

        // We'll store Student objects in an ArrayBuffer
        import scala.collection.mutable.ArrayBuffer
        val studentList = ArrayBuffer[Student]()

        var choice = 0
        while (choice != 6) {
            println("\n1. Add student")
            println("2. Show all students")
            println("3. Search by name")
            println("4. Show students above 90")
            println("5. Total students")
            println("6. Exit")
            print("Choice: ")
            choice = sc.nextInt()

            choice match {
                case 1 =>
                    print("Enter ID: ")
                    val sid = sc.nextInt()
                    print("Enter name: ")
                    val sname = sc.next()
                    print("Enter marks: ")
                    val smarks = sc.nextInt()
                    studentList += new Student(sid, sname, smarks)
                    println("Student added!")

                case 2 =>
                    if (studentList.isEmpty)
                        println("No students yet!")
                    else
                        for (s <- studentList) s.display()

                case 3 =>
                    print("Enter name to search: ")
                    val key = sc.next()
                    var found = false
                    for (s <- studentList if !found) {
                        if (s.name.equalsIgnoreCase(key)) {
                            s.display()
                            found = true
                        }
                    }
                    if (!found) println(s"No student named '$key'")

                case 4 =>
                    val toppers = studentList.filter(_.marks >= 90)
                    if (toppers.isEmpty) println("No toppers!")
                    else for (s <- toppers) s.display()

                case 5 =>
                    println(s"Total students = ${studentList.length}")

                case 6 => println("Bye!")
                case _ => println("Invalid!")
            }
        }
    }
}

// ============================================================
// CLASS DEFINITIONS GO OUTSIDE main (after the object)
// ============================================================

// A simple class with constructor parameters
class Student(val id: Int, val name: String, val marks: Int) {
    // Methods of the class
    def isPassed: Boolean = marks >= 40

    def display(): Unit = {
        println(s"ID: $id | Name: $name | Marks: $marks | " +
                (if (isPassed) "PASS" else "FAIL"))
    }
}

// Class where constructor params are NOT val/var
// -> they are NOT accessible as fields outside
class Circle(val radius: Double) {   // val radius makes it a field
    def area: Double = math.Pi * radius * radius
    def circumference: Double = 2 * math.Pi * radius
}

// CASE CLASS - automatic toString, equals, pattern matching!
case class Book(title: String, author: String, price: Int)

// ============================================================
// INHERITANCE: Animal is the BASE (parent) class
// ============================================================
class Animal(val name: String) {
    def sound(): Unit = println("...generic animal sound...")
    def eat(): Unit = println(s"$name is eating.")
    def species: String = "Animal"
}

// Dog EXTENDS Animal -> inherits name, eat, species
class Dog(name: String) extends Animal(name) {
    // OVERRIDE: change behavior from parent
    override def sound(): Unit = println(s"$name says: Woof Woof!")
    override def species: String = "Dog"
}

class Cat(name: String) extends Animal(name) {
    override def sound(): Unit = println(s"$name says: Meow!")
    override def species: String = "Cat"
}

// ============================================================
// TRAITS = interface-like, can have both abstract & concrete methods
// ============================================================
trait Vehicle {
    def start(): Unit          // abstract - implement in class
    def stop(): Unit           // abstract
    def fuel(): String = "Petrol"   // concrete - inherited as is
}

class Car(val brand: String) extends Vehicle {
    override def start(): Unit = println(s"$brand car starting... Vroom!")
    override def stop(): Unit = println(s"$brand car stopping.")
}

class Bike(val brand: String) extends Vehicle {
    override def start(): Unit = println(s"$brand bike starting... Brum!")
    override def stop(): Unit = println(s"$brand bike stopping.")
    override def fuel(): String = "Petrol/Diesel"
}