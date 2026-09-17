object ArraySum{
    def main(args: Array[String]): Unit = {
        val numbers = Array(10, 20, 30, 40, 50)
        var sum = 0
        for(num <- numbers)
            sum+=num

            print("Sum = "+sum)

        val marks = Array(80, 85, 90, 95)
        val avg = marks.sum.toDouble / marks.length

        println("Average:= "+avg)

        val numebers = List(10, 20, 30, 40, 50)

        println(numbers.head)
        println(numbers.last)
        println(numbers.length)

        val employee = (101, "ravi", 50000)
    }
}