
| 应用        | github 链接   |  描述 | 素材数据|
| --------   | :-----   | :----: | :----: |
| mathai        | [jump](https://github.com/Roujack/mathAI)     |   [jump](#mathai)    |[jump](https://github.com/Roujack/mathAI/tree/master/%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%A0%81(code)/testImgs)|
| image-stitching        | [jump](https://github.com/pavanpn/Image-Stitching)     |   [jump](#image-stitching)    |[jump](https://github.com/pavanpn/Image-Stitching/tree/master/images)|
| playing-card-recognition        | [jump](https://github.com/arnabdotorg/Playing-Card-Recognition)      |   [jump](#playing-card-recognition)    |[jump](../test/data/Playing-Card-Recognition)|
| document-scanner       | [jump](https://github.com/andrewdcampbell/OpenCV-Document-Scanner)     |   [jump](#document-scanner)    |[jump](https://github.com/andrewdcampbell/OpenCV-Document-Scanner/tree/master/sample_images)|
| lane     | [jump](https://github.com/ex2tron/OpenCV-Python-Tutorial/tree/master/%E6%8C%91%E6%88%98%E4%BB%BB%E5%8A%A13%EF%BC%9A%E8%BD%A6%E9%81%93%E6%A3%80%E6%B5%8B#%E5%BC%95%E7%94%A8)    |   [jump](#lane)    |[jump](../test/data/lane)|
| faceai-gender     | [jump](https://github.com/vipstone/faceai/blob/master/doc/gender.md)    |   [jump](#faceai-gender)    |[jump](https://github.com/vipstone/faceai/blob/master/faceai/img/gather.png)|
| faceai-colorize    | -    |   [jump](#faceai-colorize)    |[jump](https://github.com/vipstone/faceai/tree/master/faceai/img/colorize)|
| faceai-compose   | [jump](https://github.com/vipstone/faceai/blob/master/doc/compose.md)     |   [jump](#faceai-compose)    |[jump](https://github.com/vipstone/faceai/tree/master/faceai/img/compose)|
| faceai-detectionOpencv   | -     |   [jump](#faceai-detectionOpencv)    |-|
| faceai-emotion  | [jump](https://github.com/vipstone/faceai/blob/master/doc/emotion.md)    |   [jump](#faceai-emotion)    |[jump](https://github.com/vipstone/faceai/blob/master/faceai/img/emotion/happy.png)|
| faceai-faceRecognitionMakeup  | [jump](https://github.com/vipstone/faceai/blob/master/doc/faceRecognitionMakeup.md)    |   [jump](#faceai-faceRecognitionMakeup)    |-|
| faceai-faceRecognitionOutline   | [jump](https://github.com/vipstone/faceai/blob/master/doc/faceRecognitionOutline.md)     |   [jump](#faceai-faceRecognitionOutline)    |-|



--
<span id = "mathai"> mathai </span>

整个程序使用python实现，具体处理流程包括了图像预处理、字符识别、数学公式识别、数学公式语义理解、结果输出。

本程序使用opencv对输入的图像进行预处理，并将字符裁剪出来再归一化成固定大小的矩阵。我在TensorFlow上实现了一个lenet5 的卷积神经网络用来识别数学字符，训练使用CHROME数据集。对于数学公式的识别，主要是将识别出的独立的字符组织成计算机能够 理解的数学公式（这里的数学公式就是纯字符的可求解的数学计算题）。大概的方法是使用编译原理的算符优先法和递归下降法进行实现。 然后根据属性文法的值传递思想，将数学公式的值计算出来。最后使用python的matlibplot库把计算过程和答案打印出来。

优点：这是一整套拍照做题的算法框架，同时能够处理多种多样的计算题，目前市面上还没有看到实现。OCR技术如此成熟的今天字符识别 已经不算有挑战的东西了。 缺点：字符空间关系判断只用了人类启发式规则，图像预处理不够鲁棒，数学公式的结构识别算法不够完美（可以考虑使用二维文法来做）。 系统还有很大的提升空间。

这本来是一个很有野心的project，因为它试图解决所有的我们遇到的数学题。更一般的是，我试图实现一个演算系统， 在这个系统里，输入一些规则（公理），以及已知条件，我们希望它能够推出一些结论出来。但是我发现这是一个很难的问题。 最近的学习结论告诉我，一方面循环不变式的寻找无法自动化，另一方面演算的时间和空间复杂度太高（可以参考prolog语言的实现）。

什么是智能？是现在的机器学习吗？我觉得不像。SVM是最大化函数间隔的算法，神经网络是寻找损失函数局部最优解的过程。这些技术只是数学层面的优化。 还是某种推理能力？我不知道。如果给它一些演算规则，和一些具有现实意义的符号，再加上一些公理，它能够演算出一些结论，这个结论具有现实意义， 是不是就意味着智能？我觉着是的，不过很难实现。据说吴文俊采用了自动化的方法证明了几何定理（吴方法）。

我们的意识或者思维到底是什么东西？信息在大脑里面到底是如何表示的？我们为什么具有泛华的学习能力？一方面脑认知科学在求索，一方面计算科学也在求索。 我希望意识是能够认识物质的，并在最终达到越来越完美的过程。这才是科研的意义。我愿一直去寻找真理。


--
<span id = "image-stitching"> image-stitching </span>

OpenCV和Python程序可缝合两个输入图像。  
能够处理360度全景。  
支持输入图像的随机顺序。  


--
<span id = "playing-card-recognition"> playing-card-recognition </span>
<span id = "document-scanner"> document-scanner </span>

--

<span id = "lane"> lane </span>  

在所提供的公路图片上检测出车道线并标记.   

本次挑战内容来自Udacity自动驾驶纳米学位课程，素材中车道保持不变，车道线清晰明确，易于检测，是车道检测的基础版本，网上也有很多针对复杂场景的高级实现.   

要检测出当前车道，就是要检测出左右两条车道直线。由于无人车一直保持在当前车道，那么无人车上的相机拍摄的视频中，车道线的位置应该基本固定在某一个范围内  

--


<span id = "faceai-gender"> faceai-gender </span>  

使用OpenCV先识别到人脸，然后在通过keras识别性别

-- 

<span id = "faceai-colorize"> faceai-colorize </span>  

--
<span id = "faceai-compose"> faceai-compose </span>  

头像特效合成
实现思路：使用OpenCV检测出头部位置，向上移动20像素添加虚拟帽子，帽子的宽度等于脸的大小，高度等比缩小，需要注意的是如果高度小于脸部向上移动20像素的值，那么帽子的高度就等于最小高度=（脸部位置-20）。 为什么是20而不是30或者40，因为取得是检测的脸部和头顶的一般距离20，开发者可自己调整。

注意事项

图片合成元件，要是黑背景图片，透明的图片也会有问题，在ps手动处理一下透明图片，添加新图层，选中alt+Del添加黑背景，把新图层层级放到最底部即可。 


--  
<span id = "faceai-detectionOpencv"> faceai-detectionOpencv </span>   

--

<span id = "faceai-emotion"> faceai-emotion </span>  
表情识别
表情识别支持7种表情类型，生气、厌恶、恐惧、开心、难过、惊喜、平静等。
实现思路
使用OpenCV识别图片中的脸，在使用keras进行表情识别。  


--

<span id = "faceai-faceRecognitionMakeup"> faceai-faceRecognitionMakeup </span>  
<span id = "faceai-faceRecognitionOutline"> faceai-faceRecognitionOutline </span>  
