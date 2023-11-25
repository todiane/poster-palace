import unittest
from your_application.models import Category, Product
from your_application.database import db_session

"""

Category model test
Creating a category and ensuring it is stored correctly.
Validating that the category name is not empty.

"""

class CategoryModelTest(unittest.TestCase):

    def test_create_category(self):
        category = Category(name="Motivational", description="Motivational quotes")
        db_session.add(category)
        db_session.commit()

        self.assertIsNotNone(category.id)
        self.assertEqual(category.name, "Motivational")


"""
Product model test
Creating a product with all necessary fields and ensuring it's stored correctly.
Ensuring the product is linked to a category.
Validating constraints like positive price values.

"""

class ProductModelTest(unittest.TestCase):

    def setUp(self):
        self.category = Category(name="Motivational", description="Motivational poster")
        db_session.add(self.category)
        db_session.commit()

    def test_create_product(self):
        product = Product(name="Hope Multicoloured", description="Multicoloured poster", price=22.50, category_id=self.category.id)
        db_session.add(product)
        db_session.commit()

        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Hope Multicoloured")
        self.assertEqual(product.category_id, self.category.id)
        self.assertTrue(product.price > 0)

    def tearDown(self):
        db_session.query(Product).delete()
        db_session.query(Category).delete()
        db_session.commit()

if __name__ == '__main__':
    unittest.main()
