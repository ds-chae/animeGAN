# AnimeGAN

> 애니메이션에 나오는 얼굴 그림을 위한 Generative Adversarial Networks을 PyTorch로 간단하게 구현하였다. 이것은 원작자의 작업 AnimeGAN을 한글화한 것이다. 이것은 https://github.com/jayleicn/animeGAN에서 임포트 하였다.

### Randomly Generated Images

The images are generated from a DCGAN model trained on 143,000 anime character faces for 100 epochs.

![fake_sample_1](images/fake_sample.png)


### Image Interpolation

Manipulating latent codes, enables the transition from images in the first row to the last row.

![transition](images/fake_transition.png)



### Original Images

The images are not clean, some outliers can be observed, which degrades the quality of the generated images.

![real_sample](images/real_sample.png)



### Usage

To run the experiment, 

```bash
$ python main.py --dataRoot path_to_dataset/ 
```

The pretrained model for DCGAN are also in this repo, play it inside the jupyter notebook.



### anime-faces 데이터셋

[danbooru.donmai.us](http://danbooru.donmai.us/)로부터 크롤러 툴 [gallery-dl](https://github.com/mikf/gallery-dl)을 사용하여 126개 태그의 이미지를 수집하였다. 이 이미지들을 anime face 검출기 [python-animeface](https://github.com/nya3jp/python-animeface)로 처리하였다. The resulting dataset contains ~143,000 anime faces. Note that some of the tags may no longer meaningful after cropping, i.e. the cropped face images under 'uniform' tag may not contain visible parts of uniforms.

> How to construct the dataset from scratch ?

  Prequisites: gallery-dl, python-animeface

1. anime-style 이미지 다운로드 

   ```bash
   # download 1000 images under the tag "misaka_mikoto"
   gallery-dl --images 1000 "https://danbooru.donmai.us/posts?tags=misaka_mikoto"

   # 한번에 여러개 다운로드. 이 방법은 lnux나 windows bash에서 사용가능하다.
   cat tags.txt | \
   xargs -n 1 -P 12 -I 'tag' \ 
   bash -c ' gallery-dl --images 1000 "https://danbooru.donmai.us/posts?tags=$tag" '
   ```
   이 작업을 python을 실행하게 만든 것이 dlimages.py이다.
   ```python
   python dlimages.py
   ```
   실행 시간이 퍽 길어요. 다운로드 중에는 다른 일이나 해야겠습니다.

2. Extract faces from the downloaded images

   ```python
   import animeface
   from PIL import Image

   im = Image.open('images/anime_image_misaka_mikoto.png')
   faces = animeface.detect(im)
   x,y,w,h = faces[0].face.pos
   im = im.crop((x,y,x+w,y+h))
   im.show() # display
   ```


I've cleaned the original dataset, the new version of the dataset has
115085 images in 126 tags. You can access the images from:
- Brine (a python-based dataset management library): https://www.brine.io/jayleicn/anime-faces 
- Google Drive: https://drive.google.com/file/d/0B4wZXrs0DHMHMEl1ODVpMjRTWEk/view?usp=sharing
- BaiduYun: https://pan.baidu.com/s/1o8Nxllo

Non-commercial use please.

### Things I've learned
1. GANs are really hard to train.
2. DCGAN generally works well, simply add fully-connected layers causes problems.
3. In my cases, more layers for G yields better images, in the sense that G should be more powerful than D.
4. Add noise to D's inputs and labels helps stablize training.
5. Use differnet input and generate resolution (64x64 vs 96x96), there seems no obvious difference during training, the generated images are also very similar.
6. Binray Noise as G's input amazingly works, but the images are not as good as those with Gussian Noise, idea credit to @cwhy ['Binary Noise' here I mean a sequence of {-1,1} generated by bernoulli distribution at p=0.5 ]

I did not carefully verify them, if you are looking for some general GAN tips, see @soumith's [ganhacks](https://github.com/soumith/ganhacks)

### Others

1. This project is heavily influenced by [chainer-DCGAN](https://github.com/mattya/chainer-DCGAN) and [IllustrationGAN](https://github.com/tdrussell/IllustrationGAN), the codes are mostly borrowed from [PyTorch DCGAN example](https://github.com/pytorch/examples/tree/master/dcgan), thanks the authors for the clean codes.
2. Dependencies: pytorch, torchvision
3. This is a toy project for me to learn PyTorch and GANs, most importantly, for fun! :) Any feedback is welcome.

@jayleicn
