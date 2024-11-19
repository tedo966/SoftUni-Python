def checking_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"
    wining_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_wining_symbol in wining_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            wining_symbol_repetition = current_wining_symbol * uninterrupted_match_length
            if wining_symbol_repetition in left_part and wining_symbol_repetition in right_part:

                if uninterrupted_match_length == 10:
                    return  f'ticket "{ticket}" - {uninterrupted_match_length}{current_wining_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{current_wining_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [tickets.strip() for tickets in input().split(", ")]
for current_ticket in tickets:
    print(checking_ticket(current_ticket))