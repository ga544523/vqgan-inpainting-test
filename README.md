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

訓練影像位置
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/2.png?raw=true)

每張影像位置存入txt檔 命名為train.txt
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/1.png?raw=true)

custom_vqgan.yaml參數設定
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/3.png?raw=true)

運行產生的mask可透過base.py裡的 RandomIrregularMaskGenerator進行調整
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/4.png?raw=true)


## 測試

推論後儲存的圖片
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/example/6.png?raw=true)
