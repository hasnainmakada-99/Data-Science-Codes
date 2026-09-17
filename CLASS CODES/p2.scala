import scala.io.StdIn

object ArrayExample2
 {

    def calculateSum(numbers: Array[Int]): Int = numbers.sum

    def concatenateFruits(fruits: Array[String]): String = fruits.mkString(" , ")

    def main(args: Array[String]): Unit = {

        println("Enter the number of elements in the array: ")
        val n = StdIn.readInt()

        val numbers = new Array[Int](n)

        println(s"Enter every element of the array of Size $n: ")
        for (i <- 0 until n) {
            numbers(i) = StdIn.readInt()
        }

        print("Sum " + calculateSum(numbers) + "\n")

        println("Enter the number of fruits: ")
        val m = StdIn.readInt()

        val fruits = new Array[String](m)
        println(s"Enter every fruit of Size $m: ")
        for (i <- 0 until m) {
            fruits(i) = StdIn.readLine()
        }

        println("Fruits " + concatenateFruits(fruits) + "\n")

        println("Printing Array Elements: \n")
        numbers.foreach(println)
    }
}