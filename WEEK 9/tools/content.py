S = []

S.append(dict(
 no=18, week=9, date="10/09/2026", typ="Exercise Program", title="Arrays in Scala",
 problem=("Create an array of integers with the values 2, 5, 9, 14, 20. Write a function that "
          "takes this array and returns the sum of its elements. Next, create an array of strings "
          "with the names of five different fruits. Write a function that concatenates all "
          "elements of this array, separated by commas. Finally, iterate over the array of "
          "integers and print each element to the console."),
 objectives=["To declare and initialize fixed-size arrays in Scala.",
             "To write a user-defined function that aggregates an integer array.",
             "To write a user-defined function that joins a string array.",
             "To traverse an array with an index loop and print every element.",
             "To verify a computed aggregate against an independent calculation."],
 dataset=("No external dataset is required. The inputs are declared inside the program: the "
          "integer array (2, 5, 9, 14, 20) and the string array "
          "(Apple, Banana, Mango, Grapes, Orange)."),
 functions=[("Array()","Scala","Creates a fixed-size array from the supplied elements."),
            ("sum","Scala","Returns the total of all elements of a numeric array."),
            ("mkString()","Scala","Joins every element into one string using a separator."),
            ("length","Scala","Returns the number of elements stored in the array."),
            ("apply(index)","Scala","Returns the element stored at the given index."),
            ("Array[Int]","Scala","Declares an array whose elements are integers."),
            ("Array[String]","Scala","Declares an array whose elements are strings."),
            ("def","Scala","Declares the user-defined functions used by the program."),
            ("while","Scala","Repeats the traversal while the index is below the length."),
            ("println()","Scala","Writes one formatted line of text to the console."),
            ("== (equality)","Scala","Compares the manual sum with the function result."),
            ("main()","Scala","Entry point that executes the program.")],
 steps=["1. Declare the integer array with the values 2, 5, 9, 14 and 20.",
        "2. Define sumOfArray() that returns the total of the array elements.",
        "3. Print the integer array, its length and the computed sum.",
        "4. Declare the string array containing the names of five fruits.",
        "5. Define concatenateStrings() that joins the elements using mkString.",
        "6. Define printElements() that walks the array with an index loop.",
        "7. Call printElements() so every integer is printed with its index.",
        "8. Compute the sum manually and compare it with the function result.",
        "9. Print the verification line and terminate the program."],
 concl=("The integer array (2, 5, 9, 14, 20) was created successfully and the user-defined "
        "function returned a total of 50, which matched the manually calculated value. The string "
        "array of five fruits was concatenated into a single comma-separated string using "
        "mkString(). The index-based traversal printed every element of the integer array together "
        "with its position. The experiment demonstrated that Scala arrays are fixed-size, "
        "index-addressable collections and that aggregation and string joining can be expressed "
        "concisely through built-in collection methods."),
 refs=["1. Scala Array documentation: https://www.scala-lang.org/api/current/scala/Array.html",
       "2. Scala Collections overview: https://docs.scala-lang.org/overviews/collections/overview.html",
       "3. Class lecture: Arrays and array operations in Scala."],
 explain1=("The integer array is printed first with its length, and the user-defined function returns the sum 50, which the next line confirms against the manually calculated value. The string array is joined with mkString so the five fruit names appear as one comma-separated line."),
 explain2=("The index loop walks the array from position 0 to 4 and prints each element beside its index, which shows that a Scala array is addressable by position. The final verification line reports that the manual sum and the function result are equal."),
 snap1=("Fig. 1.1: Terminal execution showing creation of the integer array, its length and the "
        "sum returned by the user-defined function. The string array is concatenated using mkString()."),
 snap2=("Fig. 1.2: Index-based traversal printing every element of the integer array, followed "
        "by the verification line confirming that the function result matches the manual sum.")))

