from django.core.exceptions import ValidationError
from django.test import TestCase
from BarberBook.client.models import ClientProfile
from BarberBook.account.models import AppUser


class ClientProfileTest(TestCase):
    VALID_CLIENT_PROFILE_DATA = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'city': 'Sofia',
        'phone': '08888888'
    }
    VALID_USER_DATA = {
        'username': 'ivan',
        'email': 'ivan@mail.bg',
        'password': 'Abcde123',
        'role': 'Client'
    }

    def create_client(self, data, **kwargs):
        user = AppUser.objects.create(**self.VALID_USER_DATA)
        client_data = {
            **data,
            **kwargs,
            'user': user,
        }

        return ClientProfile(**client_data)

# TEST first_name
    def test_create__when_valid__expect_to_be_created(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA)
        client.full_clean()
        client.save()

        self.assertIsNotNone(client.pk)

    def test_create__when_first_name_has_1_more_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, first_name='A' * ClientProfile.MAX_LENGTH_FIRST_NAME + 'a')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_first_name_has_1_less_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, first_name='A' * (ClientProfile.MIN_LENGTH_FIRST_NAME-1))
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_first_name_starts_with_lowercase_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, first_name='ivan')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_first_name_contains_not_alpha_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, first_name='Ivan@')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

# TEST last_name
    def test_create__when_last_name_has_1_more_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, last_name='A' * ClientProfile.MAX_LENGTH_LAST_NAME + 'a')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_last_name_has_1_less_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, last_name='A' * (ClientProfile.MIN_LENGTH_LAST_NAME-1))
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_last_name_starts_with_lowercase_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, last_name='ivanov')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_last_name_contains_not_alpha_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, last_name='Ivan@v')
        print(client.first_name)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

# TEST city
    def test_create__when_city_has_1_more_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, city='A' * ClientProfile.MAX_LENGTH_CITY + 'a')
        print(client.city)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_test_create__when_city_has_1_less_than_valid_characters__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, city='A' * (ClientProfile.MIN_LENGTH_CITY-1))
        print(client.city)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_city_starts_with_lowercase_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, city='sofia')
        print(client.city)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)

    def test_create__when_city_contains_not_alpha_character__expect_to_raise(self):
        client = self.create_client(self.VALID_CLIENT_PROFILE_DATA, city='Sofi@')
        print(client.city)
        with self.assertRaises(ValidationError) as context:
            client.full_clean()
        print(context.exception)


# TEST phone

