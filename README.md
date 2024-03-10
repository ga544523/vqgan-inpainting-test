# vqgan-inpainting-test
程式來源<https://github.com/CompVis/taming-transformers/tree/master>


圖片添加mask然後使用vqgan前面學習離散編碼的過程,來進行影像還原
希望達到像codeformer那樣Blind face restoration的效果
沒做甚麼太大調整,感覺效果還行
多加些特徵或在調些參數效果可能更好



512x512縮放到800x600 n_embed 16384
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/demo.gif?raw=true)


512x512縮放到800x600 n_embed 65536
![image](https://github.com/ga544523/vqgan-inpainting-test/blob/main/demo1.gif?raw=true)
