import cv2
from pathlib import Path


def face_recognition():
    face_cascade_path = '/Users/moimoi_adm/python/python_image_recognition/cascade/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    path_list = Path("image/input").glob("*")

    for path in path_list:
        img = cv2.imread(str(path))
        # img_gray = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_gray)

        for index, (x, y, w, h) in enumerate(faces):
            img_cut = img[y:y + h, x:x + w]
            # name ... ファイル名(拡張子あり)
            # stem ... ファイル名(拡張子なし)
            # suffix ... 拡張子のみ
            cv2.imwrite('image/output/' + path.stem + "_result" + str(index) + path.suffix, img_cut)

        # ファイル削除
        # path.unlink()

        # 画像を表示
        # utils.show_image(img)

        # 顔の位置に線を引く
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


if __name__ == '__main__':
    face_recognition()
