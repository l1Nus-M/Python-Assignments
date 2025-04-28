class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self._name = name  # Encapsulated with underscore
        self._secret_identity = secret_identity
        self._powers = powers
        self._weakness = weakness
        self._origin_story = origin_story
        self._health = 100
        self._energy = 100

    def use_power(self, power_name):
        if power_name in self._powers:
            if self._energy >= 20:
                self._energy -= 20
                return f"{self._name} uses {power_name}!"
            else:
                return f"{self._name} is too tired to use {power_name}!"
        return f"{self._name} doesn't have the power {power_name}!"

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)
        return f"{self._name} takes {amount} damage! Health: {self._health}"

    def rest(self):
        self._energy = min(100, self._energy + 30)
        return f"{self._name} rests and recovers energy! Energy: {self._energy}"

    def get_secret_identity(self):
        return self._secret_identity

    def get_health(self):
        return self._health

    def get_energy(self):
        return self._energy

    def __str__(self):
        return f"Superhero: {self._name}\nPowers: {', '.join(self._powers)}\nWeakness: {self._weakness}"


class Avenger(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, origin_story, avenger_rank):
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self._avenger_rank = avenger_rank
        self._team_leader = False

    def assemble(self):
        if self._energy >= 10:
            self._energy -= 10
            return f"Avengers Assemble! {self._name} is ready for battle!"
        return f"{self._name} is too tired to assemble!"

    def promote_to_leader(self):
        self._team_leader = True
        return f"{self._name} has been promoted to team leader!"

    def use_avenger_power(self):
        if self._team_leader:
            return f"{self._name} uses enhanced team leadership abilities!"
        return f"{self._name} uses standard Avenger abilities!"

    def __str__(self):
        return f"{super().__str__()}\nAvenger Rank: {self._avenger_rank}\nTeam Leader: {self._team_leader}"


# Example usage
if __name__ == "__main__":
    # Create a regular superhero
    spiderman = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web-slinging", "Spider-sense", "Super strength"],
        weakness="Ethyl chloride",
        origin_story="Bitten by a radioactive spider"
    )

    # Create an Avenger
    iron_man = Avenger(
        name="Iron Man",
        secret_identity="Tony Stark",
        powers=["Powered armor", "Genius intellect", "Advanced weaponry"],
        weakness="Arc reactor dependency",
        origin_story="Built first armor to escape captivity",
        avenger_rank="Founding Member"
    )

    # Demonstrate methods
    print(spiderman.use_power("Web-slinging"))
    print(iron_man.assemble())
    print(iron_man.promote_to_leader())
    print(iron_man.use_avenger_power())
    print(spiderman.take_damage(30))
    print(spiderman.rest()) 
