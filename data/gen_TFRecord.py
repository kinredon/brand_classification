# coding:UTF-8
import sys
sys.path.insert(0, '/Users/kinredon/Documents/github/models/research/slim')   # 将arg2加入python系统路径
from datasets import dataset_utils
import math
import os
import tensorflow as tf

'''
list_path : 数据文件目录，如：list_train.txt
data_dir: 图片所在目录
output_dir: 结果输出目录
'''
def convert_dataset(list_path, data_dir, output_dir, _NUM_SHARDS=10):
    fd = open(list_path)
    lines = [line.split() for line in fd]
    fd.close()
    num_per_shard = int(math.ceil(len(lines) / float(_NUM_SHARDS))) # 分片大小
    with tf.Graph().as_default():
        decode_jpeg_data = tf.placeholder(dtype=tf.string)          # jpeg数据
        decode_jpeg = tf.image.decode_jpeg(decode_jpeg_data, channels=3)    # 将数据解码
        with tf.Session('') as sess:
            for shard_id in range(_NUM_SHARDS):
                output_path = os.path.join(output_dir,
                    'data_{:05}-of-{:05}.tfrecord'.format(shard_id, _NUM_SHARDS))
                # A class to write records to a TFRecords file.
                tfrecord_writer = tf.python_io.TFRecordWriter(output_path)
                start_ndx = shard_id * num_per_shard
                end_ndx = min((shard_id + 1) * num_per_shard, len(lines))
                # handle image from start_ndx to end_ndx
                for i in range(start_ndx, end_ndx):
                    sys.stdout.write('\r>> Converting image {}/{} shard {}'.format(
                        i + 1, len(lines), shard_id))
                    sys.stdout.flush()
                    # File I/O wrappers without thread locking
                    image_data = tf.gfile.FastGFile(os.path.join(data_dir, lines[i][0]), 'rb').read()
                    image = sess.run(decode_jpeg, feed_dict={decode_jpeg_data: image_data})
                    height, width = image.shape[0], image.shape[1]
                    # print("\n\r" + str(height) + "\t" +  str(width))
                    example = dataset_utils.image_to_tfexample(
                        image_data, b'jpg', height, width, int(lines[i][1]))
                    tfrecord_writer.write(example.SerializeToString())
                tfrecord_writer.close()
    sys.stdout.write('\n')
    sys.stdout.flush()
os.system('mkdir -p train')
convert_dataset('list_train.txt', 'vehicle', 'train/')
os.system('mkdir -p val')
convert_dataset('list_val.txt', 'vehicle', 'val/')
