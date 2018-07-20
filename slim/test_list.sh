#!/bin/sh
CUDA_VISIBLE_DEVICES='' python3 test_image_classifier_list.py \
    --checkpoint_path=train_results/train_log_inception_res_v2/ \
    --test_list=../../../data/test_list.txt \
    --test_dir=/Users/kinredon/Documents/vehicle/ \
    --num_classes=50 \
    --model_name=inception_resnet_v2
