import json
import random

def load_json(path):
    data=[]
    with open(path,'r',encoding='utf8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def dump_json(path,data):
    with open(path,'w',encoding='utf8') as f:
        for i in data:
            print(json.dumps(i, ensure_ascii=False, sort_keys=True), file=f)

train=0.8
valid=0.1

d=load_json('0.json')
random.shuffle(d)
train_list=d[:int(len(d)*train)]
valid_list=d[int(len(d)*train):int(len(d)*(train+valid))]
test_list=d[int(len(d)*(train+valid)):]
dump_json('0_train.json',train_list)
dump_json('0_valid.json',valid_list)
dump_json('0_test.json',test_list)

d=load_json('1.json')
random.shuffle(d)
train_list=d[:int(len(d)*train)]
valid_list=d[int(len(d)*train):int(len(d)*(train+valid))]
test_list=d[int(len(d)*(train+valid)):]
dump_json('1_train.json',train_list)
dump_json('1_valid.json',valid_list)
dump_json('1_test.json',test_list)