S.append(dict(
 no=19, week=10, date="17/09/2026", typ="Exercise Program", title="Lists, Sets and Tuples in Scala",
 problem=("Create a list of the first five prime numbers. Write a function that takes this list "
          "and returns a new list with each element squared. Then, create a set of unique "
          "characters from the string hello world and write a function that takes two sets and "
          "returns their intersection. Create a tuple with three elements: an integer, a string "
          "and a boolean, then access and print each element."),
 objectives=["To create immutable lists and transform their elements with a function.",
             "To build a set of unique characters from a string.",
             "To compute the intersection of two sets.",
             "To construct a tuple holding three different types and access its components.",
             "To compare immutable collections with the arrays used earlier."],
 dataset=("No external dataset is required. The inputs are the first five prime numbers "
          "(2, 3, 5, 7, 11), the literal string hello world and the tuple "
          "(101, Hasnain Makada, true)."),
 functions=[("List()","Scala","Creates an immutable linked list of elements."),
            ("map()","Scala","Applies a function to every element, returning a new list."),
            ("sum","Scala","Returns the total of all elements of a numeric list."),
            ("toSet","Scala","Converts a string or collection into a set of unique values."),
            ("Set()","Scala","Creates an immutable set that rejects duplicates."),
            ("intersect()","Scala","Returns the elements common to two sets."),
            ("size","Scala","Returns the number of elements in a set or list."),
            ("toList","Scala","Converts a set into a list so that it can be sorted."),
            ("sorted","Scala","Orders the elements of a collection in ascending order."),
            ("Tuple3 / ( )","Scala","Creates a tuple grouping three values of mixed types."),
            ("_1, _2, _3","Scala","Accesses the first, second and third tuple components."),
            ("println()","Scala","Writes one formatted line of text to the console.")],
 steps=["1. Create the list of the first five prime numbers 2, 3, 5, 7 and 11.",
        "2. Define squareList() that maps every element of the list to its square.",
        "3. Print the original list, the squared list and the sum of the squares.",
        "4. Convert the string hello world into a set of unique characters.",
        "5. Print the unique characters and their count.",
        "6. Define intersectSets() that returns the common elements of two sets.",
        "7. Intersect the character set with the vowel set and print the result.",
        "8. Create the tuple (101, Hasnain Makada, true).",
        "9. Access and print each tuple component using _1, _2 and _3."],
 concl=("A list of the first five prime numbers was created and the mapping function returned the "
        "squared list (4, 9, 25, 49, 121) with a total of 208. Converting the string hello world "
        "into a set removed all duplicate letters and left eight unique characters, and the "
        "intersection with the vowel set produced {e, o}. The three-element tuple was created and "
        "each component was accessed and printed individually. The experiment showed that Scala "
        "lists preserve order, sets guarantee uniqueness and tuples group heterogeneous values "
        "without a dedicated class."),
 refs=["1. Scala List documentation: https://www.scala-lang.org/api/current/scala/collection/immutable/List.html",
       "2. Scala Set documentation: https://www.scala-lang.org/api/current/scala/collection/immutable/Set.html",
       "3. Scala Tuples guide: https://docs.scala-lang.org/tour/tuples.html"],
 explain1=("The list of five primes is printed, followed by the squared list produced by the mapping function and the sum of those squares, so the transformation applied to every element is visible in one place."),
 explain2=("Converting the string to a set removes the repeated letters and leaves eight unique characters. Intersecting that set with the vowel set returns only e and o, and the tuple is then printed whole before each of its three components is echoed individually."),
 snap1=("Fig. 2.1: Terminal execution showing the list of prime numbers, the squared list produced "
        "by the user-defined function and the sum of the squares."),
 snap2=("Fig. 2.2: Unique characters extracted from the string, the vowel intersection and the "
        "three components of the tuple printed individually.")))

