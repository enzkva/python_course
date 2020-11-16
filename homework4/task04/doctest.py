"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    How to run doctests:
     - Install Python 3.9 (https://www.python.org/downloads/)
     - Install pytest `pip install pytest`
     - Clone the repository https://github.com/enzkva/python_course
     - Checkout branch hw04
     - Open terminal
     - Run pytest --doctest-modules homework4/task04/doctest.py
     - For more informstion, run pytest --doctest-modules homework4/task04/doctest.py -v

    Return n FizzBuzz numbers
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    fizzbuzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                fizzbuzz_list.append("fizzbuzz")
            else:
                fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(str(i))
    return fizzbuzz_list