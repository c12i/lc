class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 > len(self.balance) or account1 < 1 or account2 > len(self.balance) or account2 < 1:
            return False

        idx_from = account1 - 1
        idx_to = account2 - 1

        if self.balance[idx_from] < money:
            return False

        self.balance[idx_from] -= money
        self.balance[idx_to] += money

        return True
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > len(self.balance) or account < 1:
            return False
        
        idx = account - 1
        self.balance[idx] += money
        return True
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account > len(self.balance) or account < 1:
            return False

        idx = account - 1
        if self.balance[idx] < money:
            return False

        self.balance[idx] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)