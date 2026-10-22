// Program 22 - Case Classes
// Week 13 | 15-10-2026 | Exercise Program
object Program22 {

  // The case class required by the problem statement
  case class Person(name: String, age: Int, city: String)

  // (a) Keep only the people older than 30
  def olderThan30(people: List[Person]): List[Person] =
    people.filter(p => p.age > 30)

  // (b) Group the people by the city they live in
  def groupByCity(people: List[Person]): Map[String, List[Person]] =
    people.groupBy(p => p.city)

  // (c) Render each person as "Name is Age years old and lives in City"
  def describe(people: List[Person]): List[String] =
    people.map(p => p.name + " is " + p.age + " years old and lives in " + p.city)

  // (d) Sort the people by age, youngest first
  def sortByAge(people: List[Person]): List[Person] =
    people.sortBy(p => p.age)

  def main(args: Array[String]): Unit = {
    println("=" * 68)
    println("PROGRAM 22 : CASE CLASSES IN SCALA")
    println("=" * 68)

    val people = List(
      Person("Hasnain", 22, "Delhi"),
      Person("Amit", 35, "Mumbai"),
      Person("Neha", 41, "Delhi"),
      Person("Rahul", 28, "Pune"),
      Person("Sara", 33, "Mumbai")
    )

    println("\n1. List of Person objects")
    for (p <- people) println("   " + p)

    println("\n2. People older than 30")
    val older = olderThan30(people)
    for (p <- older) println("   " + p.name + " (" + p.age + ")")
    println("   Count: " + older.length + " of " + people.length)

    println("\n3. Grouped by city")
    val grouped = groupByCity(people)
    for (city <- grouped.keys.toList.sorted) {
      println("   " + city + " -> " + grouped(city).map(_.name).mkString(", "))
    }

    println("\n4. Formatted descriptions")
    for (line <- describe(people)) println("   " + line)

    println("\n5. Sorted by age (ascending)")
    val sorted = sortByAge(people)
    for (p <- sorted) println("   " + p.age + "  " + p.name + "  (" + p.city + ")")

    println("\n6. Case class features demonstrated")
    val a = Person("Hasnain", 22, "Delhi")
    val b = Person("Hasnain", 22, "Delhi")
    println("   copy():      " + a.copy(age = 23))
    println("   equals():    " + (a == b))
    println("   toString():  " + a.toString)
    println("   productArity:" + a.productArity)
    println("=" * 68)
  }
}
