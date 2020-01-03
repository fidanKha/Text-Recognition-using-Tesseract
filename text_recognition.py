import cv2
import glob
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract'

writer  = None
path_to_images = r"./images/*.jpg"
files = glob.glob(path_to_images) 
while(True):
	for f in files:
		image = cv2.imread(f, cv2.IMREAD_COLOR)
		image = cv2.resize(image, (640, 640))
		(H, W) = image.shape[:2]
		board = np.zeros((H, W,3), np.uint8)
		board[:] = 255
		text = pytesseract.image_to_string(image, config="-l eng --oem 1 --psm 3")
		random_text =text.splitlines()
		for i in range(len(random_text)):
			cv2.putText(board, str(random_text[i]), (20,  20*(i+1)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		final_version = np.concatenate((board,image), axis=1)
		cv2.imshow("Result", final_version)
		key = cv2.waitKey(1) & 0xFF
		if key == 27:
			break
		if writer is None:
			fourcc = cv2.VideoWriter_fourcc(*"MJPG")
			writer = cv2.VideoWriter("text_recognition1.avi", fourcc, 1,
				(final_version.shape[1], final_version.shape[0]), True)
		if writer is not None:
			writer.write(final_version)	

cv2.destroyAllWindows()
cap.release()

if writer is not None:
	writer.release()
