import struct
import json
import os
import hashlib


def send_data(client, send_dic, file):
    # 发送部分
    head_json_bytes = json.dumps(send_dic).encode('utf-8')  # 先把报头转为bytes格式
    client.send(struct.pack('i', len(head_json_bytes)))  # 先发报头的长度
    client.send(head_json_bytes)  # 再发送报头
    if file:  # 如果存在文件，再把文件打开一行一行发送
        with open(file, 'rb') as f:
            for line in f:
                client.send(line)
    # 接收部分
    back_len_bytes = client.recv(4)  # 先收报头4个bytes,得到报头长度的字节格式
    back_head_len = struct.unpack('i', back_len_bytes)[0]  # 提取报头的长度
    head_bytes = client.recv(back_head_len)  # 按照报头长度back_head_len,收取报头的bytes格式
    header = json.loads(head_bytes.decode('utf-8'))  # 把bytes格式的报头，转换为json格式

    return header


def get_allfile_by_path(path):
    file_list = os.listdir(path)
    return file_list


def make_md5(password):
    md = hashlib.md5()
    md.update(password.encode('utf-8'))
    return md.hexdigest()


def get_bigfile_md5(file_path):
    if os.path.exists(file_path):
        md = hashlib.md5()
        filesize = os.path.getsize(file_path)
        file_list = [0, filesize // 3, (filesize // 3) * 2, filesize - 10]
        with open(file_path, 'rb') as f:
            for line in file_list:
                f.seek(line)
                md.update(f.read(10))
        return md.hexdigest()
