import axelrod

# Example using TitFotTat vs. Alternator
strategies = [axelrod.TitForTat(), axelrod.Alternator()]
match = axelrod.Match(strategies, 20)
interactions = match.play()
print(interactions)