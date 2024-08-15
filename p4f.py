from gensim.utils import tokenize
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a
spacefa
ring civilization and a multi-planet

species by building a self-
sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately deve

loped
liquid-fuel launch vehicle to orbit the Earth."""

print(list(tokenize(text)))
