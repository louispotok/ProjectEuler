"""
No joy I found in this solution,
If you paid, seek restitution.
"""

ones_names = {0: '',
              1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine'}

teens_names = {10: 'ten',
               11: 'eleven',
               12: 'twelve',
               13: 'thirteen',
               14: 'fourteen',
               15: 'fifteen',
               16: 'sixteen',
               17: 'seventeen',
               18: 'eighteen',
               19: 'nineteen'
               }

tens_names = {
                   1: 'teen',
                2: 'twenty',
              3: 'thirty',
              4: 'forty',
              5: 'fifty',
                   6: 'sixty',
                   7: 'seventy',
                   8: 'eighty',
                   9: 'ninety'}

eligible_letters = map(chr,range(97,123))

def number_to_words(n):
    '''
    For 0 < n <= 1000
    '''
    if n == 1000:
        return 'one thousand'
    return three_digit_to_words(n)

def three_digit_to_words(n):
    if n % 100 == 0:
        return ones_names[n/100] + ' hundred'
    if n / 100 == 0:
        hundreds_name = ''
    else:
        hundreds_name = ones_names[n/100] + ' hundred and '

    if (n/10)%10 == 0:
        return hundreds_name + ones_names[n%10]
    return hundreds_name + two_digit_to_words(n%100)

def two_digit_to_words(n):
    if n in teens_names:
        return teens_names[n]
    ones_name = ones_names[n%10]
    if ones_name:
        ones_name = '-' + ones_name
    return tens_names[n/10] + ones_name


def clean_string(s):

    return ''.join([i for i in s if i in eligible_letters])

def main(n):
    rolling_sum = 0
    for i in range(1,n+1):
        rolling_sum += len(clean_string(number_to_words(i)))
    return rolling_sum

if __name__ == '__main__':
    print main(1000)