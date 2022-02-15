import unittest
from memento import *
from collection import Collection
from vaccination_request import Vaccination_request

one = Vaccination_request(4563,'Sofia', '+380982399237','moderna', '12/12/2021', '12:00', '12:15')
two = Vaccination_request(3647,'Anna','+380982377839', 'phizer','01/01/2022', '12:21', '14:23')
three = Vaccination_request(3445,'Katia', '+380976544567', 'astrazeneca', '21/02/2022', '15:30', '16:32')
originator = Originator()
caretaker = CareTaker()
class Test(unittest.TestCase):
    def setUp(self):
        self.all = [one,two, three]
        self.requests = Collection("un_text.txt")
        self.requests.set_requests(self.all)
        self.sort_id = [3445,3647,4563]
    def test_add(self):
        my = Vaccination_request(1234,'Lilia','+380982377485','phizer','22/02/2022','12:00','12:10')
        self.requests.add(my)
        self.assertTrue(self.requests.search(1234))
    def test_remove(self):
        size = len(self.requests)
        self.requests.remove(4563)
        self.assertFalse(self.requests.search(4563))
    def test_search(self):
        self.assertFalse(self.requests.search('oleg'))
        self.assertTrue(self.requests.search('Anna'))
    def test_replace(self):
        my = Vaccination_request(4563,'Taya', '+380982388392', 'phizer', '01/12/2022', '17:10','17:30')
        self.requests.replace(my)
        self.assertFalse(self.requests.search('Ira'))
        self.assertTrue(self.requests.search('Taya'))
    def test_sort_id(self):
        self.requests.sort('id')
        for payment, id in zip(self.requests.requests, self.sort_id):
            self.assertEqual(payment.id, id)
    def test_copy(self):
        my_copy = self.requests.do_copy()
        self.assertEqual(len(self.requests), len(my_copy))
    def test_undo_redo(self):
        size = len(self.requests)
        memento(originator, caretaker, self.requests)
        self.requests.remove(1301)
        memento(originator, caretaker, self.requests)
        originator.restore(caretaker.undo())
        self.assertEqual(len(originator.get_record()), size)
        originator.restore(caretaker.redo())
if __name__ == '__main__':
    unittest.main()