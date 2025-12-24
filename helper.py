import datetime
import typing
def print_time():
    time = datetime.datetime.now()
    print(f"Current time is {time}")

class solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%len(nums)
        start = 0
        # temp = nums[-k:]
        # for i in range(len(nums)-1,k-1,-1):
        #     nums[i] = nums[i-k]
        # for j in range(k):
        #     nums[j] = temp[j]
        while(k):
            if k <=n//2:
                print(f"Current nums:{nums}")
                for j in range(k):
                    i = j + start
                    nums[i], nums[i + n-k] = nums[i + n -k], nums[i]
                print(f"Current nums:{nums}")
                # self.rotate(nums[k:],k)
                n -= k
                start+=k
            else:
                print(f"Current nums:{nums}")
                for j in range(n-k):
                    i = j + start
                    nums[i], nums[i + k] = nums[i + k], nums[i]
                print(f"Current nums:{nums}")
                # self.rotate(nums[:k],2*k-n) 
                n, k = k, 2*k -n
            k = k%n

if __name__=='__main__':
    print_time()
    nums = [1,2,3,4,5,6,7]
    test = solution()
    test.rotate(nums,3)
    print(nums)