S.append(dict(
 no=20, week=11, date="24/09/2026", typ="Exercise Program",
 title="HashMaps: Handling Collisions and Resolving Conflicts",
 problem=("Create a HashMap with keys representing student names and values representing their "
          "grades, then insert multiple entries including a duplicate key with a different grade. "
          "Write a function to merge two HashMaps, resolving conflicts by taking the higher "
          "grade. Finally, write a function to handle collisions by chaining, using lists to "
          "store multiple values for a single key."),
 objectives=["To create and update a mutable HashMap of student names and grades.",
             "To observe how a duplicate key overwrites the previously stored value.",
             "To merge two HashMaps while resolving key conflicts deterministically.",
             "To implement separate chaining so colliding keys share a bucket.",
             "To explain the role of the hash function in distributing keys."],
 dataset=("No external dataset is required. All records are declared inside the program: student "
          "names paired with integer grades, plus a second set of six names used to force "
          "collisions across four buckets."),
 functions=[("mutable.HashMap()","Scala","Creates a mutable hash table keyed by student name."),
            ("+= (key -> value)","Scala","Inserts a new entry or overwrites an existing key."),
            ("get()","Scala","Returns the value for a key wrapped in an Option."),
            ("match / Some / None","Scala","Selects the conflict-resolution branch for a key."),
            ("++= (collection)","Scala","Copies all entries of one map into another."),
            ("toSeq.sorted","Scala","Orders entries so the map prints deterministically."),
            ("hashCode","Scala","Produces the integer hash used to choose a bucket."),
            ("abs / % (modulus)","Scala","Maps the hash onto a valid bucket index."),
            ("Array.fill()","Scala","Creates the fixed array of bucket chains."),
            ("List / :: (cons)","Scala","Stores several colliding entries in one bucket chain."),
            ("collect()","Scala","Extracts all values that match a key inside a chain."),
            ("foreach / for","Scala","Traverses the bucket array to print occupied buckets.")],
 steps=["1. Create a mutable HashMap with three student names and their grades.",
        "2. Insert two more students, then insert an existing key with a different grade.",
        "3. Observe that the duplicate key replaces the earlier grade.",
        "4. Define mergeTakingHigher() that copies the first map into a new map.",
        "5. For every key of the second map keep the larger of the two grades.",
        "6. Print both input maps and the merged map to show resolved conflicts.",
        "7. Define a ChainedHashMap class with a fixed number of buckets.",
        "8. Compute the bucket index as |key.hashCode| % bucketCount.",
        "9. Insert six names so several of them land in the same bucket.",
        "10. Print the non-empty buckets to show the chains built by separate chaining."],
 concl=("The initial HashMap stored three students and the duplicate insertion for Hasnain "
        "replaced the earlier grade of 88 with 93, confirming that a HashMap allows only one "
        "value per key. Merging two HashMaps with the higher-grade rule produced a combined map "
        "in which Hasnain kept 93 and Zoya was upgraded from 81 to 90. The chained implementation "
        "placed six keys into four buckets, with bucket 0 holding Neha and Rahul and bucket 1 "
        "holding Sara and Zoya, so no entry was lost even though the hash function assigned two "
        "keys to the same index."),
 refs=["1. Scala HashMap documentation: https://www.scala-lang.org/api/current/scala/collection/mutable/HashMap.html",
       "2. Hash table collision resolution: https://en.wikipedia.org/wiki/Hash_table#Collision_resolution",
       "3. Class lecture: Maps and HashMaps in Scala."],
 explain1=("The initial map holds three students. After the inserts the duplicate key Hasnain replaces the earlier grade of 88 with 93, which shows that a HashMap keeps one value per key. The merged map then resolves the overlapping names by keeping the higher grade."),
 explain2=("The hash function assigns every name to one of four buckets, and two pairs of names land in the same bucket. The bucket table printed underneath lists both entries in each of those chains, so no record is lost even though two keys share an index."),
 snap1=("Fig. 3.1: Terminal execution showing the initial HashMap, insertion of new entries, the "
        "duplicate-key overwrite and the merge of two HashMaps taking the higher grade."),
 snap2=("Fig. 3.2: Bucket assignment produced by the hash function and the non-empty buckets "
        "showing separate chaining for colliding keys.")))

