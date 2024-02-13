from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
    
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
    
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item_id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item_id)
        self.assertEqual(len(existing_items), 0)
    
    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/toggle/{item_id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.filter(id=item_id)
        self.assertFalse(updated_item.done)
