// Program 19 - Lists, Sets and Tuples in Scala
// Week 10 | 17-09-2026 | Exercise Program
object Program19 {

  // (a) Function that squares every element of a list
  def squareList(numbers: List[Int]): List[Int] = numbers.map(n => n * n)

  // (b) Function that returns the intersection of two sets
  def intersectSets(first: Set[Char], second: Set[Char]): Set[Char] = first.intersect(second)

  // (c) Function that prints each element of a tuple
  def printTuple(record: (Int, String, Boolean)): Unit = {
    println("  First  element (Int)     : " + record._1)
    println("  Second element (String)  : " + record._2)
    println("  Third  element (Boolean) : " + record._3)
  }

  def main(args: Array[String]): Unit = {
    println("=" * 62)
    println("PROGRAM 19 : LISTS, SETS AND TUPLES IN SCALA")
    println("=" * 62)

    val primes = List(2, 3, 5, 7, 11)
    println("\n1. List of first five primes : " + primes)
    println("   Squares of each element    : " + squareList(primes))
    println("   Sum of squares             : " + squareList(primes).sum)

    val text = "hello world"
    val uniqueChars = text.toSet
    println("\n2. Source string             : " + text)
    println("   Unique characters (Set)    : " + uniqueChars.toList.sorted.mkString("[", ", ", "]"))
    println("   Number of unique chars     : " + uniqueChars.size)

    val vowels = Set('a', 'e', 'i', 'o', 'u')
    println("   Vowel set                  : " + vowels.toList.sorted.mkString("[", ", ", "]"))
    println("   Intersection (vowels)      : " + intersectSets(uniqueChars, vowels).toList.sorted.mkString("[", ", ", "]"))

    val record = (101, "Hasnain Makada", true)
    println("\n3. Tuple                     : " + record)
    printTuple(record)
    println("=" * 62)
  }
}
