from itertools import permutations

def cryptarithmetic_solver():
    n = int(input("Enter number of words to add: "))
    words = [input(f"Enter word {i+1}: ").upper() for i in range(n)]
    result = input("Enter result word: ").upper()

    # All unique letters
    letters = set(''.join(words) + result)
    if len(letters) > 10:
        print("Too many letters! Cannot assign unique digits.")
        return

    letters = list(letters)

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if any word or result starts with 0
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue

        # Convert words to numbers
        nums = []
        for word in words:
            num = 0
            for ch in word:
                num = num * 10 + mapping[ch]
            nums.append(num)

        res_num = 0
        for ch in result:
            res_num = res_num * 10 + mapping[ch]

        if sum(nums) == res_num:
            print("Solution:", mapping)
            print(" + ".join(map(str, nums)), "=", res_num)
            return

    print("No solution found.")

# Run
cryptarithmetic_solver()
