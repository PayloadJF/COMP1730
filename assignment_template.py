"""COMP1730/6730 assignment.

Coauthors: <University ID>, <University ID>, <University ID>
Date: <Date>
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import math

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

    return atlas_data


def remove_duplicates(atlas_data):
    for data in atlas_data:
        if data[-1] == 'False':
            atlas_data.remove(data)

    return atlas_data


def function(x):
    i = 0
    y = []
    z = []
    while i < len(x):
        y.append(x[i][1])
        z.append(x[i][2])
        i = i + 1

    plt.imshow(mpimg.imread('map.png'), extent=MAP_EXTENT)
    plt.scatter(z, y)
    plt.show()


def nearest_bird(atlas_data, latitude, longitude):
    pass


def most_common_birds(atlas_data, latitude, longitude, distance):
    pass


def eucalypt_club_location(atlas_data):
    pass


if __name__ == '__main__':
    a = load_atlas("ala-acton.txt")
    distance = ["", 100.0]
    count = 0
    # for i in a:
    #     if i[0]!="Name":
    #         x=float(i[1])
    #         y=float(i[2])
    #         d = pow(pow(x+35.276733,2)+pow(y-149.125674,2),1/2)*6371*math.pi/180
    #         count =count+1
    #         if d<distance[1]:
    #             distance[1] = d
    #             distance[0] =i[0]
    # remove_duplicates(a)

    print(a[0])
    print(len(a))
    # print(d)
    # print(len(a))
    # print(distance)
    # print(count)

    function(a[0])
