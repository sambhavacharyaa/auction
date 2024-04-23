from replit import clear
from art import logo
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")






while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid price? $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        clear()





