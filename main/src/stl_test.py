import os

import numpy as np
from stl import mesh

from docs import config


def create_cube():
    vertices = np.array([
        [-1, -1, -1],
        [+1, -1, -1],
        [+1, +1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
        [+1, -1, +1],
        [+1, +1, +1],
        [-1, +1, +1]
    ])

    faces = np.array([
        [0, 3, 1],
        [1, 3, 2],
        [0, 4, 7],
        [0, 7, 3],
        [4, 5, 6],
        [4, 6, 7],
        [5, 1, 2],
        [5, 2, 6],
        [2, 3, 6],
        [3, 7, 6],
        [0, 1, 5],
        [0, 5, 4]
    ])

    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    cube.save(os.path.join(config.LOGS_DIR, "cube.stl"))


def create_tri():
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ])

    faces = np.array([
        [0, 1, 3],
        [0, 2, 3],
        [4, 5, 7],
        [4, 6, 7],
        [0, 1, 5],
        [0, 4, 5],
        [2, 3, 7],
        [2, 6, 7],
        [3, 1, 5],
        [3, 7, 5],
        [0, 2, 6],
        [0, 4, 6]
    ])

    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    cube.save(os.path.join(config.LOGS_DIR, "tri.stl"))


if __name__ == '__main__':
    create_cube()
    create_tri()
