# task #1 - prevent from crashing:
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


def ex1():
    make_pie(4)


# task #2 keyError:
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def ex2():
    total_likes = 0
    for post in facebook_posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            pass

    print(total_likes)


ex1()
ex2()
