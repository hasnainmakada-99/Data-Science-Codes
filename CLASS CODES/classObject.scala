class Student{

    var name = "Anita"
    var reg = "1234"
    def display(): Unit = {println("name= "+name); println("REG: "+reg)}
}

object classObject{
    def main(args: Array[String]): Unit = {
        val s1 = new Student()
        val s2 = new Student()
        s1.name = "Hasnain"
        s1.reg = "26MML0031"
        s1.display();

        s2.name="Kamil"
        s2.reg="26MML00011111"
        s2.display();
    }
}