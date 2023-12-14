class VotingDatabase:
    def __init__(self):
        # Ініціалізація бази даних - словник для зберігання голосів депутатів
        self.deputies_votes = {}

    def vote(self, deputy_id, decision):
        # Метод для голосування депутата з ідентифікатором deputy_id
        # decision може приймати значення 'for', 'against' або 'abstain'
        if deputy_id not in self.deputies_votes:
            self.deputies_votes[deputy_id] = decision
            print(f"Deputat {deputy_id} voted {decision}.")
        else:
            # Якщо депутат вже проголосував, вивести повідомлення
            print(f"Deputat {deputy_id} has already voted.")

    def get_decision(self, deputy_id):
        # Метод для отримання рішення (голосу) депутата за його ідентифікатором deputy_id
        if deputy_id in self.deputies_votes:
            decision = self.deputies_votes[deputy_id]
            print(f"Decision of Deputat {deputy_id}: {decision}")
            return decision
        else:
            # Якщо депутат ще не голосував, повернути None
            print(f"Deputat {deputy_id} has not voted yet.")
            return None

# Приклад використання
voting_db = VotingDatabase()

voting_db.vote(1, 'for')
voting_db.vote(2, 'against')
voting_db.vote(1, 'abstain')  # Спроба повторного голосування

decision_1 = voting_db.get_decision(1)
decision_2 = voting_db.get_decision(2)
decision_3 = voting_db.get_decision(3)  # Запит про депутата, який ще не голосував