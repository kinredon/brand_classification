#!/bin/sh
python train_image_classifier.py \
    --train_dir=train_logs \
    --dataset_dir=../../../data/train \
    --num_samples=14946 \
    --num_classes=50 \
    --labels_to_names_path=../../../data/labels.txt \
    --model_name=inception_resnet_v2 \
    --checkpoint_path=../../../data/checkpoints/inception_resnet_v2_2016_08_30.ckpt \
    --checkpoint_exclude_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits \
    --trainable_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits\
