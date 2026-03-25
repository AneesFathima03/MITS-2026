#VOWELS
VOWEL = "aeiou"
phrase = input("Enter a phrase: ").lower()
count = 0
for ch in phrase:
    if ch in VOWEL:
        count += 1
print("There is/are [0] vowels.".format(count))





#TEMPERATURE CONVERTER
celsius = 10
print("Celsius\tFahrenheit")

while celsius <= 30:
    f = (9/5 * celsius) + 32
    print("{0:^7}\t{1:^10.0f}".format(celsius,f))
    celsius += 5
