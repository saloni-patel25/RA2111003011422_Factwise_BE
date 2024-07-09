def number_to_words(n):
    ones = ["", "one" , "two" , "three" , "four" , "five" , "six" , "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen" , "nineteen"]
    tens = ["","", "twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty","ninety"]
    
    if n == 1000:
        return "onethousand"
    elif n<20:
        return ones[n]
    elif n < 100:
        return tens[n// 10] + ones[n % 10]
    else:
        hundreds_digit = n // 100
        remainder = n % 100
        if remainder == 0 :
            return ones[hundreds_digit] + "hundred"
        else:
            return ones[hundreds_digit] + "hundredand" + number_to_words(remainder)
        
total_letters = sum(len(number_to_words(i)) for i in range (1, 1001))
print(f"Total number of letters{total_letters}")
    
    
    
    
    
    

    
            