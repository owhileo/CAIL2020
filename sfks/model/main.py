import json
import os
import jieba

data_path = "data/"
test_path = "/input"
output_path = "/output"

if __name__ == "__main__":
    os.system(
        "python utils/cutter.py --input input --output data/cutted --gen_word2id")
    os.system(
        "python test.py --gpu 0 --config config/model.config --checkpoint data/model/model/31.pkl --result result.json")
    result = {}
    for item in json.load(open("result.json", "r", encoding="utf8")):
        result[item["id"]] = item["answer"]
    json.dump(result, open("output/result.txt", "w", encoding="utf8"), indent=2, ensure_ascii=False, sort_keys=True)
