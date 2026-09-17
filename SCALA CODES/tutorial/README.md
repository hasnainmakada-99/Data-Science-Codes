# 🎯 SCALA EXAM PREPARATION GUIDE (Thursday Lab Assessment)

Everything you need in one place. Read this LAST — the actual code is in the other files.

---

## 1. How a Scala Program is Structured

```scala
object ProgramName {              // object = required wrapper
    def main(args: Array[String]): Unit = {   // main = entry point
        println("Hello!")
    }
}
```

> **RULE**: Every program ALWAYS starts with an `object` containing `def main(args: Array[String]): Unit`.

---

## 2. Cheat Sheet — Quick Reference

### Printing (full details → section 4)
| Concept | Syntax | Example |
|---|---|---|
| Print with newline | `println(...)` | `println("Hi")` |
| Print no newline | `print(...)` | `print("Hi")` |
| Print blank line | `println()` | |
| Text + variable (best!) | `s"...$var..."` | `s"Sum = $sum"` |
| Text + expression | `s"...${expr}..."` | `s"2+3 = ${2 + 3}"` |
| Formatted (C-style) | `printf("%d %.2f", a, b)` | `printf("%.2f", 3.14159)` |
| Fixed decimals | `f"$num%.2f"` | `f"Pi = $pi%.2f"` |
| Print collection with commas | `.mkString(", ")` | `list.mkString(", ")` |
| No spaces string | `sc.next()` | reads one word |

### User Input (full details → section 3)
| Concept | Syntax | Example |
|---|---|---|
| Import Scanner (mandatory!) | `import java.util.Scanner` | first line |
| Create Scanner | `val sc = new Scanner(System.in)` | once |
| Read int | `sc.nextInt()` | `val n = sc.nextInt()` |
| Read double | `sc.nextDouble()` | `val d = sc.nextDouble()` |
| Read string (whole line) | `sc.nextLine()` | `val s = sc.nextLine()` |
| Read string (one word) | `sc.next()` | `val w = sc.next()` |
| Scala-native input | `import scala.io.StdIn` | `StdIn.readLine()` |
| No-import input | `readLine()` | `val s = readLine()` |

### Core concepts (full details → sections 5-11)
| Concept | Syntax | Example |
|---|---|---|
| val (constant) | `val x = 5` | cannot change |
| var (variable) | `var x = 5` | can change |
| if/else | `if (c) {...} else {...}` | |
| match (switch) | `x match { case 1 => ...; case _ => ... }` | |
| for loop | `for (i <- 1 to 10)` | includes 10 |
| | `for (i <- 1 until 10)` | excludes 10 |
| | `for (i <- 1 to 10 by 2)` | step 2 |
| while loop | `while (cond) {...}` | checks first |
| do-while | `do {...} while (cond)` | runs at least once |
| Array | `Array(1,2,3)` / `new Array[Int](5)` | mutable |
| List | `List(1,2,3)` | immutable, ordered, duplicates OK |
| Set | `Set(1,2,3)` | immutable, NO duplicates |
| Map | `Map("a" -> 1)` | key->value, keys unique |
| Tuple | `(1, "abc", true)` | holds mixed types |
| foreach | `list.foreach(println)` | do something with each |
| mkString | `list.mkString(", ")` | join with commas! |

---

## 3. USER INPUT — which library to import & every reading method

In Scala, you must **`import` a library** before you can read user input.
The import line goes at the TOP of the file, inside the object, or before main.

### 3.1 Method A: `java.util.Scanner` (Java style — MOST used in labs)

```scala
import java.util.Scanner        // <-- THE IMPORT LINE (mandatory!)

object Program {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)   // create the scanner ONCE

        // Now read as many values as you need with sc.xxx:
        val n = sc.nextInt()              // read an Int
    }
}
```

**All Scanner methods (memorize these!):**

| Method | Reads | Example | Notes |
|---|---|---|---|
| `sc.nextInt()` | Int | `val n = sc.nextInt()` | whole number |
| `sc.nextDouble()` | Double | `val d = sc.nextDouble()` | decimal number |
| `sc.nextFloat()` | Float | `val f = sc.nextFloat()` | decimal, smaller |
| `sc.nextLong()` | Long | `val l = sc.nextLong()` | very big number |
| `sc.nextBoolean()` | Boolean | `val b = sc.nextBoolean()` | true / false |
| `sc.nextByte()` | Byte | | |
| `sc.next()` | **ONE word** | `val w = sc.next()` | no spaces allowed |
| `sc.nextLine()` | **WHOLE line** | `val s = sc.nextLine()` | spaces allowed |
| `sc.hasNextInt()` | checks | `sc.hasNextInt()` | true/false |

