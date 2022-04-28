from .models import Booking
class TestClass:
    
    def set_up_user(self):
        self.user = User.objects.create_user(
            username = 'John',
            password = 'testing',
            email =  'john@gmail.com',
        )
    
        Booking.objects.create(
            fname= 'Joe',
            lname='Smith',
            location='London'
        )
        
    def test_set_up_user(self):
        self.assertEqual(response.status_code, 200)
        
    # def set_up_user(self):
    #     User.objects.create_user(username = 'user1', password = 'testpassword')        
        
    def test_one(self):
        x = "this"
        assert "h" in x
    
    def test_two(self):
        x = "this"
        assert "4" in x
    