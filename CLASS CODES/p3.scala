object program3 {
    def squareList(numbers: List[Int]): List[Int] = {
        numbers.map(x=> x*x)
    }


    def findIntersection(Set1: Set[String], Set2: Set[String]): Set[String] = {
        Set1.intersect(Set2)
    }

    def printTuple(tuple: (Int, String, Boolean)): Unit = {
        println(s"ID: ${tuple._1}, Name: ${tuple._2}, Active: ${tuple._3}")
    }



    def main(args: Array[String]): Unit = {
    //    val numbers = List(1, 2, 3, 4, 5)
        val primeNumbers = List(2, 3, 5, 7, 11)
        // println(squareList(primeNumbers))
        print("\nSquared List: \n"+squareList(primeNumbers))


        // val set1 = "Hello World Hasnain Makada".toSet

        // println(set1)


        val set1 = Set("Hello", "World", "Hasnain", "Makada")
        val set2 = Set("Hello", "World", "Hasnain", "Makada")
        print("\nIntersection: \n"+findIntersection(set1, set2))



        val studentInfo = (101, "Hasnain", true)
        print(studentInfo._1)
        print(studentInfo._2)
        print(studentInfo._3)
        printTuple(studentInfo)
    }
}