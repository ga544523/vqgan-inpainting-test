# vqgan-inpainting-test
程式來源<https://github.com/CompVis/taming-transformers/tree/master>


圖片添加mask然後使用vqgan前面學習離散編碼的過程,來進行影像還原
希望達到像codeformer那樣Blind face restoration的效果
沒做甚麼太大調整,感覺效果還行
多加些特徵或在參數再增加些效果可能更好(如下面的增加n_embed)



512x512縮放到800x600 n_embed 16384
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/demo.gif?raw=true)


512x512縮放到800x600 n_embed 65536
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/demo1.gif?raw=true)

## 訓練
與原版基本相同

存好訓練圖片
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/2.png?raw=true)

每張影像位置存入txt檔 命名為train.txt
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/1.png?raw=true)

configs/custom_vqgan.yaml參數設定
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/3.png?raw=true)

taming/data/base.py參數設定（siz影像大小,）
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/8.png?raw=true)

RandomIrregularMaskGenerator (mask大小調整) 來自<https://github.com/advimman/lama>
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/9.png?raw=true)

main.py裡infer改為0
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/7.png?raw=true)

運行python main.py --base configs/custom_vqgan.yaml -t True --gpus 0,   (需要逗號)

logs裡產生的mask圖片
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/4.png?raw=true)


## 測試
(main.py裡的infer是測試時的代碼)
讀取訓練後的ckpt
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/11.png?raw=true)

推論圖片 影像跟mask配對
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/5.png?raw=true)

main.py裡infer改為1 
運行python main.py --base configs/custom_vqgan.yaml -t True --gpus 0,   (需要逗號)

執行底下的infer程式
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/10.png?raw=true)

推論後儲存的圖片
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/6.png?raw=true)
