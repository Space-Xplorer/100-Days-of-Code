#Tip Calculator

print("Enter the bill amount: ")
bill = int(input())

print("Tip: ")
per = int(input())

tip = bill*(per/100)


print("Enter the number of people: ")
ppl = int(input())

split = (tip+bill)/ppl

print(f"Tip: {tip}")
print(f"Total Payable amount: {bill+tip}")
print(f"Total per person is: {split}")