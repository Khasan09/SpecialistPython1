# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass

def lucky_ticket(ticket):
    a = str(ticket)
    lst1 = (a[:1]) + (a[1:2])
    lst2 = (a[-1]) + (a[-2])
    if lst1 == lst2:
        return True
