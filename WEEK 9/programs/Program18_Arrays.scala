// Program 18 - Arrays in Scala
// Week 9 | 10-09-2026 | Exercise Program
object Program18 {

  // (a) Function that returns the sum of all elements of an integer array
  def sumOfArray(numbers: Array[Int]): Int = numbers.sum

  // (b) Function that concatenates all elements of a string array, separated by commas
  def concatenateStrings(names: Array[String]): String = names.mkString(", ")

  // (c) Function that prints every element of an integer array
  def printElements(numbers: Array[Int]): Unit = {
    var index = 0
    while (index < numbers.length) {
      println("  Element at index " + index + " = " + numbers(index))
      index += 1
    }
  }

  def main(args: Array[String]): Unit = {
    println("=" * 62)
    println("PROGRAM 18 : ARRAYS IN SCALA")
    println("=" * 62)

    val numbers = Array(2, 5, 9, 14, 20)
    println("\n1. Integer array         : " + numbers.mkString("[", ", ", "]"))
    println("   Length                : " + numbers.length)
    println("   Sum of all elements   : " + sumOfArray(numbers))

    val fruits = Array("Apple", "Banana", "Mango", "Grapes", "Orange")
    println("\n2. String array (fruits) : " + fruits.mkString("[", ", ", "]"))
    println("   Concatenated           : " + concatenateStrings(fruits))

    println("\n3. Iterating over the integer array:")
    printElements(numbers)

    val manualSum = 2 + 5 + 9 + 14 + 20
    println("\n4. Verification           : manual sum = " + manualSum +
            " , function sum = " + sumOfArray(numbers) +
            " , match = " + (manualSum == sumOfArray(numbers)))
    println("=" * 62)
  }
}
