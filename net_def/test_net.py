import unittest

import tensorflow as tf
from tensorflow.keras.layers import Conv2D


class KerasTest(unittest.TestCase):
    """Let's just test some keras stuff, just for fun, why not"""

    def test_conv2d(self):
        """Testing the good old conv2d layer"""
        input = tf.random.normal((1, 10, 10, 4))
        conv_layer = Conv2D(filters=5, kernel_size=(3,3), padding="same")
        output = conv_layer(input)
        self.assertEqual(output.shape, (1, 10, 10, 5))
        weights, biases = conv_layer.weights
        self.assertEqual(weights.shape, (3, 3, 4, 5))
        self.assertEqual(biases.shape, (5,))


class NetTest(unittest.TestCase):
    def test_conv_layer(self):
        pass


if __name__ == '__main__':
    unittest.main()
