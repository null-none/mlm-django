from Banking.models import Transaction

class Accountant:
    def __init__(self, marketing_plan):
        self.marketing_plan = marketing_plan

    def calculate_sales(self, user, date_from, date_to):
        transactions = Transaction.objects.filter(reciever=user, date__gte=date_from, date__lte=date_to)
        
        amount = 0.0        
        for t in transactions:
            amount += t.amount
            
        return amount