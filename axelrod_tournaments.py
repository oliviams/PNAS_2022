import axelrod

# Strategies included: TitForTat, TitFor2Tats, Cooperator, Defector, HardTitForTat, Alternator, TwoTitsForTat, Bully, Cycler, CyclerCCCD, CyclerDDC, Desperate, FirmButFair, Helpless, Willing, UsuallyCooperates, UsuallyDefects

# Example using TitFotTat vs. Alternator
strategies = [axelrod.TitForTat(), axelrod.Alternator()]
match = axelrod.Match(strategies, 20)
interactions = match.play()
print(interactions)
