class Game:
      def __init__ (self):
            self.life = 5
            
      def attack(self,enemy):
            print('Attack')
            enemy.life -=1
            
      def check_life(self):
                  print('Your Life: ',self.life)
                  
p1 = Game()
p2 = Game()
p1.check_life()
p1.attack(p2)
p1.attack(p2)
p2.attack(p1)
p2.check_life()