// Program 25 - Spire for exact statistics, Saddle for data manipulation
// Week 14 | 22-10-2026 | Exercise Program
import spire.implicits._
import spire.math._
import org.saddle._
import java.io._

object Program25 {

  def main(args: Array[String]): Unit = {
    println("=" * 68)
    println("PROGRAM 25 : EXACT PRICE STATISTICS WITH SPIRE AND SADDLE")
    println("=" * 68)

    val fruits = Array("Apple", "Apple", "Apple", "Apple", "Apple",
                       "Banana", "Banana", "Banana", "Banana", "Banana")
    val prices = Array(120.0, 125.0, 118.0, 130.0, 128.0,
                       45.0, 47.0, 44.0, 49.0, 46.0)

    // 1. Saddle holds the data
    val idx = Index((0 until prices.length).map(_.toString): _*)
    val priceSeries = Series(Vec(prices: _*), idx)

    println("\n1. Price series loaded into Saddle")
    println(priceSeries)

    // 2. Split by fruit using Saddle row selection
    val appleIdx  = fruits.zipWithIndex.collect { case (f, k) if f == "Apple"  => k }
    val bananaIdx = fruits.zipWithIndex.collect { case (f, k) if f == "Banana" => k }
    val appleVec  = priceSeries.toVec(appleIdx: _*)
    val bananaVec = priceSeries.toVec(bananaIdx: _*)

    println("\n2. Apples  (" + appleVec.length + " observations) : " + appleVec.contents.mkString(", "))
    println("   Bananas (" + bananaVec.length + " observations) : " + bananaVec.contents.mkString(", "))

    // 3. Spire gives exact rational arithmetic, so the mean and variance carry no
    //    floating point drift at all.
    def exactStats(values: Array[Double]): (Rational, Rational) = {
      val rats = values.toList.map(v => Rational(v))
      val n = Rational(rats.length)
      val mean = rats.foldLeft(Rational(0))(_ + _) / n
      val sqDev = rats.map(v => (v - mean) * (v - mean)).foldLeft(Rational(0))(_ + _)
      val variance = sqDev / n
      (mean, variance)
    }

    val (appleMean, appleVar)   = exactStats(appleVec.contents)
    val (bananaMean, bananaVar) = exactStats(bananaVec.contents)

    println("\n3. Exact statistics computed with Spire Rational")
    println("   Apple  mean     : " + appleMean + "  = " + "%.4f".format(appleMean.toDouble))
    println("   Apple  variance : " + appleVar + "  = " + "%.4f".format(appleVar.toDouble))
    println("   Banana mean     : " + bananaMean + "  = " + "%.4f".format(bananaMean.toDouble))
    println("   Banana variance : " + bananaVar + "  = " + "%.4f".format(bananaVar.toDouble))

    // 4. Cross-check against Saddle's own floating-point reductions
    println("\n4. Cross-check against Saddle")
    println("   Apple  Saddle mean : " + "%.4f".format(appleVec.mean))
    println("   Banana Saddle mean : " + "%.4f".format(bananaVec.mean))
    val diffA = (appleMean.toDouble - appleVec.mean).abs
    val diffB = (bananaMean.toDouble - bananaVec.mean).abs
    println("   difference apple   : " + diffA)
    println("   difference banana  : " + diffB)

    // 5. Comparison table
    println("\n5. Comparison")
    println("   %-10s %14s %14s".format("Fruit", "Exact mean", "Exact variance"))
    println("   " + "-" * 40)
    println("   %-10s %14s %14s".format("Apple", "%.4f".format(appleMean.toDouble), "%.4f".format(appleVar.toDouble)))
    println("   %-10s %14s %14s".format("Banana", "%.4f".format(bananaMean.toDouble), "%.4f".format(bananaVar.toDouble)))

    // 6. Vega-Lite trend spec (the grammar Vegas is built on)
    val rows = fruits.indices.map { k =>
      "{\"fruit\":\"" + fruits(k) + "\",\"index\":" + k + ",\"price\":" + prices(k) + "}"
    }.mkString(",")
    val spec =
      "{\n  \"$schema\": \"https://vega.github.io/schema/vega-lite/v5.json\",\n" +
      "  \"title\": \"Fruit price trend\",\n" +
      "  \"data\": {\"values\": [" + rows + "]},\n" +
      "  \"mark\": {\"type\": \"line\", \"point\": true},\n" +
      "  \"encoding\": {\n" +
      "    \"x\": {\"field\": \"index\", \"type\": \"quantitative\", \"title\": \"Observation\"},\n" +
      "    \"y\": {\"field\": \"price\", \"type\": \"quantitative\", \"title\": \"Price\"},\n" +
      "    \"color\": {\"field\": \"fruit\", \"type\": \"nominal\"}\n" +
      "  }\n}"
    val pw = new PrintWriter(new File("program25_price_trend.json"))
    pw.println(spec)
    pw.close()
    println("\n6. Vega-Lite trend spec written to program25_price_trend.json")
    println("=" * 68)
  }
}
