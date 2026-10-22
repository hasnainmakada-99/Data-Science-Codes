// Program 21 - Advanced functional combinators
// Week 12 | 08-10-2026 | Exercise Program
object Program21 {

  def main(args: Array[String]): Unit = {
    println("=" * 62)
    println("PROGRAM 21 : ADVANCED FUNCTIONAL COMBINATORS")
    println("=" * 62)

    val numbers = (1 to 10).toList
    println("\n1. Source list (1 to 10)     : " + numbers.mkString("[", ", ", "]"))

    // 2. filter - keep only the even numbers
    val evens = numbers.filter(n => n % 2 == 0)
    println("\n2. filter(n % 2 == 0)        : " + evens.mkString("[", ", ", "]"))
    println("   Count of even numbers     : " + evens.length)

    // 3. map - multiply every element by 3
    val tripled = numbers.map(n => n * 3)
    println("\n3. map(n => n * 3)           : " + tripled.mkString("[", ", ", "]"))
    println("   Sum after mapping         : " + tripled.sum)

    // 4. flatMap - pair every integer with its square
    val pairs = numbers.flatMap(n => List((n, n * n)))
    println("\n4. flatMap(n => (n, n*n))    :")
    println("   " + pairs.mkString("[", ", ", "]"))
    println("   Number of pairs produced  : " + pairs.length)

    // 5. foldLeft - product of all elements
    val product = numbers.foldLeft(1)((accumulator, n) => accumulator * n)
    println("\n5. foldLeft(1)(_ * _)        : " + product)
    println("   Verification (10!)         : " + (1 to 10).product +
            " , match = " + (product == (1 to 10).product))

    // 6. Combined pipeline using several combinators together
    val pipeline = numbers
      .filter(n => n % 2 == 0)
      .map(n => n * 3)
      .foldLeft(0)((accumulator, n) => accumulator + n)
    println("\n6. Combined pipeline")
    println("   evens -> x3 -> sum        : " + pipeline)

    println("\n7. Summary of combinator results")
    println("   filter   -> " + evens.length + " elements")
    println("   map      -> " + tripled.length + " elements")
    println("   flatMap  -> " + pairs.length + " elements")
    println("   foldLeft -> single value " + product)
    println("=" * 62)
  }
}
