import string
import random
min_length = 5
max_length = 7

def create_random_str( rand_flag=False):
    """

    :type rand_flag: object
    """
    alphabet = string.ascii_lowercase
    count = random.randint(1,10) if rand_flag else 2
    return alphabet * count


def create_spaces(rand_str):
    index = 0
    rand_str_to_list = list(rand_str)
    condition = True
    while condition:
        step = random.randint(1, 10)
        index += step
        if index < len(rand_str):
            rand_str_to_list[index] = " "
        else:
            condition = False
    rand_str = "".join(rand_str_to_list)
    return rand_str


def modify_word(word, comma_percentage=0.2):
    if random.random() < comma_percentage:
        word = word.capitalize()
    return word


def modify_str(rand_str):
    rand_str_split = rand_str.split()
    result = []
    for word in rand_str_split:
        word = modify_word(word)
        result.append(word)
    return " ".join(result)

def get_rnd_num_and_commas_list(num_min, num_max, length):
    nums = [" " + str(random.randint(num_min, num_max)) for i in range(length)]
    punctuation = [random.choice("," + "\n") for v in range(length)]
    rnd_punct_and_nums = [random.choice(nums + punctuation) for i in range(length)]
    return [random.choice(punctuation + rnd_punct_and_nums) for i in range(length)]

num_min = 0
num_max = 100
word_min_len = 1
word_max_len = 10
string_to_words = ( word_min_len, word_max_len)
punctuations_and_nums = get_rnd_num_and_commas_list(num_min, num_max, len(string_to_words))


rand_str = create_random_str(True)
rand_str = create_spaces(rand_str)
rand_str = modify_str(rand_str,punctuations_and_nums)
print(rand_str)