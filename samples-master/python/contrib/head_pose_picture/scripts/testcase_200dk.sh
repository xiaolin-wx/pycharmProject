﻿#!/bin/bash
yolo_tf_model="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/head_pose_picture/yolo_model.pb"
whenet_tf_model="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/head_pose_picture/WHENet_b2_a1_modified.pb"
images_link="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/head_pose_picture"

yolo_model_name="yolo_model"
whenet_model_name="WHENet_b2_a1_modified"
version=$1
data_source="../data/"
verify_source="../data/"
project_name="head_pose_picture"
script_path="$( cd "$(dirname $BASH_SOURCE)" ; pwd -P)"
project_path=${script_path}/..

declare -i success=0
declare -i inferenceError=1
declare -i verifyResError=2


function setAtcEnv() {

    if [[ ${version} = "c73" ]] || [[ ${version} = "C73" ]] || [[ ${version} = "C78" ]];then
        export install_path=/home/HwHiAiUser/Ascend/ascend-toolkit/latest
        export PATH=/usr/local/python3.7.5/bin:${install_path}/atc/ccec_compiler/bin:${install_path}/atc/bin:$PATH
        export PYTHONPATH=${install_path}/atc/python/site-packages/te:${install_path}/atc/python/site-packages/topi:$PYTHONPATH
        export ASCEND_OPP_PATH=${install_path}/opp
        export LD_LIBRARY_PATH=${install_path}/atc/lib64:${LD_LIBRARY_PATH}
    elif [[ ${version} = "c75" ]] || [[ ${version} = "C75" ]] || [[ ${version} = "C78" ]];then
        export install_path=$HOME/Ascend/ascend-toolkit/latest
        export PATH=/usr/local/python3.7.5/bin:${install_path}/atc/ccec_compiler/bin:${install_path}/atc/bin:$PATH
        export ASCEND_OPP_PATH=${install_path}/opp
        export PYTHONPATH=${install_path}/atc/python/site-packages:${install_path}/atc/python/site-packages/auto_tune.egg/auto_tune:${install_path}/atc/python/site-packages/schedule_search.egg:$PYTHONPATH
        export LD_LIBRARY_PATH=${install_path}/atc/lib64:${LD_LIBRARY_PATH}
    fi

    return 0
}

function setRunEnv() {

    if [[ ${version} = "c73" ]] || [[ ${version} = "C73" ]]  || [[ ${version} = "C78" ]];then
        export LD_LIBRARY_PATH=
        export LD_LIBRARY_PATH=/home/HwHiAiUser/Ascend/acllib/lib64:/home/HwHiAiUser/ascend_ddk/arm/lib:${LD_LIBRARY_PATH}
        export PYTHONPATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/arm64-linux_gcc7.3.0/pyACL/python/site-packages/acl:${PYTHONPATH}
    elif [[ ${version} = "c75" ]] || [[ ${version} = "C75" ]]  || [[ ${version} = "C78" ]];then
        export LD_LIBRARY_PATH=/home/HwHiAiUser/Ascend/acllib/lib64:/home/HwHiAiUser/ascend_ddk/arm/lib:${LD_LIBRARY_PATH}
        export PYTHONPATH=/home/HwHiAiUser/Ascend/ascend-toolkit/latest/arm64-linux/pyACL/python/site-packages/acl:${PYTHONPATH}
    fi

    return 0
}


function downloadOriginalModel_yolo() {

    mkdir -p ${project_path}/model/

    echo ${yolo_tf_model}

    gdown ${yolo_tf_model} -O ${project_path}/model/${yolo_model_name}.pb
    if [ $? -ne 0 ];then
        echo "Download yolo_model.pb failed, please check Network."
        return 1
    fi


    return 0
}

function downloadOriginalModel_whenet() {

    mkdir -p ${project_path}/model/

    echo ${whenet_tf_model}

    gdown ${whenet_tf_model} -O ${project_path}/model/${whenet_model_name}.pb
    if [ $? -ne 0 ];then
        echo "Download WHENet_b2_a1_modified.pb failed, please check Network."
        return 1
    fi


    return 0
}

