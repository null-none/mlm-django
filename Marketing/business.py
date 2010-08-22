from django.contrib.auth.models import User
from utilities import instantiate
from Marketing.models import MarketingRates
from Banking.business import Accountant
from datetime import datetime

class MarketingCalculator(object):
    def __init__(self, user, marketing_plan, date_from, date_to):
        self.user = user
        self.marketing_plan = marketing_plan
        self.marketing_node = instantiate(marketing_plan).filter(user=user)
        self.marketing_rates = MarketingRates.objects.filter(marketing_tree=marketing_plan).order_by('generation')
        self.accountant = Accountant(marketing_plan)
        self.date_from = date_from
        self.date_to = date_to

    def calculate_profit(self):
        return __get_generation_profit(self.marketing_node, 0)

    def __get_generation_profit(self, node, generation):
        if generation >= len(self.marketing_rates):
            return 0

        next_generation = generation + 1
        commission = self.marketing_rates[curr_gen]
        profit = 0.0
        for child in node.get_children():
            profit += commission*self.get_cashflow(child) + self.__get_generation_profit(child, next_generation)
            
        return profit

    # stub
    def get_cashflow(self, child):
        return self.accountant.get_sales(child.user, self.date_from, self.date_to)

