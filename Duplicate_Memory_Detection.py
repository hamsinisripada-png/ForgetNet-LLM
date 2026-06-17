from sentence_transformers import util

similarity = util.cos_sim(vec1, vec2)
