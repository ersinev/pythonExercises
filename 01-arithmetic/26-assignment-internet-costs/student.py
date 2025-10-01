# write your code here
def internet_costs(duration_in_seconds, cost_per_block):
    sixMinPack = duration_in_seconds//360
    restPack = (duration_in_seconds%360 +359)//360
    amount_to_paid = (sixMinPack + restPack ) * cost_per_block
    return amount_to_paid




# def internet_costs(duration_in_seconds, cost_per_block):
#     block_seconds = 360
#     blocks = (duration_in_seconds + block_seconds - 1) // block_seconds
#     return blocks * cost_per_block