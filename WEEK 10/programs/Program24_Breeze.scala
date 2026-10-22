// Program 24 - Breeze for numerical computation, Plotly for the chart
// Week 14 | 22-10-2026 | Exercise Program
import breeze.linalg._
import java.io._

object Program24 {

  def main(args: Array[String]): Unit = {
    println("=" * 68)
    println("PROGRAM 24 : FRUIT REVENUE WITH BREEZE")
    println("=" * 68)

    val fruits = Array("Apple", "Banana", "Mango", "Orange", "Grapes")

    // 1. Raw data as Breeze vectors
    val price    = DenseVector(120.0, 45.0, 90.0, 70.0, 150.0)
    val quantity = DenseVector(50.0, 80.0, 40.0, 60.0, 25.0)

    println("\n1. Price per kg (Breeze DenseVector)")
    println("   " + price)
    println("\n2. Quantity sold (Breeze DenseVector)")
    println("   " + quantity)

    // 3. Element-wise revenue
    val revenue = price *:* quantity
    println("\n3. Revenue = price *:* quantity (element-wise)")
    for (i <- 0 until fruits.length) {
      println("   " + fruits(i) + " : " + price(i) + " x " + quantity(i) + " = " + revenue(i))
    }

    // 4. Aggregate results with Breeze reductions
    println("\n4. Aggregate statistics")
    println("   total revenue : " + sum(revenue))
    println("   mean revenue  : " + sum(revenue) / revenue.length.toDouble)
    println("   max revenue   : " + max(revenue) + " (" + fruits(argmax(revenue)) + ")")
    println("   min revenue   : " + min(revenue) + " (" + fruits(argmin(revenue)) + ")")
    println("   revenue std   : " + math.sqrt(breeze.stats.variance(revenue)))

    // 5. Normalised share of total revenue
    println("\n5. Share of total revenue")
    val share = revenue / sum(revenue) * 100.0
    for (i <- 0 until fruits.length) {
      println("   " + fruits(i) + " : " + "%.2f".format(share(i)) + " %")
    }

    // 6. Build the Plotly figure as a standalone HTML file
    val bars = fruits.indices.map { i =>
      "      {\"x\": [\"" + fruits(i) + "\"], \"y\": [" + revenue(i) +
        "], \"type\": \"bar\", \"name\": \"" + fruits(i) + "\", \"marker\": {\"color\": \"" +
        List("#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd").apply(i) + "\"}}"
    }.mkString(",\n")

    val html =
      "<!DOCTYPE html>\n<html>\n<head><meta charset=\"utf-8\" />\n" +
      "<script src=\"https://cdn.plot.ly/plotly-2.27.0.min.js\"></script></head>\n" +
      "<body>\n<div id=\"chart\" style=\"width:900px;height:520px;\"></div>\n" +
      "<script>\nvar data = [\n" + bars + "\n];\n" +
      "var layout = {\"title\": \"Total revenue per fruit type\",\n" +
      "  \"xaxis\": {\"title\": \"Fruit\"},\n" +
      "  \"yaxis\": {\"title\": \"Revenue\"},\n" +
      "  \"barmode\": \"group\"};\n" +
      "Plotly.newPlot('chart', data, layout);\n</script>\n</body>\n</html>\n"

    val pw = new PrintWriter(new File("program24_revenue.html"))
    pw.println(html)
    pw.close()
    println("\n6. Interactive bar chart written to program24_revenue.html")

    // 7. ASCII bar chart for the terminal record
    println("\n7. Revenue bar chart (terminal view)")
    val top = max(revenue)
    for (i <- 0 until fruits.length) {
      val n = (revenue(i) / top * 40).toInt
      println("   " + "%-8s".format(fruits(i)) + " " + "#" * n + " " + revenue(i))
    }
    println("=" * 68)
  }
}