function main() {

    if [[ ${version}"x" = "x" ]];then
        echo "ERROR: version is invalid"
        return ${inferenceError}
    fi

    mkdir -p ${HOME}/models/${project_name}     
    # YOLO conversion
    if [[ $(find ${HOME}/models/${project_name} -name ${yolo_model_name}".om")"x" = "x" ]];then 

        downloadOriginalModel_yolo
        if [ $? -ne 0 ];then
            echo "ERROR: download original YOLO model failed"
            return ${inferenceError}
        fi

        # setAtcEnv
        export LD_LIBRARY_PATH=${install_path}/atc/lib64:$LD_LIBRARY_PATH
        if [ $? -ne 0 ];then
            echo "ERROR: set atc environment failed"
            return ${inferenceError}
        fi

        cd ${project_path}/model/
        atc --framework=3 --model=${project_path}/model/yolo_model.pb --input_shape="input_1:1,416,416,3" --input_format=NHWC --output=${HOME}/models/${project_name}/${yolo_model_name} --output_type=FP32 --soc_version=Ascend310
        if [ $? -ne 0 ];then
            echo "ERROR: convert YOLO model failed"
            return ${inferenceError}
        fi

        ln -sf ${HOME}/models/${project_name}/${yolo_model_name}".om" ${project_path}/model/${yolo_model_name}".om"
        if [ $? -ne 0 ];then
            echo "ERROR: failed to set YOLO model soft connection"
            return ${inferenceError}
        fi
    else 
        ln -sf ${HOME}/models/${project_name}/${yolo_model_name}".om" ${project_path}/model/${yolo_model_name}".om"
        if [ $? -ne 0 ];then
            echo "ERROR: failed to set model soft connection"
            return ${inferenceError}
        fi
    fi
    # WHENet Conversion
    if [[ $(find ${HOME}/models/${project_name} -name ${whenet_model_name}".om")"x" = "x" ]];then 

        downloadOriginalModel_whenet
        if [ $? -ne 0 ];then
            echo "ERROR: download original WHENet model failed"
            return ${inferenceError}
        fi

        # setAtcEnv
        export LD_LIBRARY_PATH=${install_path}/atc/lib64:$LD_LIBRARY_PATH
        if [ $? -ne 0 ];then
            echo "ERROR: set atc environment failed"
            return ${inferenceError}
        fi

        cd ${project_path}/model/
        atc --framework=3 --model=${project_path}/model/WHENet_b2_a1_modified.pb --input_shape="input_1:1,224,224,3" --input_format=NHWC --output=${HOME}/models/${project_name}/${whenet_model_name} --output_type=FP32 --soc_version=Ascend310
        if [ $? -ne 0 ];then
            echo "ERROR: convert WHENet model failed"
            return ${inferenceError}
        fi

        ln -sf ${HOME}/models/${project_name}/${whenet_model_name}".om" ${project_path}/model/${whenet_model_name}".om"
        if [ $? -ne 0 ];then
            echo "ERROR: failed to set WHENet model soft connection"
            return ${inferenceError}
        fi
    else 
        ln -sf ${HOME}/models/${project_name}/${whenet_model_name}".om" ${project_path}/model/${whenet_model_name}".om"
        if [ $? -ne 0 ];then
            echo "ERROR: failed to set model soft connection"
            return ${inferenceError}
        fi
    fi
    cd ${project_path}


    # setRunEnv
    source ~/.bashrc
    if [ $? -ne 0 ];then
        echo "ERROR: set executable program running environment failed"
        return ${inferenceError}
    fi

    test_img=${project_path}/data/test.jpg
    verify_img=${project_path}/data/verify.jpg
    wget --no-check-certificate ${images_link}/test.jpg -O ${test_img}
    wget --no-check-certificate ${images_link}/verify.jpg -O ${verify_img}

    mkdir -p ${project_path}/output
    cd ${project_path}/src
    python3 main.py --input_image ${test_img}
    if [ $? -ne 0 ];then
        echo "ERROR: run failed. please check your project"
        return ${inferenceError}
    fi   
    out_img=${project_path}/output/test_output.jpg
    python3 ${script_path}/verify_result.py ${verify_img} ${out_img}
    if [ $? -ne 0 ];then
        echo "ERROR: The result of test 1 is wrong!"
        return ${verifyResError}
    fi   

    echo "********run test success********"

    return ${success}
}
main