**⚠ THE NEWLINE TRAP (the #1 bug in lab exams!):**

`nextInt()`, `nextDouble()` etc. read the NUMBER but **leave the Enter
(newline) still in the keyboard buffer**. If you then call `nextLine()`,
it reads that leftover empty line — not what the user types!

```scala
val n = sc.nextInt()     // user types 5, presses Enter
val s = sc.nextLine()    // ❌ WRONG: gets an EMPTY string!
```

```scala
val n = sc.nextInt()
sc.nextLine()            // ✅ FIX: consume the leftover newline
val s = sc.nextLine()    // ✅ now this reads the real line
```

> **Rule**: after any `nextInt()/nextDouble()` before a `nextLine()`, add one empty `sc.nextLine()`.

**Reading MANY numbers on ONE line:**
```scala
print("Enter a and b: ")
val a = sc.nextInt()
val b = sc.nextInt()     // user can type: 10 20
```

---

### 3.2 Method B: `scala.io.StdIn` (Scala-native style)

```scala
import scala.io.StdIn     // <-- THE IMPORT LINE

val s  = StdIn.readLine()     // whole line (String)
val n  = StdIn.readInt()      // Int
val d  = StdIn.readDouble()   // Double
val f  = StdIn.readFloat()    // Float
val l  = StdIn.readLong()     // Long
val b  = StdIn.readBoolean()  // Boolean
val c  = StdIn.readChar()     // Char
```

**StdIn has NO newline trap** — each read is a separate line, so it's simpler:
```scala
val name = StdIn.readLine()    // "Ravi Kumar" — spaces fine
val age  = StdIn.readInt()     // 21
println(s"$name is $age years old")
```

---

### 3.3 Method C: `readLine()` — no import needed!

Scala predefines `readLine()`, `readInt()`, `readDouble()` that work directly:

```scala
val s = readLine()     // whole line, NO import required!
val n = readInt()      // also works!
```

---

### 3.4 Which one should YOU use?

| Situation | Use this |
|---|---|
| Faculty taught with Scanner | `java.util.Scanner` ✅ |
| Faculty taught "StdIn" style | `scala.io.StdIn` ✅ |
| Quickest, no import | `readLine()` |
| Reading mixed numbers + text | Scanner (with the newline fix!) |

> All three produce identical results. Pick the one your faculty expects.

---

## 4. PRINTING OUTPUT — every way to print anything

### 4.1 `print` vs `println`

| Function | Newline? | Example | Output |
|---|---|---|---|
| `print("Hi")` | ❌ no | `print("Hi"); print("Bye")` | `HiBye` |
| `println("Hi")` | ✅ yes | `println("Hi"); println("Bye")` | `Hi` `Bye` (2 lines) |
| `println()` | blank line | | (empty line) |

**You can print ANY value** — it's automatically converted to text:
```scala
println(123)                    // 123
println(3.14)                   // 3.14
println(true)                   // true
println('A')                    // A
println(1 + 2)                  // 3  (expressions are evaluated first!)
println("a" + "b")              // ab
println(10 + " apples")         // 10 apples  (number + string)
println(List(1, 2, 3))          // List(1, 2, 3)
```

### 4.2 Joining text + values with `+` (concatenation)

```scala
val age = 21
println("I am " + age + " years old")    // I am 21 years old
```

### 4.3 String interpolation `s"..."` — the BEST way (memorize!)

Put `$` before the variable name inside `s"..."`:

```scala
val name = "Ravi"
val marks = 85

println(s"My name is $name")        // My name is Ravi
println(s"I scored $marks")         // I scored 85
println(s"Double: ${marks * 2}")    // { } = run any expression!
println(s"Sum: ${marks + 15}")      // Sum: 100
```

> **Rule**: `$var` for variables, `${expression}` for calculations.

### 4.4 `printf` — C-style formatted output

```scala
printf("format-string", value1, value2, ...)

printf("%d %d", 10, 20)          // 10 20
printf("%s is %d years old", "Ravi", 21)
```

**Format specifiers table (when to use which):**

| Specifier | For | Example | Output |
|---|---|---|---|
| `%d` | Int | `printf("%d", 50)` | 50 |
| `%f` | Double/Float | `printf("%f", 3.14159)` | 3.141590 |
| `%.2f` | Double, 2 decimals | `printf("%.2f", 3.14159)` | 3.14 |
| `%s` | String | `printf("%s", "hi")` | hi |
| `%c` | Char | `printf("%c", 'A')` | A |
| `%b` | Boolean | `printf("%b", true)` | true |
| `%n` | newline | `printf("line1%nline2")` | line1 then line2 |
| `%%` | percent sign | `printf("100%%")` | 100% |
| `%5d` | pad spaces | `printf("%5d", 42)` | `   42` |

Multiple at once:
```scala
printf("%d %.2f %s %c %b%n", 42, 3.14159, "hello", 'A', true)
// 42 3.14 hello A true
```

### 4.5 `f"..."` interpolation — same as printf but inside a string

```scala
val pi = 3.14159
println(f"Pi = $pi%.2f")         // Pi = 3.14
println(f"$pi%-10.3f!")          // padding support too
```

### 4.6 `raw"..."` — keep backslashes literal

```scala
println(raw"Line1\nLine2")       // prints \n as \n, NOT a newline
println("Line1\nLine2")          // prints a REAL newline here
```

### 4.7 Escape sequences inside normal strings

| Code | Meaning |
|---|---|
| `\n` | new line |
| `\t` | tab (4 spaces) |
| `\"` | double quote inside string |
| `\\` | backslash itself |

```scala
println("Name\tMarks")     // Name    Marks
println("He said \"Hi\"")  // He said "Hi"
```

### 4.8 `.mkString` — print collections with commas (see section 11)

```scala
println(List(1, 2, 3).mkString(", "))    // 1, 2, 3
println(Array(1, 2, 3).mkString(", "))   // works on arrays too
println(Set(1, 2, 3).mkString(", "))     // and sets
```

### 4.9 `.format` on a string (alternative to printf)

```scala
println("%d + %d = %d".format(2, 3, 2 + 3))   // 2 + 3 = 5
```

### 4.10 Full printing cheat — quick table

| You want | Use |
|---|---|
| Simple text | `println("text")` |
| Text + variable | `println(s"text $var")` |
| 2 decimals | `printf("%.2f", num)` or `f"$num%.2f"` |
| Tabular layout | `printf("%-10s%5d", name, marks)` |
| Collection with commas | `coll.mkString(", ")` |

---

## 5. THE MENU-DRIVEN PATTERN (memorize this!)

```scala
var choice = 0
while (choice != exitOption) {          // loop until user says "Exit"
    println("1. Option one")
    println("2. Option two")
    println("3. Exit")
    print("Enter choice: ")
    choice = sc.nextInt()

    choice match {
        case 1 => ...do option 1...
        case 2 => ...do option 2...
        case 3 => println("Bye!")
        case _ => println("Invalid choice!")   // _ = default
    }
}
```

**Why this works**: while loop keeps showing the menu. `match` handles each
choice. `case _` catches invalid input. Exit option breaks the loop.

---

## 6. THE COLLECTIONS REFERENCE (List, Set, Map, Tuple, Array)

### 6.1 What is what?

| Collection | Mutable? | Ordered? | Duplicates? | Holds |
|---|---|---|---|---|
| **Array** | ✅ Yes | ✅ Yes | ✅ Yes | same type |
| **List** | ❌ No | ✅ Yes | ✅ Yes | same type |
| **Set** | ❌ No | ❌ No | ❌ **NO!** | same type |
| **Map** | ❌ No | ❌ No | keys unique | key -> value pairs |
| **Tuple** | ❌ No | ✅ Yes | ✅ Yes | **mixed types!** |

---

### 6.2 LIST — immutable ordered collection

```scala
val fruits = List("apple", "mango", "banana")
val nums   = List(10, 20, 30, 40)
```

**Basic properties**
| Code | Result | Meaning |
|---|---|---|
| `fruits.length` | 3 | number of elements |
| `fruits.head` | "apple" | FIRST element |
| `fruits.tail` | List(mango, banana) | all EXCEPT first |
| `fruits.last` | "banana" | LAST element |
| `fruits(1)` | "mango" | element at index 1 (starts at 0!) |
| `fruits.isEmpty` | false | empty or not |
| `nums.sum` | 100 | total |
| `nums.max` / `nums.min` | 40 / 10 | largest / smallest |
| `nums.contains(20)` | true | is it there? |
| `nums.indexOf(20)` | 1 | position (or -1) |

**Adding & combining (returns NEW list — List is immutable!)**
```scala
val a = 5 :: nums          // prepend     -> List(5,10,20,30)
val b = nums :+ 50         // append      -> List(10,20,30,50)
val c = nums ::: List(5)   // merge lists -> List(10,20,30,5)
```

**Sorting & transforming**
```scala
nums.sorted                    // ascending
nums.sorted.reverse            // descending
nums.reverse                   // reversed
nums.distinct                  // remove duplicates
nums.take(2)                   // first 2
nums.drop(2)                   // all after first 2
```

**PRINTING A LIST WITH COMMAS (VERY COMMON EXAM QUESTION!)**
```scala
val nums = List(10, 20, 30, 40)

// Way 1: mkString — the simplest, join with any separator
println(nums.mkString(", "))      // 10, 20, 30, 40
println(nums.mkString(" | "))     // 10 | 20 | 30 | 40
println(nums.mkString("[", ", ", "]")) // [10, 20, 30, 40]

// Way 2: loop + comma logic (what faculty expects to see!)
for (i <- 0 until nums.length) {
    print(nums(i))
    if (i != nums.length - 1) print(", ")   // comma except after last
}
println()

// Way 3: foreach + comma check
nums.foreach(x => print(s"$x, "))   // 10, 20, 30, 40,  (trailing comma!)
```

**Looping over a List**
```scala
for (f <- fruits) println(f)            // for loop
fruits.foreach(f => println(f))         // foreach (see section 4.6)
fruits.foreach(println)                 // shortest form!
```

---

### 6.3 SET — no duplicates allowed!

```scala
val s = Set(1, 2, 3, 3, 2, 1)   // becomes Set(1, 2, 3) — dupes dropped!
```

| Code | Result | Meaning |
|---|---|---|
| `s + 10` | Set(1,2,3,10) | add (new set) |
| `s - 2` | Set(1,3) | remove (new set) |
| `s.contains(3)` | true | check membership |
| `s.size` | 3 | count |
| `Set(1,2,3) union Set(3,4)` | Set(1,2,3,4) | ALL elements |
| `Set(1,2,3) intersect Set(3,4)` | Set(3) | common elements |
| `Set(1,2,3) diff Set(3,4)` | Set(1,2) | only in first |

**PRINTING A SET WITH COMMAS**
```scala
val s = Set("ram", "sita", "ravi")
println(s.mkString(", "))        // ram, sita, ravi

// or manually with a loop:
var first = true
for (x <- s) {
    if (!first) print(", ")
    print(x)
    first = false
}
println()
```

**Mutable Set** (if you NEED to change it):
```scala
val ms = scala.collection.mutable.Set(1, 2, 3)
ms += 4          // actually adds now!
ms -= 1
println(ms)
```

---

### 6.4 MAP — key -> value pairs

```scala
val marks = Map("Ravi" -> 85, "Sita" -> 92, "Ram" -> 78)
```

| Code | Result | Meaning |
|---|---|---|
| `marks("Ravi")` | 85 | value by key |
| `marks.getOrElse("Krishna", 0)` | 0 | safe get (default) |
| `marks.contains("Ram")` | true | key exists? |
| `marks.keys` | Ravi, Sita, Ram | all keys |
| `marks.values` | 85, 92, 78 | all values |
| `marks.size` | 3 | entries count |
| `marks + ("Krishna" -> 88)` | new map | add entry |

**Looping over a Map**
```scala
for ((key, value) <- marks)
    println(s"$key scored $value")

marks.foreach { case (k, v) => println(s"$k -> $v") }
```

---

### 6.5 TUPLE — group of mixed values (like a row in a table)

```scala
val emp = (101, "Ravi", 50000)    // Int, String, Int — ANY mix of types!
```

| Code | Result | Meaning |
|---|---|---|
| `emp._1` | 101 | 1st element |
| `emp._2` | "Ravi" | 2nd element |
| `emp._3` | 50000 | 3rd element |
| `val (id, n, sal) = emp` | — | destructure into 3 vars |
| `(10, 20).swap` | (20, 10) | swap a pair |

**Tuple in a function (return MULTIPLE values!):**
```scala
def minMax(l: List[Int]): (Int, Int) = (l.min, l.max)

val (mn, mx) = minMax(List(5, 2, 9, 1))
println(s"Min = $mn, Max = $mx")
```

**List of tuples (like a database table!):**
```scala
val students = List((1, "Ravi", 85), (2, "Sita", 92))
for ((sid, name, marks) <- students)     // destructure in loop!
    println(s"ID: $sid, Name: $name, Marks: $marks")
```

**Tuple Rules to memorize:**
- Access with `_1, _2, _3...` (starts at **1**, not 0!)
- A tuple's type is `(Int, String, Int)` — dims can't change
- Immutable — can't modify; make a new tuple instead
- `(a, b)` is a Pair — the most used tuple

---

### 6.6 FOREACH — do something with every element

```scala
val nums = List(10, 20, 30, 40)

// All the ways to write it (all do the same thing):
nums.foreach(x => println(x))       // full lambda
nums.foreach(x => print(s"$x "))    // transform while printing
nums.foreach(println)               // shortest — method reference
nums.foreach(print)                 // print each (no newline)
```

**foreach + comma separator (exam favourite!):**
```scala
var idx = 0
nums.foreach { x =>
    print(x)
    idx += 1
    if (idx < nums.length) print(", ")   // comma after every element except last
}
println()   // 10, 20, 30, 40
```

**foreach vs for-loop — when to use which:**
| | for-loop | foreach |
|---|---|---|
| Need index? | ✅ yes | ⚠ via zipWithIndex |
| Common in lab | ✅ most used | ✅ very used |
| One-liner | ❌ | ✅ |
| Break early | sim. with flag | sim. with flag |
| Works on any collection | ✅ | ✅ |

**zipWithIndex (get index + value in foreach):**
```scala
nums.zipWithIndex.foreach { case (value, index) =>
    println(s"Index $index = $value")
}
```

---

### 6.7 THE BIG FOUR: map, filter, reduce, foreach (+ friends)

| Function | What it does | Example | Result |
|---|---|---|---|
| **map** | transform EVERY element | `nums.map(_ * 2)` | doubled |
| **filter** | KEEP matches | `nums.filter(_ % 2 == 0)` | evens only |
| **reduce** | combine into ONE value | `nums.reduce(_ + _)` / `nums.sum` | total |
| **foreach** | act on each, no result | `nums.foreach(println)` | prints |
| **count** | how many match | `nums.count(_ > 5)` | number |
| **find** | first match | `nums.find(_ > 5)` | Some(6) |
| **exists** | any match? | `nums.exists(_ > 9)` | true/false |
| **forall** | all match? | `nums.forall(_ > 0)` | true/false |
| **sorted** | sort | `nums.sorted` | sorted list |
| **groupBy** | group | `nums.groupBy(_ % 2 == 0)` | map of groups |

**Chaining (super powerful — memorize!):**
```scala
val nums = (1 to 10).toList

// evens only -> doubled -> sum
nums.filter(_ % 2 == 0).map(_ * 2).sum

// print each even with commas
nums.filter(_ % 2 == 0).map(_ * 2).mkString(", ")
```

---

## 7. The Most Commonly Asked Lab Programs

### Numbers
- ✅ Factorial (`for i <- 1 to n; f *= i`)
- ✅ Prime check (`for i <- 2 to sqrt(n)`)
- ✅ Fibonacci (`a + b` swap loop)
- ✅ Palindrome / Reverse number (`rev = rev*10 + temp%10`)
- ✅ Armstrong number (`sum += pow(digit, digits)`)
- ✅ Sum of digits / Count digits
- ✅ GCD / LCM (Euclid's method)
- ✅ Even/Odd, Leap year, Tables

### Arrays
- ✅ Largest / smallest / sum / average (`.max .min .sum`)
- ✅ Linear search (`for ... if arr(i) == key`)
- ✅ Reverse (`.reverse`), Sort (`.sorted`)
- ✅ Count even/odd (`filter(_ % 2 == 0)`)
- ✅ 2D matrices — add/subtract/multiply (nested loops)

### Lists (immutable)
- ✅ Print with commas — `list.mkString(", ")`
- ✅ Add at start (`::`), end (`:+`), merge (`:::`)
- ✅ `head` / `tail` / `last` / `length`
- ✅ Sort, reverse, distinct, sum, min, max

### Sets
- ✅ Remove duplicates: `Set(...)` auto-dedupes
- ✅ `union` / `intersect` / `diff`
- ✅ Print with commas — `set.mkString(", ")`
- ✅ Membership check — `set.contains(x)`

### Tuples
- ✅ Group mixed data: `(101, "Ravi", 50000)`
- ✅ Access: `_1`, `_2`, `_3`
- ✅ Destructure: `val (a, b, c) = tuple`
- ✅ Return multiple values from a function

### Strings
- ✅ Reverse (`.reverse`), Palindrome (`s == s.reverse`)
- ✅ Vowel/consonant count (`"aeiou".contains(c)`)
- ✅ Word count (`split(" ")`)
- ✅ Character frequency (loop + count)
- ✅ Uppercase/lowercase, substring, split/join

### Higher Order Functions
- ✅ `map` — transform each (`_.map(_ * 2)`)
- ✅ `filter` — keep matches (`_.filter(_ % 2 == 0)`)
- ✅ `reduce`/`sum` — combine all
- ✅ `foreach` — act on each element
- ✅ `count`, `find`, `exists`, `forall`

---

## 8. Common Traps (avoid these in the lab!)

| Trap | Fix |
|---|---|
| `val` reassignment | use `var` |
| Array index starts 0 | `arr(0)` = first |
| Tuple starts at `_1` | `tuple._1` is first (NOT _0!) |
| Decimal division `5/2 = 2` | use `5/2.0` or `.toDouble` |
| Comparing strings with `==` | works in Scala, use it! |
| Leftover newline after `nextInt()` | add `sc.nextLine()` before reading text |
| Forgot to `import java.util.Scanner` | compiler error: "not found: type Scanner" |
| `sc.next()` can't read spaces | use `sc.nextLine()` for full lines |
| Typing wrong input type (e.g. text for `nextInt`) | crashes! — re-read with correct method |
| `1 to 10` vs `1 until 10` | `to` includes 10, `until` doesn't |
| Case class `new` | case classes don't need `new` |
| List is immutable | use `:+` / `::` to make NEW list |
| Set drops duplicates | expect it — that's its purpose |
| Trailing comma in loops | skip comma after last element |
| `x match` with different types | type the variable as `Any` |
| `printf` with wrong specifier | `%d` int, `%f` double, `%s` string |
| `s"$x"` missing for values | `println("x is " + x)` still works, `s"..."` is cleaner |

---

## 9. 2-Day Study Plan

### Day 1 (today): Concepts
1. Read `01_basics.scala` — types, I/O, operators
2. Read **README sections 3 & 4** — user input (Scanner/StdIn) + printing
3. Read `02_control_flow.scala` — if/else + match → *****MOST IMPORTANT*****
4. Read `03_loops.scala` — for/while/do-while
5. Rewrite the CALCULATOR menu program from memory (no peeking!)
6. Read `04_functions.scala` — def + recursion
7. Read `07_collections.scala` — List, Set, Map, Tuple, foreach

### Day 2 (tomorrow): Data + Practice
8. Read `05_arrays.scala` + `06_strings.scala` — the highest-probability topics
9. Read `08_tuples_matching.scala` — tuples + pattern matching
10. Read `09_oop.scala` + `10_higher_order.scala`
11. Run ALL 3 Practice files. Understand every line.
12. Write a menu program WITHOUT looking — mix of numbers + arrays + lists.

---

## 10. How to Practice

**Option A — Online (fastest, use in lab if internet works):**
> https://scastie.scala-lang.org → paste → RUN

**Option B — If you have `scala` installed:**
```bash
scala ProgramName.scala
```

**Option C — Compile & run:**
```bash
scalac ProgramName.scala
scala ProgramName
```

**Pro-tip for the lab:** Write the menu skeleton FIRST (the loop + match +
default case). Then fill in each case one by one. Test after each case.

---

## 11. Comma-Separation Quick Recap (answer for any "print with commas" question)

```scala
// For ANY collection (List, Set, Array, Vector):
collection.mkString(", ")          // simplest, joins with commas

// Manual loop version (always works, shows logic):
for (i <- 0 until coll.length) {
    print(coll(i))
    if (i != coll.length - 1) print(", ")
}
println()

// foreach version (no index needed):
var first = true
coll.foreach { x =>
    if (!first) print(", ")
    print(x)
    first = false
}
println()

// zipWithIndex + mkString for pure Scala style:
coll.map(_.toString).mkString(", ")
```