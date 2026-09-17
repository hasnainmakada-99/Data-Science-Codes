object p2{
    def main(args:Array[String]): Unit = {
        val nums = Array(10, 20, 30, 40, 50, 60, 70)

        // for(i<-0 until nums.length){
        //     println(nums(i))
        // }

        // nums.foreach(println)

        val nums2= Array(90, 70, 30, 12, 1, 0)

        // nums.foreach(println)

        val nums3 = nums2.sorted.mkString(",")

        nums3.foreach(println)
    }
}