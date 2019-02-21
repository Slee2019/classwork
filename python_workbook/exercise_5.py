small = float(input("How many small containers do you have?: "))
large = float(input("How many large containters do you have?: "))
refund_small = small * 0.1
refund_large = large * 0.25
refund_total = refund_small + refund_large
print(f"Your total refund is $" +("%.2f" % refund_total))