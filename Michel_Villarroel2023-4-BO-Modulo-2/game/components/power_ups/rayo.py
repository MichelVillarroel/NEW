from game.components.power_ups.power_up import PowerUp

from game.utils.constants import RAYO, RAYO_TYPE, BULLET_RAYO_LASER
#from game.components.game import Game


class Rayo(PowerUp):


    def __init__(self):
        super().__init__(RAYO, RAYO_TYPE)
       # self.can_shoot = True

  #  def shoot_rayo_laser(self):
        # Lógica para disparar el rayo láser
   #     print("Rayo láser disparado")

        # Desactiva la posibilidad de disparar nuevamente
    #    self.can_shoot = False

    #def update(self, game_speed, power_ups, game):
     #   self.rayo.update(game.game_speed, self.power_ups, game)

        # Verifica si el poder de disparo está disponible y se presionó el botón de disparo
      #  if self.can_shoot and game.player.is_shooting:
       #     self.shoot_rayo_laser()

        #super().update(game_speed, power_ups)