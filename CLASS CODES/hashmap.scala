

case class Student(id: Int, name: String, p1: Int, p2: Int)

object hashmap {
    def createHashMapOfDataSet1(): Map[Int, Student] = {
        Map(
            1 -> Student(1, "RAJ", 100, 80),
            2 -> Student(2, "BAB", 85, 90),
            3 -> Student(3, "SEKH", 30, 80)
        )
    }

    def createHashMapOfDataSet2(): Map[Int, Student] = {
        Map(
            4 -> Student(4, "JAR", 30, 60),
            5 -> Student(5, "BAB", 80, 60),
            6 -> Student(6, "EKHA", 70, 80)
        )
    }

    def createCombinedHashMap(): Map[Int, Student] = {
        createHashMapOfDataSet1() ++ createHashMapOfDataSet2()
    }

    def findStudent(id: Int): Option[Student] = {
        createCombinedHashMap().get(id)
    }

    def main(args: Array[String]): Unit = {
        val dataSet1 = createHashMapOfDataSet1()
        val dataSet2 = createHashMapOfDataSet2()
        val allStudents = createCombinedHashMap()

        println(s"Dataset 1: $dataSet1\n")
        println(s"Dataset 2: $dataSet2\n")
        println(s"Combined dataset: $allStudents\n")
        println(s"Student with ID 5: ${findStudent(5).getOrElse("Not found")}")
    }
}
