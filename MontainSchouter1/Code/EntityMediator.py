from Code.Enemy import Enemy
from Code.Entity import Entity


class EntityMediator:


    @staticmethod
    #     Os dois __ tornam o método protegido o que faz com que ele só possa ser usado dentro de EntityMediator
    # Verificar se passou da tela e zerar a vida
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

    #    Verificar se a vida é zero e remover da lista
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)