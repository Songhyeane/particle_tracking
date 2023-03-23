import os

datas_path_dir = 'C:/Users/1/Desktop/workspace/datas'
datas_list = os.listdir(datas_path_dir)

os.startfile(datas_path_dir + '/' + datas_list[2])

original_path = datas_path_dir + '/' + datas_list[2]
cropped_path = datas_path_dir + '/' + datas_list[0]
finished_path = datas_path_dir + '/' + datas_list[1]
result_path = datas_path_dir + '/' + datas_list[3]

print(
    f'original_path:{original_path} cropped_path:{cropped_path} finished_path:{finished_path} result_path:{result_path} ')
