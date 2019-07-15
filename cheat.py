sol = eval(re.sub(r"(\d+)", r"Fraction(\1, 1)", input()))
print(sol.numerator, sol.denominator)
