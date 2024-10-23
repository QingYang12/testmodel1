# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import ocr_module  # 导入模块
import json

def main():
    # 获取当前脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    taskdir = ""
    #print(sys.argv)
    # 判断命令行参数数量是否为 2
    if len(sys.argv) == 3 and sys.argv[1] == "-i":
        taskdir = sys.argv[2]
    else:
        taskdir = ""
    uploadDirRoot = "/Users/wanghao/Documents/pyimgtemp";
    image_name = "example.png";
    # 获取图片的绝对路径
    if not taskdir:
        image_name = "example.png"  # 假设图片名为 example.png
        image_path = os.path.join(script_dir, image_name)
    else:
        image_name="input.png"
        image_path = uploadDirRoot+"/"+taskdir+"/"+image_name;
    #print(image_path)
    # 检查图片文件是否存在
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_name}' does not exist in the current directory.")
        sys.exit(1)

    # 调用OCR函数
    recognized_text = ocr_module.ocr_image(image_path)

    # 将识别结果转换为JSON格式并输出到控制台
    resjsontest = {"text": recognized_text}
    #print(json.dumps(resjson, ensure_ascii=False))
    # 测试语句
    resjson = {"data": [{"name":"A","value":"xxxx","Num":"1"},{"name":"B","value":"xxxx","Num":"2"},{"name":"A","value":"xxxx","Num":"3"}],"taskdir":taskdir,"resjsontest":resjsontest}
    print(json.dumps(resjson, ensure_ascii=False))

    # 尝试修改文字


if __name__ == "__main__":
    main()