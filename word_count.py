from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    lower,
    regexp_replace,
    split,
    explode,
    length
)

def create_spark():
    return (
        SparkSession.builder
        .appName("WordCountApp")
        .master("local[*]")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )


def word_count(input_path: str, top_n: int = 10):
    spark = create_spark()

    # Read CSV file
    df = (
        spark.read
        .option("header", True)
        .csv(input_path)
    )

    # Select only the review text
    reviews_df = df.select("content")

    # Clean text:
    # - lowercase
    # - remove punctuation
    cleaned_df = reviews_df.withColumn(
        "clean_text",
        lower(regexp_replace(col("content"), "[^a-zA-Z\\s]", " "))
    )
    
    # Split text into words and explode into rows
    words_df = cleaned_df.select(
        explode(split(col("clean_text"), "\\s+")).alias("word")
    )


    # Simple stop words list
    stop_words = [
        "the", "and", "is", "to", "of", "in", "a", "for", "on",
        "this", "that", "it", "with", "as", "was", "but", "are",
        "they", "be", "at", "by", "an", "not", "from", "or", "have", "has",
        "you", "he", "she", "we", "his", "her", "its", "my", "your", "their", "i"
    ]

    # Remove empty words and stop words
    filtered_words_df = (
        words_df
        .filter(col("word") != "")
        .filter(~col("word").isin(stop_words))
        .filter(col("word") != " ")
        .filter(length(col("word")) > 1)
    )


    # Count word frequency
    word_counts_df = (
        filtered_words_df
        .groupBy("word")
        .count()
        .orderBy(col("count").desc())
    )

    # Show top N words
    print(f"\nTop {top_n} most frequent words:\n")
    word_counts_df.limit(top_n).show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    INPUT_PATH = "data/test.csv"
    TOP_N = 10

    word_count(INPUT_PATH, TOP_N)