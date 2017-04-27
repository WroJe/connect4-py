b = Board()
p1 = Player()
p2 = Player()

ill = Illustrator(b)

while True:
    ill.draw()
    p1.take_turn()
    b.check_win()
    ill.draw()
    p2.take_turn()
    b.check_win()