S.append(dict(
 no=21, week=12, date="08/10/2026", typ="Exercise Program",
 title="Advanced Functional Combinators in Scala",
 problem=("Create a list of integers from 1 to 10, then use filter to create a new list with only "
          "even numbers. Use map to create a new list where each element is multiplied by 3. Use "
          "flatMap to create a list of tuples where each integer is paired with its square. "
          "Finally, use foldLeft to calculate the product of all elements in the list."),
 objectives=["To apply filter, map and flatMap to an immutable list of integers.",
             "To distinguish flatMap from map by the shape of the returned collection.",
             "To reduce a collection to a single value with foldLeft.",
             "To chain several combinators into one readable transformation pipeline.",
             "To compare each combinator result against known values."],
 dataset=("No external dataset is required. The source collection is the list of integers from 1 "
          "to 10 generated with (1 to 10).toList."),
 functions=[("(1 to 10).toList","Scala","Builds the source list of ten integers."),
            ("filter()","Scala","Keeps only the elements that satisfy a predicate."),
            ("map()","Scala","Transforms every element, preserving the collection length."),
            ("flatMap()","Scala","Transforms each element and flattens results into one list."),
            ("foldLeft()","Scala","Reduces the list left to right using an accumulator."),
            ("product","Scala","Multiplies all elements, used to verify foldLeft."),
            ("sum","Scala","Adds all elements, used to total the mapped list."),
            ("length","Scala","Counts the elements produced by a combinator."),
            ("mkString()","Scala","Joins the resulting elements into one display string."),
            ("List((n, n*n))","Scala","Wraps each pair so flatMap can flatten it."),
            ("println()","Scala","Writes one formatted line of text to the console."),
            ("main()","Scala","Entry point that executes the program.")],
 steps=["1. Build the source list of the integers 1 to 10.",
        "2. Apply filter with the predicate n % 2 == 0 to keep the even numbers.",
        "3. Apply map with the function n * 3 to triple every element.",
        "4. Apply flatMap so each integer is paired with its square.",
        "5. Apply foldLeft with seed 1 and multiplication to obtain 10 factorial.",
        "6. Verify the foldLeft result against the built-in product of the list.",
        "7. Chain filter, map and foldLeft into a single transformation pipeline.",
        "8. Print a summary of how many elements each combinator produced."],
 concl=("Applying filter to the list 1 to 10 returned the five even numbers (2, 4, 6, 8, 10), "
        "while map with multiplication by three produced a list of the same length containing "
        "(3, 6, 9, ..., 30). flatMap paired every integer with its square and flattened the pairs "
        "into a single list of ten tuples, and foldLeft returned 3628800, which matches the "
        "built-in product and confirms 10 factorial. The combined pipeline of filter, map and "
        "foldLeft produced 90 in a single expression, showing that functional combinators can "
        "replace explicit loops with shorter and more declarative code."),
 refs=["1. Scala collections operations: https://docs.scala-lang.org/overviews/collections/operations.html",
       "2. Scala tour: anonymous function syntax: https://docs.scala-lang.org/tour/anonymous-function-syntax.html",
       "3. Class lecture: Functional combinators in Scala."],
 explain1=("The source list 1 to 10 is shown, followed by the five even numbers returned by filter and the ten tripled values returned by map. The flatMap block pairs every integer with its square and flattens the pairs into a single list."),
 explain2=("foldLeft reduces the list to 3628800, and the verification line confirms that this equals the built-in product of 1 to 10. The combined pipeline then applies filter, map and foldLeft in one expression to give 90, and the summary counts how many elements each combinator produced."),
 snap1=("Fig. 4.1: Terminal execution showing the source list, the filtered even numbers, the "
        "tripled list and the flatMap pairs generated from the input list."),
 snap2=("Fig. 4.2: foldLeft product with its verification against the built-in product, the "
        "combined pipeline result and the summary of combinator outputs.")))
