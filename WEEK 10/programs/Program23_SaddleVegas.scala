// Program 23 - Saddle for data manipulation, Vegas for visualisation
// Week 13 | 15-10-2026 | Exercise Program
import org.saddle._
import java.io._

object Program23 {

  def f2(x: Double): String = "%.2f".format(x)

  def main(args: Array[String]): Unit = {
    println("=" * 68)
    println("PROGRAM 23 : FRUIT PRICES WITH SADDLE")
    println("=" * 68)

    // 1. Build the dataset: day, price, quantity (all rows are apples)
    val days     = Array("Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7")
    val prices   = Array(120.0, 125.0, 118.0, 130.0, 128.0, 135.0, 132.0)
    val quantity = Array(50.0, 45.0, 60.0, 40.0, 55.0, 38.0, 48.0)

    val priceSeries = Series(Vec(prices: _*), Index(days: _*))
    val qtySeries   = Series(Vec(quantity: _*), Index(days: _*))

    println("\n1. Price series (Saddle Series)")
    println(priceSeries)

    println("\n2. Quantity series (Saddle Series)")
    println(qtySeries)

    // 2. Filter for apples
    // Fruit names live alongside the series; the apple rows are selected by position
    val fruits = Array("Apple", "Apple", "Apple", "Apple", "Apple", "Apple", "Apple")
    val appleIdx = fruits.zipWithIndex.collect { case (f, k) if f == "Apple" => k }
    val appleVec = priceSeries.toVec(appleIdx: _*)
    println("\n3. Filtered for apples -> " + appleVec.length + " observations")
    println(appleVec)

    // 3. Average price
    val avgPrice = appleVec.mean
    println("\n4. Average apple price : " + f2(avgPrice))

    // 4. Descriptive statistics
    println("\n5. Descriptive statistics")
    println("   count : " + appleVec.length)
    println("   min   : " + f2(appleVec.min.getOrElse(0.0)))
    println("   max   : " + f2(appleVec.max.getOrElse(0.0)))
    println("   sum   : " + f2(appleVec.sum))

    // 5. Day-on-day change
    println("\n6. Day-on-day price change")
    val vals = appleVec.contents
    var i = 1
    while (i < vals.length) {
      val d = vals(i) - vals(i - 1)
      val arrow = if (d >= 0) "UP  " else "DOWN"
      println("   " + days(i - 1) + " -> " + days(i) + " : " + arrow + " " + f2(d))
      i += 1
    }

    // 6. Revenue per day
    val revenue = priceSeries * qtySeries
    println("\n7. Daily revenue (price x quantity)")
    println(revenue)
    println("   total revenue : " + f2(revenue.sum))

    // 7. Emit an interactive Vega-Lite spec (the grammar Vegas is built on)
    val rows = days.indices.map { k =>
      "{\"day\":\"" + days(k) + "\",\"price\":" + prices(k) +
        ",\"quantity\":" + quantity(k) + "}"
    }.mkString(",")
    val spec =
      "{\n" +
      "  \"$schema\": \"https://vega.github.io/schema/vega-lite/v5.json\",\n" +
      "  \"title\": \"Apple price trend over one week\",\n" +
      "  \"data\": {\"values\": [" + rows + "]},\n" +
      "  \"mark\": {\"type\": \"line\", \"point\": true},\n" +
      "  \"encoding\": {\n" +
      "    \"x\": {\"field\": \"day\", \"type\": \"ordinal\", \"title\": \"Day\"},\n" +
      "    \"y\": {\"field\": \"price\", \"type\": \"quantitative\", \"title\": \"Price (per kg)\"}\n" +
      "  }\n" +
      "}"
    val pw = new PrintWriter(new File("program23_price_trend.json"))
    pw.println(spec)
    pw.close()
    println("\n8. Vega-Lite trend spec written to program23_price_trend.json")
    println("=" * 68)
  }
}
