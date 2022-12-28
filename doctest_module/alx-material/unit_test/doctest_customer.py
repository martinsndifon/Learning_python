class Customer:
    """
    A sample customer class
    >>> customer_1 = Customer("Martins", "Ndifon", 5000)
    >>> customer_2 = Customer("John", "Evareh", 6000)
    >>> customer_1.customer_fullname()
    'Martins Ndifon'
    >>> customer_2.customer_fullname()
    'John Evareh'
    >>> customer_2.customer_mail()
    'John.Evareh@email.com'
    >>> customer_1.apply_discount()
    4750
    >>> customer_2.apply_discount()
    5700
    """

    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    def customer_mail(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    def customer_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase

if __name__ == "__main__":
    import doctest
    doctest.testmod()
