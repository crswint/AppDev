class RSImage():
    def __init__(self, bit_depth=1, size='4x4', histogram={}, pixels=[]):
        self.bit_depth = bit_depth
        self.size = size
        self.columns = int(self.size.split("x")[0])
        self.rows = int(self.size.split("x")[1])
        self.histogram = histogram
        self.pixels = pixels

    def __repr__(self):
        return 'RSImage({}, "{}", {}, {})'.format(self.bit_depth,
                                                  self.size,
                                                  self.histogram,
                                                  self.pixels)

    def compute_histogram(self):
        """returns a histogram dict for a list of values

        >>> x = RSImage(bit_depth=1, size='2x2', pixels=[0,0,0,0])
        >>> x.compute_histogram()
        >>> x.histogram
        {0: 4, 1: 0}

        """
        self.histogram = {}
        for pixel_value in range(2**self.bit_depth):
            self.histogram[pixel_value] = 0
        for pixel_value in self.pixels:
            self.histogram[pixel_value] += 1

    def similarity(self, other):
        """Returns similarity score between 0 and 1
        >>> x = RSImage(bit_depth=1, size='2x2', pixels[0,0,0,0])
        >>> x.compute_histogram()
        >>> y = RSImage(bit_depth=1, size='2x2', pixels[0,0,0,0]
        >>> y.compute_histogram()
        >>> x.similarity(y)
        1.0

        """
        sim = 0
        for bit in range(2**self.bit_depth):
            if max(self.histogram[bit], other.histogram[bit]) > 0:
                sim += (min(self.histogram[bit], self.histogram[bit]))/(float(max(self.histogram[bit], other.histogram[bit])))
            elif self.histogram[bit] == 0 and other.histogram[bit] == 0:
                sim += 1
        if self.bit_depth == 1:
            return sim * (1.0/(2.0))
        else:
            return sim * (1.0/(2**self.bit_depth))

#  slicing method is .split('x')[0]  for example
