import csv
import numpy as np

def readWebPlotDigitizer(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # 读取标题行
        colors = [col for col in header if col]  # 获取所有颜色名称

        # 初始化字典，为每种颜色创建一个空列表
        for color in colors:
            data[color] = []

        # 读取每行数据
        for row in csv_reader:
            # 将每个颜色的X,Y数据添加到对应的列表中
            for i, color in enumerate(colors):
                x_index = i * 2  # X值的索引
                y_index = x_index + 1  # Y值的索引
                if len(row) > y_index and row[x_index] and row[y_index]:  # 确保行中有足够的列且值不为空
                    try:
                        x = float(row[x_index])
                        y = float(row[y_index])
                        data[color].append(np.array([x, y]))
                    except ValueError:
                        # 如果转换失败，则忽略这个值
                        continue
    return  data

