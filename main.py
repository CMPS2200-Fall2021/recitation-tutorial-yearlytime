def sum_of_squares(a):
        temp=0
        for i in a:
                temp+=i*i
        return temp

def test_one():
        assert sum_of_squares([1,2,3]) == 14
        
