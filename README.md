# Description
TensorFlowで転移学習を用いてパーソナルカラー診断を行うためのモデルを作成してから､カメラを用いてリアルタイムで診断を行えるように作成しました｡

![sampleee](https://user-images.githubusercontent.com/61785070/142383981-7d9cbcd1-1241-4f22-b2d5-30d182cf20ca.jpg)


# Requirement
 開発に使用したライブラリ
 
* tensorflow 2.5.0
* opencv 4.5.2.52


# Features
* パソコン等のカメラを用いてリアルタイムでカスケード分類機によって顔認識を行い､顔だけを抽出してパーソナルカラー診断を行う｡
* 複数人同時にパーソナルカラー診断を行うことができる｡

こんな感じでリアルタイムに動作を行います｡

https://youtu.be/iYd_ez8LPas


# How to use
ファイルの中身は以下のようにしておく必要があります｡

<img width="769" alt="スクリーンショット 2021-11-18 15 33 27" src="https://user-images.githubusercontent.com/61785070/142364606-fa229493-c985-41f1-99aa-9ce81d0648d0.png">

* personal_color_model1.h5は学習済みのモデルで､容量が大きいため以下からダウンロードを行って下さい｡
https://drive.google.com/file/d/1ESLm0Ri3QNrz5isLr1jwXVvSvYaBpNmi/view?usp=sharing

```bash
python camera.py
```


# Installation
 
Requirementで列挙したライブラリなどのインストール方法
```bash
pip install tensorflow 
```
```bash
pip install opencv-python
```
# Note
MacOSで開発を行いました｡モデルの開発はgoogle colob proを用いて作成しました｡

# Author
* k.junya0727@gmail.com
* 具体的な詳細であったり､質問等ございましたらご気軽に連絡ください
