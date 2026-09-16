from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Garden"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"You are entering {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening. BEWARE, for there is danger in these grounds...")

    goblin = Goblin("Thorne")
    print(f"{goblin.name} spawns in {ARENA_NAME} with {goblin.health} health.")

    secondGoblin = Goblin("Briar")
    print(f"{secondGoblin.name} spawns in {ARENA_NAME} with {secondGoblin.health} health.")

    print("A figure is approaching from the distance...")

    Gardener = Hero("Gardener")
    print(f"{Gardener.name} arrives at {ARENA_NAME} to face the danger! They enter with {Gardener.health} health.")
    
    battle(Gardener, goblin)
    battle(Gardener, secondGoblin)
    
if __name__ == "__main__":
    main()
