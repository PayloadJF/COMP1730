import matplotlib.pyplot as plt
import matplotlib.image as mpimg

MAP_EXTENT = (149.105, 149.130, -35.29, -35.27)


def load_atlas(filename):
    file = open(filename, "r")

    atlas_data = [];

    with open(filename, 'r', encoding='utf-8') as file_data:
        for s in file_data:
            s = s.split("|")

            atlas_data.append(s)

    atlas_data.pop(0)

    for data in atlas_data:
        data[-1] = data[-1][0:-1]
    file.close();

    atlas_dic = {}
    number = 0
    for data in atlas_data:
        atlas_dic.update({number: data})
        number += 1

    return atlas_dic


def remove_duplicates(atlas_data):
    indextopop = [];
    for data in atlas_data.items():
        the_key = data[0]
        the_value = data[1]
        if the_value[-1] == 'False':
            indextopop.append(the_key)

    for i in indextopop:
        atlas_data.pop(i)

    return atlas_data


def show_on_the_map(x):

    plt.imshow(mpimg.imread('map.png'), extent=MAP_EXTENT)
    for data in x.items():
        the_value = data[1]
        y=the_value[1]
        z=the_value[2]
        plt.scatter(float(z),float(y))
    plt.show()



a = load_atlas("ala-acton.txt")
print(a)
print(len(a))
print(len(a.values()))
remove_duplicates(a)

# for i in a.items():
#     print(i[1][-1])

# print(show_on_the_map(a))
show_on_the_map(a)
