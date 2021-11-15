

caffe_model="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/facedection/face_detection_fp32.caffemodel"
caffe_prototxt="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/facedection/face_detection.prototxt"
aipp_cfg="https://modelzoo-train-atc.obs.cn-north-4.myhuaweicloud.com/003_Atc_Models/AE/ATC%20Model/facedection/insert_op.cfg"
model_name="face_detection"

data_source="https://c7xcode.obs.cn-north-4.myhuaweicloud.com/models/face_detection_rtsp/"
data_name="person.mp4"
conf_file_name="multi_channels_rtsp.conf"
project_name="multi_channels_rtsp"

version=$1

script_path="$( cd "$(dirname $BASH_SOURCE)" ; pwd -P)"
project_path=${script_path}/..
common_script_dir=${script_path}/../../../../../../common/
run_command="./${project_name} ${project_path}/data/${data_name}"
model_atc="atc --model=${project_path}/model/${caffe_prototxt##*/} --weight=${project_path}/model/${caffe_model##*/} --framework=0 --output=${HOME}/models/${project_name}/${model_name} --soc_version=Ascend310 --insert_op_conf=${project_path}/model/${aipp_cfg##*/}"

declare -i success=0
declare -i inferenceError=1
declare -i verifyResError=2


. ${common_script_dir}/testcase_common.sh

function main() {

    # 下载测试集
    downloadDataWithVerifySource
    if [ $? -ne 0 ];then
        return ${inferenceError}
    fi

    modelconvert
    if [ $? -ne 0 ];then
        return ${inferenceError}
    fi

    buildproject
    if [ $? -ne 0 ];then
        return ${inferenceError}
    fi

    run_presenter
    if [ $? -ne 0 ];then
        return ${inferenceError}
    fi

    return ${success}
}
main
