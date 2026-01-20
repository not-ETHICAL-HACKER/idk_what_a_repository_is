def inr_to_usd(inr:int)->str:
    exchange =  1/80
    return f"${inr * exchange:.2f}"
def usd_to_inr(usd:int)->str:
    exchange = 80
    return f"₹{usd*exchange:.2f}"
print(inr_to_usd(1600))
print(usd_to_inr(20))
