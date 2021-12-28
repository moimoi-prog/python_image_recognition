import cv2


def show_image(img):
	# 画像を表示
	cv2.imshow('sample', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
