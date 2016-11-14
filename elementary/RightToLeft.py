def left_join(phrases):
    joined = ",".join(phrases)
    result = joined.replace("right", "left")
    return result
