from django.urls import reverse, resolve


class TestUrls:

    def test_cook_form_url(self):
        path = reverse('cook-form')
        assert resolve(path).view_name == 'cook-form'

    def test_cook_delete_url(self):
        path = reverse('cook-delete', kwargs={'pk': 1})
        assert resolve(path).view_name == 'cook-delete'

    def test_cooks_url(self):
        path = reverse('cooks')
        assert resolve(path).view_name == 'cooks'

    def test_cook_detail_url(self):
        path = reverse('cook-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'cook-detail'

    def test_cook_edit(self):
        path = reverse('cook_edit', kwargs={'pk': 1})
        assert resolve(path).view_name == 'cook_edit'

    def test_dishes_url(self):
        path = reverse('dishes')
        assert resolve(path).view_name == 'dishes'

    def test_dish_detail(self):
        path = reverse('dish-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'dish-detail'

    def test_events_url(self):
        path = reverse('events')
        assert resolve(path).view_name == 'events'

    def test_event_detail(self):
        path = reverse('event-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'event-detail'

    def test_stocks_url(self):
        path = reverse('stocks')
        assert resolve(path).view_name == 'stocks'

    def test_stock_detail(self):
        path = reverse('stock-detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'stock-detail'

    def test_contacts_url(self):
        path = reverse('contacts')
        assert resolve(path).view_name == 'contacts'

    def test_edit_contact(self):
        path = reverse('edit-contact', kwargs={'id': 1})
        assert resolve(path).view_name == 'edit-contact'

    def test_update_contact(self):
        path = reverse('update-contact', kwargs={'id': 1})
        assert resolve(path).view_name == 'update-contact'

    def test_delete_contact(self):
        path = reverse('delete-contact', kwargs={'id': 1})
        assert resolve(path).view_name == 'delete-contact'
