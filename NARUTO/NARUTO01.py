
import tensorflow as tf
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列
font_path = 'NotoSansTC-Black.otf'                                     # 字型檔路徑
font = ImageFont.truetype(font_path, 80)                             # 設定字型和大小

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((0, 50), text, font=font, fill=(255, 255, 0))
    img = np.array(img_pil)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (224, 224))
    img = img[:, ::-1]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg,c,d,e,f,g,h,i,j,k,l= prediction[0]
    if a>0.95:
        text('子')  # 使用 text() 函式，顯示文字
    if b>0.95:
        text('丑')
    if bg>0.95:
        text('')
    if c>0.95:
        text('寅')
    if d>0.95:
        text('卯')
    if e>0.95:
        text('辰')
    if f>0.95:
        text('巳')
    if g>0.95:
        text('午')
    if h>0.95:
        text('未')
    if i>0.95:
        text('申')
    if j>0.95:
        text('酉')
    if k>0.95:
        text('戌')
    if l>0.95:
        text('亥')
        
        
    cv2.imshow('NARUTO', img)
    if cv2.waitKey(1) == 27:
        break    # 按下 Esc 鍵停止
cap.release()
cv2.destroyAllWindows()