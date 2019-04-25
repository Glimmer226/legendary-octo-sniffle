import urllib.request
import easygui as g


def getSize():
    msg = "请填写喵的尺寸"
    title = "下载一只猫"
    fieldname = ["宽：", "高："]
    fieldvalue = [400, 600]

    size = g.multenterbox(msg, title, fieldname, fieldvalue)

    return size


def savePath():
    path = g.filesavebox(msg="请选择存放喵的文件夹", filetypes=["*.jpg"])
    return path


if __name__ == "__main__":
    size = getSize()
    url = "http://placekitten.com/%d/%d" % (int(size[0]), int(size[1]))

    response = urllib.request.urlopen(url)
    cat_img = response.read()

    try:
        if g.ccbox(msg="下载成功，点击确定保存", choices=["确定", "取消"]):
            path = savePath() + ".jpg"
            with open(path, 'wb') as f:
                f.write(cat_img)
    except Exception as e:
        print(e)
    finally:
        exit(0)

