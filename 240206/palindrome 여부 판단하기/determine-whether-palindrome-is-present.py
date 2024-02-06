def is_palindrome(string):
    for i in range(len(string)):
        if string[i] !=string[-i-1]:
            print('No')
            return
    print('Yes')
    

string = input()
is_palindrome(string)