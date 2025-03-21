# 請標記人員, 可以直接跳到第 4 步驟開始, 從第 4 步驟做到第 8.4 步驟做完即可

## Custom ava dataset, Custom Spatio Temporally Action Video Dataset for Windows
Custom ava dataset, Multi-Person Video Dataset Annotation Method of Spatio-Temporally Actions <br>
自定義ava數據集，多人視頻的時空動作數據集標註方法 使用到 Windows 系統上


CSDN：https://blog.csdn.net/WhiffeYF/article/details/124358725

知乎：https://zhuanlan.zhihu.com/p/503031957

B站：https://www.bilibili.com/video/BV1j3411M7Ba/

### 下面 1、2、3 部分請自己參考，在自己電腦環境上可以跳過到第 4 部份，另外建議安裝 Anaconda 的虛擬環境再進行安裝

## 1 Dataset's folder structure 數據集文件結構

![image](https://github.com/Whiffe/Custom-ava-dataset_Multi-Person-Video-Dataset-Annotation-Method-of-Spatio-Temporally-Actions/blob/95307633663fa3103a46de75220aabf1174013ca/images/DatasetFolderStructure.png)

## 2 AI platform and project download. AI平台與項目下載
## AI platform. AI 平台
The AI platform I use is: [https://cloud.videojj.com/auth/register?inviter=18452&activityChannel=student_invite](https://cloud.videojj.com/auth/register?inviter=18452&activityChannel=student_invite) <br>
我使用的AI平台：[https://cloud.videojj.com/auth/register?inviter=18452&activityChannel=student_invite](https://cloud.videojj.com/auth/register?inviter=18452&activityChannel=student_invite)

以下的操作均在該平台的基礎上完成。

實例鏡像選擇：Pytorch 1.8.0，python 3.8，CUDA 11.1.1

Instance mirroring selection：Pytorch 1.8.0，python 3.8，CUDA 11.1.1 <br>
安裝環境選擇：Pytorch 1.8.0，python 3.8，CUDA 11.1.1
![image](https://img-blog.csdnimg.cn/c6544a25f8a748c88ff4451cd1fceb39.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6K6h566X5py66KeG6KeJLeadqOW4hg==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 2.2 project download. AI平台與項目下載
為了讓項目快速下載，我將項目同步到了碼雲：[https://gitee.com/YFwinston/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset.git](https://gitee.com/YFwinston/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset.git)
```python
cd /home
git clone https://github.com/JasonHuang0119/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows.git

```

## 3 資料集影片收集
The video is 1 randomly selected from the AVA dataset, and I will crop 3 10-second segments from this video:<br>
影片是從AVA資料集中隨機選擇了1個，我會從這個影片中裁剪出3個10秒的片段：
```python
https://s3.amazonaws.com/ava-dataset/trainval/2DUITARAsWQ.mp4
```
Execute the following code on the AI platform:<br>
在AI平台執行：
```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
wget https://s3.amazonaws.com/ava-dataset/trainval/2DUITARAsWQ.mp4 -O ./1.mp4
```
![image](https://img-blog.csdnimg.cn/1f996811ec164f08b21f04e42220601a.png)

# 4 Video cropping and frame extraction 影片裁剪與抽幀
## 4.1 install ffmpeg 安裝ffmpeg
We use ffmpeg for video cropping and frame extraction, so install ffmpeg first<br>
本文使用ffmpeg進行影片裁切與抽幀，所以先安裝ffmpeg
```python
conda install x264 ffmpeg -c conda-forge -y
```
## 4.2 video cropping 影片裁剪
Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset:<br>
在C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset下執行：

```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
cut_videos.bat
```
![image](https://img-blog.csdnimg.cn/8e9b191bb72e41ee96b508ad0230a4e5.png)
## 4.3 video frame 影片抽幀
Referring to the ava dataset, crop 30 frames per second <br>
参考ava数据集，每秒裁剪 30 幀<br>

Execute the code under C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset:<br>
在C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset 下执行：

```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
cut_frames.bat 
```
![image](https://img-blog.csdnimg.cn/ff14789c0a3743e584ea11de15dfc517.png)
![image](https://img-blog.csdnimg.cn/334197c4599e4a12ab594dd8133730a4.png)

## 4.4 Consolidate and downscale frames 整合與缩减幀
The structure of the frames folder generated in Section 4.3 will be inconvenient in the subsequent yolov5 detection, so I put all the pictures in a folder (choose_frames_all) in the following way.<br>
4.3 節中產生的frames資料夾的結構，在後續yolov5檢測時會出現不方便，所以我採用下面的方式，將所有的圖片放在了一個資料夾（choose_frames_all）中。<br>

It should be noted that not all images need to be detected and labeled. In the 16-second video, the detection labels are: x_000001.jpg, x_000031.jpg, x_000061.jpg, x_000091.jpg, x_0000121jpg, x_000151.jpg, x_000181. jpg, x_000211.jpg, x_000241.jpg, x_000271.jpg, x_000301.jpg.<br>

要注意的是，並不是，所有圖片都需要偵測與標註，在16秒的影片中，偵測標註：x_000001.jpg、x_000031.jpg、x_000061.jpg、x_000091.jpg、x_0000121jpg、x_000151.jpg、x_000181.jpg、x_000211.jpg、x_000241.jpg、x_000271.jpg、x_000301.jpg、x_000331.jpg、x_000361.jpg、x_000391.jpg、x_000421.jpg、x_000451.jpg、x_000481.jpg。<br>

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset:<br>
在 C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset 下执行：

```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python choose_frames_all.py 16 0
```
In the above code, 16 represents the length of the video, and 0 represents the start from the 0th second.<br>
其中 16 代表影片長度，0代表從第0秒開始 <br>
![image](https://img-blog.csdnimg.cn/8fbb68efa7ac407db1317b1e5d202753.png)

## 4.5 Not consolidate and downscale frames 不整合的缩减幀。
The consolidate and downscale frames in 4.4 is for the detection of yolov5, and not consolidate and downscale frames here is for the labeling of VIA.
4.4 的整合與縮減是為了yolov5的偵測，這裡的不整合的縮減是為了VIA的標註。<br>

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset:<br>
在 C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset 下执行：
```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python choose_frames.py 16 0
```
![image](https://img-blog.csdnimg.cn/f5501f08cd7941c692b702f0af25f985.png)
![image](https://img-blog.csdnimg.cn/9041d1ad34ca435ebd67c2f3e1bce3c8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_15,color_FFFFFF,t_70,g_se,x_16)

# 5 yolov5 and deep sort installation. yolov5與deep sort 安裝

##  5.1 Install 安装
run the following code<br>
運行以下程式碼：<br>
```
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\yolovDeepsort
pip install -r requirements.
pip install opencv-python-headless==4.1.2.30

# 以下內容 windows 系統可以不用做 會幫你安裝在使用者環境下 這是安裝 yolo 的一種文檔
wget https://github.com/ultralytics/yolov5/releases/download/v6.1/yolov5s.pt -O C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\yolovDeepsort\yolov5\yolov5s.pt 
mkdir -p /root/.config/Ultralytics/
wget  https://ultralytics.com/assets/Arial.ttf -O /root/.config/Ultralytics/Arial.ttf
```
The reason for using deep sort: In preparation for generating [train/val].csv, dense_proposals_[train/val/test].pkl will not use the detection results of deep sort.<br>
採用deep sort的原因：為產生[train/val].csv做準備，dense_proposals_[train/val/test].pkl不會用到deep sort的偵測結果。<br>

## 5.2 Detect choose_frames_all 對 choose_frames_all 進行檢測


```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset\yolovDeepsort
python ./yolov5/detect.py --source ../Dataset/choose_frames_all/ --save-txt --save-conf 
```
The result is stored in: /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/yolov5/runs/detect/exp <br>
结果儲存在：/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/yolov5/runs/detect/exp <br>

![image](https://img-blog.csdnimg.cn/f92b6d91cfb94eb0866ac37704f3d888.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

# 6 Generate dense_proposals_train.pkl

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork：
這邊 exp 是看使用 yolo detect.py 後產生的資料夾 請用當下產生的那個資料夾，該資料夾位於 /home/jason/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/yolov5/runs/detect/exp7 <br> Ex: exp7 下面請幫我改成 exp7
```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\yolovDeepsort\mywork
python dense_proposals_train.py ../yolov5/runs/detect/exp7/labels ./dense_proposals_train.pkl show
```

# 7 import via 將須標註圖片導入 via 線上標註網頁

## 7.1 choose_frames_all_middle
The choose_frames folder under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset contains 11 pictures in the 10-second video, but the final generated annotation file does not contain the first 2 pictures and The last 2 pictures. So you need to create a choose_frames_middle folder to store the folders without the first 2 pictures and the last 2 pictures.<br>
/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset 下的 choose_frames 文件夹中包含10秒视频中11张图片，但是在最后生成的标注文件，不包含前2张图片和后2张图片。所以需要创建一个choose_frames_middle文件夾，存放不含前2張圖片與後2張圖片的文件夾。<br>

```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python choose_frames_middle.py
```
![image](https://img-blog.csdnimg.cn/db8205ef31f0417194a3f40d9bd8caf2.png)

## 7.2 Generate via annotation file 生成 via 標註文件
自定义动作在：/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork/dense_proposals_train_to_via.py文件中，具体位置如下图：<br>
The custom action is in: /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork/dense_proposals_train_to_via.py file, the specific location is as follows:<br>
![image](https://img-blog.csdnimg.cn/dc0220d520414c7e82d9fe66eb949e6c.png)

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork/:<br>
在/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork/下執行:<br>
```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\yolovDeepsort\mywork\
python dense_proposals_train_to_via.py ./dense_proposals_train.pkl ../../Dataset/choose_frames_middle/
```
The generated annotation files are saved in: /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/choose_frames_middle<br>
產生的標註文件保存在：/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/choose_frames_middle中<br>
![image](https://img-blog.csdnimg.cn/0ad5591962b64fceb90f2a26a7fa98f1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_15,color_FFFFFF,t_70,g_se,x_16)
## 7.3 Remove the default value of via 去掉via默认值
標註時有預設值，這個會影響我們的標註，需要取消掉。<br>
There is a default value when labeling, which will affect our labeling and needs to be canceled.<br>

我嘗試了很多次，想在產生via標註檔時，去掉標註選項中的預設值，但還是沒有實現，那就在生成之後，直接對via的json檔進行操作，去掉預設值。<br>
I have tried many times and want to remove the default value in the annotation option when generating the via annotation file, but it is still not implemented. Then after the generation, directly operate the via json file and remove the default value.<br>

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/:<br>
在：C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset下運行<br>

```python
cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python chang_via_json.py 
```
![image](https://img-blog.csdnimg.cn/de6866f0ef484a3ea909ce5bda598857.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_15,color_FFFFFF,t_70,g_se,x_16)

## 7.5 Download choose_frames_middle and VIA annotation 下载choose_frames_middle与VIA标注
Compress the choose_frames_middle file<br>
對choose_frames_middle文件壓縮，這部分是配合上傳到雲端平台，如果是在本地端可以不用做<br>

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset: <br>
在/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset中執行：<br>

```python
apt-get update
apt-get install zip
apt-get install unzip

cd C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
zip -r choose_frames_middle.zip choose_frames_middle
```
Download choose_frames_middle.zip<br>
下載：choose_frames_middle.zip<br>

Then use via to label<br>
然后使用via進行標註<br>

via official website:[https://www.robots.ox.ac.uk/~vgg/software/via/](https://www.robots.ox.ac.uk/~vgg/software/via/)<br>
via官网：[https://www.robots.ox.ac.uk/~vgg/software/via/](https://www.robots.ox.ac.uk/~vgg/software/via/)<br>

via annotation tool download link: [https://www.robots.ox.ac.uk/~vgg/software/via/downloads/via3/via-3.0.11.zip](https://www.robots.ox.ac.uk/~vgg/software/via/downloads/via3/via-3.0.11.zip)<br>
via標註工具下載連結：[https://www.robots.ox.ac.uk/~vgg/software/via/downloads/via3/via-3.0.11.zip](https://www.robots.ox.ac.uk/~vgg/software/via/downloads/via3/via-3.0.11.zip)<br>

Click in the annotation tool: via_image_annotator.html<br>
點選標註工具中的： via_image_annotator.html<br>

![image](https://img-blog.csdnimg.cn/fec0e87d18ab48c2af8299791a1e71af.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_18,color_FFFFFF,t_70,g_se,x_16)

The following picture is the interface of via, 1 represents adding pictures, 2 represents adding annotation files <br>
下圖是via的介面，1代表添加圖片，2代表添加標註文件<br>

![image](https://img-blog.csdnimg.cn/6c896dd36f284f2286867510c705a7de.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

Import the image, open the annotation file (note, open x_proposal_s.json), the final result:<br>
导入图片，打开标注文件（注意，打开x_proposal_s.json），最后结果：<br>
![image](https://img-blog.csdnimg.cn/ba44be0e5d454a2ba063e363b179daea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

# 8 Extraction of via annotation information. via标注信息的提取
After action annotation, the annotation information of via is saved as a json file. The json file contains: the name of the video, the number of the video frame, the boundding box of the human, and the number of the action category.<br>
經過動作標註，via的標註資訊儲存為json文件，json文件中包含：影片的名字、影片畫面的編號、人的座標值、動作類別編號<br>

These information are required for the annotation file, and the information in the json file needs to be integrated. This section is to integrate the information in the via.<br>
這些資訊都是標註文件所需要的，需要把json文件中的信息整合，這一節就是對via中信息做整合。<br>

## 8.1 ava_train
The following figure is the ava annotation file (ava_train.csv)<br>
下圖是ava標註文件（ava_train.csv）<br>

![image](https://img-blog.csdnimg.cn/0af268f7e8a94fda87dfc75797ee38da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)
Column 1: The name of the video<br>
第一列：影片的名字<br>

Column 2: the video frame ID, for example, the frame at 15:02 is expressed as 902, and the frame at 15:03 is expressed as 903<br>
第二列：视频帧ID，比如15:02这一帧，表示为902，15:03这一帧表示为903<br>

Column 3-6: the boundding box of the human (x1, y1, x2, y2)<br>
第三列到第六列： 人的坐标值（x1，y1，x2，y2）<br>

Column 7: Action category number<br>
第七列：动作类别编号<br>

Column 8: Person's ID<br>
第八列：人的ID<br>

At present, there is no ID of the last column in our data, and everything else is generated, so let's extract this information first.<nr>
目前，我们的数据中没有最后一列的ID，其它都生成了，所以我们先将这些信息提取出来。<br>
  
## 8.2 Analysis of via Json file. via Json 解析

Parse the json parsing website using the runoob platform: [https://c.runoob.com/front-end/53/](https://c.runoob.com/front-end/53/)<br>
解析使用菜鸟平台的json解析网站：[https://c.runoob.com/front-end/53/](https://c.runoob.com/front-end/53/)<br>

![image](https://img-blog.csdnimg.cn/de1fbd11744749748d2ac8c0e4611a99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_10,color_FFFFFF,t_70,g_se,x_16)
![image](https://img-blog.csdnimg.cn/ac088d5de8ff4e179e673e658d90b9fd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_10,color_FFFFFF,t_70,g_se,x_16)

  
## 8.3 Extract the uploaded json file. 提取上传标注完成的json文件

这里需要注意的是，我给每个标注完成的文件取名：视频名_finish.json，如视频1，标注完成后的名字为：1_finish.json<br>  
It should be noted here that I named the labeled file: video_name_finish.json, such as video 1, the marked name is: 1_finish.json<br>
![image](https://img-blog.csdnimg.cn/77fb16c7c221404db9544d76206ce7e1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_15,color_FFFFFF,t_70,g_se,x_16)
  

Execute the code under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset: <br>
在/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset中执行：<br>
```python
cd  C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python json_extract.py
```
It will be generated under /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/:<br>
train_without_personID.csv <br>
会在/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/下生成：<br>
train_without_personID.csv<br>
![image](https://img-blog.csdnimg.cn/c67fa6d19d3643acbcb2be835c121f85.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

## 8.4 Sort_ava_name  train_without_person_id.csv 需要進行微調
因為 train_without_person_id.csv 裡面順序是亂序，我們是用序列型資料要完整的從影片開始到結束，所以需要時間排序正確

執行 
```python
cd  C:\Users\jason\Desktop\Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset-Windows\Dataset
python sorted_ava_name.py
```

  
# 10 Generation of other annotation files 其它标注文件的生成
## 10.1 train_excluded_timestamps.csv
I spent almost 85% of the content talking about the method of ava_train.csv, and the generation method of the rest of the annotation files is relatively simple<br>
我几乎花了85%的内容说了ava_train.csv的方法，其余的标注文件的生成方法相对较为简单<br>
  
```python
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/annotations
touch train_excluded_timestamps.csv
```
  
## 10.2 included_timestamps.txt

```python
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/annotations
touch included_timestamps.txt
```
  
Then in included_timestamps.txt write:<br>
然后在included_timestamps.txt 中写入<br>
  
```python
02
03
04
05
06
07
08
```
  

## 10.3 action_list.pbtxt
```python
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/annotations
touch action_list.pbtxt
```

```python
item {
  name: "talk"
  id: 1
}
item {
  name: "bow"
  id: 2
}
item {
  name: "stand"
  id: 3
}
item {
  name: "sit"
  id: 4
}
item {
  name: "walk"
  id: 5
}
item {
  name: "hand up"
  id: 6
}
item {
  name: "catch"
  id: 7
}

## 11.1 rawframes
In the name of the video frame, there is a problem that the name of the video frame does not match the training, so it is necessary to modify the name of the picture in /home/Dataset/frames<br>
在取名上，裁剪的视频帧存在与训练不匹配的问题，所以需要对/home/Dataset/frames中的图片进行名字修改<br>

for example:<br>
例如:<br>
 
original name 原本的名字：rawframes/1/1_000001.jpg<br>
target name 目标名字：rawframes/1/img_00001.jpg<br>

```python
cp -r /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/frames/* /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/rawframes
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork/
python change_raw_frames.py
```
![image](https://img-blog.csdnimg.cn/8f5e87a194234453b10d5b4cee9e309d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_14,color_FFFFFF,t_70,g_se,x_16)

# 13 Annotation file correction. 标注文件修正
## 13.1 dense_proposals_train

```python
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork
python change_dense_proposals_train.py
```
## 13.2 dense_proposals_val

```python
cd /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/yolovDeepsort/mywork
python change_dense_proposals_val.py
```
  
# 14 mmaction2 install

```python
cd /home

git clone https://gitee.com/YFwinston/mmaction2_YF.git

pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.0/index.html

pip install opencv-python-headless==4.1.2.30

pip install moviepy

cd mmaction2_YF
pip install -r requirements/build.txt
pip install -v -e .
mkdir -p ./data/ava

cd ..
git clone https://gitee.com/YFwinston/mmdetection.git
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .

cd ../mmaction2_YF

wget https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_2x_coco/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth -P ./Checkpionts/mmdetection/

wget https://download.openmmlab.com/mmaction/recognition/slowfast/slowfast_r50_8x8x1_256e_kinetics400_rgb/slowfast_r50_8x8x1_256e_kinetics400_rgb_20200716-73547d2b.pth -P ./Checkpionts/mmaction/
```
  
# 15 Train and Test 训练与测试
## 15.1 configuration file 配置文件
Create my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py under /mmaction2/configs/detection/ava/<br>
在 /mmaction2_YF/configs/detection/ava/下创建 my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py<br>

```python
cd /home/mmaction2_YF/configs/detection/ava/
touch my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py
```
  
```python
# model setting
model = dict(
    type='FastRCNN',
    backbone=dict(
        type='ResNet3dSlowFast',
        pretrained=None,
        resample_rate=8,
        speed_ratio=8,
        channel_ratio=8,
        slow_pathway=dict(
            type='resnet3d',
            depth=50,
            pretrained=None,
            lateral=True,
            conv1_kernel=(1, 7, 7),
            dilations=(1, 1, 1, 1),
            conv1_stride_t=1,
            pool1_stride_t=1,
            inflate=(0, 0, 1, 1),
            spatial_strides=(1, 2, 2, 1)),
        fast_pathway=dict(
            type='resnet3d',
            depth=50,
            pretrained=None,
            lateral=False,
            base_channels=8,
            conv1_kernel=(5, 7, 7),
            conv1_stride_t=1,
            pool1_stride_t=1,
            spatial_strides=(1, 2, 2, 1))),
    roi_head=dict(
        type='AVARoIHead',
        bbox_roi_extractor=dict(
            type='SingleRoIExtractor3D',
            roi_layer_type='RoIAlign',
            output_size=8,
            with_temporal_pool=True),
        bbox_head=dict(
            type='BBoxHeadAVA',
            in_channels=2304,
            num_classes=81,
            multilabel=True,
            dropout_ratio=0.5)),
    train_cfg=dict(
        rcnn=dict(
            assigner=dict(
                type='MaxIoUAssignerAVA',
                pos_iou_thr=0.9,
                neg_iou_thr=0.9,
                min_pos_iou=0.9),
            sampler=dict(
                type='RandomSampler',
                num=32,
                pos_fraction=1,
                neg_pos_ub=-1,
                add_gt_as_proposals=True),
            pos_weight=1.0,
            debug=False)),
    test_cfg=dict(rcnn=dict(action_thr=0.002)))

dataset_type = 'AVADataset'
data_root = '/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/rawframes'
anno_root = '/home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/annotations'


#ann_file_train = f'{anno_root}/ava_train_v2.1.csv'
ann_file_train = f'{anno_root}/train.csv'
#ann_file_val = f'{anno_root}/ava_val_v2.1.csv'
ann_file_val = f'{anno_root}/val.csv'

#exclude_file_train = f'{anno_root}/ava_train_excluded_timestamps_v2.1.csv'
#exclude_file_val = f'{anno_root}/ava_val_excluded_timestamps_v2.1.csv'

exclude_file_train = f'{anno_root}/train_excluded_timestamps.csv'
exclude_file_val = f'{anno_root}/val_excluded_timestamps.csv'

#label_file = f'{anno_root}/ava_action_list_v2.1_for_activitynet_2018.pbtxt'
label_file = f'{anno_root}/action_list.pbtxt'

proposal_file_train = (f'{anno_root}/dense_proposals_train.pkl')
proposal_file_val = f'{anno_root}/dense_proposals_val.pkl'

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_bgr=False)

train_pipeline = [
    dict(type='SampleAVAFrames', clip_len=32, frame_interval=2),
    dict(type='RawFrameDecode'),
    dict(type='RandomRescale', scale_range=(256, 320)),
    dict(type='RandomCrop', size=256),
    dict(type='Flip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='FormatShape', input_format='NCTHW', collapse=True),
    # Rename is needed to use mmdet detectors
    dict(type='Rename', mapping=dict(imgs='img')),
    dict(type='ToTensor', keys=['img', 'proposals', 'gt_bboxes', 'gt_labels']),
    dict(
        type='ToDataContainer',
        fields=[
            dict(key=['proposals', 'gt_bboxes', 'gt_labels'], stack=False)
        ]),
    dict(
        type='Collect',
        keys=['img', 'proposals', 'gt_bboxes', 'gt_labels'],
        meta_keys=['scores', 'entity_ids'])
]
# The testing is w/o. any cropping / flipping
val_pipeline = [
    dict(type='SampleAVAFrames', clip_len=32, frame_interval=2),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='FormatShape', input_format='NCTHW', collapse=True),
    # Rename is needed to use mmdet detectors
    dict(type='Rename', mapping=dict(imgs='img')),
    dict(type='ToTensor', keys=['img', 'proposals']),
    dict(type='ToDataContainer', fields=[dict(key='proposals', stack=False)]),
    dict(
        type='Collect',
        keys=['img', 'proposals'],
        meta_keys=['scores', 'img_shape'],
        nested=True)
]

data = dict(
    #videos_per_gpu=9,
    #workers_per_gpu=2,
    videos_per_gpu=5,
    workers_per_gpu=2,
    val_dataloader=dict(videos_per_gpu=1),
    test_dataloader=dict(videos_per_gpu=1),
    train=dict(
        type=dataset_type,
        ann_file=ann_file_train,
        exclude_file=exclude_file_train,
        pipeline=train_pipeline,
        label_file=label_file,
        proposal_file=proposal_file_train,
        person_det_score_thr=0.9,
        data_prefix=data_root,
        start_index=1,),
    val=dict(
        type=dataset_type,
        ann_file=ann_file_val,
        exclude_file=exclude_file_val,
        pipeline=val_pipeline,
        label_file=label_file,
        proposal_file=proposal_file_val,
        person_det_score_thr=0.9,
        data_prefix=data_root,
        start_index=1,))
data['test'] = data['val']

#optimizer = dict(type='SGD', lr=0.1125, momentum=0.9, weight_decay=0.00001)
optimizer = dict(type='SGD', lr=0.0125, momentum=0.9, weight_decay=0.00001)
# this lr is used for 8 gpus

optimizer_config = dict(grad_clip=dict(max_norm=40, norm_type=2))
# learning policy

lr_config = dict(
    policy='step',
    step=[10, 15],
    warmup='linear',
    warmup_by_epoch=True,
    warmup_iters=5,
    warmup_ratio=0.1)
#total_epochs = 20
total_epochs = 100
checkpoint_config = dict(interval=1)
workflow = [('train', 1)]
evaluation = dict(interval=1, save_best='mAP@0.5IOU')
log_config = dict(
    interval=20, hooks=[
        dict(type='TextLoggerHook'),
    ])
dist_params = dict(backend='nccl')
log_level = 'INFO'
work_dir = ('./work_dirs/ava/'
            'slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb')
load_from = ('https://download.openmmlab.com/mmaction/recognition/slowfast/'
             'slowfast_r50_4x16x1_256e_kinetics400_rgb/'
             'slowfast_r50_4x16x1_256e_kinetics400_rgb_20200704-bcde7ed7.pth')
resume_from = None
find_unused_parameters = False


```

## 15.2 训练

```python
cd /home/mmaction2_YF
python tools/train.py configs/detection/ava/my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py --validate

```
![image](https://img-blog.csdnimg.cn/296943c198974c27ae1338bc28647663.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

The weights after training are:<br>
训练后的权重在：home/mmaction2/work_dirs/ava/slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb：<br>
![image](https://img-blog.csdnimg.cn/296943c198974c27ae1338bc28647663.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)

## 15.3 Test 測試
First, create a new label_map<br>
首先，創建新的label_map<br>

```python
cd /home/mmaction2_YF/tools/data/ava
touch label_map2.txt
```
The content of label_map2.txt is as follows:<br>
label_map2.txt内容如下：<br>

```python
1: talk
2: bow
3: stand
4: sit
5: walk
6: hand up
7: catch
```
Then run: <br>
然后运行：<br>

```python
cd /home/mmaction2_YF
python demo/demo_spatiotemporal_det.py --config configs/detection/ava/my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py --checkpoint /home/mmaction2_YF/work_dirs/ava/slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb/best_mAP@0.5IOU_epoch_10.pth --det-config demo/faster_rcnn_r50_fpn_2x_coco.py  --det-checkpoint Checkpionts/mmdetection/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth   --video /home/Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/video_crop/1.mp4  --out-filename demo/det_1.mp4   --det-score-thr 0.5 --action-score-thr 0.5 --output-stepsize 4  --output-fps 6 --label-map tools/data/ava/label_map2.txt
```
where best_mAP@0.5IOU_epoch_47.pth is the weight after training, and 441.mp4 is the video uploaded by yourself<br>
其中 best_mAP@0.5IOU_epoch_47.pth 是训练后的权重，441.mp4是自己上传的视频<br>

The detection result is in: /home/mmaction2/demo/det_1.mp4<br>
检测结果在：/home/mmaction2/demo/det_1.mp4<br>
![image](https://img-blog.csdnimg.cn/ba457d7f76424f5fb6d502cd39fb8185.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ1Yt5p2o5biG,size_20,color_FFFFFF,t_70,g_se,x_16)


The test results are not good for two reasons:<br>
检测结果不好，原因有两个：<br>
  
1. The dataset is very small
1，数据集非常小

2. Almost 90% of the labels are stand, causing imbalance
2，几乎90%的标注为stand，造成了不平衡
