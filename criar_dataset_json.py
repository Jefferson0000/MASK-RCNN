import json
import os

train_path = "C:\\VS Code Envs\\Data\\CT_Train_1"
test_path = "C:\\VS Code Envs\\Data\\CT_Train_1"
save_json_path = "C:\\VS Code Envs\\Data\\CT_Train_1"

# cria os dados referente ao treinamento
image_path = []
label_path = []
for (dirpath, dirnames, filenames) in os.walk(train_path + "\Images"):
    for i in filenames:
        image_path.append(dirpath + "\\" + i)
        label_path.append(train_path + "\\Labels\\" + i[:14] + "label.nii.gz")
train_paths = [{"image" : i, "label" : j} for i, j in zip(image_path, label_path)]

# cria os dados referentes ao teste
image_path = []
label_path = []
for (dirpath, dirnames, filenames) in os.walk(test_path + "\Images"):
    for i in filenames:
        image_path.append(dirpath + "\\" + i)
        label_path.append(test_path + "\\Labels\\" + i[:14] + "label.nii.gz")
test_paths = [{"image" : i, "label" : j} for i, j in zip(image_path, label_path)]

# cria o arquivo json
json_file = {"trainning" : train_paths, "testing" : test_paths}
json_file = json.dumps(json_file)
json_file = json.loads(json_file)

with open(save_json_path + '\\dataset.json', 'w') as file:
    json.dump(json_file, file)

json_file["testing"]