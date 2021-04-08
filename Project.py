def solution(x):
    """
    Solution

    This Method takes in an integer and reverses that integer.
    The integer could be negative or positive

    examples: -231 produces -132
               345 produces 543

    This section is an example of a Python "Doc-String"
    See this link for one description of a Doc-String  https://realpython.com/documenting-python-code/
    """
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])

if __name__ == '__main__':
    print(solution(-231))
    print(solution(345))