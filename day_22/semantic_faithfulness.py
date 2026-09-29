import math

def cosine_similarity(a:list[float], b:list[float]) -> float:

    dot = sum(x*y for x,y in zip(a,b))
    mag_a = math.sqrt(sum(x*x for x in a))
    mag_b = math.sqrt(sum(y*y for y in b))

    return dot / (mag_a*mag_b)

def semantic_faithfulness(answer: str, source: str, embed_client) -> float:
    # step 1: turn each text into a vector using the injected client
    answer_vec = embed_client.embed(answer)
    source_vec = embed_client.embed(source)

    # step 2: return how close there meanings are
    return cosine_similarity(answer_vec, source_vec)