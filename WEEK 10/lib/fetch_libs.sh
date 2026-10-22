#!/usr/bin/env bash
# Fetch the Scala libraries needed by Week 10 programs 23-25.
# Run from this directory:  bash fetch_libs.sh
set -e
BASE=https://repo1.maven.org/maven2
JARS=(
  org/scalanlp/breeze_2.11/1.0/breeze_2.11-1.0.jar
  org/scalanlp/breeze-macros_2.11/1.0/breeze-macros_2.11-1.0.jar
  org/scalanlp/breeze-viz_2.11/1.0/breeze-viz_2.11-1.0.jar
  org/scala-saddle/saddle-core_2.11/1.3.4/saddle-core_2.11-1.3.4.jar
  org/spire-math/spire_2.11/0.13.0/spire_2.11-0.13.0.jar
  org/spire-math/spire-macros_2.11/0.13.0/spire-macros_2.11-0.13.0.jar
  com/chuusai/shapeless_2.11/2.3.3/shapeless_2.11-2.3.3.jar
  org/scala-lang/modules/scala-java8-compat_2.11/0.8.0/scala-java8-compat_2.11-0.8.0.jar
  org/scala-lang/modules/scala-collection-compat_2.11/1.0.0/scala-collection-compat_2.11-1.0.0.jar
  org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar
  joda-time/joda-time/2.9.9/joda-time-2.9.9.jar
  org/slf4j/slf4j-api/1.7.25/slf4j-api-1.7.25.jar
  org/slf4j/slf4j-simple/1.7.25/slf4j-simple-1.7.25.jar
)
for j in "${JARS[@]}"; do
  f=$(basename "$j")
  [ -f "$f" ] && { echo "have $f"; continue; }
  echo "fetching $f"
  curl -sS --max-time 300 -o "$f" "$BASE/$j"
done
echo "done: $(ls *.jar | wc -l) jars"
