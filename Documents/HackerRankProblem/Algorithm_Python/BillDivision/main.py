def bonAppetit(bill, k, b):
    # Write your code here
    actual_share = (sum(bill) - bill[k]) // 2
    if actual_share == b:
        print('Bon Appetit')
    else:
        print(int(b - actual_share))