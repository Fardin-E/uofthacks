import cohere

co = cohere.Client('sC2sHJQzVNhDbXiQZtYlUYvJbUc1OnnmIQPpAAff')
response = co.generate(
  model='command-xlarge-nightly',
  prompt='Write me a haiku about Tim hortons using imagery, metaphors, rhymes, and proper punctuation',
  temperature=0.4,
  
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  return_likelihoods='NONE')
poem='Poem: {}'.format(response.generations[0].text)
print(poem)
