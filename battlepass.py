from PIL import Image

roadmap = Image.open('images/roadmap.png')
user = Image.open('images/user.png')

result = roadmap.copy()
level = int(input(':::> '))

grid = {
    1: [118, 215],
    2: [567, 215],
    3: [343, 472],
    4: [343, 674],
    5: [572, 871],
}

x, y = grid.get(level)[0], grid.get(level)[1]

result.paste(user, (x, y), user)
result.show()
