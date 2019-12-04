class account:
    def __init__(self, customer_name):
        self.name = customer_name

    def get_cus_name(self):
        return self.name



account_holder = account('chumbi')
print(account_holder.get_cus_name())