def timeRequiredToBuy(tickets, k) -> int:
    res = 0
    
    for i in range(len(tickets)):
        if i <= k:
            res += min(tickets[i], tickets[k])
        else:
            res += min(tickets[i], tickets[k] - 1)
    return res

# Example usage:
tickets = [2, 3, 2]
k = 2
print(timeRequiredToBuy(tickets, k))  # Output: 6