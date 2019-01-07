from app import app
from flask import render_template, request, url_for, redirect
import matplotlib.pyplot as plt
import numpy as np
import os
import re

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def save_pic():
    pictures = os.listdir("static/images")
    url = None
    save_pic = None
    if request.method == "POST":
        #画像名を決定
        if len(pictures) == 1:
            url = "../static/images/create_pic1.png"
            save_pic = "/static/images/create_pic1.png")
        else:
            picture_str = "".join(pictures)
            pic_numList = re.findall("\d*", picture_str)
            pic_IntnumList = [int(num) for num in pic_numList if not num == ""]
            next_max = max(pic_IntnumList)+1
            url = "../static/images/create_pic"+str(next_max)+".png"
            save_pic = "app/static/images/create_pic"+str(next_max)+".png"
        #入力された値の取得
        x_value = request.form["x_value"]
        y_value = request.form["y_value"]
        color = request.form["color"]
        #配列としてデータ生成
        x = np.linspace(0, int(x_value), 100)
        y = np.linspace(0, int(y_value), 100)
        #プロット
        plt.figure()
        ax = plt.scatter(x, y, color=color)
        plt.xlabel("x")
        plt.ylabel("y")
        title_txt = "x_max: {} y_max: {} color: {} Plot".format(x_value, y_value, color)
        plt.title(title_txt)
        plt.tight_layout()
        #プロット結果を保存
        plt.savefig(save_pic)
        plt.close("all")

        return render_template("result.html", url=url)

    return redirect(url_for('index'))
