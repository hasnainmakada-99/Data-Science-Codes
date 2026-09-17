
object ArrayExample{

    def calculateSum(numbers: Array[Int]): Int = numbers.sum

    def concatenateFruits(fruits: Array[String]): String = fruits.mkString(" , ")

    def main(args: Array[String]): Unit = {
        val numbers = Array(2, 5, 9, 14, 20)

        print("Sum "+calculateSum(numbers)+"\n")


        val fruits = Array("Apple", "Pineapple", "Watermelon", "Peach", "Papaya")

        println("Fruits"+ concatenateFruits(fruits)+"\n")


        println("Printing Array Elements: \n")
        numbers.foreach(println)
    }
}