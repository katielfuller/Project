def solution(x):
    
    """
    #is this how you make changes?
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
    import numpy as np
    import matplotlib.pyplot as plt

    print(solution(-231))
    print(solution(345))

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min()*1.1,C.max()*1.1)
    plt.yticks([-1, 0, +1],
               [r'$-1$', r'$0$', r'$+1$'])

    plt.show()
