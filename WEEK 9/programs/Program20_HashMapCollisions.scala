// Program 20 - HashMaps: collisions and conflict resolution
// Week 11 | 24-09-2026 | Exercise Program
import scala.collection.mutable

// A HashMap that resolves collisions by separate chaining with lists
class ChainedHashMap(bucketCount: Int) {

  private val table: Array[List[(String, Int)]] = Array.fill(bucketCount)(List.empty[(String, Int)])

  // Hash function that maps a key to a bucket index
  private def bucketIndex(key: String): Int = math.abs(key.hashCode) % bucketCount

  // Insert a key-value pair, prepending it to the bucket chain
  def put(key: String, grade: Int): Unit = {
    val index = bucketIndex(key)
    table(index) = (key, grade) :: table(index)
  }

  // Look up every value stored under a key (a chain may hold several)
  def get(key: String): List[Int] =
    table(bucketIndex(key)).collect { case (k, v) if k == key => v }

  // Show the non-empty buckets, proving that chaining holds the collisions
  def display(): Unit = {
    println("   Bucket | Chain (key -> grade)")
    println("   -------+---------------------")
    for (index <- table.indices; if table(index).nonEmpty) {
      val chain = table(index).reverse.map { case (k, v) => k + " -> " + v }.mkString(" , ")
      println("   " + index + "      | " + chain)
    }
  }
}

object Program20 {

  // (a) Merge two HashMaps, resolving conflicts by keeping the higher grade
  def mergeTakingHigher(first: mutable.HashMap[String, Int],
                        second: mutable.HashMap[String, Int]): mutable.HashMap[String, Int] = {
    val merged = mutable.HashMap[String, Int]()
    merged ++= first
    for ((name, grade) <- second) {
      merged.get(name) match {
        case Some(existing) => if (grade > existing) merged(name) = grade
        case None           => merged(name) = grade
      }
    }
    merged
  }

  // (b) Handle collisions by chaining when many keys land in one bucket
  def demonstrateChaining(): Unit = {
    val chained = new ChainedHashMap(4)
    val entries = List("Amit" -> 78, "Neha" -> 85, "Rahul" -> 66, "Sara" -> 92,
                       "Vikram" -> 74, "Zoya" -> 88)
    for ((name, grade) <- entries) chained.put(name, grade)
    println("   Hash function      : index = |key.hashCode| % 4")
    for ((name, _) <- entries) {
      println("   " + name + " -> bucket " + (math.abs(name.hashCode) % 4))
    }
    println()
    chained.display()
  }

  def main(args: Array[String]): Unit = {
    println("=" * 62)
    println("PROGRAM 20 : HASHMAPS - COLLISIONS AND CONFLICT RESOLUTION")
    println("=" * 62)

    // 1. Create a HashMap of student names and grades
    val grades = mutable.HashMap(
      "Hasnain" -> 88,
      "Amit"    -> 76,
      "Neha"    -> 91
    )
    println("\n1. Initial HashMap           : " + grades.toSeq.sorted.mkString("{", ", ", "}"))

    // 2. Insert multiple entries, including a duplicate key with a different grade
    grades += ("Rahul" -> 69)
    grades += ("Sara"  -> 95)
    grades += ("Hasnain" -> 93)
    println("   After inserts + duplicate : " + grades.toSeq.sorted.mkString("{", ", ", "}"))
    println("   Note: the duplicate key Hasnain replaced 88 with " + grades("Hasnain"))

    // 3. Merge two HashMaps, resolving conflicts by taking the higher grade
    val sectionA = mutable.HashMap("Hasnain" -> 93, "Amit" -> 76, "Zoya" -> 81)
    val sectionB = mutable.HashMap("Hasnain" -> 85, "Zoya" -> 90, "Vikram" -> 74)
    val merged   = mergeTakingHigher(sectionA, sectionB)
    println("\n2. Section A                 : " + sectionA.toSeq.sorted.mkString("{", ", ", "}"))
    println("   Section B                 : " + sectionB.toSeq.sorted.mkString("{", ", ", "}"))
    println("   Merged (higher grade wins): " + merged.toSeq.sorted.mkString("{", ", ", "}"))
    println("   Hasnain 93 vs 85 -> " + merged("Hasnain") + " | Zoya 81 vs 90 -> " + merged("Zoya"))

    // 4. Collision handling by chaining
    println("\n3. Collision handling by separate chaining:")
    demonstrateChaining()
    println("=" * 62)
  }
}
