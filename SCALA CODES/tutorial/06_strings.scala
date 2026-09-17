/* ============================================================
   LESSON 6: STRINGS - every method you need for the lab
   ============================================================
   String = sequence of characters, like "Hello".
   Big difference from Java:  can use == to compare strings!
   ============================================================ */

object StringsLesson {
    def main(args: Array[String]): Unit = {
        import java.util.Scanner
        val sc = new Scanner(System.in)

        // ---------- 1. CREATING STRINGS ----------
        val s1 = "Hello, Scala!"
        val s2: String = "World"
        val s3 = new String("Another way")

        // String interpolation (BEST way to build strings)
        val name = "Ravi"
        val age = 21
        println(s"My name is $name and I am $age years old")

        // ---------- 2. COMMON PROPERTIES ----------
        val str = "Scala Programming"
        println(s"Length = ${str.length}")
        println(s"Is empty? ${str.isEmpty}")
        println(s"Character at index 2 = ${str.charAt(2)}")   // 'a'
        println(s"Same with (2) = ${str(2)}")                  // 'a' (shorthand!)

        // ---------- 3. CASE-RELATED ----------
        println(s"Uppercase = ${str.toUpperCase}")
        println(s"Lowercase = ${str.toLowerCase}")

        // ---------- 4. SEARCHING ----------
        println(s"Contains 'gram'? ${str.contains("gram")}")
        println(s"Starts with 'Scala'? ${str.startsWith("Scala")}")
        println(s"Ends with 'ing'? ${str.endsWith("ing")}")
        println(s"Index of 'a' = ${str.indexOf('a')}")
        println(s"Last index of 'a' = ${str.lastIndexOf('a')}")

        // ---------- 5. CUTTING / SUBSTRING ----------
        val s = "Hello, World"
        println(s"Substring from index 7: '${s.substring(7)}'")  // World
        println(s"Substring 0 to 5: '${s.substring(0, 5)}'")     // Hello
        println(s"First 3 chars: '${s.take(3)}'")
        println(s"Last 3 chars: '${s.takeRight(3)}'")
        println(s"Drop first 7: '${s.drop(7)}'")

        // ---------- 6. REPLACING ----------
        val t = "a-b-c-d"
        println(s"Replace - with *: ${t.replace('-', '*')}")
        println(s"Replace a with X: ${t.replace("a", "X")}")
        println(s"Replace first: ${t.replaceFirst("a", "X")}")

        // ---------- 7. SPLITTING (VERY COMMON IN EXAM) ----------
        val csv = "apple,mango,banana,grapes"
        val fruits = csv.split(",")
        println(s"Split by comma: ${fruits.mkString(" | ")}")
        println(s"Number of fruits = ${fruits.length}")

        val sentence = "Hello how are you"
        val words = sentence.split(" ")
        println(s"Words: ${words.mkString(", ")}")

        // ---------- 8. JOINING (reverse of split) ----------
        println(s"Join: ${fruits.mkString(" + ")}")

        // ---------- 9. COMPARING STRINGS (== works in Scala!) ----------
        val p1 = "Ravi"
        val p2 = "ravi"
        val p3 = "Ravi"

        println(s""""Ravi" == "Ravi": ${p1 == p3}""")        // true
        println(s""""Ravi" == "ravi": ${p1 == p2}""")        // false
        println(s"Ignore case equal: ${p1.equalsIgnoreCase(p2)}") // true
        println(s"Compare to: ${p1.compareTo(p2)}")          // not 0 = different

        // ---------- 10. TRIMMING (remove extra spaces) ----------
        val messy = "   Hello   World   "
        println(s"Trimmed: '${messy.trim}'")

        // ---------- 11. CHECKS ----------
        val digitStr = "12345"
        println(s"Is '12345' all digits? ${digitStr.forall(_.isDigit)}")
        println(s"Is 'abc' all letters? ${"abc".forall(_.isLetter)}")

        // ---------- 12. REVERSING AND REPEATING ----------
        println(s"Reverse: ${"Scala".reverse}")
        println(s"Repeat 3x: ${"AB".*(3)}")

        // ---------- 13. STRING BUILDER (efficient loop building) ----------
        println("\nJoin numbers 1..5 with comma using StringBuilder:")
        val sb = new StringBuilder
        for (i <- 1 to 5) {
            sb.append(i)
            if (i != 5) sb.append(", ")
        }
        println(sb.toString)

        // ============ LAB-STYLE STRING PROGRAMS ============

        // 1) Count vowels & consonants in a string
        print("\nEnter a string: ")
        val inp = sc.nextLine()
        var vowels = 0
        var consonants = 0
        for (ch <- inp.toLowerCase) {
            if (ch.isLetter) {
                if ("aeiou".contains(ch)) vowels += 1
                else consonants += 1
            }
        }
        println(s"Vowels = $vowels, Consonants = $consonants")

        // 2) Check if string is palindrome
        print("Enter a string to check palindrome: ")
        val w = sc.nextLine()
        if (w == w.reverse) println(s"'$w' is a PALINDROME")
        else println(s"'$w' is NOT a palindrome")

        // 3) Count words in a sentence
        print("Enter a sentence: ")
        val sen = sc.nextLine()
        println(s"Word count = ${sen.trim.split("\\s+").length}")

        // 4) Frequency of a character
        print("Enter a string: ")
        val str2 = sc.nextLine()
        print("Enter character to count: ")
        val ch = sc.nextLine().charAt(0)
        var count = 0
        for (c <- str2 if c == ch) count += 1
        println(s"Frequency of '$ch' = $count")

        // 5) Reverse words in a sentence   ("Hello World" -> "World Hello")
        print("Enter a sentence: ")
        val sents = sc.nextLine()
        println(s"Reversed words: ${sents.split(" ").reverse.mkString(" ")}")

        // ============ STRING MENU-DRIVEN PROGRAM ============
        println("\n=========== STRING OPERATIONS MENU ===========")
        print("Enter a base string: ")
        sc.nextLine()  // consume leftover newline
        val base = sc.nextLine()

        var schoice = 0
        while (schoice != 7) {
            println("\n1. Length")
            println("2. Uppercase / Lowercase")
            println("3. Reverse")
            println("4. Count vowels")
            println("5. Check palindrome")
            println("6. Count occurrences of a character")
            println("7. Exit")
            print("Choice: ")
            schoice = sc.nextInt()

            schoice match {
                case 1 => println(s"Length = ${base.length}")
                case 2 =>
                    println(s"Upper = ${base.toUpperCase}")
                    println(s"Lower = ${base.toLowerCase}")
                case 3 => println(s"Reverse = ${base.reverse}")
                case 4 =>
                    var v = 0
                    for (c <- base.toLowerCase if "aeiou".contains(c)) v += 1
                    println(s"Vowels = $v")
                case 5 =>
                    if (base == base.reverse) println("Palindrome!")
                    else println("Not palindrome!")
                case 6 =>
                    print("Enter character: ")
                    val ch2 = sc.next().charAt(0)
                    var cnt = 0
                    for (c <- base if c == ch2) cnt += 1
                    println(s"'$ch2' appears $cnt times")
                case 7 => println("Bye!")
                case _ => println("Invalid!")
            }
        }

        println("\nString concepts complete!")
    }
}