class OldCoinStash:
    def __init__(self, owner) -> None:
        # these attributes are public
        self.owner = owner

        # private - by convention use underscore prefix
        self._riksdaler = 0
        self._shilling = 0

    def deposit(self, riksdaler, shilling):
        if riksdaler <= 0 or shilling <= 0:
            raise ValueError(f"Stop depositing negative values. {riksdaler} riksdaler or {shilling} not okay")

        self._riksdaler += riksdaler
        self._shilling += shilling

    def withdraw(self, riksdaler, shilling):
        if riksdaler > self._riksdaler or shilling > self._shilling:
            raise ValueError(f"You can not withdraw more coins than you have")
        self._riksdaler -= riksdaler
        self._shilling -= shilling
    
    def check_balance(self):
        return f"Coins in stash: {self._riksdaler} riksdaler and {self._shilling} shilling"

    def __repr__(self) -> str:
        return f"OldCoinStash(owner='{self.owner}')"