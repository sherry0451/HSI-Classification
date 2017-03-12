# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:34:06 2016
测试验证码分类模型的准确率
@author: Administrator
"""
from keras.models import model_from_json
import numpy as np
#from keras.utils.visualize_util import plot
from keras import backend as K
from ImagePre import getPicArrWithLab

def oneHotLab2str(labArr):
    num=[]
    strs=[]
    for i in labArr:
        for idx,j in enumerate(i):
            if np.round(j)==1:
                num.append(idx)
                break
    for i in num:
        if 0<=i<10:
            strs.append(str(i))
        if 9<i<37:
            strs.append(chr(i+97-10))
    return strs

picBasePath="D:/project/VertCode/tuniu"
labPath="D:/project/VertCode/1(1).txt"
X_train,Y_train=getPicArrWithLab(picBasePath,labPath,reverse=True,binary=False,skele=False)

    
    
modelPath="D:/project/VertCode/mycode/output/model"
model0 = model_from_json(open(modelPath+"/model0.json").read())    
model0.load_weights(modelPath+"/model0_weight.h5")    
model1 = model_from_json(open(modelPath+"/model1.json").read())    
model1.load_weights(modelPath+"/model1_weight.h5")   
model2 = model_from_json(open(modelPath+"/model1.json").read())    
model2.load_weights(modelPath+"/model1_weight.h5")    
model3 = model_from_json(open(modelPath+"/model1.json").read())    
model3.load_weights(modelPath+"/model1_weight.h5")     

#模型可视化
# with a Sequential model,visualize
#get_3rd_layer_output =theano.function([model1.layers[0].input],
#model1.layers[2].get_output(train=False))
#layer_output =get_3rd_layer_output(X_train)

#plot(model1, to_file='model.png')
# with a Sequential model
#get_3rd_layer_output = K.function([model1.layers[0].input],
#                                  [model1.layers[3].output])
#X_train=theano.shared(X_train,borrow=True)                                 
#layer_output = get_3rd_layer_output([X_train])[0]

ori =[]#真实标签
pred=[]#预测标签
for i in range(len(Y_train)):
    ori_t=[]
    pred_t=[]
    ori_t.append(oneHotLab2str([Y_train[i,0,:]]))
    ori_t.append(oneHotLab2str([Y_train[i,1,:]]))
    ori_t.append(oneHotLab2str([Y_train[i,2,:]]))
    ori_t.append(oneHotLab2str([Y_train[i,3,:]]))
    
    pred_w=model0.predict(np.array([X_train[i]]))
    pred_t.append(oneHotLab2str(pred_w))
    pred_w=model1.predict(np.array([X_train[i]]))
    pred_t.append(oneHotLab2str(pred_w))
    pred_w=model2.predict(np.array([X_train[i]]))
    pred_t.append(oneHotLab2str(pred_w))
    pred_w=model3.predict(np.array([X_train[i]]))#oneHot
    pred_t.append(oneHotLab2str(pred_w))#str
    ori.append(ori_t)
    pred.append(pred_t)

count=0
for idx,i in enumerate(ori):
    if i[1]==pred[idx][1]:
        count+=1
#    if i[2]==pred[idx][2]:
#        count+=1
#    if i[3]==pred[idx][3]:
#        count+=1

#