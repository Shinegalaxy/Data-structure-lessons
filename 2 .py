class DoubleEndedQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0
    
    def push_back(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1

    def push_front(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.first = (self.first - 1) % self.max_size
        self.Q[self.first] = item
        self.num += 1

    def pop_front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return item



polynomials = [] # لیست برای سیو کردن چند جمله ای ها

while True:
    user_input = input(" Input: 1, Sum: 2, Multiply: 3, Print: 4, Exit: 5 :عدد را با توجه به دستورات داده شده وارد کنید:")
    if user_input == '1':
        get_and_store_polynomial()
        print("چند جمله ای ذخیر شد.", polynomials)

    elif user_input == '2':
        if len(polynomials) > 1:
            add_and_simplify_polynomials()
        else:
            print("حداقل باید دو چند جمله ای وارد کنید.")

    elif user_input == '3':
        if len(polynomials) > 1:
            multiply_and_simplify_polynomials()
        else:
            print("حد اقل باید دو چند جمله ای وارد کنید.")

    elif user_input == '4':
        if polynomials:
            print_polynomial()
        else:
            print("  چند جمله ای برای چاپ وجود ندارد.")

    elif user_input == '5':
        print("پایان برنامه.")
        break
    else:
        print("عدد خارج ازمحدوده است")