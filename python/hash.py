class HashTable:
  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.table = [None] * self.number_of_buckets
    

  def hash(self, value):
    hash=0
    for i in range(0,len(value)):
      

  def set(self, value):
    # here is where you'll perform your logic to insert the value into your table
    # you'll also call your hash method here to get the index where you'll store the value
    pass

  def get(self, value):
    # here is where you'll retreive your value from the hash table
    # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
    pass

  def has_key(self, value):
    # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
    pass
