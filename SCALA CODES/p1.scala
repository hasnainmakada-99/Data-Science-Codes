object HelloWorld{
    def main(args: Array[String]): Unit = {
        val arr = Array(10, 20, 30, 40, 50)
        val arr2 = new Array[Int](5)
        arr2(0)=100
        arr2(1)=200
        println(arr(0))
        println(arr2(0))
        val numbers = Array(10, 20, 30)
        numbers(1)= 50

        println(numbers.mkString(","))
    }
}