from TicketCounter import TicketCounter

if __name__ == '__main__':
    ticketcounter = TicketCounter()
    ticketcounter.getticketype()
    ticketcounter.getname()
    ticket = ticketcounter.createticketobject()
    ticket.createdrink()
    ticket.createseat()
    ticket.createfood()
    print(ticket)
    print(f"Ticket has booked Successfully. \nTicket Details:\n Name: {ticketcounter.name} \n Type: {ticketcounter.typ} \nThank you choosing us !!")
