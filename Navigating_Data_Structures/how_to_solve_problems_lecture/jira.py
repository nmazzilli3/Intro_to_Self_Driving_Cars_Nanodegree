from sample_data import big_tickets
import random

print("there are", len(big_tickets), "big tickets")

def get_popular_tickets(tickets):
    """
    From a list of tickets, fetch all the tickets with 8 or 
    more "watchers". 
    """
    popular_tickets = []
    #
    # TODO - your code here
  
    for key in tickets:
        #print(len(key['people']['watchers']))
        if len(key['people']['watchers']) >= 8:    
            
            popular_tickets.append(key)
            
    return popular_tickets

popular = get_popular_tickets(big_tickets)

# TESTING CODE 
assert( len(popular) > 0 ) # must be at least one popular ticket

for ticket in popular:
    assert( len(ticket['people']['watchers']) >= 8 )
    
    
print("Nice job! It looks like your function is working.")