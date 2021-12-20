import numpy as np

with open("input.txt") as fin:
    lines = fin.readlines()
    enhancement = lines[0].strip()
    img = np.array([list(a.strip()) for a in lines[2:]])   

pad_value = "."
for k in range(50):
    img = np.pad(img, 3, constant_values=pad_value)
    new_pad_value = enhancement[int("".join([pad_value] * 9).replace(".", "0").replace("#", "1"), 2)]
    output = np.full_like(img, new_pad_value)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            index = int("".join(img[i-1:i+2, j-1:j+2].ravel()).replace(".", "0").replace("#", "1"), 2)
            output[i - 1, j - 1] = enhancement[index]
    pad_value = new_pad_value
    img = output
    print(k, (img == "#").sum())

