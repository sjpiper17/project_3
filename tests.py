#import stuff you need
import unittest
import pandas as pd
import ray

#import your map and reduce functions from the program
from part_3a import map
from part_3a import reduce

#read in your data
data = pd.read_csv("test_data.txt", sep='\t')

#Define the test function
class TestMapReduce(unittest.TestCase):
    #this test tests if the total count of variants across quarters equals the number of data entries from the original data file.
    def test_map_reduce(self):
        map_result_test = map.remote(data)
        count_test = reduce.remote(map_result_test)
        sum_test = sum(ray.get(count_test))
        self.assertEqual(sum_test, data.shape[0])
        print('pass test')

if __name__ == '__main__':
    unittest.main()