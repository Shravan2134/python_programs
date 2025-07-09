class Question:
    def __init__(self, question, options, correct, prize):
        self.question = question
        self.options = options
        self.correct = correct
        self.prize = prize
    
    def is_correct(self, answer):
        return self.correct == answer
    
    