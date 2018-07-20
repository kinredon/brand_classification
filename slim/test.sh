#!/bin/sh
python test_image_classifier.py \
    --checkpoint_path=train_logs1/ \
    --test_path=test/image/ \
    --num_classes=50 \
    --model_name=inception_resnet_v2
