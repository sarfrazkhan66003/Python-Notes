class Game:
      def __init__ (self):
            self.life = 5
            
      def attack(self):
            self.life-=1
            
      def check_life(self):
                  print('Your Life: ',self.life)
                  
obj = Game()
obj.check_life()
obj.attack()
